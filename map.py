import random
from Room import Room
from utils import randpoint
from fighting import fight


class Map:
	deltas = [[-1, 0], [0, 1], [1, 0], [0, -1]]

	def __init__(self, character, item_probs, enemy_probs, height=10, width=10, num_rooms=10, room_height=9, room_width=15):
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
			'U': 'move_user_up',
			'D': 'move_user_down',
			'L': 'move_user_left',
			'R': 'move_user_right',
			'Q': 'quit_game',
			'E': 'move_rooms',
			'P': 'pick_up_item',
			'S': 'show_inventory',
			'F': 'final_exit'
		}

	def generate_rooms(self):
		rooms = {}
		pos = randpoint(self.height, self.width)
		vis = set()
		while len(vis) < self.num_rooms:
			if pos in vis: break
			rooms[pos] = Room(self.item_probs, self.enemy_probs, room_id=len(vis), height=self.room_height, width=self.room_width, is_final_room=(len(vis) == 0))
			vis.add(pos)
			sx, sy = pos
			for dx, dy in random.sample(self.deltas, len(self.deltas)):
				nx = sx + dx
				ny = sy + dy
				if 0 <= nx < self.height and 0 <= ny < self.width:
					pos = (nx, ny)
					break

		for i in range(self.height):
			for j in range(self.width):
				if (i, j) in rooms:
					for k, (di, dj) in enumerate(self.deltas):
						if (i+di, j+dj) in rooms:
							rooms[i, j].connect(k, rooms[i+di, j+dj])

		for room in rooms.values():
			print(room.id, room.neighbors)

		return rooms

	def final_exit(self):
		print("exiting final door")
		self.game_status = 'WON'

	def get_status(self):
		return self.game_status

	def is_room_action(self, choice):
		return choice in 'UDLR'

	def pick_up_item(self):
		self.character.add_item(self.current_room.pick_up_item())

	def show_inventory(self):
		self.character.show_inv()

	def move_rooms(self):
		curr_id = self.current_room.id
		next_id = self.current_room.current_door()
		for room in self.rooms.values():
			if room.id == next_id:
				self.current_room = room
				user_new_location = self.current_room.get_user_position_after_enter(curr_id)
				self.current_room.user_location = user_new_location

				for dir in ['top', 'bottom', 'left', 'right']:
					if self.current_room.neighbors[self.current_room.direction_map[dir]] == curr_id:
						self.current_room.user_location = self.current_room.location_map[dir]
						break
				break

	def generate_options(self):
		options = {'U': 'p', 'D': 'own', 'L': 'eft', 'R': 'ight', 'Q': 'uit', 'S': 'how inventory'}
		curr_door = self.current_room.current_door()
		if curr_door != -1:
			options['E'] = 'nter'
		curr_item = self.current_room.current_item()
		# print(curr_item)
		if curr_item is not None:
			options['P'] = f'ick up {str(curr_item)}'
		return options

	def generate_prompt_string(self, options):
		commands = [f'({opt}){rest}' for opt, rest in options.items()]
		return '\n'.join(commands + ['\t>> '])

	def print_move_prompt(self):
		options = self.generate_options()
		prompt_string = self.generate_prompt_string(options)

		while True:
			print(f'{self.current_room.id=} {self.current_room.neighbors} {self.current_room.current_door()}')
			user_input = input(prompt_string).upper()
			choice = user_input and user_input[0]

			if choice in options:
				target = self.current_room if self.is_room_action(choice) else self
				action = getattr(target, self.actions[choice])
				action()
				curr_enemy = self.current_room.current_enemy()
				if curr_enemy is not None:
					result = fight(self.character, curr_enemy)
					if result == 1:
						for enemy_pos, enemy in self.current_room.enemies.items():
							if curr_enemy == enemy:
								dead_enemy_pos = enemy_pos
								break
						del self.current_room.enemies[dead_enemy_pos]
					elif result == 0:
						self.game_status = 'LOST'
				break
			else:
				print("-" * 120)
				print("Invalid option, try again.")
				print("-" * 120)

	def run(self):
		while True:
			self.current_room.print_room()
			self.print_move_prompt()
			# if they go to the ennd:
			# 	reutner True



# if __name__ == '__main__':
# 	map = Map(room_height=10, room_width=13)
# 	# run the game
# 	map.run()
