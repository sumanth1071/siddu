# duck typing = concept wjhere class of an object is less important than the methods and objects
# class type is not checked if minimum numnber of methods/attributes are present
# "if it walks like a duck and it quack like a duck, then it is a duck"


class Duck:

	def walk(self):
		print("the duck is walking")

	def talk(self):
		print("the duck is quacking")

class Chicken:

	def walk(self):
		print("The chicken is walking")

	def talk(self):
		print("The chicken is walking")

class Person:

	def catch(self,duck):
		duck.walk()
		duck.talk()
		print("You caught the thing!")

person=Person()
duck=Duck()
chicken=Chicken()

person.catch(chicken)