try:
    a=int(input("enter a number: "))
    b=1/a
    print(b)
except Exception as e:
    print(e)
else:
    print("you have done.")