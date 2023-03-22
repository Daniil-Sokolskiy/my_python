"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b''(без encode decode)

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""
message = ['attribute', 'класс', 'функция', 'type']
for word in message:
    try:
        if len(word) != len(bytes(word, encoding='utf-8')):
            raise SyntaxError("Невозможно записать в байтовом типе")
        else:
            print(bytes(word, encoding='utf-8'))
    except SyntaxError:
        print("Невозможно записать в байтовом типе")
