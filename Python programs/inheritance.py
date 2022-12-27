class Employee:
    company="Google"
    def __init__(self,name):
        print(f"My name is {name} and I work at {self.company}")
    
class programmer(Employee):
    salary=450000
    def __init__(self,name):
        super().__init__(name)
        print(f"my name is {name} and my salary is {self.salary} and I Work at {self.company}")
p=programmer("Shrinath")