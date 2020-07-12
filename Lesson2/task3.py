list = ['Зима', 'Весна', 'Лето', 'Осень']
while True:
    user_number = input('Введите номер месяца:')
    if user_number.isnumeric() and int(user_number) <= 12:
        user_number = int(user_number)
        if 1 <= user_number <= 2 or user_number == 12:
            print(f'Это {list[0]}!')
        elif 3 <= user_number <= 5:
            print(f'Это {list[1]}!')
        elif 6 <= user_number <= 8:
            print(f'Это {list[2]}!')
        else:
            print(f'Это {list[3]}!')
        break
    else:
        print('Номер месяца должен быть числом не более 12-ти!')