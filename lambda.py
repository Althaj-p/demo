# x=lambda a,b,c,:a+b+c
# print(x(2,3,4))

def add():
    return lambda a,b,c:a+b+c
num1=add()
print(num1(2,3,5))