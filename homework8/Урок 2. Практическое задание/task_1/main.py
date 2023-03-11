import csv
import re


def get_data(file_name, main_list):
    titles_list = []
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    file_obj = open(file_name, 'r')
    data = file_obj.read()
    os_prod_re = re.compile(r'Изготовитель системы:\s*\S*')
    os_prod_list.append(os_prod_re.findall(data)[0].split()[2])
    os_name_re = re.compile(r'Название ОС:\s*\S*\s*\S*\s*\S*\s*\S*')
    os_name_list.append(os_name_re.findall(data)[0].split()[2:6])
    os_code_re = re.compile(r'Код продукта:\s*\S*')
    os_code_list.append(os_code_re.findall(data)[0].split()[2])
    os_type_re = re.compile(r'Тип системы:\s*\S*')
    os_type_list.append(os_type_re.findall(data)[0].split()[2])
    res = list(map(lambda x: ' '.join(x), os_prod_list))
    res += list(map(lambda x: ' '.join(x), os_name_list))
    res += list(map(lambda x: ' '.join(x), os_code_list))
    res += list(map(lambda x: ' '.join(x), os_type_list))
    main_list.append(res)
    return main_list


def write_to_csv(csv_name):
    main_lst = [['Изготовитель системы:''\t''Название ОС:''\t''Код продукта:'
                 '\t''Тип системы:']]
    get_data('info_1.txt', main_lst)
    get_data('info_2.txt', main_lst)
    get_data('info_3.txt', main_lst)
    print(main_lst)
    with open(csv_name, 'w') as out:
        out = csv.writer(out)
        for row in main_lst:
            out.writerow(row)
    with open(csv_name) as out:
        print(out.read())


write_to_csv('out_data.csv')


