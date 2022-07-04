#if  statement =a block of code that will execute if its condition is true

age=int(input("enter ur age: "))

if age==100:
	print("u are already dead!")
elif age>=18:
	print("you are an adult!")
elif age<0:
	print("u haven't been born yet!")
else:
	print("you are a child!")
