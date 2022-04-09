# Toteutusdokumentti

## Käyttötarkoitus

Sovelluksen ensisijainen käyttötarkoitus on kirjoituisvirheiden korjaus. Sovellus tunnistaa englanninkielisestä syötetystä tekstistä kirjoitusvirheet ja antaa niille korjausehdotukset. Toisena toimintona sovellus laskee kahden merkkijonon editointietäisyyden.

## Toteutus

Sovellus on toteuttu **Pythonilla** ja riippuvuuksien hallinta **Poetrylla**. Sovelluksen toiminta perustuu [trie-tietorakenteen](https://en.wikipedia.org/wiki/Trie) ja [Damerau–Levenshtein -etäisyyden](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance) hyödyntämiseen. 

Sovelluksen tämänhetkinen kirjoitusvirheen korjaustoiminto ja editointietäisyyden laskeminen perustuvat Levenshtein -etäisyyden mittaamiseen. Algoritm(e)istä puuttuu siis vielä Damerau-osa, eli transpoosin hyödyntäminen. Kirjoitusvirheen korjaustoiminto toimii siten, että sovellus tarkistaa ensiksi, löytyykö tekstisyötteen sanat (tai sana) trie-puuhun tallennetusta sanastosta. Jos sanastosta ei löydy jotain sanaa, laskee sovellus rekursiivisesti trie-puuta ja Levenshtein -etäisyyttä hyödyntäen sanalle korjausehdotuksia tietyn maksimieditointietäisyyden (tällä hetkellä maksimietäisyys 3) puitteissa. Lopuksi sovellus valitsee korjausehdotuksista sen sanan, jolla on pienin editointietäisyys. 

Tarkoitukseni on kehittää tähän korjausehdotuksen valintaan muitakin kriteereitä, jotta kirjoitusvirheiden korjaus toimisi paremmin. Sovellus voisi sanaa korjausehdotus-listasta valitessa tarkastella esimerkiksi tyypillisimpiä kirjoitusvirheitä tai sitä, mitkä sanat esiintyvät useimmin englannin kielisessä tekstissä (ehkä myös sitä, mitkä sanat esiintyvät useimmin yhdessä).

Sovellus käsittelee tällä hetkellä sanoja pienillä kirjaimilla, sovellus ei siis huomioi eroa pienten ja isojen kirjainten välillä. Sovellus käsittelee myös välimerkit osana sanaa, ja tulkitsee siis esim. lauseen perässä olevan pisteen kirjoitusvirheeksi.

## Saavutetut aika- ja tilavaativuudet 
