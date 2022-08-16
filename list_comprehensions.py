from audioop import mul


def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    #print(squares)

    #Crear una lista con todos los mutiplos de 4 que a la vez sea multiplo de 6 y 9 hasta 99999

    mult = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(mult)

if __name__ == '__main__':
    run()