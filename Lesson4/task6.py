from itertools import count
from itertools import cycle

def generator(len):
    my_list = []
    for el in count(1):
        if el < len + 1:
            my_list.append(el)
        else:
            return my_list


def povtorator(list):
    k = 0
    for el in cycle(list):
        if k < len(list) * 3:
            print(el, end=',')
            k += 1
    return

while True:
    try:
        dlin = int(input('Введите желаемую длинну списка:'))
        break
    except ValueError:
        print('Циферками вводите, пожалуйста')

my_list = generator(dlin)
print(my_list)
povtorator(my_list)
