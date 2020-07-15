def my_func(x, y):
    i = 1
    res = 1.0
    while i <= abs(y):
        res = res * (1 / x)
        i += 1
    return res


def prov_1(x):
    try:
        int(x)
        return x
    except:
        return None


def prov_2(y):
    if (float(y) % 1 == 0):
        return y
    else:
        return None


x = input('Введите действительное положительное число:')
while (prov_1(x) is None) or float(x) <= 0:
    x = input('Учите математику за пятый класс. Повторим. Введите действительное положительное число:')

y = input('Введите целое отрицательное число:')
while (prov_2(y) is None) or int(y) > 0:
    y = input('Повторим. Введите целое отрицательное число:')

print(f'Результат - {my_func(float(x), int(y))}')
