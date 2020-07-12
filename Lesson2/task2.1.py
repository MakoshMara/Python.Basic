list = list(input('Введите любую строчку:'))
count = len(list) // 2
i = 0
while i < count:
    list_n = list[::2]
    current_item = list[list.index(list_n[i])]
    next_item = list[list.index(list_n[i]) + 1]
    list[list.index(list_n[i]) + 1] = current_item
    list[list.index(list_n[i])] = next_item
    i += 1
print(list)