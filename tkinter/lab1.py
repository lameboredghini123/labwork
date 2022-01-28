#registration page using pack, place and grid method.

from tkinter import *
nexus=Tk()
nexus.title("registration page")
name=Label(nexus,text="Name").grid(row=0,column=0)
e1=Entry(nexus).grid(row=0,column=1)
email=Label(nexus,text="Email").grid(row=1,column=0)
e2=Entry(nexus).grid(row=1,column=1)
submitButton=Button(nexus,text="proceed").grid(row=4,column=1)

nexus.mainloop()