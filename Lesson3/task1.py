n_1 = input('Введите делимое:')
n_2 = input('Введите делитель:')


def proverka_delimogo(delimoe):
    while True:
        try:
            delimoe = float(delimoe)
            return delimoe
        except ValueError:
            delimoe = input('Делимое должно быть числом! Введите делимое:')


def proverka_delitel(delitel):
    while True:
        try:
            delitel = float(delitel)
            return delitel
        except ValueError:
            delitel = input('Делимое должно быть числом! Введите делимое:')


def proverka_zero(delimoe, delitel):
    while True:
        try:
            delimoe / delitel
            return delitel
        except ZeroDivisionError:
            delitel = proverka_delitel(input('На ноль делить нельзя (но это не точно). Введите делитель: '))


def delenie(delimoe, delitel):
    delimoe, delitel = float(delimoe), float(delitel)
    print(f'Результат деления: {delimoe / delitel:.2f}')


n_1 = proverka_delimogo(n_1)
n_2 = proverka_delitel(n_2)
n_2 = proverka_zero(n_1, n_2)

delenie(n_1, n_2)
