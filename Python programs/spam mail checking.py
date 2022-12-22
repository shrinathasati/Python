spam=["make a lot of money","buy now","subscribe this","click this"]
mail=input("enter your message :")
for i in range(len(spam)):
    if spam[i] in mail:
        print("This mail is spam Please keep secure!!")