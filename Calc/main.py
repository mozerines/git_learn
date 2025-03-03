def operation(oper, a, b):
    if oper == '+' or oper == '1':
        return a + b
    if oper == '-' or oper == '2':
        return a - b
    if oper == '*' or oper == '3':
        return a * b
    if oper == ':' or oper == '4':
        return a / b
    if oper == '^' or oper == '**' or oper == '5':
        return a ** b
    if oper == '%' or oper == '6':
        return (a / 100) * b


while True:
    oper = input('1) +\n'
                 '2) -\n'
                 '3) *\n'
                 '4) :\n'
                 '5) ^ (или **)\n'
                 '6) %\n'
                 'Какую операцию вы хотите произвести (stop - остановка)? ')

    a = float(input('Число a: '))
    b = float(input('Число b: '))

    print(f'Результат: {operation(oper, a, b)}')
