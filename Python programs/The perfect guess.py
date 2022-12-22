import random
randNumber=random.randint(1,100)
userguess=None
guess_no=0
while(userguess!=randNumber):
    userguess=int(input("enter the number: "))
    guess_no+=1
    if(userguess==randNumber):
        print("you have guessed right!")
    else:
        if(userguess>randNumber):
            print("You have entered the wrong! please enter the smaller number...")
        else:
            print("You have entered the wrong! please enter the larger number...")
print(f"you have taken {guess_no} of chances...")
with open("history.txt") as f:
    highscore=int(f.read())
if guess_no<highscore:
    print("you have just broken the high score.....")
    with open("history.txt","w") as f:
        f.write(str(guess_no))