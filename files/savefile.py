from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="/Users/sumanth/Desktop/siddu/files",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("textfile",".txt"),
                                        ("HTML",".html"),
                                        ("All files",".*")
                                    ])
    #before saving the file
    file.write(str(text.get(1.0,END)))
    # filetext=str(text.get(1.0,END))
    # file.write(filetext)s
    # after saving the file editing it using CONSOLE
    filetext = input("enter some text here :")
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text="save",command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()