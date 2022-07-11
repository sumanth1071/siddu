from tkinter import *

# grid() = geometry manager that organizes widgets in a table like structure in a 

window  = Tk()

titleLabel = Label(window,text = "Ente ryour info",font =("magento",20)).grid(row=0,column=1)

firstnameLabel = Label(window,text="First name:",width=20,bg="beige").grid(row=1,column=0)
# label = text widget 
# width of the height column is also effects the width of other widgets in the row

firstnameEntry = Entry(window).grid(row=1,column=1)
# Entry = used to enter data

lastnameLabel = Label(window,text="First name:",width=30,bg="orange").grid(row=2,column=0)
lastnameEntqry = Entry(window).grid(row=2,column=1)

emailLabel = Label(window,text="First name:",width=50,bg="maroon").grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)

submitbutton = Button(window,text="SUBMIT").grid(row=4,column=0,columnspan=2) 
#columnspan = used to allocat more than 1 column space for the widget

window.mainloop()