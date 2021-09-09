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

if __name__ == '__main__':
    rok = 2002
    miesiac = 11
    dzien = 3
    nr = 34
    plec_facet = True
    
    rok_s = str(rok)[2:]
    miesiac_s = str(miesiac + 20 if rok >= 2000 else miesiac).zfill(2)
    dzien_s = str(dzien).zfill(2)
    nr_s = str(nr).zfill(3)
    plec_s = str(int(plec_facet))
    pesel = f'{rok_s}{miesiac_s}{dzien_s}{nr_s}{plec_s}'

    suma = 0
    for cyfra in pesel:
        i = int(cyfra)
        suma = suma + i

    pesel = f'{pesel}{suma % 10}'
    print(pesel)
