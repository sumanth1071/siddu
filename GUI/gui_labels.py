from tkinter import *

# label = an area widget that holds text and / or an image within a window

window = Tk()

photo = PhotoImage(file="/Users/sumanth/Desktop/siddu/GUI/icon.png")

label = Label(window,
		text="hello world "+"bro do you even code",
		font=("Arial",50,
		"bold"), #text family,size,style
		fg="orange", #foreground
		bg="blue", #background
		# relief=SUNKEN, #border 
		# relief=RAISED, #border
		bd=10, #border width
		padx=20, #padding horizontally
		pady=30, #padding vertically
		image=photo,
		compound='bottom' #placing of the image 
		)
label.pack()
# label.place(x=10,y=100)

window.mainloop()