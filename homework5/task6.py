"""
Задание 6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def quiz(n, attempt=10):
    if attempt == 0:
        print(f"Game over. Загаданное число - {n}")
    else:
        user_number = int(input("Ваше число?: "))
        if user_number > n:
            return print('Загаданное число меньше вашего.'), quiz(n, attempt-1)
        elif user_number < n:
            return print('Загаданное число больше вашего.'), quiz(n, attempt-1)
        return print("Вы победили!")


guessed_num = random.randint(0, 100)
quiz(guessed_num)
