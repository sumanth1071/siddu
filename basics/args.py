# *args = parameter that will pack all arguments into a tuple
	# useful so that a function can accept a varying amount of arguments
# name args can be anything

def add(n1,n2):
	sum=n1+n2
	return sum

print(add(1,2))

def add1(*args):
	sum=0
	args=list(args) #casting a tuple into a list
	args[0]=0 		#work only due to casting the tuple 
					# into list in the upper statement
	for i in args:
		sum +=i
	return sum

print(add1(1,2,3,4,5))

