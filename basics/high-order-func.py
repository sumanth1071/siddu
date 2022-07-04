# higher order function = a function that either:
# 1. accepts a function as an argument
# OR
# 2. return a funtion
#(in python functions are also treated as objects)

def loud(text):
	return text.upper()

def quite(text):
	return text.lower()
def hello(func):
	text = func("hello")
	print(text)

hello(loud)
hello(quite)


#2nd part

# here a function divisor is call of arg 2 of variable divide
# then it return a function dividend
# so assignning a value to the variable functions
# assign value to the returned fucntion

def divisor(x):
	def dividend(y):
		return y/x
	return dividend

divide = divisor(2)
print(divide(10))