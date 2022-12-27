try:
    age=int(input("enter the age: "))
    if(age>=18):
        print("you are eligible for voting...")
    else:
       
        print("you are not eligible for voting...")
except:
    raise ValueError("sandhya please enter a valid number.")

