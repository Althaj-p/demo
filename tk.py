from tkinter import*
import pymysql
x=pymysql.connect(host='localhost',user='root',password='123321',database='shop')
cur=x.cursor()
t=Tk()
Label(text='name').place(x=10,y=10)
nm=Entry()
nm.place(x=50,y=15)
def abcd():
    n=nm.get()
    cur.execute('insert into employees values(%s)',n)
    x.commit()
    x.close()
    t.destroy()
Button(text='submit',command=abcd).place(x=10,y=45)
t.mainloop()