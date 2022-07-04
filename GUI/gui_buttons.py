# button = you click it, then it does stuff

from tkinter import *

window = Tk()

count = 0

# PhotoImage is used to use a photo in GUI by getting its source location
photo = PhotoImage(file="/Users/sumanth/Desktop/siddu/GUI/icon.png")


# here when click is called it gets the global varibale increment it and then print it

def click():
	global count
	count+=1
	print(count)

button = Button(window,
			text="click me!",
			command=click, # click command is used to give click action for the label
			font=("Comic Sans",40,"bold"),
			# fg="orange",
			bg="blue",
			bd="10",
			padx=30,
			pady=40,
			activeforeground="green",
			activebackground="black",
			state=ACTIVE, #keeping state = ACTIVE keeps the button in a active state
			# state=DISABLED, # #keeping state = DISABLED keeps the button in a inactive state
			image=photo,
			compound="right")


button.pack()
window.mainloop()