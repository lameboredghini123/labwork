from tkinter import *
window=Tk()
e=Entry(window,width=50,bg="blue",fg="green",borderwidth=5,font=20)
e.pack()
def myclick():
    myLabel=Label(window,text="hello"+e.get())
btn=Button(window,text="click me",padx=10,pady=10,command=myclick)
btn.pack()
window.mainloop()