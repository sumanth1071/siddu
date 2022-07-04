#nested function calls = function calls inside other functions calls
# inner most functions are resolved first
# returned value is used for input for the outer most function
num=input("enter a whole number")

num=(float(num))
num=(abs(num))
num=(round(num))
print(num)

print(round(abs(float(input("enter a whole positive number: ")))))
