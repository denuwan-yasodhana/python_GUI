import tkinter as tk
from tkinter import *

root = Tk()

#Create label
myLabel1 = Label(root, text = "Hello World")
myLabel2 = Label(root, text = "My name is Denuwan")
myLabel3 = Label(root, text = "Age is 26") # can empty like this"   " 

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=2, column=1)

root.mainloop()
