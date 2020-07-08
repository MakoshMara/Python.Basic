basic_rez = int(input('Сколько километров вы пробежали за тренировку в первый день?:'))
target = int(input('Сколько вы хотите пробегать за тренировку?:'))
day = 1
rez = basic_rez
while rez < target:
    rez = basic_rez*1.1
    basic_rez = rez
    day +=1
print (f'Вы достигнете результата на {day} день')
