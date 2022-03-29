import sys

# global variables


def run_game():
	game_status = ''
	while True:
		decision = input("Type 'W' to win\nType 'L' to lose\n")
		if decision in "Ww":
			game_status = 'WON'
			end_game(game_status)
		elif decision in "Ll":
			game_status = 'LOST'
			end_game(game_status)
		else:
			print("Invalid input: Please type 'W' or 'L'")


def end_game(game_status):
	print(game_status)
	sys.exit(0)


def show_start_menu():
	prompt_string = \
		"(S)tart\n" \
        "(O)ptions\n" \
        "(H)ow to Play\n" \
        "(Q)uit\n" \
        "Input: "
	print('-------------------------')
	print('|  CS 498 Project Game  |')
	print('-------------------------')
	while True:
		choice = input(prompt_string)[0].upper()
		if choice == 'S':
			print('choice was s')
			run_game()
			break
		elif choice == 'O':
			print('choice was o')
			break
		elif choice == 'H':
			print('choice was h')
			break
		elif choice == 'Q':
			print('choice was q')
			sys.exit(0)
		else:
			print("Invalid input: Please choose from following options: ")


if __name__ == '__main__':
    show_start_menu()
