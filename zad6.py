"""
Ćwiczenie:

Z pliku tekstowego w formacie:
Jan 888999777
Ola 333444555
Paweł 111222333
Ula 333444000
wczytac słownik w postaci:
{'Jan': '888999777',}

Następnie napisać pętlę w której użytkownik będzie podawał imiona
a program będzie podawał numery telefonów, lub komunikat, że nie ma takiego numeru
w książce telefonicznej. Warunkiem wyjścia z pętli będzie podanie 'koniec' zamiast imienia.
"""
if __name__ == '__main__':
    with open('telefony.txt', 'rt', encoding='utf8') as f:
        ksiazka = {}
        for linia in f:
            imie, telefon = linia.split()
            ksiazka[imie] = telefon

    while True:
        imie = input('podaj imię (koniec aby skończyć): ')
        if imie == 'koniec':
            break
        if imie in ksiazka:
            print(f'{imie} ma numer telefonu {ksiazka[imie]}')
        else:
            decyzja = input(f'Brak numeru do {imie} w książce telfonicznej. Czy chcesz dodać (tak/nie)? ').lower()
            if decyzja == 'tak':
                nr = input('W takim razie podaj numer: ')
                ksiazka[imie] = nr
                print('Dodano.')
