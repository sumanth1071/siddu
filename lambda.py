# lambda function = function written in 1 line using lamda keyword
# you can also write in two lines but it doesm't make sense of using it then
# lambda characteristics:

	# arguments = any number
	# expression = only one

# it is a shortcut 
# useful if needed for a short period of time
# later throw away

# usual method

def double(x):
	return x*2

print(double(2))

#using lambda

double = lambda x:x*2
print(double(2))

# 2 args
multiply = lambda x,y:x*y
print(multiply(2,3))

# 3 args
add = lambda x,y,z: x+y+z
print(add(1,2,3))

# strings
full_name = lambda f_name,l_name:\
f_name+" "+l_name
print(full_name("siddu","sumanth"))

#boolean
age_check = lambda age:True if age >= 18 else False
print(age_check(20))