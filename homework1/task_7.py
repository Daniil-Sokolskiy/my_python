# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

x = int(input("Enter x: "))
y = int(input("Enter y: "))
if x > 0 and y > 0:
    print("1 quarter")
elif x < 0 < y:
    print("2 quarter")
elif x < 0 and y < 0:
    print("3 quarter")
elif x > 0 > y:
    print("4 quarter")
elif x == 0 and y != 0:
    print("Point on the X axis")
elif y == 0 and x != 0:
    print("Point on the Y axis")
else:
    print("Point at the origin")
