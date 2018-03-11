while True:
    print('Выберите логическое выражение:\n', 'xor - ^\nand - &\nor - |\nnot - ~\n', 'Для завершения программы - end')
    z = input()
    if z == '^':
        print('Введите две бинарные последовательности')
        a = '0b' + ''.join([i for i in input('1) ') if i in '01'])
        b = '0b' + ''.join([i for i in input('2) ') if i in '01'])
        print('1) ', a, '\n2) ', b, '\nResult: ', bin(int(a, 2) ^ int(b, 2)))
    elif z == '&':
        print('Введите две бинарные последовательности')
        a = '0b' + ''.join([i for i in input('1) ') if i in '01'])
        b = '0b' + ''.join([i for i in input('2) ') if i in '01'])
        print('1) ', a, '\n2) ', b, '\nResult: ', bin(int(a, 2) & int(b, 2)))
    elif z == '|':
        print('Введите две бинарные последовательности')
        a = '0b' + ''.join([i for i in input('1) ') if i in '01'])
        b = '0b' + ''.join([i for i in input('2) ') if i in '01'])
        print('1) ', a, '\n2) ', b, '\nResult: ', bin(int(a, 2) | int(b, 2)))
    elif z == '~':
        print('Введите бинарную последовательность')
        a = '0b' + ''.join([i for i in input('1) ') if i in '01'])
        print('1) ', a, '\nResult: ', bin(~int(a, 2)))
    elif z == 'end':
        break
    else:
        print('Некорректная команда.')
print('Завершение программы')
