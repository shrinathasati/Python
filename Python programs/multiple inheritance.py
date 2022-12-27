class Python:
    language="pyhton"
    def __init__(self):
        print(f"{self.language} is coding language")
class cpp:
    language="C++"
    def __init__(self):
        print(f"{self.language} is coding language")
class programmer(cpp,Python):
    def __init__(self):
        print(f"the programmer knows {self.language}.")
p1=programmer()