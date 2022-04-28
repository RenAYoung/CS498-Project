# file to deal with fighting interactions between characters and enemies


# import character and enemy files
import character
import enemy
import random as rand
import item_list as itlist
import time


# function to handle overall fight
def fight(player, curr_enemy):
	# variable for checking if player successfully fled or not
	flee_status = False
	
	print("-" * 60)
	print('\nFight time! You\'ve approached the', curr_enemy.name)
	print("-" * 60)
	
	# loop that continues while
	# - player is not dead
	# - enemy is not dead
	# - player has not fled
	while player.health > 0 and curr_enemy.health > 0 and flee_status != True:
		
		# loop to display options for user and check validity
		valid_options = 'AF'
		action = 'X'
		while action not in valid_options:
			# print health info
			print("\nYour Health:", player.health)
			print("Your Max Health:", player.max_health)
			print("Your Attack:", player.damage)
			print("Your Defense:", player.defense)
			print(curr_enemy.name, "Health:", curr_enemy.health)
			
			# print options
			print("\n(A)ttack")
			# check that there are items to use
			if len(player.inventory) > 0:
				print("(U)se Item")
				valid_options = 'AUF'
			print("(F)lee")
			print()
			try:
				action = input("\t>> ")[0].upper()
			except:
				action = 'X'
			
			if action not in valid_options:
				# user input a choice that was not listed, so they need to be reprompted
				print('Invalid Choice. Please choose from the following options: ')
		
		# call function based on user's input action choice
		if action in 'A':
			# call attack function
			attack_enemy(player, curr_enemy)
		elif action in 'U' and len(player.inventory) > 0:
			# call use item function
			use_item(player)
		elif action in 'F':
			# call flee function
			flee_status = flee_fight(player, curr_enemy)
		
		# if user has not fled, enemy is not dead, and player is not dead
		if player.health > 0 and curr_enemy.health > 0 and flee_status != True:
			# enemy attacks player
			enemy_attack(player, curr_enemy)
	
	# return 0 if player died
	if player.health < 1:
		print("You have died. Sad times.")
		return 0
	# return 1 if enemy died
	elif curr_enemy.health < 1:
		print("\nCongrats! You defeated the villian. The valley of plenty should toss you a coin.")
		player.slay()
		return 1
	# return 2 if neither died
	else:
		return 2


# function for attacking the enemy
def attack_enemy(player, curr_enemy):
	print()
	
	# get player's attack value
	damage = player.damage
	# determine whether it is a critical hit or not
	if rand.random() < 0.2:
		print("Critical Hit!!!!!! Niiiiice!")
		damage = player.damage * 1.5
	print("You did", damage, "damage to the enemy.")
	# if enemy health is less than damage amount
	if curr_enemy.health < damage:
		# enemy health is 0
		curr_enemy.health = 0
		print("The enemy is dead!!!! Woo")
	# else - if enemy health is greater than or equal to damage amount
	else:
		# take damage off of enemy
		curr_enemy.health -= damage


# function for using an item
def use_item(player):
	if len(player.inventory) <= 0:
		print("Inventory is empty")
		print("You have", player.health, "health.")
	else:
		print("\nInventory: ")
		player.show_inv()
		
		print("---------------")
		for item, count in player.inventory.items():
			if count > 0:
				beginning = item.name[:2].upper()
				rest = item.name[2:]
				print("(" + beginning + ")" + rest)
		
		choice = input("Input which item you would like to use: ").upper()
		val_choice = False
		
		while val_choice != True:
			
			for item, count in player.inventory.items():
				
				if choice == item.name[:2].upper():
					val_choice = True
				
				if val_choice == True:
					# check for health recovery item
					if item.health_recovery > 0:
						# use the potion
						player.use_potion(item)
						
						print("Your health:", player.health)
					# check for max health increasing item
					elif item.health_max_inc > 0:
						# update player's max health
						player.max_health += item.health_max_inc
						# update player's current health
						player.health += item.health_max_inc
						# remove item from inventory
						player.del_item(item)
						
						print("Your health:", player.health)
					# check for sword
					elif item.attack > 0:
						# equip sword
						player.sword_equip(item)
						# remove item from inventory
						player.del_item(item)
						
						print("Your attack has increased to", player.damage)
					# check for shield
					elif item.defense > 0:
						# equip shield
						player.shield_equip(item)
						# remove item from inventory
						player.del_item(item)
						
						print("Your defense has increased to", player.defense)
					break
			
			if val_choice != True:
				choice = input("Invalid choice. Try again: ")


# function for fleeing from the enemy
def flee_fight(player, curr_enemy):
	# get player defense
	play_def = player.defense
	# get enemy attack
	enemy_dam = curr_enemy.damage
	
	# compare enemy and player values based on specific chance values
	# if difference is <= 1, 75% chance to flee
	if abs(play_def - enemy_dam) <= 1:
		flee_chance = 0.75
	# if enemy larger, reciprocal chance of difference between two values
	# ex: enemy has 5, player has 3, chance is 1/2
	elif enemy_dam > play_def:
		flee_chance = 1 / (enemy_dam - play_def)
	# if player larger, 90% chance to flee
	else:
		flee_chance = 0.9
	
	# get flee randomonized result
	flee_res = rand.random()
	# if flee successful
	if flee_res <= flee_chance:
		# flee
		print("-" * 60)
		print("You've Fled the Fight!")
		print("-" * 60)
		return True
	# else
	else:
		# print failure message
		print("-" * 60)
		print("Failed to flee. OOF!")
		print("-" * 60)
		return False


# function for the enemy attacking the player
def enemy_attack(player, curr_enemy):
	time.sleep(1.5)
	
	print("\nEnemy is attacking. \n")
	
	time.sleep(1)
	
	# get enemy attack value
	damage = curr_enemy.damage
	
	# determine whether it's a critical hit or not
	if rand.random() < 0.2:
		damage = curr_enemy.damage * 1.5
	
	# if player's health (+def) is less than damage amount
	if (player.health + player.defense) < damage:
		print("Enemy did", player.health + player.defense, "damage.")
		# player's health becomes 0
		player.update_health(0)
	# else - if player's health (+def) is greater than or equal to damage amount
	# but, defense is less than damage
	elif player.defense < damage:
		# take damage off of player
		player.health -= (damage - player.defense)
		print("Enemy did", damage - player.defense, "damage.")
	# else - enemy did no damage
	else:
		print("Enemy did no damage")
	
	time.sleep(2)


def test():
	c = character.myCharacter("lol", 10, 8, 2, 3, 5, None, None)
	en = enemy.Enemy("oof", 15, 30)
	c.add_item(itlist.small_potion)
	c.add_item(itlist.medium_potion)
	c.add_item(itlist.magic_star)
	c.add_item(itlist.basic_sword)
	# c.add_item("sm potion")
	print(len(c.inventory))
	
	fight(c, en)
	
	'''
    print("c def: ", c.defense)
    print("en dam: ", en.damage)
    
    flee_fight(c, en)
    
    flee_fight(c, en)
    
    print("h1: ", en.health)
    attack_enemy(c, en)
    print("h2: ", en.health)
    attack_enemy(c, en)
    print("h3: ", en.health)
    '''


if __name__ == '__main__':
	test()
