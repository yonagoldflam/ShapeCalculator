from  calculator import Calculator


def menu():
    calculator = Calculator()
    out = False
    while not out:
        choose = input("1.disply all shapes \n2. create rectangle \n3. create square \n")
        match choose:
            case '1':
                calculator.disply_shaps()
            case '2':
                calculator.add_shape("rectangle")
            case '3':
                calculator.add_shape("square")
            case _:
                out =True


if __name__ == '__main__':
    menu()




