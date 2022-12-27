class Number:
    def add(self,a,b):
        self.a=a
        self.b=b
        print(f"the sum of {a} and {b} is {self.a+self.b}")
numbers=Number()
numbers.add(5,4)