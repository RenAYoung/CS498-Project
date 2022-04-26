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
        print("-" * 120)
        print("Inventory: ")
        for item, count in self.inventory.items():
            print(f" {item} {count}")
        print("-" * 120)

    def use_item(self):
        if len(self.inventory) <= 0:
            print("Inventory is empty")
            print("You have", self.health, "health.")
        else:
            print("\nInventory: ")
            self.show_inv()
            
            print("---------------")
            for item, count in self.inventory.items():
                beginning = item_list.dict_of_items[item].name[0].upper()
                rest = item_list.dict_of_items[item].name[1:]
                print("(" + beginning + ")" + rest)
            print("(Q)uit")

            choice = input("Input which item you would like to use: ").upper()
            val_choice = False
            
            while val_choice != True:

                if choice in "Q":
                    break
                
                for item, count in self.inventory.items():
                    if choice == item[0].upper():
                        val_choice = True
    
                        if self.health == self.max_health:
                            print("Your health is full")
                            break

                        heal_amount = item_list.dict_of_items[item].health_recovery
                        if (self.max_health - self.health) > heal_amount:
                            self.health += heal_amount
                        else:
                            self.health = self.max_health
                        self.del_item(item)
                    
                    if val_choice == True:
                        break
                
                if val_choice != True:
                    choice = input("Invalid choice. Try again: ")
                
            print("You have", self.health, "health.")

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
    c = myCharacter("lol", 12, 12, 0, 0, 5, None, None)
    c.add_item("small_potion")
    c.add_item("medium_potion")
    c.add_item("small_potion")
    c.use_item()
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

    