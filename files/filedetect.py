import os

path = "/Users/sumanth/Desktop/siddu"

if os.path.exists(path):
	print("the location does exists")
	if os.path.isfile(path):
		print("that is a file")
	elif os.path.isdir(path):
		print("it is a directory")
else:
	print("that location doesn't exist!")