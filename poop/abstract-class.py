# abstarct class 
# prevents a user from creating an object 
# compels a user to override methods in a child class

# abstarct class = a class which contains one or more abstract methods
# abstract metgid = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod


class Vehicle(ABC):

	@abstractmethod
	# the below method should be instansiate at any cost
	# otherwise the class will not be initiated
	def go(self):
		pass

	@abstractmethod
	def stop(self):
		pass

class Car(Vehicle):
	def go(self):
		print("This is a car")
	def stop(self):
		print("The car is stopped")

class Motorcycle(Vehicle):
	def go(self):
		print("This is a motor cycle")
	def stop(self):
		print("the Motorcycle is stopped")


# vehicle = Vehicle() the abstarct parent class cannot be modified
car = Car()
motor_cycle = Motorcycle()


car.go()
motor_cycle.go()




car.stop()
motor_cycle.stop()