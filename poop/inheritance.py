"""
INHERITANCE:

1.using a class in sub class decreases the repitition of the code
2.classes have child class who can inheit the characteristics of the parent class
3.Child classes can have their own functions
4.each child class can have the access of the parent classes functions by calling them

"""
class Animal:

	alive = True

	def eat(self):
		print("This animal is eating")

	def sleep(self):
		print("This animal is sleeping")

class Rabbit(Animal):
	
	def run(self):
		print("the rabbit is running")

class Fish(Animal):
	def swim(self):
		print("the fish is swimming")

class Hawk(Animal):
	def fly(self):
		print("the hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()
rabbit.run()
fish.swim()
hawk.fly()