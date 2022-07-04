#loop control statement
#break	= terminate the loop
#continue	= skips the iteration
#pass	= does nothing,acts as a placeholder

while True:
	name=input("enter your name! ")
	if name != "":
		break

num="628_1301_949"

for i in num:
	if i=="_":
		continue
	print(i)

for i in num:
	if i == "_":
		pass
	else:
		print(i)