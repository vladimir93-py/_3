def int_func():
    a = 0
    for i in input('Введите слова на латинской раскладке через пробел :\n').split():
        for a, letter in enumerate(i):
            if ord(letter) == 32 or 97 <= ord(letter) <= 122:
                a += 1
            if a == len(i):
                print(i.title())
                a = 0
            else:
                print('')

int_func()