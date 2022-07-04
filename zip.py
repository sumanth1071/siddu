# zip(*iterables) = aggregate elements from 2 or more iterables (list,tuples,sets,etc.)
# creates a zip object with paired elements stored in tuples for each element within the zip object

usernames = ["sumanth","siddu","mister"]
passwords = ("pa@sword","AbC10295@","miss")
login_date = {"10/10/2002","11/10/2002","30/11/2002"}

users_date = zip(usernames,passwords,login_date)
print(type(users_date))
for i in users_date:
	print(i)

users = dict(zip(usernames,passwords))
print(type(users))
for key,value in users.items():
	print(key+" "+value)