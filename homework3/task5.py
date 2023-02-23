"""
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""
import math


def multi(lst):
    multi_list = []
    for i in range(0, math.floor(len(lst)/2)):
        multi_list.append(lst[i]*lst[-(i+1)])
    return print(multi_list)


lst = []
try:
    while True:
        num = int(input('Введите число: '))
        lst.append(num)
        if not num:
            break
except ValueError:
    print("Неверные данные, выход из цикла")
multi(lst)
