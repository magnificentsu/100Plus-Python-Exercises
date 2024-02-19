# Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.

#MY SOLUTION:
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
        
rectangle_1 = Rectangle(8, 8)
print(rectangle_1.area())

#COURSE SOLUTION:
class Rectangle():
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def area(self):
        return self.length*self.width


rect = Rectangle(2,4)
print(rect.area())
