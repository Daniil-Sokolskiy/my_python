"""
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
"""


def read_file(filename):
    with open(filename) as file:
        return file.read()


def split_polinom(polinom):
    polinom = polinom[:-4].split(' + ')
    for i, element in enumerate(polinom):
        polinom[i] = element.strip().split('*x')
    return polinom


def sum_polinoms(polinom1, polinom2):
    if len(polinom2) < len(polinom1):
        polinom1, polinom2 = polinom2, polinom1
    sum_polinom = []
    for element in polinom2:
        if len(element) > 1:
            filter_el = list(filter(lambda el: element[-1] in el, polinom1))
            if filter_el:
                filter_el = filter_el.pop()
                element[0] = str(int(element[0]) + int(filter_el[0]))
            sum_polinom.append(element)
        else:
            s = polinom1.pop()
            xs = ''.join(s)
            element[0] = str(int(element[0]) + int(xs))
            sum_polinom.append(element)
    return sum_polinom


def lst_to_strpolinom(polinom_list):
    expression = ''
    for i, element in enumerate(polinom_list):
        expression += '*x'.join(element)
        if i != len(polinom_list):
            expression += ' + '
        if len(element) == 1:
            expression = expression[:-3]
    expression += ' = 0'
    return expression


multinomial1 = read_file("multinomial.txt")
multinomial2 = read_file("multinomial2.txt")
multinomial1 = split_polinom(multinomial1)
multinomial2 = split_polinom(multinomial2)
lst_multinomials = sum_polinoms(multinomial1, multinomial2)
final_file = open('sum_multinomial.txt', 'w')
final_file.write(lst_to_strpolinom(lst_multinomials))
