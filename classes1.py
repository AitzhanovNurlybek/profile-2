class getuppercase():
    def __init__(self, string):
        self.string = string
        
    def toupper(self):
        self.string = self.string.upper()
        
    def print(self):
        print(f"Our upper case is {self.string}")

string = input()
upper = getuppercase(string)
upper.toupper()
upper.print()
