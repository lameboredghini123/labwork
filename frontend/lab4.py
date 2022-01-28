from tkinter import *
root=Tk()
def click():
    text1="address:"+mytext.get('1.0',END)
    lbl.config(text=str(text1))
mytext=Text(root,font=20,width=20,height=10)
mytext.place(x=0,y=50)
btn=Button(root,text="click me",font=30,command=click)
btn.place(x=400,y=300)
lbl=Label(root,text="",font=30)
lbl.place(x=200,y=300)
root.mainloop()