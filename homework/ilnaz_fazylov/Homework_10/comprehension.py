PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

pairs = [element.split() for element in PRICE_LIST.split('\n')]
my_dict = {supply: int(price[:-1]) for supply, price in pairs}
print(my_dict)
