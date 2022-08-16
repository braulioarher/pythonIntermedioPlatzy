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


def letter_check(s_word, letter, guessed):
    s_word_set = set([i for i in s_word])
    enu_s_word = dict(enumerate(s_word))
    enu_guessed = dict(enumerate(guessed.replace(" ", "")))
    if (letter in s_word_set) == True:
        indexes = list(i for i in enu_s_word if enu_s_word[i] == letter)
        for i in indexes:
            enu_guessed[i] = letter
        guessed_list = enu_guessed.values()
        w_guessed = [i + " " for i in guessed_list]
        guessed = "".join(w_guessed)
        return(guessed)
    else:
        return(guessed)



def run():
    palabras = read()
    current_word = rword(palabras).upper()
    decoded_word = unidecode.unidecode(current_word)
    s_word = decoded_word
    guessed = "".join(["_ " for i in s_word])
    spaced_word = "".join([i + " " for i in s_word])
    print(spaced_word)
    
    while True:
        if guessed == spaced_word:
            break
        else:
            letter = input(f"Adivina la palabra \n{guessed}\nIngresa una letra: ").upper()
            assert not letter.isnumeric(), "Se debe introducir solo letras"
            assert (len(letter)) == 1, "Intruzca solo una letra a la vez"
            guessed = letter_check(s_word, letter, guessed)
            os.system("clear")
    print(f"FELICIDADES GANASTE LA PALABRA ES: {s_word}")




if __name__ == "__main__":
    run()