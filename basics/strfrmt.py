#str.format() = optional method that gives users
#				more control while displaying output

animal = "cow"
item = "moon"

print("the "+animal+" jumped over the "+item)
print("the {} jumped over the {}".format(animal,item))
print("the {1} jumped over the {0}".format(animal,item)) #positional arguments
print("the {animal} jumped over the {item}".format(animal="lion",item="moon"))# keyword argument

#using mutliple times

print("the {1} jumped over the {1}".format(animal,item)) #positional arguments
print("the {animal} jumped over the {animal}".format(animal="lion",item="moon"))# keyword argument

#using as a variable

text="the {1} jumped over the {0}"
print(text.format(animal,item))


name = "siddu"

print("hello, my name is {}".format(name))

#for spacing or padding 
print("hello, my name is {name:10}. nice to meet you".format(name="sumanth"))
print("hello, my name is {:10}. nice to meet you".format(name))
print("hello, my name is {:<10}. nice to meet you".format(name))#left
print("hello, my name is {:>10}. nice to meet you".format(name))#right
print("hello, my name is {:^10}. nice to meet you".format(name))#centre


#formating numbers
num=1838030039392

#for float to show 2 decimal places
print("the number pi is {:.2f}".format(num))
#(,) after thousands place
print("the number pi is {:,}".format(num))
#convert to binary
print("the number pi is {:b}".format(num))
#convert to octal
print("the number pi is {:o}".format(num))
#convert to hexadecimal
print("the number pi is {:X}".format(num))
#convert to exponent
print("the number pi is {:E}".format(num))








