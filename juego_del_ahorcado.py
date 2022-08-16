from ntpath import join
import random
import os
import unidecode
from base64 import decode
from functools import partial



def read():
    palabras = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            palabras.append(line)
    palabras = list(map(lambda palabra: palabra.strip(), palabras))
    return(palabras)


def rword(lista):
    longitud = len(lista)
    return(lista[random.randrange(longitud)])


def letter_check(s_word, letter, u_word):
    if len(u_word) == 0:
        returned = ["_ " for i in s_word]
        return("".join(returned))



def run():
    palabras = read()
    current_word = rword(palabras).upper()
    decoded_word = unidecode.unidecode(current_word)
    u_word = ""
    s_word = decoded_word
    guessed = "".join(["_ " for i in s_word])
    a = dict(enumerate(decoded_word))
    print(a)
    
    while True:
        letra = input(f"Adivina la palabra \n{guessed}\n{decoded_word} \nIngresa una letra: ").upper()
        letter_check(s_word, )
        os.system("clear")



if __name__ == "__main__":
    run()