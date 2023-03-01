"""Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг
после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не
более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты
у своего конкурента?
А) Добавьте игру против бота
B) Подумайте как наделить бота "интеллектом"
"""
import random


def sweets_pvp(who_first, all_sw, plr_1=0, plr_2=0):
    print(f"There are {all_sw} sweets now")
    if who_first == 1:
        who_win = 2
    else:
        who_win = 1
    if all_sw <= 0:
        return print(f'Player {who_win} win! Congratulations!') and exit()
    if who_first == 1:
        try:
            plr_1 = int(input(f"Player 1 Turn\nEnter count of sweets, what "
                              f"you want to take: "))
            if plr_1 not in range(1, 29):
                raise ValueError
            all_sw -= plr_1
            who_first = 2
            if all_sw <= 0:
                return print(
                    f'Player {who_win} win! Congratulations!') and exit()
            print(f"There are {all_sw} sweets now")
            plr_2 = int(input(f"Player 2 Turn\nEnter count of sweets, what "
                              f"you want to take: "))
            if plr_2 not in range(1, 29):
                raise ValueError
            all_sw -= plr_2
            who_first = 1
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            sweets_pvp(who_first, all_sw, plr_1, plr_2)
            exit()
    else:
        try:
            plr_2 = int(input(f"Player 2 Turn\nEnter count of sweets, what "
                              f"you want to take: "))
            if plr_2 not in range(1, 29):
                raise ValueError
            all_sw -= plr_2
            who_first = 1
            if all_sw <= 0:
                return print(
                    f'Player {who_win} win! Congratulations!') and exit()
            print(f"There are {all_sw} sweets now")
            plr_1 = int(input(f"Player 1 Turn\nEnter count of sweets, what "
                              f"you want to take: "))
            if plr_1 not in range(1, 29):
                raise ValueError
            all_sw -= plr_1
            who_first = 2
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            sweets_pvp(who_first, all_sw, plr_1, plr_2)
            exit()
    sweets_pvp(who_first, all_sw, plr_1, plr_2)
    exit()


def sweets_pve(who_first, all_sw, plr_1=0, plr_2=0):
    print(f"There are {all_sw} sweets now")
    if who_first == 1:
        who_win = "PC"
    else:
        who_win = "player"
    if all_sw <= 0:
        return print(f'Player {who_win} win! Congratulations!') and exit()
    if who_first == 1:
        try:
            plr_1 = int(input(f"Player 1 Turn\nEnter count of sweets, what "
                              f"you want to take: "))
            if plr_1 not in range(1, 29):
                raise ValueError
            all_sw -= plr_1
            who_first = 2
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            sweets_pve(who_first, all_sw, plr_1, plr_2)
            exit()
        if all_sw <= 0:
            return print(
                    f'Player {who_win} win! Congratulations!') and exit()
        print(f"There are {all_sw} sweets now")
        if all_sw in range(30, 57):
            plr_2 = all_sw - 29
        else:
            plr_2 = random.randint(1, 29)
        print(f"Player 2 Turn\nPC was taken: {plr_2} sweets")
        all_sw -= plr_2
        who_first = 1
    else:
        if all_sw in range(30, 57):
            plr_2 = all_sw - 29
        else:
            plr_2 = random.randint(1, 29)
        print(f"Player 2 Turn\nPC was taken: {plr_2} sweets")
        all_sw -= plr_2
        who_first = 1
        if all_sw <= 0:
            return print(
                    f'Player {who_win} win! Congratulations!') and exit()
        print(f"There are {all_sw} sweets now")
        try:
            plr_1 = int(input(f"Player 1 Turn\nEnter count of sweets, what "
                              f"you want to take: "))
            if plr_1 not in range(1, 29):
                raise ValueError
            all_sw -= plr_1
            who_first = 2
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            sweets_pve(who_first, all_sw, plr_1, plr_2)
            exit()
    sweets_pve(who_first, all_sw, plr_1, plr_2)
    exit()


all_sweets = 2021
print('PVP(enter 1) or PVE(enter 2)?')
if int(input()) == 1:
    first_step = random.randint(1, 2)
    player_1 = player_2 = 0
    print(f'First step do player number {first_step}')
    sweets_pvp(first_step, all_sweets, player_1, player_2)
else:
    first_step = random.randint(1, 2)
    player_1 = pc = 0
    if first_step == 1:
        print(f'First step do player')
    else:
        print(f'First step do PC')
    sweets_pve(first_step, all_sweets, player_1, pc)
