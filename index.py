# index operator [] = gives access to a sequence's element(str,list,tuples)

name = "siddu sumanth"

if (name[0].islower()):
	name=name.capitalize()
print(name)

f_name=name[0:5].upper()
l_name=name[6:].lower()
l_char=name[-1]
print(l_name)
print(f_name)
print(l_char)