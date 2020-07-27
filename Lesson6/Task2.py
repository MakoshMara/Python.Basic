class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa(self, ):
        m = (self._length * self._width * 25 * 5) / 1000
        print(f'Вам потребуется: {m} тонн асфальта')


while True:
    try:
        road_1 = Road(int(input('Введите длинну дороги в метрах:')), int(input('Введите ширину дороги в метрах:')))
        break
    except ValueError:
        print('Вы ввели не числа')
road_1.massa()
