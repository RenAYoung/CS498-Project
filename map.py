import random
from Room import Room
from utils import randpoint


class Map:
	deltas = [[-1, 0], [0, 1], [1, 0], [0, -1]]

	def __init__(self, height=10, width=10, num_rooms=10, room_height=9, room_width=15):
		self.height = height
		self.width = width
		self.num_rooms = num_rooms

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
			'M': 'move_rooms'
		}

	def generate_rooms(self):
		rooms = {}
		pos = randpoint(self.height, self.width)
		vis = set()
		while len(vis) < self.num_rooms:
			rooms[pos] = Room(room_id=len(vis), height=self.room_height, width=self.room_width)
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

		return rooms

	def is_room_action(self, choice):
		return choice in 'UDLR'

	def generate_options(self):
		options = {'U': 'p', 'D': 'own', 'L': 'eft', 'R': 'ight', 'Q': 'uit'}
		if self.current_room.user_on_door():
			options['M'] = 'ove'
		return options

	def generate_prompt_string(self, options):
		commands = [f'({opt}){rest}' for opt, rest in options.items()]
		return '\n'.join(commands + ['\t>> '])

	def print_move_prompt(self):
		options = self.generate_options()
		prompt_string = self.generate_prompt_string(options)

		while True:
			user_input = input(prompt_string).upper()
			choice = user_input and user_input[0]

			if choice in options:
				target = self.current_room if self.is_room_action(choice) else self
				action = getattr(target, self.actions[choice])
				action()
				break
			else:
				print("-" * 120)
				print("Invalid option, try again.")
				print("-" * 120)

	def run(self):
		while True:
			map.current_room.print_room()
			if not map.print_move_prompt():
				return False
			if they go to the ennd:
				reutner True



if __name__ == '__main__':
	map = Map(room_height=6, room_width=8)
	while True:
		map.current_room.print_room()
		map.print_move_prompt()
