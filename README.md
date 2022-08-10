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
