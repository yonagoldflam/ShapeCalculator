from rectangle import Rectangle
from square import Square
from  triangle import Triangle

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


    def disply_shaps(self):
        for shape in self.shapes:
            print(shape)
            print(shape.get_area())
            print(shape.get_perimeter())


