#required module
from tkinter import *
import pymysql
import matplotlib.pyplot as mat
import numpy as np
import itertools
import os

#initiate tkinter and pymysql
i=Tk()
i.geometry('900x350')
i.title('WORLD COVID DATABASE')
db = pymysql.connect(host='localhost', user='root',password='Mysql@13',database='brintha')
con= db.cursor()

#function to perform
def graph():
    country=tables.get()
    date1.get()
    date2.get()
    date=date1.get()
    dates=date2.get()
    x_axis=[]#create list to append data 
    y_axis=[]
    y_axes=[]
    con.execute("SELECT New_cases FROM region where country='"+country+"' and Date_rep between '"+date+"' and '"+dates+"'")
    for s in con:
        y_axis.append(s)
    con.execute("SELECT date_rep FROM region where country='"+country+"' and Date_rep between '"+date+"' and '"+dates+"'")
    for r in con:
        x_axis.append(r)
    con.execute("SELECT New_deaths FROM region where country='"+country+"' and Date_rep between '"+date+"' and '"+dates+"' ")
    for t in con:
        y_axes.append(t)
    m = np.array((list(itertools.chain.from_iterable(x_axis))))#to form array
    n = np.array((list(itertools.chain.from_iterable(y_axis))))
    mat1=mat.figure(figsize=(13, 6))#graph size
    mat.subplot(1,2,1)#new case graph 
    mat.barh(m,n)
    mat.title("Positive Cases")
    mat.xlabel("No.of.Cases")
    mat.ylabel("Date")
    m = np.array((list(itertools.chain.from_iterable(x_axis))))
    n = np.array((list(itertools.chain.from_iterable(y_axes)))) 
    mat.subplot(1,2,2)#death case graph
    mat.barh(m,n)
    mat.title("Death cases")
    font1 = {'family':'serif','color':'blue','size':20}
    mat.suptitle("COVID DATABASE",fontdict = font1)
    mat.xlabel("No.of.Cases")
    mat1.show()
    path='D:\\'
    newpath=os.path.join(path,country+'.png')
    mat1.savefig(newpath)
def get():
    country=tables.get()
    date1.get()
    date2.get()
    date=date1.get()
    dates=date2.get()
    con.execute("SELECT sum(New_cases) FROM region where country='"+country+"' and Date_rep between '"+date+"' and '"+dates+"'")
    for x in con:
        a.set(x)
    con.execute("SELECT ROUND(avg(Cumulative_cases)) FROM region where country='"+country+"' and Date_rep between '"+date+"' and '"+dates+"'")
    for  y in con:
        b.set(y) 
    con.execute("SELECT sum(New_deaths) FROM region where country='"+country+"' and Date_rep between '"+date+"' and '"+dates+"'")
    for z in con:
        c.set(z)
    con.execute("SELECT ROUND(avg(Cumulative_deaths)) FROM region where country='"+country+"' and Date_rep between '"+date+"' and '"+dates+"'")
    for v in con:
        d.set(v)
def clear():
    a.set("")
    b.set("")
    c.set("")
    d.set("")
    tables.set("Select Country")
    date1.set('yyyy-mm-dd')
    date2.set('yyyy-mm-dd')

#to select table and date
tables= StringVar()
table=tables.set("Select Country")
options=['India','The United Kingdom','China','USA','Canada','Japan','Australia']
drop = OptionMenu( i ,tables,*options)
drop.config(width=20, font=('Helvetica', 12),bg='white',fg='blue')
drop.place(x=10,y=10)
date1=StringVar()
date1.set('2020-01-13')
txt=Entry( i ,textvariable=date1,width=20,font=('Helvetica', 12),bg='white',fg='blue')
txt.place(x=300,y=15)
date2=StringVar()
date2.set('2020-01-31')
txt1=Entry( i ,textvariable=date2,width=20,font=('Helvetica', 12),bg='white',fg='blue')
txt1.place(x=600,y=15)
l5=Label(i,text='Note: Database from "2020-01-03" to "2022-05-31" ',width=50)
l5.place(x=350,y=40)

#button -to get and clear
button=Button(i,text='Get',width=10,bg='yellow',fg='black',command=get)
button.place(x=350,y=70)
clear_btn = Button( text='Clear ',width=7, command=clear,bg='yellow',fg='black')
clear_btn.place(x=200,y=250)
graph=Button( text='Graph',width=7, command=graph,bg='yellow',fg='black')
graph.place(x=265,y=250)

#label and entry for new and total case and death
a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
l1=Label(i,text='Total New Cases',bg='yellow',fg='blue',width=20)
l1.place(x=5,y=130)
e1=Entry(i,textvariable=a,width=20,bg='white',fg='blue')
e1.place(x=200,y=130)
l2=Label(i,text='Avg Cumulative Case',bg='yellow',fg='blue',width=20)
l2.place(x=5,y=160)
e2=Entry(i,textvariable=b,width=20,bg='white',fg='blue')
e2.place(x=200,y=160)
l3=Label(i,text='Total New Deaths',bg='yellow',fg='blue',width=20)
l3.place(x=5,y=190)
e3=Entry(i,textvariable=c,width=20,bg='white',fg='blue')
e3.place(x=200,y=190)
l4=Label(i,text='Avg Cumulative Deaths',bg='yellow',fg='blue',width=20)
l4.place(x=5,y=220)
e4=Entry(i,textvariable=d,width=20,bg='white',fg='blue')
e4.place(x=200,y=220)
db.commit()
i.mainloop()





