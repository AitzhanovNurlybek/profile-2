import math

class mathematic():
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
    def move(self):
        self.distance = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        
    def show(self):
        print(f"Our distance is: {self.distance}")

x1 = int(input("Enter x1: "))
x2 = int(input("Enter x2: "))
y1 = int(input("Enter y1: "))
y2 = int(input("Enter y2: "))

my_math = mathematic(x1, x2, y1, y2)
my_math.move()
my_math.show()