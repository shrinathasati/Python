num=int(input("enter the number: "))
isprime=True
for i in range(2,num):
    if(num%i==0):
        isprime=False
        break
if(isprime):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")