# super() = Funtion used in a child class to call methods from a parent class.
#           Allows you to extend the functionality of a inherited methods

class Shape:
    def __init__(self, colour, filled):
        self.colour = colour
        self.filled = filled
    
    def describe(self):
        print (f"Shape with colour {self.colour} and filled: {self.filled}")


class Circle(Shape):
    def __init__(self, colour, filled, radius):
        super().__init__(colour, filled)
        self.radius = radius
    
    #This method overrides the describe method in the Shape class
    def describe(self):
        print (f"Circle with area of {3.14 * self.radius ** 2} cm^2")

class Square(Shape):
    def __init__(self, colour, filled, width):
        super().__init__(colour, filled)
        self.width = width
    

class Triangle(Shape):
    def __init__(self, colour, filled, width, height):
        super().__init__(colour, filled)
        self.width = width
        self.height = height

    #This method adds additional functionality to the describe method in the Shape class
    def describe(self):
        super().describe()
        print(f"Triangle with area of {0.5 * self.width * self.height} cm^2")

circle = Circle("red", True, 5)
square = Square("blue", False, 10)
triangle = Triangle("green", True, 8, 12)

print(f"Circle: Colour={circle.colour}, Filled={circle.filled}, Radius={circle.radius}")
print(f"Square: Colour={square.colour}, Filled={square.filled}, Width={square.width}")
print(f"Triangle: Colour={triangle.colour}, Filled={triangle.filled}, Width={triangle.width}, Height={triangle.height}")


square.describe()
circle.describe()  
triangle.describe()