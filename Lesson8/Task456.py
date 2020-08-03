class Stock:
    printer_array = []
    scaner_array = []
    copir_array = []
    stock = [printer_array, scaner_array, copir_array]

    @staticmethod
    def arrival_Equipment():
        while True:
            user_choise = input(
                'Выберите что вы хотите добавить на склад оргтехники\n'
                '[1] - Принтер\n'
                '[2] - Сканер\n'
                '[3] - Копир\n'
                '[4] - Назад\n'
                'Выберите пункт меню:')
            if user_choise == '1':
                Stock().printer_array.append(Printer(input('Введите модель принтера:'),
                                                     input('Введите количество:'),
                                                     input('Введите цветопередачу (черно-белый или цветной):')))
            elif user_choise == '2':
                Stock().scaner_array.append(Scanner(input('Введите модель сканера:'),
                                                    input('Введите количество:'),
                                                    input('Введите тип (ручной, планшетный и пр):')))
            elif user_choise == '3':
                Stock().copir_array.append(Сopier(input('Введите модель копира:'),
                                                  input('Введите количество:'),
                                                  input('Введите габариты (A4,A3,A2,A1):')))
            elif user_choise == '4':
                break

    @staticmethod
    def showing_Equipment():
        while True:
            user_choise = input(
                'Выберите тип оргтехники список которого вы хотели бы посмотреть:\n'
                '[1] - Принтер\n'
                '[2] - Сканер\n'
                '[3] - Копир\n'
                '[4] - Назад\n'
                'Выберите пункт меню5:')
            if user_choise == '1':
                sum = 0
                for i in Stock().printer_array:
                    print(i.param)
                    sum = sum + int((i.param).get('Количество'))
                print(f'Общее количество на складе {sum}')
            elif user_choise == '2':
                sum = 0
                for i in Stock().scaner_array:
                    print(i.param)
                    sum = sum + int((i.param).get('Количество'))
                    print(f'Общее количество на складе {sum}')
            elif user_choise == '3':
                sum = 0
                for i in Stock().copir_array:
                    print(i.param)
                    sum = sum + int((i.param).get('Количество'))
                    print(f'Общее количество на складе {sum}')
            elif user_choise == '4':
                break

    def find_Equipment(self):
        user_choise = input('Какую модель оргтехники вы ищите?:')
        for i in self.stock:
            for j in i:
                if j.param['Модель'] == user_choise:
                    print(j.param)

    def moving_Equipment(self):
        user_choise_1 = input('Какую модель оргтехники вы хотите переместить?:')
        user_choise_2 = input('Куда вы хотите переместить?:')
        for i in self.stock:
            for j in i:
                if j.param['Модель'] == user_choise_1:
                    print(f'{j.param} был переведен в {user_choise_2}')
                    if int(j.param['Количество']) == 1:
                        i.remove(j)
                    else:
                        j.param['Количество'] = int(j.param['Количество']) - 1
                print(f'На складе осталось {j.param}')

    def change_count(self):
        user_choise_1 = input('Количество какой модели оргтехники вы хотели бы сменить:')
        for i in self.stock:
            for j in i:
                if j.param['Модель'] == user_choise_1:
                    user_choise_2 = input(
                        f'На складе единиц такой модели:{j.param["Количество"]}. На какое хотите поменять?:')
                    j.param["Количество"] = user_choise_2


class Equipment:
    def __init__(self, model, count, name):
        self.model = model
        self.count = count
        self.name = name
        self.param = {'Тип': self.name, 'Модель': self.model, 'Количество': self.__count}

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        try:
            self.__count = int(count)
        except ValueError:
            print('Вы ввели не числа в поле колличества! Колличество установлено равным нулю')
            self.__count = 0


class Printer(Equipment):
    def __init__(self, model, count, color, name='Принтер'):
        super().__init__(model, count, name)
        self.param['Цветопередача'] = color


class Scanner(Equipment):
    def __init__(self, model, count, types, name='Сканер'):
        super().__init__(model, count, name)
        self.param['Вид'] = types


class Сopier(Equipment):
    def __init__(self, model, count, demen, name='Копир'):
        super().__init__(model, count, name)
        self.param['Габариты'] = demen


while True:
    print("*" * 5, 'Меню', "*" * 5)
    user_choise = input('[1] - Добавить оргтехнику\n'
                        '[2] - Посмотреть оргтехнику\n'
                        '[3] - Найти оргтехнику по модели\n'
                        '[4] - Переместить оргтехнику в подразделение\n'
                        '[5] - Именение количества оргтехники по модели\n'
                        '[6] - Выход\n'
                        'Выберите пункт меню:')
    if user_choise == '1':
        Stock().arrival_Equipment()
    if user_choise == '2':
        Stock().showing_Equipment()
    if user_choise == '3':
        Stock().find_Equipment()
    if user_choise == '4':
        Stock().moving_Equipment()
    if user_choise == '5':
        Stock().change_count()
    if user_choise == '6':
        print('До новых встреч!')
        break
