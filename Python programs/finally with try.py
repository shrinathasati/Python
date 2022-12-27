try:
    a=int(input("enter a number: "))
    b=1/a
except Exception as e:
    print("error message is:",e)
    exit()
finally:
    print("we have done irrespective of the exception block.")
print("Thanks")   