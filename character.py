import sys

from collections import Counter
import item_list

class myCharacter:
    def __init__(self, name, max_health=20, health=20, damage=10, defense=0, inventory_size=5, item_sword=None,
                 item_shield=None, num_killed=None):
        self.name = name
        self.max_health = max_health
        self.health = health
        self.damage = damage
        self.defense = defense
        self.inventory_size = inventory_size
        self.inventory = Counter()
        self.item_sword = item_sword
        self.item_shield = item_shield
        self.num_killed = num_killed

    def add_item(self, item):
        if len(self.inventory) < self.inventory_size:
            self.inventory[item] += 1
        else:
            print("Inventory is full")

    def del_item(self, item):
        if len(self.inventory) > 0:
            if self.inventory[item] > 0:
                self.inventory[item] -= 1
            else:
                #print("You do not have anymore of that item")
                pass
        else:
            print("Inventory is empty")

    def show_inv(self):
        print("-" * 60)
        print("Inventory: ")
        for item, count in self.inventory.items():
            if count:
                print(f" {item} {count}")
        print("-" * 60)

    def use_potion(self, potion):
        # get potion healing amount
        heal_amount = potion.health_recovery
        
        # check for full health
        if self.health == self.max_health:
            print("Your health is full")
        # if difference between current and max health is greater than potion amount
        elif (self.max_health - self.health) > heal_amount:
            self.health += heal_amount # add potion amount
            self.del_item(potion)
        # if difference between current and max health is less than potion amount
        else:
            self.health = self.max_health # go back to full health
            self.del_item(potion)

    def sword_equip(self, sword):
        if self.item_sword != None:
            self.damage -= self.item_sword.attack
        self.item_sword = sword
        self.damage += sword.attack

    def sheild_equip(self, shield):
        if self.item_shield != None:
            self.defense -= self.item_shield.defense
        self.item_shield = shield
        self.defense += shield.defense

    def display_info(self):
        print("Name: " + self.name)
        print("Health: " + str(self.health) + "/" + str(self.max_health))
        print("Damage: " + str(self.damage))
        print("Sword: " + self.item_sword.name)
        print("Shield: " + self.item_shield.name)
        self.show_inv()

    def slay(self):
        self.num_killed += 1

    def reset_character(self):
        self.max_health = 20
        self.health = health
        self.damage = damage
        self.defense = defense
        self.inventory_size = inventory_size
        self.inventory = Counter()
        self.item_sword = item_sword
        self.item_shield = item_shield
        self.num_killed = num_killed



## this is to test this file of code
def test():
    c = myCharacter("lol", 12, 12, 0, 0, 5, None, None)
    c.add_item(item_list.small_potion)
    c.add_item(item_list.medium_potion)
    c.add_item(item_list.small_potion)
    c.use_potion()
    '''
    print(c.damage)
    c.sword_equip(item_list.wooden_stick)
    print(c.damage)
    c.sword_equip(item_list.basic_sword)
    print(c.damage)
    c.sword_equip(item_list.rusty_sword)
    '''

if __name__ == '__main__':
    test() 

    