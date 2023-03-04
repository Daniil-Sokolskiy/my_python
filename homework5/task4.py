"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""
import random


def sum_of_elem(k, elem, sum_of_elems):
    if k == 0:
        return print(f'Cумма элементов последовательности: {sum_of_elems}')
    sum_of_elems += elem
    sum_of_elem(k - 1, -elem / 2, sum_of_elems)


n = int(input("Enter count of elements: "))
element = 1
sum_of_elements = 0
print(f'Количество элементов = {n}')
sum_of_elem(n, element, sum_of_elements)
