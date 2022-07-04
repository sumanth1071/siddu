# list comprehension = a way to create new list by using less syntax
# can mimic certain lambda functions,easier to read

# list = [expression for item in iterable ]
# list = [expression for item in iterable if condition]
# list = [expression if/else condition for item in iterable]

students = [100,90,80,70,60,50,40,30,20]

passed_studnets = list(filter(lambda x:x>=50,students))

print(passed_studnets)

passed_studnets = [i for i in students if i>=50]

print(passed_studnets)

passed_studnets = [i if i >= 50 else "FAILED" for i in students]

print(passed_studnets)