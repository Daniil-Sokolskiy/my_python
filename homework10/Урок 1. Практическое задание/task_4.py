"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


mess = ['разработка', "администрирование", "protocol", "standard"]
encode_mess = []
for word in mess:
    encode_mess.append(word.encode())
print(*encode_mess, sep='\n')

decode_mess = []
for code in encode_mess:
    decode_mess.append(code.decode())
print(*decode_mess, sep='\n')

