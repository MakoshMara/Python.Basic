my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
gen_list = [el for el in my_list if
            my_list[my_list.index(el)] > my_list[my_list.index(el) - 1] and my_list.index(el) != 0]
print(gen_list)
