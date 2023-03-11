import sys
from tkinter import *
from tkinter import ttk

def timestable():
    print('\n')
    for x in range(1,13):
        m=int(userin.get())
        print('\t\t', (m) , 'X', (x) ,'=', (m*x))




windows=Tk()
windows.geometry('250x250+700+200')
windows.title('multiplication table')
ttk.Label(windows,text='enter number').grid(row=1,column=0)


userin=StringVar()
user=Entry(windows,textvariable=userin).grid(column=1,row=1)

ttk.Button(windows,text='multiply',command=timestable).grid(column=2,row=1)



windows.mainloop()

