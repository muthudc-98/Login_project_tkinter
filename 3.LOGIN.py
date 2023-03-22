from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb=mysql.connector.connect(host='localhost',user='root',password='',database='shop')
mycursor=mydb.cursor()
a=Tk()
a.title('Login Page...')
a.geometry('350x500')

'''j=0
r=0
for i in range(100):
    c=str(222222+r)
    Frame(a,width=10,height=500,bg='#'+c).place(x=j,y=0)
    j=j+10
    r=r+1 '''

Frame(a,width=500,height=500,bg='purple').place(x=0,y=0)

Frame(a,width=250,height=400,bg='white').place(x=50,y=50)
l1=Label(a,text='Username',bg='white')
l=('rockwell',15)    
l1.config(font=l)
l1.place(x=80,y=200)    
en=Entry(a,width=20,border=0)
en.config(font=l)
en.place(x=80,y=230)
l2=Label(a,text='Password',bg='white')
l=('rockwell',15)
l2.config(font=l)
l2.place(x=80,y=280)
en_1=Entry(a,width=20,border=0)
en_1.place(x=80,y=310)
Frame(a,width=180,height=2,bg='black').place(x=80,y=250)
Frame(a,width=180,height=2,bg='black').place(x=80,y=330)
image2=PhotoImage(file='reg1.png')
label1=Label(image=image2,border=0,justify='center')
label1.place(x=105,y=80)
def process():
    name1=Entry.get(en)
    password=Entry.get(en_1)
    sql=('select * from login where name = %s and password= %s')
    na=(name1,password)
    mycursor.execute(sql,na)
    v=mycursor.fetchall()
    mydb.commit()
    if v:
        messagebox.showinfo('LOGIN','Successfull Login')
    else:
        messagebox.showinfo('Error','Incorrect Username or password.....!')
        
btn=Button(a,width=7,height=1,fg='white',bg='dark green',border=4,command=process,text='Login',font=('Times new roman',16,'bold'))
btn.place(x=113,y=375)
a.mainloop()