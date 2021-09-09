"""
Napisać program, który:
1. Wczyta napis z konsoli:
2. Sprawdzi, czy czy:
    2.1 Chociaż jedna z liter napisu jest jedną z liter napisu 'abcdef'
Podpowiedzi:
 - pętla for dla napisów iteruje po literach
 - break
Rozszerzenia ćwiczenia:
 - sprawdzić czy wszystkie litery spełniają warunek
 """

nazwa_tagu = input('nazwa tagu: ')
nazwa_atrybutu = input('nazwa atrybut: ')
wartosc_tagu = input('wartosc tagu: ')
wartosc_atrybut = input('wartosc atrybutu: ')
print(f'<{nazwa_tagu} {nazwa_atrybutu}="{wartosc_atrybut}">{wartosc_tagu}</{nazwa_tagu}>')
