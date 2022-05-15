class Animal:

	def eat(self):
		print("This animal is eating")

class Rabbit(Animal):
 	
 	def eat(self):
 		print("This rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()
#method-overriding uses it's closest object even 
#that object present in the parent class