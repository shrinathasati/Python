class employee:
    salary=1250000
    increment=600000
    @property
    def total(self):
        return self.salary+self.increment
    @total.setter
    def total(self,val):
        self.increment=val-self.salary
e=employee()
print(e.total)
e.total=2000000
print(e.salary)
print(e.increment)