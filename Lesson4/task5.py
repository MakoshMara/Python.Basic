from functools import reduce

my_list = [el for el in range(99, 1001) if el % 2 == 0]


def proiz(x, y):
    return int(x) * int(y)


print(reduce(proiz, my_list))
