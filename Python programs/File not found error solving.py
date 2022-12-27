def openfile(filename):
    try:
        with open(filename) as f:
            print(f.read())
    except FileNotFoundError as e:
        print(f"I have not found any file with the name {filename}")
        print("The error message associated is : ",e)
openfile("1.txt")
openfile("2.txt")
openfile("3.txt")