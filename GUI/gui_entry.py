# entry box  = textbox that accepts a sibgle line of user input
from tkinter import *

entry_box = Tk()

def submit():
    username = entry.get()
    print("hello "+username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)


entry = Entry(entry_box,
        font=("Arial",50,"italic"),
        fg="yellow",
        bg="black",
        show="*")
entry.insert(0,"Mr. ")

submit_button= Button(entry_box,
                text="submit",
                font=(None,20),
                command=submit)


delete_button=Button(entry_box,
                text="delete",
                command=delete
                )


backspace_button = Button(entry_box,
                    text="backspace",
                    command=backspace
                    )   


entry.pack(side="left")
submit_button.pack(side="right")
delete_button.pack(side="right")
backspace_button.pack(side="right")

entry_box.mainloop()    