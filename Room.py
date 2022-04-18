import math


class Room:

    def __init__(self, user_entrance=[2, 2], room_id=0, neighbors=[-1, -1, -1, -1]):
        self.user_location = user_entrance  # current location of user in room [x, y]

        # array of room ids [top, right, bottom, left]
        self.neighbors = neighbors

        # dimensions for the room
        self.grid_size = [12, 19]  # rows and cols of grid
        self.cell_width = 6  # width of cells (should be even)
        self.cell_height = 3  # height of cells (should be odd)

        # initialize correct id for the room
        self.id = room_id

    def move_user_position(self, x=0, y=0):
        self.user_location = [self.user_location[0] + x, self.user_location[1] + y]

    def print_room(self):
        # print top row cap
        print("_" * (self.grid_size[1] * self.cell_width + 1))
        # print each row
        for i in range(self.grid_size[0]):
            self.print_row(i)

    def has_door(self, which_door):
        if which_door == 'top':
            return self.neighbors[0] != -1
        elif which_door == 'right':
            return self.neighbors[1] != -1
        elif which_door == 'bottom':
            return  self.neighbors[2] != -1
        elif which_door == 'left':
            return self.neighbors[3] != -1

    # this is the one without the space btwn the rows (bottom cap only)
    def print_row(self, row_num):
        # print cells
        for j in range(self.cell_height):  # print each horizontal cross-section
            for i in range(self.grid_size[1] * self.cell_width):
                col_num = i // self.cell_width  # which col is currently rendering (0-numCols)
                # border of the cells
                if i % self.cell_width == 0:
                    if row_num == math.floor(self.grid_size[0] / 2) and col_num == 0:  # check if door
                        print(" ", end='')
                    else:
                        print("|", end='')
                # print at the middle of the cell
                elif j == math.floor((self.cell_height - 1) / 2) and i % self.cell_width == math.floor(
                        self.cell_width / 2):
                    # print("Col NUM: ", col_num, end='')
                    if self.user_location[0] == col_num and self.user_location[1] == row_num:
                        print("U", end='')
                    else:
                        print("?", end='')
                # bottom boundary of the cell
                elif j == self.cell_height - 1:
                    print("_", end='')
                # blank space in cells
                else:
                    print(" ", end='')
            print("|")  # end cap of each row

    def print_move_prompt(self):
        prompt_string = \
            "(L)eft\n" \
            "(R)ight\n" \
            "(D)own\n" \
            "(U)p\n" \
            "(Q)uit\n" \
            "\t>>"

        while True:
            user_input = input(prompt_string).upper()
            choice = ""
            if user_input == "":
                choice = ""
            else:
                choice = user_input[0]
            if choice == 'L':
                self.move_user_position(x=-1)
                break
            elif choice == 'R':
                self.move_user_position(x=1)
                break
            elif choice == 'U':
                self.move_user_position(y=-1)
                break
            elif choice == 'D':
                self.move_user_position(y=1)
                break
            elif choice == 'Q':
                print("YOU QUIT LOL")
                break
            else:
                print("-" * 120)
                print("Invalid Option, try again.")
                print()
                print("-" * 120)


if __name__ == '__main__':
    room = Room()
    room.print_room()
    while True:
        room.print_move_prompt()
        room.printRoom()
