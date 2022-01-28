from tkinter import *
root=Tk()
root.title("GUI")
root.maxsize(width=600,height=300)
root.minsize(width=600,height=300)
def add():
    x=var.get()
    print(x)
    mylabell.config(text=x,bg="green")
mylabel=Label(root,text="username",fg="red",bg="yellow")
mylabel.place(x=10,y=10)
mylabell=Label(root,text="nothing",fg="red",bg="yellow")
mylabell.place(x=40,y=120)
var=StringVar()
ent=Entry(root,bg="black",fg="white",textvariable=var)
ent.place(x=80,y=10)
btn=Button(root,text="submit",bg="green",fg="white",command=add)
btn.place(x=20,y=80)
root.mainloop()

#stringvar() is used when we know that there is only string to be used
#in that function.
#intvar() is used when some integers are inside the function to do some 
#calculation
#x=var.get()
#.get() is used to fetch the data stored in database, which here is var
