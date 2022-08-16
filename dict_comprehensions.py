def run():
    # dict = {}
    # for i in range(1 ,102):
    #     if i % 3 != 3:
    #         dict[i] = i**3

    # print(dict)

    # my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # print(my_dict)

    #Crear un dictionary comprehension cuyas llaves sean los 1000 primeros numero con sus raices
    #cuadradas como valores

    my_dict = {i: round(i**0.5 , 2) for i in range(1,1001)}
    print(my_dict)

if __name__ == '__main__':
    run()
