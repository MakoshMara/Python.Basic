with open("text_for_5.txt", "w", encoding="utf-8") as text:
    while True:
        try:
            user_list = input('Введите числа через пробел:').split()
            user_list = list(map(int, user_list))
            for i in user_list:
                text.write(str(i) + ' ')
            break
        except ValueError:
            print('Вы ввели не число')
    print(f'\nСумма чисел - {sum(user_list)}', file=text)
    print(f'Сумма чисел - {sum(user_list)}')
