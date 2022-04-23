try:
    def division(a,b):
        c=a/b
        return c
    a=int(input("enter first number :"))
    b=int(input("enter second number :"))
    print(division(a, b))

except ValueError as e:
    print("please enter Integer value...")
except ZeroDivisionError as e:
    print(e)
finally:
    print("its finalised")
