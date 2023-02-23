"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""


def month(num):
    mon = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
           'august', 'september', 'october', 'november', 'december']
    months = {1: 'january', 2: 'february', 3: 'march', 4: 'april', 5: 'may',
              6: 'june', 7: 'july', 8: 'august', 9: 'september', 10: 'october',
              11: 'november', 12: 'december'}
    return print(f'Результат через список: {mon[num - 1]}'),\
        print(f'Результат через словарь: {months[num]}')


try:
    num_month = int(input('Введите номер месяца: '))
except ValueError:
    print('Неверные входные данные')
else:
    month(num_month)
