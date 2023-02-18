"""
Задайте список из вещественных чисел. Напишите программу, которая найдёт
разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
import random

n = int(input('Введите длину списка: '))
lst = []
for i in range(n):
    num = random.uniform(0, 100)
    lst.append(round(num, 2))
print(lst)
for i in range(len(lst)):
    lst[i] = round(lst[i] % 1, 2)
print(round(max(lst) - min(lst), 2))

