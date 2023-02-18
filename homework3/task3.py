"""
3. Реализовать структуру данных «Товары». Она должна представлять собой список
кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у
пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""


i = 0
naming_lst = []
cos_lst = []
cou_lst = []
un_set = set()


def goods(lst, lst_1):
    global i
    while True:
        goods_dict = {}
        i += 1
        try:
            name = input('Введите название товара: ')
            if not name:
                break
        except ValueError:
            print('Неверный тип данных')
            i -= 1
            goods(lst, lst_1)
        else:
            goods_dict['Название'] = name
        try:
            cost = input('Введите цену товара: ')
            if not cost:
                break
            cost = int(cost)
        except ValueError:
            print('Неверный тип данных')
            i -= 1
            goods(lst, lst_1)
            break
        else:
            goods_dict['цена'] = cost
        try:
            count = input('Введите количество товара: ')
            if not count:
                break
            count = int(count)
        except ValueError:
            print('Неверный тип данных')
            i -= 1
            goods(lst, lst_1)
            break
        else:
            goods_dict['количество'] = count
        try:
            unit = input('Введите единицу товара: ')
            if not unit:
                break
        except ValueError:
            print('Неверный тип данных')
            i -= 1
            goods(lst, lst_1)
            break
        else:
            goods_dict['единица'] = unit
        naming_lst.append(name)
        cos_lst.append(cost)
        cou_lst.append(count)
        un_set.add(unit)
        lst.append((i, goods_dict))
        lst_1['название'] = naming_lst
        lst_1['цена'] = cos_lst
        lst_1['количество'] = cou_lst
        lst_1['единица'] = un_set


list_of_goods = []
dict_of_categories = {}
goods(list_of_goods, dict_of_categories)
print(*list_of_goods, sep='\n')
for key, value in dict_of_categories.items():
    print(key, value)