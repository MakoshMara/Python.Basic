def my_func(n_1, n_2, n_3):
    my_list = [n_1, n_2, n_3]
    my_list.remove(min(my_list))
    return sum(my_list)


def proverka(list):
    for i in list:
        try:
            float(i)
        except:
            print(f' {list.index(i) + 1} элемент не был числом. Повторим.')
            return None
    return list


user_list = input('Введите три числа через пробел:').split()
while (proverka(user_list) == None):
    user_list = input('Введите три числа через пробел:').split()

print(my_func(float(user_list[0]), float(user_list[1]), float(user_list[2])))
