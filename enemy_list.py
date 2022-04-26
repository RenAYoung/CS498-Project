from enemy import Enemy

# level 1 enemies
baby_slime = Enemy("Baby Slime", 8, 2)
goblin_scout = Enemy("Goblin Scout", 5, 4)
baby_dragon = Enemy("Baby Dragon", 10, 5)

# level 2 enemies
adult_slime = Enemy("Adult Slime", 20, 5)
goblin_trooper = Enemy("Goblin Trooper", 10, 7)
dragon_youngling = Enemy("Dragon Youngling", 18, 12)

# level 3 enemies
minotaur = Enemy("Minotaur", 30, 15)
goblin_gladiator = Enemy("Goblin Gladiator", 18, 12)
adult_dragon = Enemy("Adult Dragon", 40, 18)

list_of_enemies = [baby_slime, goblin_scout, baby_dragon,
                  adult_slime, goblin_trooper, dragon_youngling,
                  minotaur, goblin_gladiator, adult_dragon]

