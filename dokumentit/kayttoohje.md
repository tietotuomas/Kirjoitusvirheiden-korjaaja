# Käyttöohje

## Asennus & käynnistys

Sovelluksen voi ladata komennolla:
```
git clone https://github.com/tietotuomas/Kirjoitusvirheiden-korjaaja/
```
Ladattuasi sovelluksen, navigoi src-kansioon ja asenna riippuvuudet komennolla:
```
poetry install
```
Tämän jälkeen sovelluksen voi käynnistää komennolla:
```
poetry run python index.py
```
## Sovelluksen toiminnot

![Päävalikko](/dokumentit/paavalikko.png)

Sovelluksen käynnistettyä aukeaa päävalikko.  
Sovelluksen päätoiminnallisuus eli englanninkielisen tekstin kirjoitusvirheiden korjaus valitaan komennolla ```1```.  

![Komento1](/dokumentit/komento1.png)

Ensimmäisellä kerralla sovellus ohjeistaa käyttäjää välttämään pisteitä ja pilkkuja.  
Sovellus pyytää käyttäjää syöttämään englanninkielisen tekstin.  

![Korjaus](/dokumentit/korjaus.png)

Syötteen luvun jälkeen sovellus merkkaa virheelliseksi tunnistamansa sanat tähdellä ja esittää korjausehdotuksen, minkä jälkeen käyttäjä ohjataan takaisin päävalikkoon.  

Kahden merkkijonon välisen editointietäisyyden laskeminen valitaan komennolla ```2```.  

![Komento2](/dokumentit/komento2.png)

Sovellus pyytää käyttäjältä kaksi merkkijonoa. Kun käyttäjä on syöttänyt merkkijonot, laskee sovellus merkkijonojen välisen Levenshtein-etäisyyden ja Damerau-Levenshtein-etäisyyden. Sovellus tulostaa samassa yhteydessä lisäksi tulosmatriisit. Tulostuksien jälkeen käyttäjä ohjataan takaisin päävalikkoon.

Sovellus suljetaan komennolla ```3```.  

## Muuta

Yksikkötestit (kts. [testausdokumentti](https://github.com/tietotuomas/Kirjoitusvirheiden-korjaaja/blob/main/dokumentit/toteutus.md)) voi ajaa projektin juurikansiosta komennolla:
```
poetry run pytest src
```
Trie-tietorakenteen suorituskykytestin (kts. [testausdokumentti](https://github.com/tietotuomas/Kirjoitusvirheiden-korjaaja/blob/main/dokumentit/toteutus.md)) voi ajaa projektin juurikansiosta komennolla:
```
poetry run python src/datastructures/trie_performance_testing.py
```
Koodin staattisen analyysin voi ajaa projektin juurikansiosta komennolla:
```
poetry run pylint src
```
Pylintin säännöt on määritelty [ohjelmistotekniikka-lähteen](https://github.com/ohjelmistotekniikka-hy/ohjelmistotekniikka-hy.github.io/blob/master/materiaali/python/.pylintrc) mukaisesti lukuun ottamatta metodille sallittujen parametrien maksimimäärää (7 -> 9, kts. [etsi_rekursiivisesti](/src/services/damerau_levenshtein.py)).

