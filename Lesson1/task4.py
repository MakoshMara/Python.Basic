user_answer = int(input('Введите целое положительнео число:'))
maxim = user_answer % 10
while user_answer > 0:
    if user_answer % 10 >= maxim:
        maxim = user_answer % 10
    user_answer = user_answer//10
print(f'Наибольшая цифра в числе: {maxim}')