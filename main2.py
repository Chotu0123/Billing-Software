from tkinter import *
from PIL import Image,ImageTk
root =Tk()
photo = PhotoImage(file="b0.png")
Label = Label(root, image=photo)
Label.pack()
root.mainloop()