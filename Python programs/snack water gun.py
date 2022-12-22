def gamewin(computer,user):
    if computer==user:
        return None
    elif computer=='w':
        if user=='s':
            return True
        elif user=='g':
            return False
    elif computer=='g':
        if user=='s':
            return False
        elif user=='w':
            return True
    else:
        if user=='w':
            return False
        elif user=='g':
            return True
import random
p1=random.randint(1,3)
if p1==1:
    computer ='s'
elif p1==2:
    computer ='w'
else:
    computer ='g'
print('''
Snake : s
Water : w
Gun   : g
''')
user=input("enetr Choice: ")
result=gamewin(computer,user)
print("Computer choose: "+computer)
print("User choose "+user)
if result==None:
    print("game is tie")
elif result:
    print("You win")
else:
    print("You lose")
