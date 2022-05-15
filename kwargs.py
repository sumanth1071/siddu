# **kwargs= parameter that will pack all arguments into a dictionary
		# useful so that a fuction can accept a varying amount of keyword arguments

# kwargs means keyword arguments into a dictionary

#prints even having extra key values
def hello(**kwargs):
	print("hello "+kwargs["f_name"] + " "+ kwargs["l_name"])
hello(f_name="siddu",mid="dude",l_name="sumanth")


#iterate through key values
def hello(**info):
	print("hello",end=" ")
	for key,value in info.items():
		print(key,end=" ")
		print(value,end=" ")

hello(title="Mr.",f_name="sumanth",mid="dude",l_name="siddu")


def hello(f_name,l_name):
	print("hello"+f_name+" "+l_name)

hello(f_name="sumanth",mid="dude",l_name="siddu") #raises error because of extra keyword argument

