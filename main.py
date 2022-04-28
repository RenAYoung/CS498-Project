import sys
from character import myCharacter
import item_list
from map import Map
from datetime import datetime
import story


# global variables

def run_game(player):
	# go through first phase of story
	# story.begin_story()
	
	# equip sword and shield
	player.sword_equip(item_list.wooden_stick)
	player.shield_equip(item_list.wooden_plank)
	
	# set up item and enemy probabilities
	# item_probs = [[1] * len(array_of_items)]
	# enemy_probs = [[1] * len(list_of_enemies)]
	
	item_probs = [[2, 1, 0, 0.5, 0, 0.25, 0, 0, 3, 1, 0.05, 0, 0, 0, 0, 3, 1.2, 0.07, 0, 0, 0],
	              [2, 1, 0, 0.5, 0, 0.25, 0, 0, 3, 1, 0.05, 0, 0, 0, 0, 3, 1.2, 0.07, 0, 0, 0],
	              [2, 1, 0, 0.5, 0, 0.25, 0, 0, 3, 1, 0.05, 0, 0, 0, 0, 3, 1.2, 0.07, 0, 0, 0]]
	
	enemy_probs = [[3, 4, 2, 0.5, 0.4, 0.1, 0, 0, 0],
	               [3, 4, 2, 0.5, 0.4, 0.1, 0, 0, 0],
	               [3, 4, 2, 0.5, 0.4, 0.1, 0, 0, 0]]
	
	num_maps = len(item_probs)
	for i in range(num_maps):
		m = Map(player, item_probs[i], enemy_probs[i], room_height=7, room_width=9, num_rooms=5)
		m.run()
		if m.get_status() == 'LOST':
			end_game(player, m.get_status())
			break
	else:
		end_game(player, 'WON')


def end_game(player, game_status):
	print()
	# print final game status
	if game_status == 'WON':
		print('Congrats! You won! :))))')
	else:
		print('Awww :( you lost.')
	
	# print game results statistics
	print()
	print('Results')
	print("-" * 60)
	player.display_info()
	print('Number of enemies defeated:', player.num_killed)
	print()
	
	# provide option for game result download
	while True:
		print("Would you like to download your game results? (y/n): ")
		res_down_choice = input('\t>> ')
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
			out_file.write('Number of enemies defeated: ' + player.num_killed + "\n")
			
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


def options(player):
	print()
	print("Options")
	print("----------------------")
	new_name = input("Enter your character's name: ")
	print("----------------------")
	player.name = new_name
	input('Press enter to return to starting menu')


def how_to_play():
	print()
	print(" | How To Play")
	print("-"*100)
	print(" - When the game begins your character will spawn into a room in a randomly generated map.")
	print(" - There is a prompt at the bottom of the terminal that allows you to interact with the game.")
	print(" - Use WASD keys to navigate through different rooms.")
	print(" - Along the way you will find items (?) you can pick up or enemies (!) that you can fight.")
	print(" - To interact with an enemy/item, move into the given entity.")
	print()
	print(" | Your Goal ")
	print("-"*100)
	print(" - Your goal is to find the final room in the dungeon and exit at the 'X' to escape.")
	print()
	print(" | What the symbols mean in the map: ")
	print("-"*100)
	print("U - your character\n? - an item\n! - an enemy\nX - the exit to go to the next level\n")
	print()
	input('Press enter to return to starting menu')


def show_start_menu():
	player = myCharacter("Coolio")
	prompt_string = \
		"(S)tart\n" \
		"(O)ptions\n" \
		"(H)ow to Play\n" \
		"(Q)uit\n" \
		'\t>> '
	print('-------------------------')
	print('|    The Quest Begins   |')
	print('-------------------------')
	while True:
		choice = input(prompt_string)
		choice = choice and choice[0].upper()
		if choice == 'S':
			print()
			run_game(player)
			break
		elif choice == 'O':
			print()
			options(player)
		elif choice == 'H':
			print()
			how_to_play()
		elif choice == 'Q':
			print()
			sys.exit(0)
		else:
			print("Invalid input: Please choose from following options: ")


if __name__ == '__main__':
	show_start_menu()
