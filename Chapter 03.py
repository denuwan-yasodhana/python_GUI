import tkinter as tk
from tkinter import *

root = Tk()

myButton1 = Button(root, text = "Click me 01!", state=DISABLED)
myButton2 = Button(root, text = "Click me 02!", padx=50, pady=20)

def myClick():
    myLabel = Label(root, text="Look!, I clicked a Button 03")
    myLabel.pack()

myButton3 = Button(root, text = "Click me 03!", command=myClick, fg="yellow", bg="red")

myButton1.pack()
myButton2.pack()
myButton3.pack()

root.mainloop()