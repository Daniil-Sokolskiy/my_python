# Для списка реализовать обмен значений соседних элементов,
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

s = input("Введите целые числа через пробел: ").split(' ')
print(f'Исходный список: {s}')
i = 0
while i < len(s):
    if i % 2 == 1:
        s[i], s[i-1] = s[i-1], s[i]
    i += 1
print(f'Преобразованный список: {s}')
