number = 0
num = 0
base_item = []
user_answer = 'да'
while True:
    if user_answer == 'да':
        name_item = input('Введите наименование товара:')
        price_item = int(input('Введите цену товара:'))
        count_item = int(input('Введите количество товара:'))
        ed_item = input('Введите единицы измерения товара:')
        dict_item = {'Наименование': name_item, 'Цена': price_item, 'Количество': count_item,
                     'Единицы измерения': ed_item}
        base_item.insert(number, (number + 1, dict_item))
        number += 1
        user_answer = input('Хотите ввести еще товар?:')
    else:
        break
for i in base_item:
    print(i, end='\n')
user_answer = input('Хотите увидеть аналитику по товарам?:')
if user_answer == 'да':
    dict_analitic = {'Наименование': [], 'Цена': [], 'Количество': [], 'Единицы измерения': []}
    while num < len(base_item):
        dict_analitic['Наименование'].insert(num, base_item[num][1]['Наименование'])
        dict_analitic['Цена'].insert(num, base_item[num][1]['Цена'])
        dict_analitic['Цена'] = list(set(dict_analitic['Цена']))
        dict_analitic['Количество'].insert(num, base_item[num][1]['Количество'])
        dict_analitic['Количество'] = list(set(dict_analitic['Количество']))
        dict_analitic['Единицы измерения'].insert(num, base_item[num][1]['Единицы измерения'])
        dict_analitic['Единицы измерения'] = list(set(dict_analitic['Единицы измерения']))
        num += 1
    user_answer = input('Хотите увидеть список наименований товаров?:')
    if user_answer == 'да':
        print(dict_analitic['Наименование'])
    user_answer = input('Хотите увидеть возможные цены товаров?:')
    if user_answer == 'да':
        print(dict_analitic['Цена'])
    user_answer = input('Хотите отстатки на складе?:')
    if user_answer == 'да':
        print(dict_analitic['Количество'])
    user_answer = input('Хотите увидеть общую аналитику?:')
    if user_answer == 'да':
        print(dict_analitic)
else:
    print('До новых встреч!')