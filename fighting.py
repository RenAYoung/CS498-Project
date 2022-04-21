# file to deal with fighting interactions between characters and enemies


# import character and enemy files
import character
import enemy
import random as rand
import item_list as itlist
import time
 



# function to handle overall fight
def fight(self, curr_enemy):
    
    # variable for checking if player successfully fled or not
    flee_status = False
    
    print('fight time!')
    
    # loop that continues while 
    # - player is not dead
    # - enemy is not dead
    # - player has not fled
    while self.health > 0 and curr_enemy.health > 0 and flee_status != True:
        
        # loop to display options for user and check validity
        valid_options = 'AUF'
        action = 'X'
        while action not in valid_options:
            print("\nYour Health:", self.health)
            print("Enemy Health:", curr_enemy.health)
            options_string = \
                "(A)ttack\n" \
                "(U)se Item\n" \
                "(F)lee\n" \
                "Enter Choice: "
            action = input(options_string)[0].upper()
            if action not in valid_options:
                # user input a choice that was not listed, so they need to be reprompted
                print('Invalid Choice. Please choose from the following options: ')
                
        # call function based on user's input action choice
        if action in 'Aa':
            # call attack function
            attack_enemy(self, curr_enemy)
        elif action in 'Uu':
            # call use item function
            use_item(self)
        elif action in 'Ff':
            # call flee function
            flee_status = flee_fight(self, curr_enemy)
        
        # if user has not fled, enemy is not dead, and player is not dead
        if self.health > 0 and curr_enemy.health > 0 and flee_status != True:
            # enemy attacks player
            enemy_attack(self, curr_enemy)

    # return 0 if player died
    if self.health < 1:
        return 0
    # return 1 if enemy died
    elif curr_enemy.health < 1:
        return 1
    # return 2 if neither died
    else: 
        return 2

# function for attacking the enemy
def attack_enemy(self, curr_enemy):
    
    print()
    
    # get player's attack value
    damage = self.damage
    # determine whether it is a critical hit or not
    if rand.random() < 0.2: 
        print("Critical Hit!!!!!! Niiiiice!")
        damage = self.damage * 1.5
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
def use_item(self):
    print("\nInventory: ")
    # display inventory for player
    self.show_inv()
    
    # check if user has any items in inventory
    
    # ask user to type in first letter of item
    choice = input("Which item would you like to use? (type first letter): ")
    val_choice = False
    
    # loop while choice not matching valid option
    while val_choice != True:
        
        # loop through items and check if one matches
        for item, count in self.inventory.items():
            # check if choice found
            if choice == item[0]:
                val_choice = True
                # get amount to heal from item
                heal_amount = itlist.dict_of_items[item].health_recovery
                # add health recovery amount up to max health
                if (self.max_health - self.health) > heal_amount: # if less, add healing
                    self.health += heal_amount
                else: # if greater than difference, just set back to max
                    self.health = self.max_health
                self.del_item(item)
            
            if val_choice == True:
                break
        
        if val_choice != True:
            choice = input("Invalid choice. Try again (type first letter): ")
        
    print("You have", self.health, "health.")



# function for fleeing from the enemy
def flee_fight(self, curr_enemy):
    # get player defense
    play_def = self.defense
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
def enemy_attack(self, curr_enemy):
    
    time.sleep(2)
    
    print("\nEnemy is attacking. \n")
    
    time.sleep(2)
    
    # get enemy attack value
    damage = curr_enemy.damage
    
    # determine whether it's a critical hit or not
    if rand.random() < 0.2: 
        damage = curr_enemy.damage * 1.5
        
    # if player's health (+def) is less than damage amount
    if (self.health + self.defense) < damage:
        # player's health becomes 0
        self.health = 0
        print("Enemy did", self.health + self.defense, "damage.")
    # else - if player's health (+def) is greater than or equal to damage amount
    # but, defense is less than damage
    elif self.defense < damage:
        # take damage off of player
        self.health -= (damage - self.defense)
        print("Enemy did", damage - self.defense, "damage.")
    # else - enemy did no damage
    else:
        print("Enemy did no damage")
        
    time.sleep(2)




def test():
    c = character.myCharacter("lol", 10, 8, 2, 3, 5, None, None)
    en = enemy.Enemy("oof", 15, 4)
    c.add_item("small_potion")
    c.add_item("medium_potion")
    c.add_item("small_potion")
    
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
    
    
test()
    
    
    
    