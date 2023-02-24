"""
Задайте натуральное число N. Напишите программу, которая составит список
простых множителей числа N.
"""
import math


def check_prime(n):
    factorial_prev = math.factorial(n - 1)
    if (factorial_prev + 1) % n == 0:
        return True


def multipliers(n):
    primes = []
    for numb in range(2, n + 1):
        if not n % numb and check_prime(numb):
            primes.append(numb)
    return print(primes)


num = int(input("Введите натуральное число: "))
multipliers(num
            )