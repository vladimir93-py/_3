#num_1 = int(input('Введите первое число'))Введите второе число
#num_2 = int(input('Введите второе число' ))
#num_3 = num_1 // num_2
#print(num_3)



def two_arg(a, b):
    return a//b
print(two_arg(35, 20))

def arg(a, b):
    try:
        a, b = int(a), int(b)
        two_arg = a / b
        return round(two_arg)
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
print(arg(input('Введите первое число - '), input('Введите второе число - ')))


