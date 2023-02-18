"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных
 индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1,
 2, 3, 5, 8, 13, 21]
"""


def feb(n):
    lst_feb = []
    if n == 0:
        return 0
    if n in (1, 2):
        return 1
    return feb(n-1) + feb(n-2)


num = int(input('Введите число: '))
list_feb = []
for i in range(num+1):
    list_feb.append(feb(i))
    list_feb = [-feb(i)]+list_feb
print(list_feb)
