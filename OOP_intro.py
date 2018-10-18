import math

class Apple:
    def __init__(self, weight, kind, color, region):
        self.weight = weight
        self.kind = kind
        self.color = color
        self.region = region
class Circle:
    def __init__(self, r):
        self.radius = r
    def area(self):
        return math.pi*(self.radius**2)

circle = Circle(5)
# print(circle.area())

class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h
    def area(self):
        return self.base*self.height/2

triangle = Triangle(10, 5)
# print(triangle.area())

class Hexagon:
    def __init__(self, s):
        self.side = s
    def calculate_perimeter(self):
        return self.side*6

hexagon = Hexagon(7)
print(hexagon.calculate_perimeter())


