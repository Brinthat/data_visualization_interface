import re
from tkinter import *
i=Tk()
i.geometry('200x250')
i.title('Calculator')
input= StringVar()
func=''
def click(num):
    global func
    func=func+str(num)
    input.set(func)    
def clear():
    global func
    funct=''
    input.set('')
def equal():
    global func
    output = str(eval(func)) 
    input.set(output)
    func= ""
def equals():
    global func
    output = str(eval(str(func)[:-1]))
    input.set(output)
    func= ""    
txt=Entry(i,textvariable=input,font=('Arial 20'),justify='right',width=13)
txt.grid(row=0,column=0)
b1=Button(i,text="←",fg='navyblue',font=('Arial,8'),padx=4,command = lambda:equals())
b1.place(x=10,y=40)
b2=Button(i,text=" C ",fg='navyblue',font=('Arial,8.5'),padx=2.5,command = lambda:clear())
b2.place(x=60,y=40)
b3=Button(i,text=" √ ",font=('Arial,8'),fg='navyblue',padx=4,command = lambda: click('**0.5'))
b3.place(x=110,y=40)
b4=Button(i,text="  / ",font=('arial,8'),fg='navyblue',padx=4,command = lambda: click('/'))
b4.place(x=160,y=40)
b5=Button(i,text=" 7 ",font=('Arial,8'),fg='navyblue',padx=4,command = lambda: click(7))
b5.place(x=10,y=80)
b6=Button(i,text=" 8 ",font=('arial,8'),fg='navyblue',padx=4,command = lambda: click(8))
b6.place(x=60,y=80)
b7=Button(i,text=" 9 ",font=('arial,8'),fg='navyblue',padx=4,command = lambda: click(9))
b7.place(x=110,y=80)
b8=Button(i,text=" * ",font=('arial,8'),fg='navyblue',padx=5,command = lambda: click('*'))
b8.place(x=160,y=80)
b9=Button(i,text=" 4 ",font=('arial,8'),fg='navyblue',padx=4,command = lambda: click(4))
b9.place(x=10,y=120)
b10=Button(i,text=" 5 ",font=('arial,8'),fg='navyblue',padx=4,command = lambda: click(5))
b10.place(x=60,y=120)
b11=Button(i,text=" 6 ",font=('arial,8'),fg='navyblue',padx=4,command = lambda: click(6))
b11.place(x=110,y=120)
b12=Button(i,text="  - ",font=('arial,8'),fg='navyblue',padx=3,command = lambda: click('-'))
b12.place(x=160,y=120)
b13=Button(i,text=" 1 ",font=('arial,8'),fg='navyblue',padx=4,command = lambda: click(1))
b13.place(x=10,y=160)
b14=Button(i,text=" 2 ",font=('arial,8'),fg='navyblue',padx=4,command = lambda: click(2))
b14.place(x=60,y=160)
b15=Button(i,text=" 3 ",font=('arial,8'),fg='navyblue',padx=4,command = lambda: click(3))
b15.place(x=110,y=160)
b16=Button(i,text=" + ",font=('arial,8'),fg='navyblue',padx=3,command =lambda: click('+'))
b16.place(x=160,y=160)
b17=Button(i,text=" .  ",font=('arial,8'),fg='navyblue',padx=4,command = lambda: click('.'))
b17.place(x=10,y=200)
b18=Button(i,text=" 0 ",font=('arial,8,bold'),fg='navyblue',padx=4,command = lambda: click('0'))
b18.place(x=60,y=200)
b20=Button(i,text="= ",font=('arial,8,bold'),fg='navyblue',padx=30,command = lambda: equal())
b20.place(x=110,y=200)




