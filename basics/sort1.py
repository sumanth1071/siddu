# sort() method = used with lists
# sorted() function = used with tuples(iterables)
# using the above function we can sort a tuple by making it into a list
print()
students = [("deku",'A',15),
			("all-might",'S',45),
			("bakugo",'B',15),
			("todoroki",'A',14),
			("uravity","C",14)]

students.sort()

for i in students:
	print(i)
print()

age = lambda ages:ages[2]
students.sort(key=age,reverse=True)

for i in students:
	print(i)
print()

# TUPLE

students = (("deku",'A',15),
			("all-might",'S',45),
			("bakugo",'B',15),
			("todoroki",'A',14),
			("uravity","C",14))
garde = lambda gardes:gardes[1]
sorted_students = sorted(students,key=garde)


for i in sorted_students:
	print(i)
print()