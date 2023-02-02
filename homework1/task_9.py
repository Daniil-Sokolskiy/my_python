# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

x_a = int(input("Enter x of point A = "))
y_a = int(input("Enter y of point A = "))
x_b = int(input("Enter x of point B = "))
y_b = int(input("Enter y of point B = "))
print(f"Distance between points: {((x_a-x_b)**2+(y_a-y_b)**2) ** 0.5}")
