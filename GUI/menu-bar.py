from tkinter import *

def openfile():
    print("file has been opened")
def savefile():
    print("file has been saved")
def cut():
    print("the text has been cutted")
def copy():
    print("the text have been copied ")
def paste():
    print("the texts have been pasted succesfully")


window = Tk()

openImage = PhotoImage(file="/Users/sumanth/Desktop/siddu/GUI/icon3.png")
saveImage = PhotoImage(file="/Users/sumanth/Desktop/siddu/GUI/icon2.png")
exitImage = PhotoImage(file="/Users/sumanth/Desktop/siddu/GUI/icon1.png")

menubar = Menu(window)
window.config(menu=menubar)

# file menu

fileMenu = Menu(menubar,tearoff=0,font=("magneto",20))
# tearoff(-----) is 0 because to remove lines already exist
menubar.add_cascade(label="File",menu=fileMenu)
# cascade used to create DROP DOWN menu
fileMenu.add_command(label="open",command=openfile,image=openImage,compound="left")
fileMenu.add_command(label="save",command=savefile,image=saveImage,compound="left")
fileMenu.add_separator()
fileMenu.add_command(label="exit",command=quit,image=exitImage,compound="left")

# edit menu

editMenu = Menu(menubar,tearoff=0,font=("magneto",20))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="cut",command=cut)
editMenu.add_command(label="copy",command=cut)
editMenu.add_command(label="paste",command=paste)
window.mainloop()