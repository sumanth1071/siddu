from tkinter import *

window = Tk()

hot = PhotoImage(file="GUI/hot.png")
labelhot = Label(image=hot)
labelhot.pack()

def submit():
    print("The temperature is: "+str(scale.get())+" degrees C")

scale = Scale(window,
            from_=100,
            to=0,
            length=500,
            orient=VERTICAL, #orientation of scale
            font=("Consolas",20),
            tickinterval=10, #adds numeric indicators for value 
            showvalue=1,# show(1) or hide(0) current value
            resolution=5, #sets the increment of the slider
            troughcolor="YELLOW",
            fg="#FF1C00",
            bg="BLACK") 

scale.set(50) #set the current value of the slider

scale.pack()

cold = PhotoImage(file="GUI/cold.png")
labelcold = Label(image=cold)
labelcold.pack()

button = Button(window,text="submit",command=submit)
button.pack()

window.mainloop()


