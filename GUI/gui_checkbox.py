
from tkinter import *

window = Tk()

def display():
    if(x.get()==1 or x.get=="yes" or x.get()):
        print("You agree")
    else:
        print("You don't agree")

x = IntVar()
x = StringVar()
x = BooleanVar()
photo = PhotoImage(file="GUI/icon.png")

check_button = Checkbutton(window,
                    text="I agree to something",
                    variable=x,
                    # onvalue=1,
                    # offvalue=0,
                    onvalue="yes",
                    offvalue="no",
                    # onvalue=True,
                    # offvalue=False,
                    command=display,
                    font=("Arial",20),
                    bg="yellow",
                    fg="black",
                    activebackground="yellow",
                    activeforeground="black",
                    padx=25,
                    pady=25,
                    image=photo,
                    compound="left")

check_button.pack(side="left")
window.mainloop()