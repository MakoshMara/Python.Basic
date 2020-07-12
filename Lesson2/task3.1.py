my_dict = {'k1': 'Зима', 'k2': 'Весна', 'k3': 'Лето', 'k4': 'Осень'}
while True:
    user_number = input('Введите номер месяца:')
    if user_number.isnumeric() and int(user_number) <= 12:
        user_number = int(user_number)
        if 1 <= user_number <= 2 or user_number == 12:
            print(f'Это {my_dict[k1]}!')
        elif 3 <= user_number <= 5:
            print(f'Это {my_dict[k2]}!')
        elif 6 <= user_number <= 8:
            print(f'Это {my_dict[k3]}!')
        else:
            print(f'Это {my_dict[k4]}!')
        break
    else:
        print('Номер месяца должен быть числом не более 12ти!')