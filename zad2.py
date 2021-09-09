"""
Ćwiczenie:
Napisać program, który:
 1. Wczyta z konsoli kwotę brutto i stawkę VAT
 2. Wypisze kwotę netto i kwotę VAT wg podanej stawki
"""
a = int(input('podaj kwote:'))
z = int
r1 = int
r2 = int
x = int
y = int

if a >= 5:
    z = a // 5
    r1 = a % 5
    if r1 >= 0:
        x = r1 // 2
        r2 = r1 % 2
    else:
        print(int(z), 'x 5PLN', 0, 'x 2PLN', 0, 'x 1PLN')

    if r2 > 0:
        y = r2 / 1
        print(int(z), 'x 5PLN', int(x), 'x 2PLN', int(y), 'x 1PLN')
    else:
        print(int(z), 'x 5PLN', int(x), 'x 2PLN', 0, 'x 1PLN')
else:
    if a <= 4:
        x = a // 2
        r2 = a % 2
    else:
        print(0, 'x 5PLN', x, 'x 2PLN', y, 'x 1PLN')

    if r2 > 0:
        y = r2 / 1
        print(0, 'x 5PLN', x, 'x 2PLN', int(y), 'x 1PLN')
    else:
        print(0, 'x 5PLN', x, 'x 2PLN', 0, 'x 1PLN')
if a == 0:
    print('nie może być zero!!')
