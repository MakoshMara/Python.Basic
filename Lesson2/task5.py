my_list = [8,7,7,6,5,5,4,3]
user_number = input('Введите любое число:')
while not user_number.isnumeric():
    user_number = input('Это было не число!:')
for number in my_list:
    index = my_list.index(number)
    if number < int(user_number):
        if index == 0:
            my_list.insert(0,(user_number))
            break
        my_list.insert((index-1),(user_number))
        break
    elif index == len(my_list)-1:
        my_list.insert((index +1), (user_number))
        break
print(my_list)