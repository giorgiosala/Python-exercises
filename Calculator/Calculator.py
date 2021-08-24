#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 14:19:46 2021

@author: giorgiosala
"""

from tkinter import *


root=Tk()
root.title("Simple calculator")

#Create an entry
e=Entry(root, width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

f_num=0
op=0
def buttonclick(number):
    #
    current= e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
    
def buttonclear():
    e.delete(0,END) 
    global f_num
    f_num=0

def buttonadd(): 
    firstnumber=e.get()
    global f_num
    global op
    f_num= int(f_num) + int(firstnumber)
    op=1
    print("fnum"+str(f_num))
    e.delete(0,END)
    
    
    
def buttonminus():
    global f_num
    if f_num==0:
        f_num=e.get()
    else:
        firstnumber=e.get()
        
        global op
        f_num= int(f_num) - int(firstnumber)
    print("fnum"+str(f_num))
    op=2
    e.delete(0,END)
    
  

def buttonequal():
    secondnumber=e.get()
    print("seconfnumber="+secondnumber)
    e.delete(0,END)
    global f_num
    global op
    print("op="+str(op))
    if op==1:
        e.insert(0, int(f_num) + int(secondnumber))
    elif op==2:
        e.insert(0, int(f_num) - int(secondnumber))
  

    
#create a button  

button1 = Button(root, text="1",padx=40,pady=20, command=lambda: buttonclick(1))
button2 = Button(root, text="2",padx=40,pady=20, command=lambda: buttonclick(2))
button3 = Button(root, text="3",padx=40,pady=20, command=lambda: buttonclick(3))

button4 = Button(root, text="4",padx=40,pady=20, command=lambda: buttonclick(4))
button5 = Button(root, text="5",padx=40,pady=20, command=lambda: buttonclick(5))
button6 = Button(root, text="6",padx=40,pady=20, command=lambda: buttonclick(6))

button7 = Button(root, text="7",padx=40,pady=20, command=lambda: buttonclick(7))
button8 = Button(root, text="8",padx=40,pady=20, command=lambda: buttonclick(8))
button9 = Button(root, text="9",padx=40,pady=20, command=lambda: buttonclick(9))

button0 = Button(root, text="0",padx=40,pady=20, command=lambda: buttonclick(0))

buttonadd=  Button(root, text="+",padx=39,pady=20, command=buttonadd)
buttonminus=  Button(root, text="-",padx=39,pady=20, command=buttonminus)
buttonmultiply=  Button(root, text="x",padx=39,pady=20, command=lambda: buttonclick())
buttondivide=  Button(root, text=":",padx=39,pady=20, command=lambda: buttonclick())

buttonequal=  Button(root, text="=",padx=100,pady=20, command=buttonequal)
buttonclear=  Button(root, text="Clear",padx=89,pady=20, command=buttonclear)
#put button on screen

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)

buttonadd.grid(row=1,column=3)
buttonminus.grid(row=2,column=3)
buttonmultiply.grid(row=3,column=3)
buttondivide.grid(row=4,column=3)


buttonequal.grid(row=4,column=1,columnspan=2)
buttonclear.grid(row=5,column=1,columnspan=2)

  



root.mainloop()

"""

def myclick():
    #Create a label
    mylabel= Label(root, text="hello "+ e.get())
 """