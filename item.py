# Item class file

# create Item class
class Item:
	
	# create initialization function for Item class
	def __init__(self, name, health_recovery, health_max_inc, attack, defense):
		self.name = name
		self.health_recovery = health_recovery
		self.health_max_inc = health_max_inc
		self.attack = attack
		self.defense = defense
	
	def __str__(self):
		return self.name
	
	def __repr__(self):
		return self.name
