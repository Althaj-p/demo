from tkinter import *
root=Tk()
class demo:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()
        self.p=Button(frame,text="hai",command=self.printmsg)
        self.p.pack()
        Button(frame,text="exit",command=frame.quit).pack()
    def printmsg(self):
        print("hai althaj")
obj=demo(root)
root.mainloop()









root.mainloop()