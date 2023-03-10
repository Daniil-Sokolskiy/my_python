"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для
формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных
в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы
в привычном виде. Далее реализовать перегрузку метода add() для реализации
операции сложения двух объектов класса Matrix (двух матриц). Результатом
сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки
второй матрицы и т.д.
"""


class Matrix:
    matr_list = None

    def __init__(self, new_list):
        self.matr_list = new_list

    def __str__(self):
        return '\n'.join(str('\t'.join(str(el) for el in x))
                         for x in self.matr_list)

    def __add__(self, other):
        return Matrix(list(map(
            lambda x, y: list(map(lambda z, w: z + w, x, y)),
            self.matr_list, other.matr_list)))


matr1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matr2 = Matrix([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
print(matr2)
matr = matr1 + matr2
print(matr)
