## Testaus  

### Yksikkötestaus

Projektin testaus on toteutettu Pythonin unittest-sovelluskehyksen avulla. Riippuvuuksia on tarvittaessa eliminoitu Mock-kirjastolla. Yksikkötestaus on pyritty toteuttamaan kattavasti mutta tarkoituksenmukaisesti, kuitenkin testaten myös ns. reunatapauksia ja vähemmän odotettuja syötteitä, kuten tyhjää merkkijonoa. Sanaehdotuksien oikeellisuutta on testattu käyttämällä taulukkomuodossa syötettyä, hyvin rajattua sanastoa. Editointietäisyyksiä on testattu erikseen mahdollisimman monipuolisilla syötteillä niin, että kaikkia sanapituuksia ja operaatioita (lisäys, poisto, vaihto, transpoosi) tulisi testattua tasaisesti. Olen tarkistanut useimpien testien editointietäisyyksien oikeellisuuden manuaalisesti, ja isommissa matriiseissa käyttänyt apuna [Damerau-Levenshtein-etäisyyden](http://fuzzy-string.com/) ja [Levenshtein-etäisyyden](https://planetcalc.com/1721/) laskemiseen tarkoitettuja web-sovelluksia.

Testien hakemistorakenne jäljittelee sovelluksen rakennetta. Testit on toteutettu tiedostoille vocabulary_service.py, trie.py sekä damerau_levenshtein.py. 

Tiedostot index.py ja trie_performance_testing.py sekä ui.py on rajattu testien ulkopuolelle. 

![Testikattavuus](/dokumentit/coverage.png)

Raportti testikattavuudesta on rakennettu coverage-työkalun avulla. Lisää statistiikkaa [codevocissa](https://app.codecov.io/gh/tietotuomas/Kirjoitusvirheiden-korjaaja).

### Suorituskyky

Suorituskyvyn testausta varten services-kansioon on luotu trie_performance_testing.py. Ko. tiedoston ajamalla voi testata suorituskykyeroja (nopeutta) pythonin sisäänrakennetun listan ja luomani trie-tietorakenteen välillä. Odotetusti sanaston lukeminen/tallentaminen listaan on nopeampaa listaan kuin trie-puuhun, mutta sanojen etsiminen puusta on nopeampaa kuin listasta etsiminen.

```
Sanaston lukeminen listaan: 0:00:00.120748
Sanaston lukeminen trie-puuhun: 0:00:03.923156
Tuhannen yleisimmän sanan etsintä listan avulla: 0:00:02.525362
Tuhannen yleisimmän sanan etsintä trie-puun avulla: 0:00:00.006210
Tuhannen yleisimmän sanan ja tuhannen tietorakenteesta löytymättömän sanan etsintä listan avulla: 0:00:04.920071
Tuhannen yleisimmän sanan ja tuhannen tietorakenteesta löytymättömän sanan etsintä trie-puun avulla: 0:00:00.008948
```
