"""
Задана натуральная степень k.
Сформировать случайным образом список коэффициентов
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
"""
import random


def list_coefficients(n):
    lst_coef = []
    for i in range(0, n + 1):
        lst_coef.append(random.randint(0, 100))
    return lst_coef


def multinom(n, lst_coef, s):
    lst_multinom = []
    for i in range(0, n + 1):
        if lst_coef[i] == 0:
            continue
        if i == n:
            lst_multinom.append(f'{lst_coef[i]} = 0')
        elif i == n - 1:
            lst_multinom.append(f'{lst_coef[i]}*x')
        else:
            lst_multinom.append(f'{lst_coef[i]}*x**{n - i}')
        s = ' + '
        s = s.join(lst_multinom)
    return s


k = int(input("Введите высшую степень многочлена: "))
m = int(input("Введите высшую степень второго многочлена: "))

str_ = None
file = open("multinomial.txt", "w")
file2 = open("multinomial2.txt", "w")
file.write(multinom(k, list_coefficients(k), str_))
file2.write(multinom(m, list_coefficients(m), str_))
