"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через
перегрузку str
str(self) - вызывается функциями str, print и format.
Возвращает строковое представление объекта.
"""


class Worker:
    name = "name"
    surname = "surname"
    position = "position"
    _income = "{'wage': wage, 'bonus': bonus}"

    def __init__(self, new_name, new_surname, new_position, wage, bonus):
        self.name = new_name
        self.surname = new_surname
        self.position = new_position
        self._income = {'wage': wage, 'bonus': bonus}

    def __str__(self):
        return f'Сотрудник: {self.name} {self.surname}, {self.position}, ' \
               f'{self._income["wage"]+self._income["bonus"]}'


class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(f'{self.name[:1]}.{self.surname} - {self._income}')


position_1 = Position("namee", "suurname", "pos", 5000, 1000)
position_2 = Position("nameeeee", "suuuuurname", "pooos", 10000, 2000)

position_1.get_full_name()
position_2.get_total_income()

print(position_1)
