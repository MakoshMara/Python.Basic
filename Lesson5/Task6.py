import re

with open("text_6.txt", "r", encoding="utf-8") as text:
    my_dict = {}
    for i in text:
        my_list = i.split()
        res = []
        for el in my_list:
            if len(re.findall(r'\d', el)) != 0:
                res.append(re.split('[(]', el)[0])
            if my_list.index(el) == 0:
                my_dict[el[:-1]] = res
    for i in my_dict:
        my_dict[i] = sum(list(map(int, my_dict[i])))
    print(my_dict)
