user_str = input('Введите слова через пробел:')
user_list = user_str.split()
i = 0
while i < len(user_list):
    if len(user_list[i]) > 10:
        user_list[i] = (user_list[i])[0:10]
    i += 1
for ind, el in enumerate(user_list, start=1):
    print(ind, ')', el)