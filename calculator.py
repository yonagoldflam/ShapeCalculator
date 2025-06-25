from rectangle import Rectangle

def main():
    shapes = [Rectangle(4, 5)]

    for shape in shapes:
        print(shape)
        print(shape.get_area())
        print(shape.get_perimeter())

if __name__ == '__main__':
    main()