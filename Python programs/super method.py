class company:
    company_name="google"
    worth=800000000000000
    def __init__(self):
        print(f"The company name is {self.company_name} and it is worth {self.worth}")
class software(company):
    def __init__(self):
        super().__init__()# this method is used to call upper class attributes.
        print(f"{self.company_name} is a software company.")
s=software()
