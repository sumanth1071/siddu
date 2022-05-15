

text1="i am sumanth\ni live in vijayawada\n"
#w is used to write data to the file
with open("demo.txt","w") as file:
	file.write(text1)

text="have a nice day"
#a is used to append data to the file
with open("demo.txt","a") as file:
	file.write(text)