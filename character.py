import sys

from collections import Counter
import item_list

class myCharacter:
    def __init__(self, name, max_health, health, damage, defense, inventory_size, item_sword, item_shield):
        self.name = name
        self.max_health = max_health
        self.health = health
        self.damage = damage
        self.defense = defense
        self.inventory_size = inventory_size
        self.inventory = Counter()
        self.item_sword = item_sword
        self.item_shield = item_shield

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
                print("You do not have anymore of that item")
        else:
            print("Inventory is empty")

    def show_inv(self):
        for item, count in self.inventory.items():
            print(" " + item, count)

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
        print("Inventory - " + str(len(self.inventory)) + " item(s):")
        self.show_inv()


## this is to test this file of code
def test():
    c = myCharacter("lol", 10, 12, 0, 0, 5, None, None)
    print(c.damage)
    c.sword_equip(item_list.wooden_stick)
    print(c.damage)
    c.sword_equip(item_list.basic_sword)
    print(c.damage)
    '''
    c.add_item("s potion")
    c.add_item("m potion")
    c.add_item("s potion")
    c.show_inv()
    c.del_item("s potion")
    c.show_inv()
    c.sword_equip(item_list.rusty_sword)
    '''

if __name__ == '__main__':
    test() 

    