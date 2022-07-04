from tkinter import *
from tkinter import messagebox
# import messagebox library

def click():
    # showinfo = gives a message 
    messagebox.showinfo(title="This is in an info message",message="do you need anything?")
    
    # showerror = displays an error
    messagebox.showerror(title="This is an error",message="an error occured")
    
    # showwarning = shows warning message
    # using while prompts infinte warning messages 
    # while(True):
        # messagebox.showwarning(title="This is a warning message",message="i am warning you")
    
    # askokcancel = used to ask ok and cancel
    if messagebox.askokcancel(title="ask ok cancel",message="do you want to do the thing"):
        print("You want to do the thing")
    else:
        print("You don't want to do the thing")
    
    # askretrycancel = used to ask 
    if messagebox.askretrycancel(title="ask retry and cancel",message="do you want to retry the thing"):
        print("you retried the thing")
    else:
        print("You cancelled the thing")

    if messagebox.askyesno(title="ask yes or no",message="Do u like pizza"):
        print("I like cake too ;)")
    else:
        print("why the hell do you even don't like cake")

    answer =  messagebox.askyesnocancel(title='ask yes no and cancel',message="do you like pie?")
    if (answer==True):
        print("yeah i like pie")
    elif(answer==False):
        print("WHy do you even eating it then")
    else:
        print("you have dodged the question") 

    answer = messagebox.askquestion(title="ask a question",message="are you a robot")
    if (answer==True):
        print("you are not eligible")
    else:
        print("You are  eligible")


window = Tk()

button  = Button(window,command=click,text="Click Me!")
button.pack()

window.mainloop()