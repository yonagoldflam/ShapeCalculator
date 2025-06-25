from rectangle import Rectangle
from square import Square

class Calculator:
    def __init__(self):
        self.shapes=[]

    def add_shape(self,type_shape):
        match type_shape:
            case 'rectangle':
                self.shapes.append(Rectangle(int(input('enter width: ')), int(input('enter height: '))))
            case 'square':
                self.shapes.append(Square(int(input('enter side: '))))


    def disply_shaps(self):
        for shape in self.shapes:
            print(shape)
            print(shape.get_area())
            print(shape.get_perimeter())


