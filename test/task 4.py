# Написать метод/функцию, который/которая на вход принимает целое число,
# а на выходе возвращает то, является ли число простым
# (не имеет делителей кроме 1 и самого себя).
import math


def is_prime(num):
    if num % 2 == 0:
        return num == 2
    num2 = 3
    while num2 * num2 <= num and num % num2 != 0:
        num2 += 2
    return num2 * num2 > num


print(is_prime(int(input("Enter a number: "))))
