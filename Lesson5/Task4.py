with open("text_4.txt", "r", encoding="utf-8") as text:
    dict = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}
    with open("text_for_4.txt", "w", encoding="utf-8") as text2:
        for el in text:
            list = el.split()
            list[0] = dict.get(el.split()[2])
            print(' '.join(list), file=text2)
