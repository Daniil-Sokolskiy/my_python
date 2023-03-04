"""
Задача 30: Заполните массив элементами арифметической прогрессии.
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""


def arith_progression():
    a1 = int(input("Enter the first el: "))
    count = int(input("Enter count of elements: "))
    d = int(input("Enter a difference: "))
    i = 0
    arith_progress = [a1, ]
    for el in range(count):
        an = a1 + (i + 1) * d
        i += 1
        arith_progress.append(an)
    return print(*arith_progress, sep='\n')


arith_progression()
