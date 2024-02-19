# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.

#MY SOLUTION
class MyCircle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * (self.radius**2)

a = MyCircle(8)
print(a.area())


#COURSE SOLUTION:
class Circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return 3.1416*(self.radius**2)


circle = Circle(5)
print(circle.area())
