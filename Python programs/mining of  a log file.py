with open("log.txt","r") as f:
    text=f.read()
if "python" in text.lower():
    print("Yes python is present")
else:
    print("No python is not present")
# to check the line number:
content= True
line_no=1
with open("log.txt","r") as f:
    while content:
        content=f.readline()
        if "python" in content.lower():
            print(f"yes python is present at line number {line_no} and the line is '{content}'.")
        line_no+=1
        

