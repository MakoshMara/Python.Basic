from abc import ABC, abstractmethod


class Сlothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def raschet(self):
        pass


class Coat(Сlothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            print('На детей не шьем. Начнем с сорокового.')
            self.__size = 40
        elif size > 58:
            print('Вы не офигели там? 58 - МАКСИМУМ, для него и посчитаю')
            self.__size = 58
        else:
            self.__size = size

    def raschet(self):
        return self.__size / 6.5 + 0.5


class Сostume(Сlothes):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        while True:
            try:
                self.__height = int(height)
                break
            except ValueError:
                height = input('Введите только числа:')

    def raschet(self):
        return 2 * (self.__height / 100) + 0.3


coat_1 = Coat(int(input('Введите размер пальто для рассчета:')))
print(f'Вам потребуется {coat_1.raschet():.2f} метров ткани на пальто {coat_1.size} размера ')
costume_1 = Сostume(input('Введите рост для костюма для рассчета (как обычно, в сантиметрах):'))
print(f'Вам потребуется {costume_1.raschet():.2f} метров ткани на костюм {costume_1.height} роста ')
print(f'Всего вам потребуется {coat_1.raschet() + costume_1.raschet():.2f} метров ткани')
