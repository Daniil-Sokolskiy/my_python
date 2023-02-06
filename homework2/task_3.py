# Создать список и заполнить его элементами различных типов данных.
# Реализовать проверку типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

from ast import literal_eval


def types(s, d):
    for ele in s.split(d):
        try:
            yield literal_eval(ele)
        except ValueError:
            yield ele


string = input("Введите элементы через пробел: ")
lst = list(types(string, " "))
print(lst)

for el in lst:
    print(type(el))
