import math

from shape import Shape

class Triangle(Shape):
    def __init__(self,first_side,second_side,third_side):
        if first_side <= 0 or second_side <= 0 or third_side <= 0:
            raise ValueError("must be positive number")
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side

    def get_perimeter(self):
        return self.first_side + self.second_side + self.third_side

    def get_area(self):
        self.s = self.get_perimeter() / 2
        return math.sqrt(self.s * (self.s - self.first_side) * (self.s - self.second_side) * (self.s - self.third_side))

    def __str__(self):
        return f'Triangle(first_side={self.first_side}, second_side={self.second_side}, third_side={self.third_side})'