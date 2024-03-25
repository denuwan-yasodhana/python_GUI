import tkinter as tk
from tkinter import *

root = Tk()

e1 = Entry(root, width=50)
e2 = Entry(root, width=50, borderwidth=5)
e1.pack()
e2.pack()

e3 = Entry(root, width=50)
e3.pack()

def myClick():
    myLabel = Label(root, text=e3.get())
    display = "Hello " + e3.get()
    myLabel2 = Label(root, text= display)
    myLabel.pack()
    myLabel2.pack()

myButton3 = Button(root, text = "Click me 03!", command=myClick )

myButton3.pack()

root.mainloop()