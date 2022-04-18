# Enemy class
class Enemy:
    
    # initialization function
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    # display basic information about enemy
    def display_info(self):
        print("Name: " + self.name)
        print("Health: " + str(self.health) + "/" + str(self.max_health))
        print("Damage: " + str(self.damage))
    