class Shape:
    def area(self):
        return 0 

class Square(Shape):
    def __init__(self,lenght):
        self.lenght = lenght

    def area(self):
        return self.lenght**2

square = Square(int(input()))
print(f"Square area:{square.area()}")