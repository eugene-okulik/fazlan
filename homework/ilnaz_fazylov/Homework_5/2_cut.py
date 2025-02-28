str_1 = 'результат операции: 42'
str_2 = 'результат операции: 514'
str_3 = 'результат работы программы: 9'

print(int(str_1[str_1.index(':') + 1:]) + 10)
print(int(str_2[str_2.index(':') + 1:]) + 10)
print(int(str_3[str_3.index(':') + 1:]) + 10)
