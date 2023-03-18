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


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class IsString:
    def __set__(self, instance, value):
        if type(value) != str:
            raise TypeError(f'The {self.my_attr} must be a string!')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class NonNegative:
    def __set__(self, instance, value):
        if type(value) not in (int, float):
            raise TypeError(f'The {self.my_attr} must be a number!')
        elif value < 0:
            raise ValueError(f'The {self.my_attr} '
                             f'must be a non-negative number!')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    name = IsString()
    surname = IsString()
    wage = NonNegative()
    bonus = NonNegative()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker, metaclass=Singleton):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self.wage + self.bonus

    def __str__(self):
        return f"Position: {self.position}\n"\
               f"Name: {self.get_full_name()}\nSalary: " \
               f"{self.get_total_income()}\n"


obj1 = Position("name", "surname", "chief", 100000, 30000)
obj2 = Position("name", "surname", "chief", 100000, 20000)
print(obj1 is obj2)
print(obj1)
print(obj2)
