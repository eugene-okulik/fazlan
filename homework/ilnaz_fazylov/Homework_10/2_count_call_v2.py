def repeat_me(count):
    def my_decorator(func):
        def wrapper(*args):
            for i in range(count):
                func(*args)

        return wrapper

    return my_decorator


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
