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
Koodin staattisen analyysin voit ajaa projektin juurikansiosta komennolla:
```
poetry run pylint src
```
Trie-tietorakenteen suorituskykytestin voit ajaa projektin juurikansiosta komennolla:
```
poetry run python /src/datastructures/trie_performance_testing.py
```
