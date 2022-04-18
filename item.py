# Item class file

# create Item class
class Item:
    
    # create initialization function for Item class    
    def __init__(self, name):
        self.name = name 
        
    def apply_effect():
        pass
    
    def get_value(self):
        pass
        
    
# create Health class for health recovery items
class Health(Item):
    
    def __init__(self, name, health_recovery):
        Item.__init__(self, name)
        self.health_recovery = health_recovery
        
    def get_value(self):
        return self.health_recovery



# create MaxHealth class for max health increasing items
class MaxHealth(Item):
    
    def __init__(self, name, health_max_inc):
        Item.__init__(self, name)
        self.health_max_inc = health_max_inc
        
    def get_value(self):
        return self.health_max_inc


# create Attack class for attack based items
class Attack(Item):
    
    def __init__(self, name, attack):
        Item.__init__(self, name)
        self.attack = attack
        
    def get_value(self):
        return self.attack


# create Defense class for defense based items
class Defense(Item):
    
    def __init__(self, defense):
        self.defense = defense
        
    def get_value(self):
        return self.defense