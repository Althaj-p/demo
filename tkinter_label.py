from tkinter import *
root=Tk()
f=Frame(root)
f.pack()
def login():
    print("you are logged in")
Label(f,text="hello world",bg="red").pack()
Label(f,text="i am here",fg="black").pack()
Button(f,text="login",command=login).pack()
Button(f,text="exit",command=f.quit).pack()
root.mainloop()