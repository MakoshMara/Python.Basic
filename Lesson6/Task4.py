class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.color} {self.name} поехал')

    def stop(self):
        print(f'{self.color} {self.name} остановился')

    def turn(self, direction):
        print(f'{self.color} {self.name} повернул {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} - {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость {self.name} - {self.speed} км/ч') if int(self.speed) < 60 else print(f'Вы превысили скорость!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость {self.name} - {self.speed} км/ч') if int(self.speed) < 40 else print(f'Вы превысили скорость!')


class PoliceCar(Car):
    pass


auto_1 = TownCar(40, 'Синий', 'FunCargo', False)
auto_1.go()
auto_1.show_speed()
auto_1.speed = 65
auto_1.show_speed()

auto_2 = SportCar(40, 'Красный', 'Audi S7', False)
auto_2.turn('налево')
print(f'Цвет {auto_2.name} - {auto_2.color}')

auto_3 = WorkCar(80, 'Зеленый', 'УАЗ Хантер', False)
auto_3.go()
auto_3.show_speed()

auto_4 = PoliceCar(100, 'Бело-синий', 'ВАЗ-2109', True)
auto_4.stop()
