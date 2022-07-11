# text widget = functions like a text area ,you can enter multiple lines of text

from tkinter import *

def submit():
    input = text.get("1.0",END)
    print(input)

window = Tk()
text = Text(window,bg="beige",fg="purple",font=("magento",25),
                height=20,width=25,padx=10,pady=20)
text.pack()
button = Button(window,text="submit",command=submit)
button.pack()

window.mainloop()
