 #logicalmoperatores (and ,or,not) = used to check if 2 or more conditional statements

temp = int(input("what is the temperature outside?: "))

if not(temp >=0 and temp <=30):
  	print("the temperatre is good today: ")
  	print("go outside")
elif not(temp <0 or temp >30):
	print("the temperature is bad outside")
	print("please stay inside!")