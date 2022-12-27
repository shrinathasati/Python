''' method 1:- to change class attribute without using @classmethod fuction.'''
# class employee:
#     id=786
#     salary=150000
#     company="shell"
#     def print(self):
#         print(f"the id of the empolyee is {self.id} and salary is {self.salary} and works at {self.company}.")
# f=employee()
# f.company="google"
# print(f.company)
# print(employee.company)
# employee.company="google"# changing the class attributes.
# g=employee()
# g.print()
# print(employee.company)

'''method 2 to change class attribute using @classmethod function.'''
class employee:
    id=786
    salary=150000
    company="shell"

    # @classmethod
    # def change_company(cls,company):     # method 1
    #     cls.company=company

    def change_company(self,company):
        self.__class__.company=company


    # def change_company(self,company):
    #     self.company=company

    def print(self):
        print(f"the id of the empolyee is {self.id} and salary is {self.salary} and works at {self.company}.")
e=employee()
e.print()
e.change_company("Oracle")
e.print()
f=employee()
print(f.company)