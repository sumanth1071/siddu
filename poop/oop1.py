from car import Car

car1 = Car("ford","mustang",2022,"red")
car2 = Car("honda","civic",2001,"black")

print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)


car2.drive()
car2.stop()
car1.drive()
car1.stop()


car1.wheels=2 #only car1 changes

print(car1.wheels)
print(car2.wheels)

Car.wheels=2 #effects the whole class 
			 #because the class varibale is modified

print(car1.wheels)
print(car2.wheels)