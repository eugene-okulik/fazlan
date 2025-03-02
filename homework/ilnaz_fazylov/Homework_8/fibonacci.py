def fibonacci(n):
    n_1, n_2 = 0, 1
    for n in range(n):
        yield n_1
        n_1, n_2 = n_2, n_2 + n_1


def get_number(n):
    count = 1
    for number in fibonacci(n):
        if count == n:
            print(number)
        count += 1


get_number(5)
get_number(200)
get_number(1000)
get_number(100000)
