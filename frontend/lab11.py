from tkinter import *
from PIL import Image,ImageTk

window=Tk()
window.title("LOGIN")
window.geometry("800x600")
my_image=ImageTk.PhotoImage(Image.open("eagle.png"))
my_label=Label(window,image=my_image)
my_label.pack()


window.mainloop()