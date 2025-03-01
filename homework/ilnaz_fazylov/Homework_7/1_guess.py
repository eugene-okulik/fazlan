def guess(digit):
    while True:
        user_input = int(input('Угадай цифру '))
        if user_input == digit:
            print('Поздравляю! Вы угадали!')
            break
        else:
            print('попробуйте снова')


guess(4)