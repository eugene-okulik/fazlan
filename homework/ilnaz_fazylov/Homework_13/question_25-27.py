import datetime
import os

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(file_path, 'r', encoding='utf-8') as data_file:
        for line in data_file.readlines():
            yield line


def find_date():
    for line in read_file():
        lst = line.split(' - ')
        date_line = ''.join(lst[0][3:])
        date = datetime.datetime.strptime(date_line, '%Y-%m-%d %H:%M:%S.%f')
        yield date


def print_result():
    for line in read_file():
        # Подскажи как одновременно работать со значениями 2 генераторов?
        # Как получать сразу строку и дату?
        # пробовал через chain и yield from, но ничего не подошло

        # date = find_date()
        ...

# print_result()
