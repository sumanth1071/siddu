from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) #widget that manages a collection of windows/displays

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1,text="tab 1")
notebook.add(tab2,text="tab 2")
notebook.pack(expand=True,fill=BOTH) #expand = expand to fill any space out otherwise used
                           #fill = fill space on x and y axis 

Label(tab1,text="Hello ,this is tab1",width=50,height=50).pack()
Label(tab2,text="Hello ,this is tab2",width=50,height=50).pack()

window.mainloop()