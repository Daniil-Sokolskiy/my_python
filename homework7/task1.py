"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод
running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import keyword
import time


class trafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        time_start = time.time()
        while True:
            dif = time.time() - time_start
            print(dif)
            if dif > 20:
                break
            self.__color = "red"
            print(self.__color)
            time.sleep(7)
            self.__color = "yellow"
            print(self.__color)
            time.sleep(2)
            self.__color = "green"
            print(self.__color)
            time.sleep(5)


traffic_light_1 = trafficLight()
traffic_light_1.running()
