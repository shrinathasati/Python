class operation:
    # def __init__(self,num):
    #     self.num=num
    def __add__(self,n2):
        print("I am doing addition:")
        return self.num+n2.num
    def __mul__(self,n2):
        print("I am doing multiplication:")
        return self.num*n2.num
    def __sub__(self,n2):
        print("I am doing subtraction:")
        return self.num-n2.num
    def __truediv__(self,n2):
        print("I am doing division:")
        return self.num/n2.num
    def __floordiv__(self,n2):
        print("I am doing floor division:")
        return self.num//n2.num

n1=operation()
n2=operation()
n1.num=5
n2.num=20
print(n1+n2)
print(n1*n2)
print(n1-n2)
print(n1/n2)
print(n1//n2)

