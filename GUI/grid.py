from tkinter import *

# grid() = geometry manager that organizes widgets in a table like structure in a 

window  = Tk()

firstnameLabel = Label(window,text="First name:").grid(row=0,column=0)
firstnameEntry = Entry(window).grid(row=0,column=1)

lastnameLabel = Label(window,text="First name:").grid(row=1,column=0)
lastnameEntsiddury = Entry(window).grid(row=1,column=1)

emailLabel = Label(window,text="First name:").grid(row=2,column=0)
emailEntry = Entry(window).grid(row=2,column=1)

submitbutton = Button(window,text="SUBMIT").grid()

window.mainloop()