from tkinter import *
window=Tk()
def add():
    if var.get()==1:
        print("male")
    else:
        print("female")
var=IntVar()
r1=Radiobutton(window,text="male",variable=var,value=1,command=add)
r1.pack(anchor=W)
r2=Radiobutton(window,text="female",variable=var,value=1,command=add)
r2.pack(anchor=E)

