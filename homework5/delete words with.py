"""Напишите программу, удаляющую из текста все слова, содержащие ""абв""."""


def deleting_words(words_lst, new_words_lst, symbol_):
    if len(words_lst) == 0:
        return new_words_lst
    if symbol_ not in words_lst[0]:
        new_words.append(words_lst[0])
    return deleting_words(words_lst[1:], new_words_lst, symbol_)


text = input('Enter string: ')
words = text.split(' ')
symbols = input('Enter symbols: ')
new_words = []
deleting_words(words, new_words, symbols)
new_text = ' '.join(new_words)
print(new_text)



