# file for list of all items

# import Item class
from item import Item

# Health Recovery
small_potion = Item('Small Potion', 5, 0, 0, 0)
medium_potion = Item('Medium Potion', 10, 0, 0, 0)
large_potion = Item('Large Potion', 15, 0, 0, 0)

# Health Max Increasing
magic_star = Item('Magic Star', 0, 10, 0, 0)
epic_magic_star = Item('Epic Magic Star', 0, 25, 0, 0)

# Attack
wooden_stick = Item('Wooden Stick', 0, 0, 1, 0)
rusty_sword = Item('Rusty Sword', 0, 0, 2, 0)
basic_sword = Item('Basic Sword', 0, 0, 5, 0)

# Defense
wooden_plank = Item('Wooden Plank', 0, 0, 0, 3)
basic_shield = Item('Basic Shield', 0, 0, 0, 6)

array_of_items = [small_potion, medium_potion, large_potion,
                  magic_star, epic_magic_star,
                  wooden_stick, rusty_sword, basic_sword,
                  wooden_plank, basic_shield]