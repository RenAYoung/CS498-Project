import math
import random
import item_list
from utils import randpoint


class Room:

    def __init__(self, user_entrance=[2, 2], room_id=0, height=9, width=15, max_items=4):
        self.user_location = user_entrance  # current location of user in room [row, col]

        # array of room ids [top, right, bottom, left]
        self.neighbors = [-1] * 4
        self.direction_map = {'top': 0, 'right': 1, 'bottom': 2, 'left': 3}
        self.location_map = {
            'top': [width // 2, 0],
            'right': [width - 1, height // 2],
            'bottom': [width // 2, height - 1],
            'left': [0, height // 2]
        }

        # dimensions for the room
        self.height = height
        self.width = width # arrays of coords for enemies and items
        self.cell_width = 4  # width of cells (should be even)
        self.cell_height = 2  # height of cells (should be odd)

        self.max_items = max_items
        # arrays of coords for enemies and items
        self.items_location = []
        self.enemy_locations = []
        # set up enemy and item locations in the room
        self.set_enemies()
        self.set_items()

        # initialize correct id for the room
        self.id = room_id

    def set_items(self):
        """ Randomly generates position of x number of items in room
        where x is in the range [0, max_items]"""
        num_items = random.randrange(self.max_items)
        for _ in range(num_items):
            new_point = list(randpoint(self.height, self.width))
            while new_point in self.enemy_locations:  # make sure item isn't placed on an enemy
                new_point = list(randpoint(self.height, self.width))
            self.items_location.append(new_point)

    def set_enemies(self):
        # can add more valid enemy locations here...
        valid_enemy_locations = [[1, 1], [1, self.width - 2], [self.height - 2, 1], [self.height - 2, self.width - 2]]
        self.enemy_locations.append(random.choice(valid_enemy_locations))

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
        print()
        # print each row
        for i in range(self.height):
            self.print_row(i)

    def user_on_door(self):
        for dir in ['top', 'bottom', 'left', 'right']:
            if self.has_door(dir) and self.user_location == self.location_map[dir]:
                return True
        return False

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
                    elif [row_num, col_num] in self.enemy_locations:  # Enemy location
                        print("!", end='')
                    elif [row_num, col_num] in self.items_location:  # Item locations
                        print("?", end='')
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
