# Enemy class
class Enemy:
    
    # initialization function
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage
