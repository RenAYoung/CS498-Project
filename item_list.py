# file for list of all items

# import Item class
from item import Item
import random

# Health Recovery
small_potion = Item('Small Potion', 5, 0, 0, 0)
medium_potion = Item('Medium Potion', 10, 0, 0, 0)
large_potion = Item('Large Potion', 15, 0, 0, 0)
mysterious_liquid = Item('Mysterious Liquid', random.randint(1, 6), 0, 0, 0)
glowing_mysterious_liquid = Item('Glowing Mysterious Liquid', random.randint(1, 11), 0, 0, 0)

# Health Max Increasing
magic_star = Item('Magic Star', 0, 10, 0, 0)
star_drop_magic = Item('Star Drop (magic)', 0, 15, 0, 0)
epic_magic_star = Item('Epic Magic Star', 0, 25, 0, 0)

# Attack
wooden_stick = Item('Wooden Stick', 0, 0, 1, 0)
nail_rusty = Item('Nail (Rusty)', 0, 0, 2, 0)
rusty_sword = Item('Rusty Sword', 0, 0, 3, 0)
beginner_sword = Item('Beginner\'s Sword', 0, 0, 5, 0)
gold_sword = Item('Gold Sword', 0, 0, 8, 0)
sword_iron = Item('Sword (Iron)', 0, 0, 10, 0)
diamond_sword = Item('Diamond Sword', 0, 0, 15, 0)

# Defense
wooden_plank = Item('Wooden Plank', 0, 0, 0, 2)
thick_playing_card = Item('Thick Playing Card', 0, 0, 0, 3)
basic_shield = Item('Basic Shield', 0, 0, 0, 6)
iron_shield = Item('Iron Shield', 0, 0, 0, 9)
shield_steel = Item('Shield (Steel)', 0, 0, 0, 12)
fancy_vest = Item('Fancy Vest', 0, 0, 0, 15)

array_of_items = [small_potion, medium_potion, large_potion, mysterious_liquid, glowing_mysterious_liquid,
                  magic_star, star_drop_magic, epic_magic_star,
                  wooden_stick, nail_rusty, rusty_sword, beginner_sword, gold_sword, sword_iron, diamond_sword,
                  wooden_plank, thick_playing_card, basic_shield, iron_shield, shield_steel, fancy_vest]
