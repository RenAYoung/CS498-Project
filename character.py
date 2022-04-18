import sys

from collections import Counter

class myCharacter:
    def __init__(self, info, name, max_health, health, damage, inventory_size, item_sword, item_shield):
        self.info = info
        self.name = name
        self.max_health = max_health
        self.health = health
        self.damage = damage
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
            print(item, count)

    def sword_equip(self):
        if self.item_sword != "":
            pass

    def sheild_equip(self):
        if self.item_shield != "":
            pass


## this is to test this file of code
def test():
    c = myCharacter("", "lol", 10, 12, 3, 5, "", "")
    c.add_item("s potion")
    c.add_item("m potion")
    c.add_item("s potion")
    c.show_inv()
    c.del_item("s potion")
    c.show_inv()

if __name__ == '__main__':
    test() 

    