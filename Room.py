import math
import random
import item_list
from utils import randpoint
from enemy_list import list_of_enemies
from item_list import array_of_items


class Room:

    def __init__(self, item_probs, enemy_probs, user_entrance=[3, 2], room_id=0, height=9, width=15, max_items=4,
                 is_final_room=False):
        self.user_location = user_entrance  # current location of user in room [row, col]

        # array of room ids [top, right, bottom, left]
        self.neighbors = [-1] * 4
        self.direction_map = {'top': 0, 'right': 1, 'bottom': 2, 'left': 3}
        self.direction_map_2 = {0: 'top', 1: 'right', 2: 'bottom', 3: 'left'}
        self.location_map = {
            'top': [0, width // 2],
            'right': [height // 2, width - 1],
            'bottom': [height - 1, width // 2],
            'left': [height // 2, 0]
        }


        # dimensions for the room
        self.height = height
        self.width = width  # arrays of coords for enemies and items
        self.cell_width = 4  # width of cells (should be even)
        self.cell_height = 2  # height of cells (should be odd)

        self.item_probs = item_probs
        self.enemy_probs = enemy_probs

        self.max_items = max_items

        # is this the final room
        self.is_final_room = is_final_room
        self.final_door_cells = None  # will be changed by self.set_final_door() if self.is_final_room
        self.set_final_door()

        # arrays of coords for enemies and items
        self.items = {}
        self.enemies = {}

        # set up enemy and item locations in the room
        self.set_enemies()
        self.set_items()

        # initialize correct id for the room
        self.id = room_id

    def set_items(self):
        """ Randomly generates position of x number of items in room
        where x is in the range [0, max_items) """
        num_items = random.randrange(self.max_items)
        for _ in range(num_items):
            item_loc = randpoint(self.height, self.width)
            while item_loc in self.enemies or item_loc in self.items or item_loc in self.final_door_cells:  # make sure item placement is valid
                item_loc = randpoint(self.height, self.width)
            item_type = random.choices(array_of_items, weights=self.item_probs)[0]
            self.items[item_loc] = item_type

    def set_final_door(self):
        self.final_door_cells = []
        self.final_door_cells.append((self.height // 2, self.width // 2))

        # exit_loc = randpoint(self.height, self.width)
        # while exit_loc in self.items or exit_loc in self.enemies:
        #     exit_loc = randpoint(self.height, self.width)
        # self.final_door_cell = exit_loc
        # jic we want it

    def set_enemies(self):
        # can add more valid enemy locations here...
        valid_enemy_locations = [(1, 1), (1, self.width - 2), (self.height - 2, 1), (self.height - 2, self.width - 2)]
        enemy_loc = random.choice(valid_enemy_locations)
        while enemy_loc in self.final_door_cells:
            enemy_loc = random.choice(valid_enemy_locations)
        enemy_type = random.choices(list_of_enemies, weights=self.enemy_probs)[0]
        self.enemies[enemy_loc] = enemy_type

    def connect(self, dir, other):
        """ helper function to connect this room to another """
        if dir in range(4):
            self.neighbors[dir] = other.id
            other.neighbors[(dir + 2) % 4] = self.id
        else:
            print('bad direction')

    def move_user_position(self, x=0, y=0):
        """ changes position of user in room when user moves"""
        nx = max(0, min(self.user_location[0] + x, self.width - 1))
        ny = max(0, min(self.user_location[1] + y, self.height - 1))
        self.user_location = [nx, ny]

    def move_user_left(self):
        self.user_location[1] = max(0, self.user_location[1] - 1)

    def move_user_right(self):
        self.user_location[1] = min(self.width - 1, self.user_location[1] + 1)

    def move_user_up(self):
        self.user_location[0] = max(0, self.user_location[0] - 1)

    def move_user_down(self):
        self.user_location[0] = min(self.height - 1, self.user_location[0] + 1)

    def print_room(self):
        """ prints the terminal visualization of the room for the user """
        # print top row cap
        for i in range(self.width * self.cell_width + 1):
            if self.has_door('top') and \
                    (i // self.cell_width == self.width // 2 and i % self.cell_width):
                print(" ", end='')
            elif i % self.cell_width == 0:
                print("+", end='')
            else:
                print("-", end='')
        if self.is_final_room:
            print("\t [Final Dungeon] ", end='')
        print()
        # print each row
        for i in range(self.height):
            self.print_row(i)

    def current_door(self):
        for dir in ['top', 'bottom', 'left', 'right']:
            if self.has_door(dir) and self.user_location == self.location_map[dir]:
                return self.neighbors[self.direction_map[dir]]

        return -1

    def current_enemy(self):
        return self.enemies.get(tuple(self.user_location), None)

    def current_item(self):
        return self.items.get(tuple(self.user_location), None)

    def pick_up_item(self):
        return self.items.pop(tuple(self.user_location))

    def has_door(self, which_door):
        return self.neighbors[self.direction_map[which_door]] != -1

    def print_row(self, row_num):
        # print cells
        for j in range(self.cell_height):  # print each horizontal cross-section
            for i in range(self.width * self.cell_width + 1):
                col_num = i // self.cell_width  # which col is currently rendering (0-numCols)
                # vertical borders of the cells
                if i % self.cell_width == 0:
                    # check if there is left door
                    if i % self.cell_width == 0 and j % self.cell_height == self.cell_height - 1:  # + border
                        print("+", end='')
                    elif self.has_door('left') and row_num == self.height // 2 and col_num == 0:
                        print(" ", end='')
                    elif self.has_door('right') and row_num == self.height // 2 and col_num == self.width:  # right door
                        print(" ", end='')
                    else:
                        print("|", end='')
                # print at the middle of each cell
                elif j == (self.cell_height - 1) // 2 and i % self.cell_width == self.cell_width // 2:
                    # print("Enemy locations rn:" , self.enemy_locations)
                    # print user location
                    if self.user_location[1] == col_num and self.user_location[0] == row_num:  # User location
                        print("U", end='')
                    elif (row_num, col_num) in self.enemies:  # Enemy location
                        print("!", end='')
                    elif (row_num, col_num) in self.items:  # Item locations
                        print("?", end='')
                    elif (row_num, col_num) in self.final_door_cells:
                        print("E", end='')
                    else:  # middle of each cell
                        print(" ", end='')
                # horizontal border of cells
                elif j == self.cell_height - 1:
                    # check if there is a bottom door
                    if self.has_door('bottom') and row_num == self.height - 1 and col_num == self.width // 2:
                        print(" ", end='')
                    else:
                        print("-", end='')
                # blank space in cells
                else:
                    print(" ", end='')
            print()

    def get_user_position_after_enter(self, prev_id):
        """ returns the position in this room where the user should be if it entered from room with prev_id"""

        if prev_id in self.neighbors:
            entry_position = self.location_map[self.direction_map_2[self.neighbors.index(prev_id)]]
            print("You should land at :", entry_position)
            return entry_position
        else:
            return [1,1]  # get in corner if not valid LOLS
