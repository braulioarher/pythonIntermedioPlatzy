def run():
    myList = [1, "Hello", True, 4.5]
    myDict = {"firstname": "Braulio", "lastname": "Braulio",}

    super_list = [
        {"firstname": "Braulio", "lastname": "Arcos"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Susana", "lastname": "Martines"},
        {"firstname": "Jose", "lastname": "Garcia"},    
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "flooting_nums": [1.1, 4.5, 6.43],
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        for key, value in i.items():
            print(key, "-", value)

if __name__ == '__main__':
    run()