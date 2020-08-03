class Data:
    def __init__(self, user_str):
        self.user_str = user_str

    def prime(self):
        print(self.number_of_user_str(self.user_str))
        self.validation(self.number_of_user_str(self.user_str))

    @classmethod
    def number_of_user_str(cls, user_str):
        try:
            return list(map(int, user_str.split('-')))
        except ValueError:
            print('Вы ввели дату не в числовом формате')

    @staticmethod
    def validation(obj):
        if obj[0] > 31 or obj[1] > 12 or obj[1] < 1 or obj[2] > 2020:
            print('Некорректные данные')


date_1 = Data(input('Введите дату в формате дд-мм-гггг:'))
date_1.prime()
