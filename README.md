# Python intermadio

## Principios de python

Para visualizar los principios de python se usa:

    import this

## Creacion de un entorno virtual

Para construir un proyecto se necesita de construir un etorno vitual para esto se usa

        python3 -m venv venv

venv    -virtual enviroment

Lo anterior crea una carpeta

Para activar el entorno virtual se debe de usar el comando

source venv/bin/activate

## Instalaccion de dependecias con PIP

Pip es un manejador de dependencias o un instalador de paquetes

### Modulos populares

    -Requests
    -BeatifulSoup4
    -Pandas
    -Numpy
    -Pytest

Estos modulos sirven para hacer web scrapping
Despues para cinciencia de datos
Pytest sirve para realizar testig

Para visualizar los modulos instalados se usan los modulos instalados en el entorno virtual

    pip freeze

Para compartir nuestro proyecto con sus respectivas dependecias se debe de usar el comando

    pip freeze > requirements.txt

Para instalar las dependecias desde un archivo se usa

    pip install -r archivo.txt

## Listas y diccionarioas anidados

Ejemplo en archivo lists_and_dicts.py

## List comprehensions

Los list comprhensions se utiliza para crear nuevas listas dentro de python

La estructura de los list comprehensions es la siguiente:

    [element for element in iterable if condition]

element: representa cada uno de los elementos a poner en la nueva lista
for: ciclo a partir del cual se extraeran elementos de otra lista o cualquier iterable
codition: condicion opcional para filrar los elemntos del ciclo

y se le de la siguiente manera:

    para cada elemento en el iterable guarda el elemento si se cumple la condicion

ejemplo:
    [i**2 for i in range(1,101) if i % 3 != 0]
    para cada i en el rango de 1 a 101 guarda i al cuadrado si el modulo de i es diferente a 0

## Dict comprehensions

Los dict comprehensions se utilizan para crear nuevos diccionarios dentro de python

La estructura es la siguiente

    {key:value for value in iterable if condition}

key:value   -representa a cada una de las llaves u calores a poner en el nuevo diccionario
for         -ciclo a partir del cual se extraen los elementos de cualquier iterable
if          -condicion para filtrar los elementos del ciclo

y se le de la siguiente manera:

    para cada elementos en un iterable se va guardar una llave y un valor si cumple la condicion

ejemplo:
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

Paara cada i en el rango de 1 a 101 guardar la llave i con el valor i al cubo si el modulo de i es diferenre a 0

## Funciones anonimas

Lamda son funciones anonimas que no tienen un nombre

lambda argumentos: expresion

La funciones lambda solo pueden contener una expresion a diferencia de JavaScript ejemplo

palidrome = lambda string: string == string[::-1]
print(palindrome('ana')) //True

Una funcion anonima puede tener un numero infinito de argumetos pero esta solo puede tener una expresion

## High order functions: filter, map y reduce

Una funcion de order superior es una funcio que recibe como parametro otra funcion, existen tres funciones de order superior basicas en la mayoria de los lenguajes de progremacion las cuales son

        filter      -recibe una funcion que retorna true o false y un iterable ejemplo:
                odd = list(funcion, objeto iterable)
                odd = list(lambda x: x%2 == 0, lista)
        map         -recibe una funcion que altera cada elemento de la lista y un iterable
                double = list(funcion, objeto iterable)
                double = list(lambda x: x*2, lista)
        reduce      -reduce una lista a un unico valor recibe una funcion y un objeto iterable se      debe de importar la importar el modulo functools
                from functools import reduce
                all_multiplied = reduce(lambda a, b: a * b, my_list)
                donde lambda recibe dos parametros a y b y la funcion multiplica los parametros hasta agotar los elementos en el array

## Los errores en el codigo

Existen errores de sintaxis y errores de excepccion

Errores

    SyntaxError                     se tiene un error de escritura dentro de nuestro codigo

    Exception
            -KeyboardInterrupt      se interrumpe el proceso con ctrl + c
            -KeyError               se accede a una llave que no existe
            -IndexError             se trata de acceder a un elemento que no exite
            -FileNotFound           se trata de abrir un archivo que no exite
            -ZeroDivisionError      se trata de dividir un numero entre cero
            -ImportError            se importa un modulo que tiene un error

cuando python regresa un error este lo hace a travez de un traceback lo ideal para leer este traceback se debe de leer del final al incio

## Debugging

Visual Studio Code tiene una funcion que nos permite debuggear nuestro codigo y correrlo paso a paso

Existe tambien la herramienta para poner un breakpoint para de esta forma parar nuetro programa donde seleccionemos un punto rojo

## Manejo de excepciones

    try/ except

    def palindrome(string):
        return string == string(::-1)

    try:
        print(palindrome(1))
    except:
        print("Solo se pueden ingresar strings")

El except solo sirve para errores de tipo TypeError

## Assert Statements

Son expresiones para manejar errores

    assert condicion, mensaje de error

afirmo que esta condicion es verdadera si no imprimo este mensaje

    def palindrome(string):
        assert len(string) > 0, "No se puede ingresar una cadena vacia"
        return string == string(::-1)

    print(palindrome(""))

## Como trabajar con archivos

Modos de apertura de archivos

    R -> Lectura
    W -> Escritura (Sobrescribir)
    A -> Escritura (agregar al final)

with open("./ruta/archivo.txt", "r") as f

open("ruta", "modo de apertura") as nombreHipotetico

## Reto de juego del ahorcado

Investigar la funcion enumerate

Investigar el metodo get de los diccionarios

Investigar las sentencias
        os.system("cls")    -Para windows
        os.system("clear")  -Para linux

Para limpiar la pantalla cada vez que ingresamos una letra

Mejorar el juego anniadiendo un sistema de puntos, dibujar al ahorcado en cada jugada o mejorar la interfaz