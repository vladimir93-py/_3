def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'Не корректные данные:\nх должен быть больше 0\ny должен быть меньше 0'
        else:
            result = 1
            for _ in range(abs(y)):
                result *= 1 / x
            return f'х в степени у равен: {round(result, 6)}'
    except ValueError:
        return 'Вводите только числа.'

a = input('Введите положительное число, х =')
b = input('Введите отрицательное число, y =')

print(my_func(a, b))


def my_func2(x, y):
    try:
        result = x ** y
    except TypeError:
        return ""
    return result


print(my_func2(4.7, -3))

