def polzovatel(**kwargs):
    my_list = list(kwargs.values())
    return my_list


name = input('Введите имя:')
surname = input('Введите фамилию:')
gb = input('Введите год рождения:')
sity = input('Введите город проживания:')
pochta = input('Введите емейл:')
phone = input('Введите телефон:')

my_list = (polzovatel(name=name, surname=surname, gb=gb, town=sity, email=pochta, phone=phone))
for i in my_list:
    print(i, end=',')
