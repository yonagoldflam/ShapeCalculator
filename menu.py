from  calculator import Calculator


def menu():
    calculator = Calculator()
    out = False
    while not out:
        choose = input("\n1.disply all shapes \n2. create rectangle \n3. create square \n4. create triangle \n5. create circle \n6.create hexagon \nother key to exit\n")
        match choose:
            case '1':
                calculator.disply_shaps()
            case '2':
                calculator.add_shape("rectangle")
            case '3':
                calculator.add_shape("square")
            case '4':
                calculator.add_shape('triangle')
            case '5':
                calculator.add_shape('circle')
            case '6':
                calculator.add_shape('hexagon')

            case _:
                out =True


if __name__ == '__main__':
    menu()




