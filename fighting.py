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
    
    print('fight time!')
    
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
            print("Enemy Health:", curr_enemy.health)
            
            # print options
            print("\n(A)ttack")
            # check that there are items to use
            if len(player.inventory) > 0:
                print("(U)se Item")
                valid_options = 'AUF'
            print("(F)lee")
            action = input("Enter Choice: ")[0].upper()
            
            if action not in valid_options:
                # user input a choice that was not listed, so they need to be reprompted
                print('Invalid Choice. Please choose from the following options: ')
                
        # call function based on user's input action choice
        if action in 'A':
            # call attack function
            attack_enemy(player, curr_enemy)
        elif action in 'U' and len(player.inventory) > 0:
            # call use item function
            use_item(player, curr_enemy)
        elif action in 'F':
            # call flee function
            flee_status = flee_fight(player, curr_enemy)
        
        # if user has not fled, enemy is not dead, and player is not dead
        if player.health > 0 and curr_enemy.health > 0 and flee_status != True:
            # enemy attacks player
            enemy_attack(player, curr_enemy)

    # return 0 if player died
    if player.health < 1:
        return 0
    # return 1 if enemy died
    elif curr_enemy.health < 1:
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
def use_item(player, curr_enemy):
    
    print("\nInventory: ")
    # display inventory for player
    player.show_inv()
        
    # ask user to type in first letter of item
    choice = input("Which item would you like to use? (type first letter): ")
    val_choice = False
        
    # loop while choice not matching valid option
    while val_choice != True:
        
        # loop through items and check if one matches
        for item, count in player.inventory.items():
            # check if choice found
            if choice == item[0]:
                val_choice = True
                # get amount to heal from item
                heal_amount = itlist.dict_of_items[item].health_recovery
                # add health recovery amount up to max health
                if (player.max_health - player.health) > heal_amount: # if less, add healing
                    player.health += heal_amount
                else: # if greater than difference, just set back to max
                    player.health = player.max_health
                player.del_item(item)
            
            if val_choice == True:
                break
        
        if val_choice != True:
            choice = input("Invalid choice. Try again (type first letter): ")
        
    print("You have", player.health, "health.")



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
        flee_chance = 1/(enemy_dam - play_def)
    # if player larger, 90% chance to flee
    else:
        flee_chance = 0.9
    
    # get flee randomonized result
    flee_res = rand.random()
    # if flee successful
    if flee_res <= flee_chance:
        # flee
        print("fled. heck yeah!")
        return True
    # else
    else:
        # print failure message
        print("failed to flee. oof")
        return False
        

# function for the enemy attacking the player
def enemy_attack(player, curr_enemy):
    
    time.sleep(2)
    
    print("\nEnemy is attacking. \n")
    
    time.sleep(2)
    
    # get enemy attack value
    damage = curr_enemy.damage
    
    # determine whether it's a critical hit or not
    if rand.random() < 0.2: 
        damage = curr_enemy.damage * 1.5
        
    # if player's health (+def) is less than damage amount
    if (player.health + player.defense) < damage:
        # player's health becomes 0
        player.health = 0
        print("Enemy did", player.health + player.defense, "damage.")
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
    en = enemy.Enemy("oof", 15, 4)
    #c.add_item("sm potion")
    #c.add_item("med potion")
    #c.add_item("sm potion")
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
