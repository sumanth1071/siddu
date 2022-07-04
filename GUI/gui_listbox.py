# listbox = a listing of selectable text items within it's own container
from ctypes import sizeof
from tkinter import *

window = Tk()

def submit():
    # for selecting single object in list
    # print(listbox.get(listbox.curselection()))
    
    food=[] #list food has to be created to store multiple items
    for index in listbox.curselection(): #accessing the index of 
                                        # listbox current element
        food.insert(index,listbox.get(index)) # storing that index in list 
                                            # along with index element
    print("You have ordered: ",end="")
    for index in food:
        print(index)
    
def add():
    # using entry adding elements
    listbox.insert(listbox.size(),entrybox.get())# inserting the index and element entered in the entry box
    listbox.config(height=listbox.size())

def delete():
    # deleting the mutilple elements
    # reverse is used because after deleteing an element the index
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())
    # the below can only delete only one objct in the listbox
    # listbox.delete(listbox.curselection())


listbox = Listbox(window,
                bg="pink",
                fg="green",
                font=("Arial",20,"bold"),
                width=10,
                selectmode=MULTIPLE #used to select multiple elements in a listbox
                )
listbox.pack()


# listbox.insert should be used seperatly
# to insert elements in to list box
listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"burger")
listbox.insert(4,"taco")
listbox.insert(5,"soup")

# change the size of the listbox
# config is used to make independent changes
# listbox.size() is correct
# sizeof(listbox) is incorrect
listbox.config(height=listbox.size())

entrybox = Entry(window)
entrybox.pack()

submitbutton = Button(window,text="submit",command=submit)
submitbutton.pack()

addbutton = Button(window,text="add",command=add)
addbutton.pack()

deletebutton = Button(window,text="delete",command=delete)
deletebutton.pack()

window.mainloop()
