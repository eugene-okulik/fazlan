my_dict = {'tuple': (3, '22', 0, 5.43, -2),
           'list': ['one', 4.31, 5, 0, -3],
           'dict': {'1': 'one', '2': 2, '3': 3.0, '4': -2, '5': [1, 'two']},
           'set': {-2, '21', 4.32, 0, 3}}

print(my_dict['tuple'][-1])

my_dict['list'].append(8)
my_dict['list'].remove(4.31)

my_dict['dict']['i am a tuple'] = 'new'
my_dict['dict'].pop('2')

my_dict['set'].add('new')
my_dict['set'].discard('21')

print(my_dict)
