def sum_sum():
    result = 0
    while True:
        print(f'Текущая сумма = {result}')
        num_1 = input('Введите какое-то количество чисел через пробел для подсчета суммы (# - команда для выхода): ').split()
        for value in num_1:
            if value == '#':
                print(f'Сумма равна = {result}')
                break
            try:
                result += float(value)
            except ValueError:
                print(f'Значение {value} было введено не корректно')
        else:
            continue
        break
    return f'Сумма равна = {result}'
sum_sum()