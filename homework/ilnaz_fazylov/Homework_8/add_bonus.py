import random


SALARY = int(input('Input salary: '))

# Вначале реализовал через функцию ниже и передавал в salary.
# Однако при вызове print_result() дублируется ввод пользователя.
# Остановился на текущем решении.
# Подскажи, как можно было сделать по-другому?

def input_salary():
    salary = int(input('Input salary: '))
    return salary


def calculate_bonus():
    bonus = bool(random.choice([True, False]))
    return bonus


def add_bonus():
    salary = SALARY
    bonus = calculate_bonus()
    if bonus:
        salary += random.randint(0, 5000)
    return salary


def print_result():
    salary = SALARY
    bonus = calculate_bonus()
    new_salary = add_bonus()
    print(f"{salary}, {bonus} - '${new_salary}'")


print_result()
