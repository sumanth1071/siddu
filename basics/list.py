#list = used to store multiple items in a single variable

food = ["pizza",'hamburger','hotdog','ratatoullie']

food[0]="sushi"
print(food[3])
print(food[0])

food.append("ice cream")
food.remove("hotdog")
food.pop()
food.insert(0,"cake")
food.sort()
food.clear()

for x in food:
	print(x)