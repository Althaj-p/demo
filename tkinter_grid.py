from tkinter import *
root=Tk()
# def saved(self):
#     print("saved details")
Label(root,text="username").grid(row=0,column=0)
Label(root,text="password").grid(row=1,column=0)
Entry(root).grid(row=0,column=1)
Entry(root).grid(row=1,column=1)
# Button(root,text="cancel",command=root.quit).pack()
# Label(root,text="save",command=self.saved).pack()
# def saved():
#     print("saved details")
root.mainloop()