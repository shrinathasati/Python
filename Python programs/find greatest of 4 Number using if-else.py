num1=int(input("enter the number1: "))
num2=int(input("enter the number2: "))
num3=int(input("enter the number3: "))
num4=int(input("enter the number4: "))
if(num1>=num2):
    f1=num1
else:
    f1=num2
if(num3>=num4):
    f2=num3
else:
    f2=num4
if(f1>=f2):
    print(f"{f1} is greatest number.")
else:
    print(f"{f2} is greatest number.")