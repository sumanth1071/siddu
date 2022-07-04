# reduce() = apply a function to an iterable and reduce it into a single cumulative value

# usually performs funtion on first 2 elements and repeats process until 1 value remains

# reduce(function,iterable)


import functools

letters = ["h","e","l","l","o"]

word = functools.reduce(lambda x,y:x+y,letters)

print(word)


numbers = [1,2,3,4,5]

factorial = functools.reduce(lambda x,y:x*y,numbers)

print(factorial)