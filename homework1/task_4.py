# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника.

revenue = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
print(f"прибыль фирмы: {revenue-costs}")
print(f"Рентабельность выручки: {(revenue-costs)/revenue}")
numbers = int(input("Введите численность сотрудников: "))
print(f"Прибыль фирмы в расчёте на 1 сотрудника: {(revenue-costs)/numbers}")