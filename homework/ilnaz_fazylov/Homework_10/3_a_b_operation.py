def control_operation(func):
    def wrapper(first, second, operation):
        if first == second:
            operation = '+'
        elif first < 0 or second < 0:
            operation = '*'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'
        result = func(first, second, operation)
        return result

    return wrapper


@control_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return round((first / second), 2)
    else:
        return first * second


first = int(input('Input first number: '))
second = int(input('Input second number: '))
print(calc(first, second, operation=control_operation))
