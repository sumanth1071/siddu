# radio button = similar to checkbox, but only select one from a group
from curses import window
from tkinter import *
from turtle import left

window = Tk()

food = ["burger","pizza","icecream"]

def order():
    if(x.get()==0):
        print("you ordered a "+food[0])
    elif(x.get()==1):
        print("you ordered a "+food[1])
    elif(x.get()==2):
        print("you ordered a "+food[2])
    else:
        print("huh!")

x = IntVar()

pizzaImage = PhotoImage(file="GUI/pizza-icon.png")
burgerImage = PhotoImage(file="GUI/burger-icon.png")
icecreamImage = PhotoImage(file="GUI/ice-Cream-icon.png")

foodimages = [burgerImage,pizzaImage,icecreamImage]

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                            text=food[index],# adds text to radio buttons
                            variable=x,# groups radiobuttons together if they share same variable
                            value=index, # assigns each radiobutton a different value
                            fg="yellow",# add colors to the text
                            padx=30, # adds padding on x-axis
                            pady=35,# adds padding on y-axis
                            font=("Impact",50),# changes font style and size
                            image=foodimages[index],# add images to the radio button
                            compound="left",#add image to the left side
                            indicatoron=0,# eliminate the circle indicators
                            width = 400,
                            command=order)# sets width to the radio button
    radiobutton.pack(anchor=W) #used to shift the group of buttons W(west) E(east)


window.mainloop()