def int_fync(user_string):
    return user_string.title()


def proverka(string):
    list_string = []
    string = string.replace(' ', '')
    for i in string:
        list_string.append(i)
    for i in list_string:
        if ord(i) < 97 or ord(i) > 122:
            return None
    return string


user_string = input('Введите строку маленькими латинскими буквами:')
while proverka(user_string) is None:
    user_string = input('Введите строку МАЛЕНЬКИМИ ЛАТИНСКИМИ буквами:')
print(int_fync(user_string))
