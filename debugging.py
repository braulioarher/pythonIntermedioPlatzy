from __future__ import barry_as_FLUFL
import pstats

a = True


def divisors(num):
    try:
        if num <= 0:
            raise ValueError("Debes ingresar un numero mayor a cero")
        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        return(ve)



def run():
    while True:
        try:
            num = int(input("Dame un numero: "))
            print(divisors(num))
            break
        except ValueError:
            print("Debes ingresar un numero")

    print("Programa termino")
    

if __name__ == "__main__":
    run()