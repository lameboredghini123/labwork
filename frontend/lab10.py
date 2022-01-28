from tkinter import *
window=Tk()
def show():
    myLabel=Label(window,text=var.get()).pack()
var=StringVar()
checkbtn=Checkbutton(window,text="check this box",variable=var,onvalue="on",offvalue="off")
checkbtn.deselect()
checkbtn.pack()
btn=Button(window,text="show selection",command=show).pack()
window.mainloop()