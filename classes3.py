class Shape:
    def __init__(self, length,width):
        self.length = length
        self.width = width
    def rectangle(self):
        return self.length * self.width

length = int(input("Enter the length: "))
width = int(input("Enter the width: "))


my_shape = Shape(length,width)

answer = my_shape.rectangle()

print(answer)
