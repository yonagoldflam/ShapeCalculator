from shape import Shape
import math

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius **2

    def get_perimeter(self):
        return math.pi * self.radius * 2

    def __str__(self):
        return f'Circle(radius={self.radius})'