import math  # Import math module to use pi

class Shape:
    def area(self):
        raise NotImplementedError  # Forces subclasses to implement this method

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Initialize radius
    
    def area(self):
        return math.pi * self.radius ** 2  # Area formula: πr²

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length  # Initialize length
        self.width = width  # Initialize width
    
    def area(self):
        return self.length * self.width  # Area formula: length × width

# Test Input
circle = Circle(7)
print(f"{circle.area():.2f}")  # Expected Output: ~153.94 (π × 7²)
