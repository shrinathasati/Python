class Calulator:
    def square(self):
        print(f"the sqaure of {self.num} is {self.num**2}")
    def cube(self):
        print(f"the cube of {self.num} is {self.num**3}")
    def sqaureroot(self):
        print(f"the sqaureroot of {self.num} is {self.num**(1/2)}")
number=Calulator()
number.num=4
number.square()
number.cube()
number.sqaureroot()
