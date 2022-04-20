import math
import random
import item_list
from utils import randpoint


class Room:
    def __init__(self, user_entrance=[2, 2], room_id=0, height=9, width=15, max_items = 4):
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
        self.width = width
        self.cell_width = 4  # width of cells (should be even)
        self.cell_height = 2  # height of cells (should be odd)

        # get random items for this room
        self.num_items = random.randrange(max_items)
        self.items_location = [randpoint(1,1)]
            # [random.sample(item_list.array_of_items, self.num_items)]
        # print("Items: ", self.items)

        # initialize correct id for the room
        self.id = room_id

    def connect(self, dir, other):
        if dir in range(4):
            self.neighbors[dir] = other.id
            other.neighbors[(dir + 2) % 4] = self.id
        else:
            print('bad direction')

    def move_user_position(self, x=0, y=0):
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
                    # print user location
                    if self.user_location[1] == col_num and self.user_location[0] == row_num:
                        print("U", end='')
                    else:  # middle of each cell
                        print("?", end='')
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


if __name__ == '__main__':
    room1 = Room(room_id=0)
    room2 = Room(room_id=1)
    room2.connect(0, room1)
    room3 = Room(room_id=2)
    room3.connect(1, room1)
    room4 = Room(room_id=3)
    room4.connect(2, room1)
    room5 = Room(room_id=4)
    room5.connect(3, room1)
    print(room1.neighbors, room2.neighbors)
    print("has door top:", room1.has_door('bottom'))
    room1.print_room()
    while True:
        room1.print_move_prompt()
        room1.print_room()
