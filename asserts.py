def divisors(num):
    divisors = []
    for i in range(1,num + 1):
        if num % i == 0:
            divisors.append(i)
    return(divisors)

def run():
    num = input("Dame un numero: ")
    assert num.isnumeric(), "Debes de introducir un numeros positivos"
    print(divisors(int(num)))
    print("Termino el programa")


if __name__ == "__main__":
    run()