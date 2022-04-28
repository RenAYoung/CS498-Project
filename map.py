import random
from Room import Room
from fighting import fight


class Map:
    deltas = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def __init__(self, character, item_probs, enemy_probs, height=10, width=10, num_rooms=10, room_height=9,
                 room_width=15):
        self.character = character

        self.game_status = 'PLAYING'

        self.height = height
        self.width = width
        self.num_rooms = num_rooms

        self.item_probs = item_probs
        self.enemy_probs = enemy_probs

        self.room_height = room_height
        self.room_width = room_width

        self.rooms = self.generate_rooms()
        self.current_room = random.choice([*self.rooms.values()])

        self.actions = {
            'W': 'move_user_up',
            'S': 'move_user_down',
            'A': 'move_user_left',
            'D': 'move_user_right',
            'Q': 'quit_game',
            'E': 'move_rooms',
            'P': 'pick_up_item',
            'I': 'show_info',
            'X': 'final_exit'
        }

    def generate_rooms(self):
        rooms = {}
        pos = (self.height // 2, self.width // 2)  # first room in middle of map
        vis = set()
        while len(vis) < self.num_rooms:  # iterate until all rooms made
            # instantiate new room and add to rooms dict
            rooms[pos] = Room(self.item_probs, self.enemy_probs, room_id=len(vis), height=self.room_height,
                              width=self.room_width, is_final_room=(len(vis) == 0))
            vis.add(pos)  # add new position
            sx, sy = pos  # get x, y of last room
            # set change to 0s
            nx = 0
            ny = 0
            counter = 0
            while pos in vis:  # retry until pos of room is unique
                if counter > 6:  # branch off of another room if this one is being difficult
                    vis_without_pos = list(vis - {pos})
                    pos = random.choice(vis_without_pos)
                # set new room pos to a neighbor of last room added (pos)
                for dx, dy in random.sample(self.deltas, len(self.deltas)):
                    nx = sx + dx
                    ny = sy + dy
                # make sure new pos fits within map
                if 0 <= nx < self.height and 0 <= ny < self.width:
                    pos = (nx, ny)
                counter += 1

        for i in range(self.height):
            for j in range(self.width):
                if (i, j) in rooms:
                    for k, (di, dj) in enumerate(self.deltas):
                        if (i + di, j + dj) in rooms:
                            rooms[i, j].connect(k, rooms[i + di, j + dj])

        # for room in rooms.values():
        #     print(room.id, room.neighbors)

        return rooms

    def quit_game(self):
        self.game_status = 'LOST'

    def final_exit(self):
        if self.current_room.enemy_dead:
            self.game_status = 'WON'
        else:
            print("-" * 100)
            print("You have to defeat the enemy in this room to escape the dungeon!")
            print("-" * 100)
            print()

    def get_status(self):
        return self.game_status

    def is_room_action(self, choice):
        return choice in 'WASD'

    def pick_up_item(self):
        item = self.current_room.pick_up_item()
        self.character.add_item(item)

    def show_info(self):
        self.character.display_info()
        input('Press enter')

    def move_rooms(self):
        curr_id = self.current_room.id
        next_id = self.current_room.current_door()
        next_user_location = []
        for room in self.rooms.values():
            if room.id == next_id:
                self.current_room = room
                for side in ['top', 'bottom', 'left', 'right']:
                    if self.current_room.neighbors[self.current_room.direction_map[side]] == curr_id:
                        next_user_location = list(Room.location_map[side])
                        break
                break
        self.current_room.user_location = next_user_location

    def generate_options(self):
        options = {'W': 'Up', 'A': 'Left', 'S': 'Down', 'D': 'Right', 'Q': 'Quit', 'I': 'Info'}
        
        curr_door = self.current_room.current_door()
        if curr_door != -1:
            options['E'] = 'Enter'
        
        curr_item = self.current_room.current_item()
        if curr_item is not None:
            options['P'] = f'Pick up {str(curr_item)}'

        if self.current_room.is_final_room and self.current_room.user_location == self.current_room.final_door_cells[0]:
            options['X'] = 'Exit the map'
        return options

    def generate_prompt_string(self, options):
        commands = [f'({opt}) {rest}' for opt, rest in options.items()]
        return '\n'.join(commands)

    def print_move_prompt(self):
        options = self.generate_options()
        prompt_string = self.generate_prompt_string(options)
        print(prompt_string)

        while True:
            user_input = input('\t>> ').upper()
            choice = user_input and user_input[0]

            if choice in options:
                target = self.current_room if self.is_room_action(choice) else self
                action = getattr(target, self.actions[choice])
                action()
                curr_enemy = self.current_room.current_enemy()
                if curr_enemy is not None:
                    result = fight(self.character, curr_enemy)
                    if result == 1:  # enemy died
                        curr_enemy.health = curr_enemy.max_health
                        self.current_room.enemy_dead = True
                        for enemy_pos, enemy in self.current_room.enemies.items():
                            if curr_enemy == enemy:
                                dead_enemy_pos = enemy_pos
                                break
                        del self.current_room.enemies[dead_enemy_pos]
                    elif result == 0:
                        self.game_status = 'LOST'
                break
            else:
                print("-" * 60)
                print("Invalid option, try again.")
                print("-" * 60)

    def run(self):
        print("-"*100)
        print("You've entered a new dungeon!")
        print("-"*100)
        while self.game_status == 'PLAYING':
            self.current_room.print_room()
            self.print_move_prompt()
