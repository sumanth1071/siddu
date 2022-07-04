#read a file = read data from a file 

# open and read a file using oprn and read command

# using exception handling if file does not exists

try:
	
	with open("demo.tx") as file:
	
		print(file.read())

except FileNotFoundError:
	
	print("That file was not found :(")
