#for loop = a statement that will execute its block of code 
# a limited amount of time
#		while loop=unlimited
#		for loop=limited
import time
for i in range(10):
	print(i+1)

for i in range(50,100+1,2):
	print(i)

for i in "sumanth":
	print(i)

for seconds in range(10,0,-1):
	print(seconds)
	time.sleep(0.5)
print("HAPPY NEW YEAR!")

for stop in range(20,0,-1):
	print(stop)
	time.sleep(0.5)
print("hi mummy")