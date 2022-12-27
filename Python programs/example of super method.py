class Grandfather:
    grand_age=78
    def getinfogrand(self,name):
        print(f"The name of Grandfather is {name} and his age is {self.grand_age}")
class father(Grandfather):
    father_age=48
    def getinfofather(self,name_father,name_grand):
        super().getinfogrand(name_grand)
        print(f"The name of Father is {name_father} and his age is {self.father_age}")
class son(father):
    son_age=19
    def getinfoson(self,name,name_father,name_grand):
        super().getinfofather(name_father,name_grand)
        print(f"The name of son is {name} and his age is {self.son_age}")
# gf=Grandfather()
# gf.getinfogrand("Ganpat Lal Asati")

# f=father()
# f.getinfofather("Nandkishor Asati")
# f.getinfogrand("Ganpat Lal Asati")

s=son()
s.getinfoson("Shrinath Asati","Nandkishor Asati","Ganpat Lal Asati")
# s.getinfofather("Nandkishor Asati")
# s.getinfogrand("Ganpat Lal Asati")