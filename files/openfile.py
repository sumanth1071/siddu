from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="/Users/sumanth/Desktop/siddu/files/demo.txt"#file path
                                    ,title="open file okay?",
                                    filetypes=(("text","*.py"),
                                    # filetypes=(filename,*(* is used to show the files with the extension
                                    #                       (*.* is used to show every type of file).file type)
                                    ("all files","*.*")))
    file = open(filepath,"r")
    # "r" = used to read the file
    # "rb" = used to read binary
    print(file.read())
    file.close()

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()