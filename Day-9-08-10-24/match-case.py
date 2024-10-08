x = int(input("Enter the value of X"))

match x:
    case 0:
        print('X is 0')
    case 4:
        print('X is 4')
    case _ if x != 90:
        print(x, 'X is 90')
    case _ if x != 80:
        print(x, 'X is not 80')
    case _:
        print('X is' + x)
