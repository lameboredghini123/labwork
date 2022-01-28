from tkinter import *
window=Tk()
frame=LabelFrame(window,text="this is my frame",padx=10,pady=10)
frame.pack(padx=50,pady=50)
b=Button(frame,text="dont click here")
b2=Button(frame,text="...here")
b.grid(row=0,column=0)
b2.grid(row=1,column=1)
window.mainloop()