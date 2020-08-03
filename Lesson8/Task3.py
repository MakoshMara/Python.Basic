class MyException(Exception):
    def __init__(self, text):
        self.text = text


def proverka(list):
    try:
        for i in list:
            if not i.isnumeric() and i != '=':
                raise MyException('Вы ввели не число!')
            i = int(i)
    except (ValueError, MyException) as err:
        print(err)
        return 0


def new_el(list, k):
    for i in list:
        if not i.isnumeric():
            list = list[0:list.index(i)]
            k = 1
    return list, k


k = 0
user_list = input('Введите числа через пробел:').split()
if proverka (user_list) == 0:
    print('А надо было вводить числа( все сломалось')
print(f'Сумма чисел: {sum(list(map (int,user_list)))}')
while k == 0:
    new_list = input('Продолжим? Когда зохотите закончить просто нажмите "=" :').split()
    if proverka(new_list) == 0:
        print('А надо было вводить числа( все сломалось')
    res = new_el(new_list, k)
    new_list = res[0]
    k = res[1]
    for i in new_list:
        user_list.append(i)
    print(f'Итоговая сумма: {sum(list(map (int,user_list)))}')
print('Приходите еще поссумировать!')