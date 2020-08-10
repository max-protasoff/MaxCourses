import pprint


# ЧАСТЬ 1
def headers():
    with open(r'C:\MaxCourses\PythonBasics\6.files\rec.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip()
            if '|' in line or line == '' or line.isdigit():
                continue
            else:
                print(line)

# Пж, подскажите, почему это не работает, если писать в стиле:
# if '|' not in line or line != ''
#    print(line)


# ЧАСТЬ 2
def cook_bk():
    cook_book = {}
    with open(r'C:\MaxCourses\PythonBasics\6.files\rec.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip()
            if line.isdigit():
                ingr_nums = int(line)
            elif "|" in line:
                if ingr_nums > 0:
                    line = line.split(' | ')
                    ingr_name = line[0]
                    ingr_quant = line[1]
                    ingr_measure = line[2]
                    cook_book[dish_name].append(
                        {'ingredient_name': ingr_name, 'quantity': ingr_quant, 'measure': ingr_measure})
                    ingr_nums -= 1
            elif line != '':
                dish_name = line
                cook_book[dish_name] = []

        return cook_book

# ЧАСТЬ 3

def get_shop_list_by_dishes(dishes_arr, people):    # (['Запеченный картофель', 'Омлет'], 2)
    global dish_dict
    user_ingrs = dict()
    for dish in dishes_arr:
        if dish in dish_dict:
            for ingr in dish_dict[dish]:
                if ingr.get('ingredient_name') in user_ingrs:
                    user_ingrs[ingr['ingredient_name']] += int(ingr['quantity']) * people
                else:
                    user_ingrs[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': (int(ingr['quantity']) * people)}
    return user_ingrs



'''
{
'Картофель': {'measure': 'кг', 'quantity': 2},
'Молоко': {'measure': 'мл', 'quantity': 200},
'Помидор': {'measure': 'шт', 'quantity': 4},
'Сыр гауда': {'measure': 'г', 'quantity': 200},
'Яйцо': {'measure': 'шт', 'quantity': 4},
'Чеснок': {'measure': 'зубч', 'quantity': 6}
}
'''



# Вызов функций 1-3
headers()
print('==========================================')
dish_dict = cook_bk()
pprint.pprint(dish_dict, indent=4)
print('==========================================')
request_dishes = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint.pprint(request_dishes, indent=4)
