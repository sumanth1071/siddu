#nested loop= a loop inside a loop
# 			the "innerloop" finish all of its iterations before finishing
#			one iterations of the outer loop

rows=int(input("how many rows: "))
colums=int(input("how many colums: "))
symbol=input("enter a desired symbol:")

for i in range(rows):
	for j in range(colums):
		print(symbol,end="")
	print()