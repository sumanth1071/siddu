#  frames = a rectangular container to group and hold widgets together

from tkinter import *

window = Tk()
frame = Frame(window,bg="yellow",bd=5,relief=RAISED)
frame.place(x=150,y=150) # place used for coordinates in a window
# frame.pack(side=BOTTOM)

button = Button(frame,text="W",font =("magneto",20),width=3).pack(side=TOP)
button = Button(frame,text="A",font =("magneto",20),width=3).pack(side=LEFT)
button = Button(frame,text="S",font =("magneto",20),width=3).pack(side=LEFT)
button = Button(frame,text="D",font =("magneto",20),width=3).pack(side=LEFT)

window.mainloop()