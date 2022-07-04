# filter() = creates a collection of elements from an iterable for which a function returns true

# filter(function,iterable)

friends = [("rachel",19),
			("chandler",20),
			("joey",17),
			("ross",20),
			("phoebe",18),
			("monica",17)]

age  = lambda data:data[1] >= 18

drinking_buddies = list(filter(age,friends))

for i in drinking_buddies:
	print(i)

