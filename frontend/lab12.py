from tkinter import *
from PIL import Image,ImageTk
window=Tk()
window.maxsize(width=300,height=200)
window.minsize(width=300,height=200)
photo2=Image.open("eagle.ping")
resized_image=photo2.resize(300,250),Image.ANTIALIAS
converted_image=imageTk.PhotoImage(resized_image)
lbl=Label(window,image=converted_image,width=300,height=180)
lbl.pack(pady=10)
window.mainloop()