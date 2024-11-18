def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params()
print_params(5, 'Armagedon', False)
print_params(4, 'Null')
print_params(a = 'one', b = 'two', c = 'three')
print_params(a = '', b = True)
print_params(b=5)
print_params(c=8)

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [5.7, False, 'fruit']
values_dict = {'a': 'else', 'b': True, 'c': 9}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'String' ]
print_params(*values_list_2, 42)