# multiple-inheritance = when a child is derived from than one parent class
class Organism:
	alive=True

class Prey(Organism):

	def flee(self):
		print("This animal flees")

class Predator(Organism):

	def hunt(self):
		print("This animal is hunting")

class Rabbit(Prey):
	pass

class Hawk(Predator):
	pass

class Fish(Predator,Prey):
	pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

