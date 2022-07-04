# map() = applies a function to each item in an iterable (list,tuple ,etc.)

# map(funtion,iterable)

store = [("shirt",20.00),
		("pants",15.00),
		("jackets",50.00),
		("socks",10.00)]

to_euros = lambda data:(data[0],data[1]*0.8)

store_euros = list(map(to_euros,store))

for i in store_euros:
	print(i)

print()

to_dollars = lambda data:(data[0],data[1]/0.8)

store_dollars = list(map(to_dollars,store))

for i in store_dollars:
	print(i)

print()