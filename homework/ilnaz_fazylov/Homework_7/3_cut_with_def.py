def convert_to_list(str_1, str_2, str_3, str_4):
    lst = []
    str_in_list = [str_1, str_2, str_3, str_4]
    for elem in str_in_list:
        lst.append(int(elem.split()[-1]))
    return lst


def add_number():
    lst = convert_to_list('результат операции: 42',
                          'результат операции: 54',
                          'результат работы программы: 209',
                          'результат: 2'
                          )
    for number in lst:
        print(number + 10)


add_number()
