class father:
    colour="light"
    father_age=48
    def getinfofather(self):
        print(f"Father skin color is {self.colour} and age is {self.father_age}")
class son(father):
    age=19
    def getinfoson(self):
        super().getinfofather()
        print(f"Son colour is same as father which is {self.colour} and age is {self.age}")

shrinath=son()
shrinath.getinfoson()
nandkishor=father()
nandkishor.getinfofather()