class Car:

	color = None

class Motorcycle:

	color = None

def change_color(vehicle,color):

	vehicle.color = color

car1= Car()#obj1
car2= Car()#obj2
car3= Car()#obj3
bike1= Motorcycle()#obj4

change_color(car1,"red")
change_color(car2,"white")
change_color(car3,"black")
change_color(bike1,"yellow")

print(car1.color)
print(car2.color)
print(car3.color)
print(bike1.color)