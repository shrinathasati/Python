def game():
    return 54
score=game()
with open("hiscore.txt") as f:
    score1=f.read()
if score1=="":
    with open("hiscore.txt","w") as f:
        f.write(str(score))

elif score>int(score1):
    print(f"your new highscore is: {score}")
    with open("hiscore.txt","w") as f:
        f.write(str(score))