## Testaus  

### Yksikkötestaus

Projektin testaus on toteutettu Pythonin unittest-sovelluskehyksen avulla. Testit on toteutettu tällä hetkellä tiedostoille vocabulary_service.py ja trie.py, välillisesti myös tiedostolle levenshtein_distance.py. 

Tiedostot index.py ja performance_testing.py sekä käyttöliittymä on rajattu testien ulkopuolelle. 

![Testikattavuus](/dokumentit/coverage.png)

Raportti testikattavuudesta on rakennettu coverage-työkalun avulla.

### Suorituskyky

Suorituskyvyn testausta varten services-kansioon on luotu performance_testing.py. Tällä hetkellä ko. tiedoston ajamalla voi testata suorituskykyeroja (nopeutta) pythonin sisäänrakennetun listan ja luomani trie-tietorakenteen välillä. Odotetusti sanaston lukeminen/tallentaminen listaan on nopeampaa listaan kuin trie-puuhun, mutta sanojen etsiminen puusta on nopeampaa kuin listasta etsiminen.

```
Sanaston lukeminen listaan: 0:00:00.120748
Sanaston lukeminen trie-puuhun: 0:00:03.923156
Tuhannen yleisimmän sanan etsintä listan avulla: 0:00:02.525362
Tuhannen yleisimmän sanan etsintä trie-puun avulla: 0:00:00.006210
Tuhannen yleisimmän sanan ja tuhannen tietorakenteesta löytymättömän sanan etsintä listan avulla: 0:00:04.920071
Tuhannen yleisimmän sanan ja tuhannen tietorakenteesta löytymättömän sanan etsintä trie-puun avulla: 0:00:00.008948
```
