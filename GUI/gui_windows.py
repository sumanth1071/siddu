from tkinter import *
# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() #instantiate an instance of a window
window.geometry("500x500") #dimesnions of the window
window.title("my first GUI program")# title for the window

icon = PhotoImage(file="GUI/icon.png")
window.iconphoto(True,icon)# to get the icon image of the file
window.config(background = "#ed6039") #background color for the window
window.mainloop()