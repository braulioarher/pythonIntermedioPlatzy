def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Braulio", "Miguel", "Pepe", "Christina"]
    with open("./archivos/name.txt", "w", encoding="utf-8") as f: #Si queremos agregar informacion 
        for name in names:              #Sin la necesidad de borrar la informacion de debe usar "a" append
            f.write(name)
            f.write("\n")


def run():
    read()


if __name__ == "__main__":
    run()