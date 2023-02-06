# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.

from random import randint


def lst(q):
    my_lst = []
    for i in range(q):
        my_lst.append(randint(-q, q))
    return my_lst


n = int(input('Введите число N: '))
numbers = lst(n)
print(numbers)
x = open('file.txt', 'r')
result = numbers[int(x.readline())] * numbers[int(x.readline(2))]
print(result)
