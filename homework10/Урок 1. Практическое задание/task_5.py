"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import time

import chardet
import os

args = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]
ya_ping = subprocess.Popen(args[0], stdout=subprocess.PIPE)
youtube_ping = subprocess.Popen(args[1], stdout=subprocess.PIPE)
print(ya_ping.stdout)
print(youtube_ping.stdout)
for line in ya_ping.stdout:
    # res = chardet.detect(line)
    # print(res)
    # print(line)
    result = chardet.detect(line)
    print(line.decode(result['encoding']))
time.sleep(3)
for line in youtube_ping.stdout:
    res = chardet.detect(line)
    print(line.decode(res['encoding']))
