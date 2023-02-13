# Написать метод, который определяет, какие элементы присутствуют в двух
# экземплярах в каждом из массивов (= в двух и более, причем в каждом).
# На вход подаются два массива. На выходе массив с необходимыми совпадениями.
from collections import Counter

a = [10, 10, 23, 10, 123, 66, 78, 123, 66]
b = [10, 11, 32, 56, 10, 123, 17, 66, 89, 66]
doubles_a = []
doubles_b = []

for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

for i in range(len(b)):
    for j in range(len(b)-1):
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]

for i in range(len(a)-1):
    if a[i] == a[i+1] and a[i] != a[i-1]:
        doubles_a.append(a[i])

for i in range(len(b)-1):
    if b[i] == b[i+1] and b[i] != b[i-1]:
        doubles_b.append(b[i])

print(set[doubles_a] and set[doubles_b])