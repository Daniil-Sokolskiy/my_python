# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня,
# на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b
# и выводить одно натуральное число — номер дня.

a = int(input("Введите результат пробежки в первый день в км: "))
b = int(input("Введите цель  пробежки в км: "))
day = 0
while a < b:
    a *= 1.1
    day += 1
print(f"Результат был достигнут на {day} день")
