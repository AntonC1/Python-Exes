"""
Ćwiczenie:
 1. Wczytać z konsoli kwotę w zł jako liczbę całkowitą
 2. Policzyć w jaki sposób rozmienić daną kwotę używając jak najmniejszej ilości monet.
    Zakładamy że mamy do dyspozycji dowolną ilość monet 1, 2 i 5 zł.
 3. Wyniki wypisać na ekran.
 """
kwota = int(input('Podaj kwotę: '))
ilosc = kwota // 5

print(ilosc, 'x 5zł')
kwota = kwota % 5
ilosc = kwota // 2

print(ilosc, 'x 2zł')
kwota = kwota % 2

# wypisać komunikat
print(kwota, 'x 1zł')
