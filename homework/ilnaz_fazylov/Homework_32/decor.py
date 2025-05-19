import time
import requests


def my_decorator(func):
    def wrapper():
        time_start = time.time()
        print(f'Определим время начала выполнения функции {round(time_start, 2)}')
        func()
        time_end = time.time()
        print(f'Определим время завершения выполнения функции {round(time_end, 2)}')
        print(f'Определим время выполнения функции {round((time_end - time_start), 2)}')

    return wrapper


@my_decorator
def get_url():
    print('Выполняем функцию')
    response = requests.get('https://www.google.ru/')
    return response


get_url()
