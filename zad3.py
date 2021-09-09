"""
Ćwiczenie:

Napisać program, który:

1. Na podstawie:
 - roku urodenia,
 - miesiąca urodzenia
 - dnia urodzenia
 - nr kolejnego
 - określenia płci True == mężczyzna

wygeneruje pesel w następującego schematu:
 - 2 ostatnie cyfry roku
 - 2 cyfrowy miesiąc uzupełniony od lewej zerem (jeżeli rok >= 2000 to do miesiąca dodajemy 20)
 - 2 cyfrowy dzień uzupełniony od lewej zerem
 - 3 cyfrowy nr kolejny
 - cyfra płci - 1 mężczyzna, 0 kobieta
 - suma kontrolna będąca ostatnią cyfrą sumy powyższych cyfr

Np dla kobiety urodzonej 3.12.2005r jako 13ta osoba powinno wyjść:
05320301307

Podpowiedzi:
rok = 2002
miesiac = 11
dzien = 3
nr = 34
plec_facet = True
"""


rok = 1999
miesiac = 3
dzien = 3
nr = 34
plec_m = True

rok_2 = str(rok)[-2:]

if rok >=2000:
    miesiac+=20
elif rok < 2000 and miesiac<10:
    miesiac=str(miesiac).zfill(2)
if dzien <10:
    dzien=str(dzien).zfill(2)
if len(str(nr))!=3:
    nr=str(nr).zfill(3)

to_checksum = f'{rok_2}{miesiac}{dzien}{nr}{int(plec_m)}'

suma=0
for cyfra in to_checksum:
    suma = suma + int(cyfra)

print(to_checksum+str(suma)[-1])
