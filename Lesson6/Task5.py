class Stationery:
    def __init__(self, name):
        self.title = name

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title}: Запуск отрисовки каракулей на бумаге во время телефонного разговора')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title}: Запуск отрисовки наброска')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title}: Запуск отрисовки типа умной схемы на вайтборде')


pen_1 = Pen('Просто ручка')
print(pen_1.title)
pen_1.draw()
pencil_1 = Pencil('Черный карандаш')
print(pencil_1.title)
pencil_1.draw()
handle_1 = Handle('Синий маркер')
print(handle_1.title)
handle_1.draw()
