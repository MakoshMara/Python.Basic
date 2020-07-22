import json

with open("text_7.txt", "r", encoding="utf-8") as text:
    average_dict = {'Средняя прибыль': []}
    firms = {}
    for i in text:
        my_list = i.split()
        pribyl = (int(my_list[2]) - int(my_list[3]))
        firms[my_list[0]] = pribyl
        if pribyl > 0:
            average_dict['Средняя прибыль'].append(pribyl)
        print(f'Прибыль {my_list[1]} {my_list[0]} - {pribyl}')
    ist_average = sum(average_dict['Средняя прибыль']) / len(average_dict['Средняя прибыль'])
    print(f'Средняя прибыль - {ist_average}')
    average_dict['Средняя прибыль'] = ist_average

    print(f'Итоговый список - {[firms, average_dict]}')

with open("text_for_7.json", "w", encoding="utf-8") as write_json:
    json.dump([firms, average_dict], write_json, indent=2, ensure_ascii=False)
