import random


a = [random.randint(-100, 100) for el in range(random.randint(10, 20))]
print(a)
min_number = int(input("Min: "))
max_number = int(input('Max: '))
for i in range(len(a)):
    if min_number <= a[i] <= max_number:
        print(f"{a[i]} ({i})")
