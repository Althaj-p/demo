class student:
    def __init__ (self,name,roll):
        self.name=name
        self.roll=roll
        print(self.roll)
    def getdata(self):
        self.name=input("enter your name")
        self.roll=input("enter your roll")
    def putdata(self):
        print("my name is: "+self.name,"\n","my roll  number is: "+self.roll)
obj=student('','')
obj.getdata()
obj.putdata()
