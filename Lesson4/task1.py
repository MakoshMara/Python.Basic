from sys import argv

name, v, s, p = argv


def zarplata(v, s, p):
    return print(f'Зарплата сотрудника:{(v * s) + p}')


zarplata(int(v), int(s), int(p))
