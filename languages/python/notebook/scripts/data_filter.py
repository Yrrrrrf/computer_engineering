from concurrent.futures.thread import _worker

DATA = [
    {'name': 'Facundo',  'age': 72, 'organization': 'Platzi',   'position': 'Technical Coach',   'language': 'python',},
    {'name': 'Luisa',    'age': 33, 'organization': 'Globant',  'position': 'UX Designer',       'language': 'javascript',},
    {'name': 'Hector',   'age': 19, 'organization': 'Platzi',   'position': 'Associate',         'language': 'ruby',},
    {'name': 'Gabriel',  'age': 20, 'organization': 'Platzi',   'position': 'Associate',         'language': 'javascript',},
    {'name': 'Isabella', 'age': 30, 'organization': 'Platzi',   'position': 'QA Manager',        'language': 'java',},
    {'name': 'Karo',     'age': 23, 'organization': 'Everis',   'position': 'Backend Developer', 'language': 'python',},
    {'name': 'Ariel',    'age': 32, 'organization': 'Rappi',    'position': 'Support',           'language': '',},
    {'name': 'Juan',     'age': 17, 'organization': '',         'position': 'Student',           'language': 'go',},
    {'name': 'Pablo',    'age': 32, 'organization': 'Master',   'position': 'Human Resources Manager',   'language': 'python',},
    {'name': 'Lorena',   'age': 56, 'organization': 'Python Organization', 'position': 'Language Maker', 'language': 'python',},
]


def run():
    print([worker['name'] for worker in DATA if worker['language'] == 'python'])  # Print the name of the workers that know python
    print([worker['name'] for worker in DATA if worker['organization'] == 'Platzi'])  # Print the name of the workers that work at Platzi
    # print([worker['name'] for worker in DATA if worker['age'] > 18])  # Save the name of the workers that are older than 18
    adults_in_data = (list(filter(lambda worker: worker['age']>18, DATA)))  # Save the data of the workers that are older than 18
    print([x for x in map(lambda worker: worker['name'], adults_in_data)])  # Print the name of the workers that are older than 18
    # create a new dictionary with an additional key called 'old' that is True if the worker is older than 70 years old
    print(list(map(lambda worker: worker | {'old': worker['age']>70}, DATA)))  # map(lambda key: key | {'key': new_value or logic expression}, dict_list)))


if __name__ == '__main__':
    run()



