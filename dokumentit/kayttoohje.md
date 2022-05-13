# Käyttöohje

Ladattuasi sovelluksen, navigoi src-kansioon ja asenna riippuvuudet komennolla:
```
poetry install
```
Tämän jälkeen voit käynnistää sovelluksen komennolla:
```
poetry run python index.py
```
Tai ajaa yksikkötestit komennolla:
```
poetry run pytest
```
Trie-tietorakenteen suorituskykytestin voit ajaa projektin juurikansiosta komennolla:
```
poetry run python src/datastructures/trie_performance_testing.py
```
Koodin staattisen analyysin voit ajaa projektin juurikansiosta komennolla:
```
poetry run pylint src
```
Pylintin säännöt on määritelty [ohjelmistotekniikka-lähteen](https://github.com/ohjelmistotekniikka-hy/ohjelmistotekniikka-hy.github.io/blob/master/materiaali/python/.pylintrc) mukaisesti lukuunottamatta metodille sallittujen parametrien maksimimäärää (7 -> 9, [etsi_rekursiivisesti](/src/services/damerau_levenshtein.py)).

