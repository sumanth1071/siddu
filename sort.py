# sort() method = used with lists
# sorted() function = used with tuples(iterables)
# using the above function we can sort a tuple by making it into a list
print()
#LISTS
students = ["deku","bakugo","all-might","uravity","todoroki"]

students.sort()
for i in students:
	print(i)
print()

#REVERSE A LIST
students.sort(reverse=True)
for i in students:
	print(i)
print()

#TUPLE
students =("deku","bakugo","all-might","uravity","todoroki")

sorted_students = sorted(students)
for i in sorted_students:
	print(i)
print()

#REVERSE A TUPLE
sorted_students = sorted(students,reverse=True)
for i in sorted_students:
	print(i)
print()

