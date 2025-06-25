from rectangle import Rectangle
from square import Square
from  triangle import Triangle
from circle import Circle
from hexagon import Hexagon

class Calculator:
    def __init__(self):
        self.shapes=[]

    def add_shape(self,type_shape):
        match type_shape:
            case 'rectangle':
                self.shapes.append(Rectangle(float(input('enter width: ')), float(input('enter height: '))))
            case 'square':
                self.shapes.append(Square(float(input('enter side: '))))
            case 'triangle':
                self.shapes.append(Triangle(float(input('enter first_side: ')), float(input('enter second_side: ')), float(input('enter third_side: '))))
            case 'circle':
                self.shapes.append(Circle(float(input('enter radius: '))))
            case 'hexagon':
                self.shapes.append(Hexagon(float(input('enter side: '))))


    def disply_shaps(self):
        for shape in self.shapes:
            print(shape)
            print(f'area: {shape.get_area()}')
            print(f'perimeter: {shape.get_perimeter()}')


