"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""


mess = ['class', 'function', 'method']

for word in mess:
    b_word = bytes(word, encoding='utf-8')
    print(f'{word} - {len(word)} - {type(word)}\n'
          f'{b_word} - {len(b_word)} - {type(b_word)}')
