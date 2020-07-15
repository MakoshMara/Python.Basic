def summ(list):
    list = [int(i) for i in list]
    return sum(list)


def new_el(list, k):
    for i in list:
        if not i.isnumeric():
            list = list[0:list.index(i)]
            k = 1
    return list, k


k = 0
user_list = input('Введите числа через пробел:').split()
print(f'Сумма чисел: {summ(user_list)}')
while k == 0:
    new_list = input('Продолжим? Когда зохотите закончить просто нажмите любой символ, даже в процессе:').split()
    res = new_el(new_list, k)
    new_list = res[0]
    k = res[1]
    for i in new_list:
        user_list.append(i)
    print(f'Итоговая сумма: {summ(user_list)}')
print('Приходите еще поссумировать!')
