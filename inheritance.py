class manager:
    # def __init__(self,employer):
    #     self.emp=employer
        # self.emp = "23"
    def details(self):
        print("my name is ")
    def sample(self):
        self.emp1 = input("enter your age:")
        print("my age is",self.emp1)
class worker(manager):
    def __init__(self,workers):
        self.workers=workers
    def workername(self):
        print("worker name is aaa")
class multilevel(worker):
    def sample1(self):
        print("just for rasam")
obj=multilevel("")
obj.details()
obj.workername()
obj.sample()
obj.sample1()




# class A:
#     def __init__(self,a1):
#         self.a1=a1
#     def