vyrushka = float(input('Введите значение выручки в рублях:'))
izder = float(input('Введите значение издержек в рублях:'))
if vyrushka > izder:
    print('Вы работаете с прибылью!')
    pribil = (vyrushka - izder)
    rent = pribil/vyrushka
    print (f'Рентабельность выручки:{rent:.2f}')
    shtat = int(input('Какова численность штата?:'))
    pribil_sotr = pribil/shtat
    print(f'Прибыль на каждого сотрудника:{pribil_sotr:.2f} рублей')
elif vyrushka < izder:
    print('У вас убытки')
else:
    print('Вы в точке безубыточности')
