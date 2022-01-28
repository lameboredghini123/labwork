from tkinter import *
from PIL import Image,ImageTk
window=Tk()
window.geometry("500x500")
image=Image.open("sunflower.jpg")
image=image.resize((500,300),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
label=Label(window,image=photo)
label.pack()
window.mainloop()