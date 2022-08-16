DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_python_dev = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_plazi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    old_workers = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA)) 
    # El simbolo pipe | une un diccionario con otro nuevo
    # Para cada trabajador de DATA guardar ese diccionario mas el diccionario old

    print(all_python_dev)
    print(all_plazi_workers)
    print(adults)
    print(old_workers)

    print("Ahora con los metodos invertidos")

    all_python_dev_2 = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_dev_2 = list(map(lambda worker: worker["name"], all_python_dev_2))
    all_plazi_workers_2 = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_plazi_workers_2 = list(map(lambda worker: worker["name"], all_plazi_workers_2))
    adults_2 = [worker["name"] for worker in DATA if worker["age"] > 18]
    old_workers_2 = [worker | {"old": worker["age"] > 70} for worker in DATA]

    print(all_python_dev_2)
    print(all_plazi_workers_2)
    print(adults_2)
    print(old_workers_2)

if __name__ == '__main__':
    run()