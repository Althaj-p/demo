def bmi_value(weight,height):
    bmi = weight/ (height**2)
    return bmi
weight=float(input("enter your body weight in kg :"))
height=float(input("enter your height in meter :"))


print(bmi_value(weight,height))