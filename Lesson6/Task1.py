import time


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        colors = {'1': [TrafficLight.__color[0], '31m', 7], '2': [TrafficLight.__color[1], '0;33m', 2],
                  '3': [TrafficLight.__color[2], '32m', 7]}
        for i in colors:
            k = 0
            while k < colors.get(i)[2]:
                print(
                    f'\033[0;{colors.get(i)[1]}Светофор сейчас {colors.get(i)[0]}. Осталось {colors.get(i)[2] - k} сек.',
                    end='')
                time.sleep(1)
                k += 1
                print('\r', end='')
            print('\r', end='')


trafficLight_1 = TrafficLight()
trafficLight_1.running()
