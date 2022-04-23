dict1={
    1:"althaj",
    2:"rafa",
    3:"sfa"
}
print(dict1.get(1))
print(dict1[3])
print(dict1.get(4,"key not found"))
# for changing the values
dict1[1]="alfa"
print(dict1)
for i in dict1:
    print(dict1[i])
if "rafa" in dict1:
    print("avilable")
# for addding new one
# dict1[4]="alfa"
# print(dict1)
dict1.pop(1)
print(dict1)
dict1.popitem()
print(dict1)
# dict2=dict1.copy
# print(dict1)
mydic=dict(dict1)
print(mydic)
new=dict(a="car",b="bus")
print(new)
print(dict1)