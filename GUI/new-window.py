from tkinter import *

def create_window():
    new_window = Toplevel() #Toplevel() = new window 'on top' of other window
                            #linked to botton window
                            #Tk() = new independent window
    old_window.destroy()    #close old window

old_window = Tk()

Button(window,text="create a new window",command=create_window).pack()

old_window.mainloop()