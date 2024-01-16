from tkinter import *
from tkinter import messagebox
root=Tk()
def func():
    a=messagebox.askquestion('information','are you a human')
Label(root,text='do you want to continue?').grid(row=1,column=2)
Button(root,text='next',command=func).grid(row=2,column=3)
root.mainloop()