# scope=the region a variable is recognised
# a variable is only available from inside the region it is created
# a global and locally scoped versions of a variable can be created

name="siddu1" #global variable (inside and outside of function)

def display_name():
	name="siddu"  #local scope onkly inside of the function
	print(name)

display_name()
print(name)