def write_text():
    with open("text_for_1.txt", "w", encoding="utf-8") as user_text:
        user_string = '1'
        while len(user_string) != 0:
            user_string = input('Введите строку: Если хотите прекратить, просто оставьте строку пустой:')
            user_text.write(user_string + '\n')
    return


def podschet_strok():
    with open("text_for_1.txt", "r", encoding="utf-8") as user_text:
        return len(user_text.readlines()) - 1


def podschet_slov():
    with open("text_for_1.txt", "r", encoding="utf-8") as user_text:
        for i in user_text.readlines():
            if len(i.split()) != 0:
                yield len(i.split())


write_text()
with open("text_for_1.txt", "r", encoding="utf-8") as user_text:
    content = user_text.read()
    print(content)
print(f'Число строк - {podschet_strok()}')
i = 1
for el in podschet_slov():
    print(f'Слов в строке {i} - {el}')
    i += 1
