from tkinter import *
from tkinter import colorchooser #sub module

def click():
# 3 lines of code
    color = colorchooser.askcolor()
    # print(color)
    colorHex=color[1]
    # print(colorHex)
    window.config(bg=colorHex) #change background color

# 2 lines of code
    color = colorchooser.askcolor()
    window.config(bg=color[1])

# 1 line of code
    window.config(bg=colorchooser.askcolor())

window=Tk()
window.geometry("150x150")
button=Button(text="click me",command=click)
button.pack()
window.mainloop()
