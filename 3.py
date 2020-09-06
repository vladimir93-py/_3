def my_func(a, b, c):
    my_list = [a, b, c]
    try:
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return 'Введите число'
print(my_func(9, 99, 99))

my_func = lambda a, b, c: (a + b + c) - min(a, b, c)
print(my_func(9, 99, 99))