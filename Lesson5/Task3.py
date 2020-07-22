with open("text_3.txt", "r", encoding="utf-8") as text:
    spisok_looserov = []
    for el in text:
        fot = []
        zarplata = float(el.split()[1])
        fot.append(zarplata)
        if zarplata < 20000.0:
            spisok_looserov.append(el.split()[0])
    print(f'Список тех, кто получает меньше 20 0000 - {(", ".join(spisok_looserov))}')
    print(f'Средняя зарплата - {sum(fot) / len(fot)}')
