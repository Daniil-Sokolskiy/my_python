"""
Задайте последовательность чисел. Напишите программу, которая выведет список
неповторяющихся элементов исходной последовательности.
"""


def unique(list_):
    uniq = []
    for elem in list_:
        if elem not in uniq:
            uniq.append(elem)
    return uniq


lst = input("Введите числа через пробел: ").split(" ")
print(unique(lst))
