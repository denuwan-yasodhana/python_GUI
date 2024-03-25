import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Software App')
root.iconbitmap('F:\#1_SRQ Robotics\Sample_Projects\icon.ico')

my_img = ImageTk.PhotoImage(Image.open("image.jpg"))
my_label = Label(image=my_img)
my_label.pack()

buttonToExit = Button(root, text="Exit Program", command=root.quit)
buttonToExit.pack()

root.mainloop()