# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

n = float(input('Введите число N: '))
h = float(input('Введите шаг: '))
s = 1
i = 1
while i <= n:
    s *= i
    i += h
    print(s)
