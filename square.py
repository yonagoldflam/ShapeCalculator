from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

    def __str__(self):
        return f'Rectangle(side={self.width})'