items= {
    "nike":500,
    "addidas":600,
    "puma":700,
}
print("available products are...\n""1.nike\n""2.addidas\n""3.puma")
a=input("choose your product :")
print(a)
if a=="nike":
    print(items["nike"])
elif a=="addidas":
    print(items["addidas"])
else:
    print("price of puma is : 700")


