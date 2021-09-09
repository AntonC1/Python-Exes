"""
Ćwiczenie:
Napisać program który:
1. Wczyta artykuł z wikipedii:
import wikipedia
wikipedia.set_lang('pl')
p = wikipedia.page('Średniowiecze')
print(p.content)
2. Wyczyści artykuł ze zbędnych znaków przestankowych i zamieni na małe litery
     Możliwe podejścia:
       - przepisujemy artykuł znak po znaku do nowego analizując czy znak jest literą: np 'a'.isalpha()
       - seria zamian - np .replace(', ', ' ')
       - użycie regex:
        import re
        wr = r'[\W\d]'
        artykul = re.sub(wr, ' ', artykul)
3. Podzieli artykuł na słowa - do listy słów
4. Sparsować słownik języka polskiego:
Pobrać i rozpakować do katalogu projektu plik:
http://zil.ipipan.waw.pl/PoliMorf?action=AttachFile&do=get&target=PoliMorf-0.6.7.tab.gz
Nasz program ma sparsować powyższy plik do formatu słownika:
{'forma odmieniona': 'forma podstawowa',
 'abażurami': 'abażur'}
5. Zamieni wszystkie słowa artykułu na ich gramatyczne formy podstawowe
   np jechała -> jechać
Proponuję tworzyć kolejne listy na drzodze przepisywania elementów do nowej listy.
6. Odfiltruje słowa krótsze niż 4 znaki
7. Policzy ilość wystąpień słów w artykule
Tak jak w porzednim ćwiczeniu.
8. Wypisze 10 najczęściej występujących
"""

import wikipedia
import re

wikipedia.set_lang('pl')
p = wikipedia.page('Średniowiecze')
wr = r'[\W\d]'
artykul = re.sub(wr, ' ', p.content)
slowa_w_artykule = artykul.split()
nowy_artykul = []
arytkul_bez_krotkich_wyrazuw = []
slownik = {}
powturzen_slow = {}

# dzielenie na pojedyncze słowa
with open('PoliMorf-0.6.7.tab', 'rt', encoding='utf_8') as file:
    for linia in file:
        slowa = linia.split()
        zmienione = slowa[0]
        niezmienione = slowa[1]
        slownik[zmienione] = niezmienione

# dodawanie wszystkich słów
for wyraz in slowa_w_artykule:
    if wyraz in slownik:
        wyraz = slownik[wyraz]
        nowy_artykul.append(wyraz)

# oddzielanie krótkich
for nowe_wyrazy in nowy_artykul:
    if len(nowe_wyrazy) >= 4:
        arytkul_bez_krotkich_wyrazuw.append(nowe_wyrazy)

# zliczanie słów w
for slowo_w in arytkul_bez_krotkich_wyrazuw:
    if slowo_w not in powturzen_slow:
        powturzen_slow[slowo_w] = 1
    else:
        powturzen_slow[slowo_w] += 1
print(powturzen_slow)
