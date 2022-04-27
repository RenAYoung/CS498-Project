import sys
from character import myCharacter
import item_list
from map import Map
from datetime import datetime
from item_list import array_of_items
from enemy_list import list_of_enemies
import story


# global variables

def run_game():
    game_status = ''
    
    # create character
    character = myCharacter("name", 10, 10, 0, 0, 6, None, None)
    
    # go through first phase of story
    story.begin_story()
    character.sword_equip(item_list.wooden_stick)
    character.sheild_equip(item_list.wooden_plank)

    # set up item and enemy probabilities
    item_probs = [1] * len(array_of_items)
    enemy_probs = [1] * len(list_of_enemies)
    
    num_maps = 1
    for i in range(num_maps):
        m = Map(character, item_probs, enemy_probs)
        m.run()
        if m.getStatus() == 'LOST':
            end_game(m.getStatus())
            break
    else:
        end_game('WON')


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
    print('Total points collected: ')
    print()

    # provide option for game result download
    while True:
        res_down_choice = input('Would you like to download your game results? (y/n): ')
        if res_down_choice in 'Yy':
            file_name = input("Enter name of file for results to go to (ex: results.txt): ")
            out_file = open(file_name, "a")
            
            # datetime object containing current date and time
            now = datetime.now()
            # dd/mm/YY H:M:S
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            
            out_file.write("Run (finished): " + dt_string + "\n")
            print("Run (finished): " + dt_string + "\n")
            out_file.write("Result: " + game_status + "\n")
            out_file.write("Name: " + player.name + "\n")
            out_file.write("Final Health: " + str(player.health) + "/" + str(player.max_health) + "\n")
            out_file.write("Final Damage: " + str(player.damage) + "\n")
            out_file.write("Final Sword: " + player.item_sword.name + "\n")
            out_file.write("Final Shield: " + player.item_shield.name + "\n")
            out_file.write('Number of enemies defeated: ' + "\n")
            out_file.write('Total points collected: ' + "\n")
            out_file.write("\n")
            
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
    print("When the game begins your character will spawn into a room in a randomly generated map.")
    print("Your goal is to navigate through the various rooms to find the exit that leads to the next level.")
    print("Along the way you will find items you can pick up or enemies that you can fight.")
    print("In your terminal, your character, the room, and other entities will be displayed.")
    print("Below the text-based imagery will be prompts providing you with different options to choose how you want to navigate the game.")
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
    print('|    The Quest Begins   |')
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
    #end_game("WON")
    show_start_menu()
