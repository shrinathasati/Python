def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)
n=int(input("enter number : "))
total_sum=sum(n)
print("the sum of first",n,"number is",total_sum)
