"""
1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
элементов списка, стоящих на нечётной позиции.

*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""


def summa(lt):
    s = 0
    for i in range(1, len(lt), 2):
        s += lt[i]
    return print(s)


lst = []
try:
    while True:
        num = int(input('Введите число: '))
        lst.append(num)
        if not num:
            break
except ValueError:
    print("Неверные данные, выход из программы")
print(lst)
summa(lst)
