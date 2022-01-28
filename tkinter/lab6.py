#carry out arithmetic operations of two numbers

from tkinter import *
class MyWindow:
    def __init__(aa, win):
        aa.lbl1=Label(win, text='First number')
        aa.lbl2=Label(win, text='Second number')
        aa.lbl3=Label(win, text='Result')
        aa.t1=Entry(bd=3)
        aa.t2=Entry()
        aa.t3=Entry()
        aa.btn1 = Button(win, text='Add')
        aa.btn2=Button(win, text='Subtract')
        aa.btn3=Button(win,text="Multilication")
        aa.btn4=Button(win,text="Division")
        aa.lbl1.place(x=100, y=50)
        aa.t1.place(x=200, y=50)
        aa.lbl2.place(x=100, y=100)
        aa.t2.place(x=200, y=100)
        aa.b1=Button(win, text='Add', command=aa.add)
        aa.b2=Button(win, text='Subtract')
        aa.b2.bind('<Button-1>', aa.sub)
        aa.b3=Button(win,text="Multiplication")
        aa.b3.bind('<Button-1>',aa.nul)
        aa.b4=Button(win,text="Divisin")
        aa.b4.bind('<Button-1>',aa.div)
        aa.b1.place(x=100, y=150)
        aa.b2.place(x=200, y=150)
        aa.b3.place(x=300,y=150)
        aa.b4.place(x=400,y=150)
        aa.lbl3.place(x=100, y=200)
        aa.t3.place(x=200, y=200)
    def add(aa):
        aa.t3.delete(0, 'end')
        num1=int(aa.t1.get())
        num2=int(aa.t2.get())
        result=num1+num2
        aa.t3.insert(END, str(result))
    def sub(aa, event):
        aa.t3.delete(0, 'end')
        num1=int(aa.t1.get())
        num2=int(aa.t2.get())
        result=num1-num2
        aa.t3.insert(END, str(result))
    def nul(aa, event):
        aa.t3.delete(0, 'end')
        num1=int(aa.t1.get())
        num2=int(aa.t2.get())
        result=num1*num2
        aa.t3.insert(END, str(result)) 
    def div(aa, event):
        aa.t3.delete(0, 'end')
        num1=int(aa.t1.get())
        num2=int(aa.t2.get())
        result=num1/num2
        aa.t3.insert(END, str(result))       

window=Tk()
mywin=MyWindow(window)
window.title('Tkinter Arthematic operations')
window.geometry("700x500+10+10")
window.mainloop()