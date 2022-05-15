import os

source = "demo1.txt"
destination = "/Users/sumanth/Desktop/demo1.txt"

try:
	if os.path.exists(destination):
		print("there is a file already there")
	else:
		os.replace(source,destination)
		print(source+"was moved")
except FileNotFoundError:
<<<<<<< HEAD
	print(source+"was not found")
=======
	print(source+"was not found")
>>>>>>> parent of 89326e1 (Revert "this my python programming")
