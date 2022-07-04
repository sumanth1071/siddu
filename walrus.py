# walrus operator :=

# assignment expression aka walrus operator
# assigns values to the variables asa part of a large expression

# example1
happy = True
print(happy)

#using walrus operator
print(sad := False)


# example2
foods = list()

while True:
	food=input("your favorite food is? ")
	if food == "quit":
		break
	foods.append(food)

# using walrus operator
foods = list()

while food := input("your fav food is ?") != "quit":
	foods.append(food)