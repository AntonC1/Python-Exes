"""
Ćwiczenie:
 1. Wczytać z konsoli długości 3 boków trójkąta
 2. Policzyć pole takiego trójkąta ze wzoru Herona
 3. Wypisać wynik na ekran
"""
import math

if __name__ == '__main__':

    a = float(input('Podaj długość boku: '))
    b = float(input('Podaj długość boku: '))
    c = float(input('Podaj długość boku: '))

    p = 0.5 * (a + b + c)
    x = p * (p - a) * (p - b) * (p - c)

    if x < 0:
        print('Takiego trójkąta nie da się stworzyć.')
    else:
        s = (x) ** 0.5
        print(s)
