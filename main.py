import sys

def run_game():
    while True:
        decision = input("Type 'W' to win\nType 'L' to lose\n")

        if decision in "Ww":
            win = 1
            print("nice")
            break
        elif decision in "Ll":
            win = 0
            break
        else:
            print("Incorrect input: Please type 'W' or 'L'")

run_game()

def show_start_menu():
	prompt_string = \
	"(S)tart\n" \
	"(O)ptions\n" \
	"(H)ow to Play\n" \
	"(Q)uit\n" \
	"Input: "

	print('CS 498 Project Game')
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

