import sys
from character import myCharacter
import item_list

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
    print()
    # print final game status
    if game_status == 'WON':
        print('Congrats! You won! :))))')
    else:
        print('Awww :( you lost.')
 
    # print game results statistics
    print()
    print('Results')
    print("-------------------------")
    player.display_info()
    print("-------------------------")
    print('Number of enemies defeated: ')
    print('Highest level weapon acquired: ')
    print('Highest level armor acquired: ')
    print('Total gold collected: ')
    print()

    # provide option for game result download
    while True:
        res_down_choice = input('Would you like to download your game results? (y/n): ')
        if res_down_choice in 'Yy':
            print('downloaded')
            break
        elif res_down_choice in 'Nn':
            break
        else:
            print('Invalid input: Please choose another option. ')

    # provide option to return to starting menu
    input('Press enter to return to starting menu')
    show_start_menu()

def options():
    print()
    print("Options")
    print("----------------------")
    new_name = input("Enter your character's name: ")
    print("----------------------")
    player.name = new_name
    input('Press enter to return to starting menu')
    show_start_menu()

def how_to_play():
    print()
    print("How To Play")
    print("----------------------")
    print("Stuff")
    print("----------------------")
    input('Press enter to return to starting menu')
    show_start_menu()


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
            options()
            break
        elif choice == 'H':
            print('choice was h')
            how_to_play()
            break
        elif choice == 'Q':
            print('choice was q')
            sys.exit(0)
        else:
            print("Invalid input: Please choose from following options: ")


if __name__ == '__main__':
    player = myCharacter("Coolio", 20, 20, 10, 0, 5, None, None)
    player.sword_equip(item_list.basic_sword)
    player.sheild_equip(item_list.basic_shield)
    player.add_item("s potion")
    
    show_start_menu()
