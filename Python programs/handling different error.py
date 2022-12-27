try:
    a=int(input("enter the number1: "))
    b=int(input("enter the number2: "))
    print(f"your answer is {a/b}.")
except ValueError:
    print("please enter the valid number.")
except ZeroDivisionError:
    if a==0 and b==0:
        print(f"0/0 is not defined format.")
    else:
         print(f"your answer is infinity.")

        
except Exception as e:
        print("error is: "+e)