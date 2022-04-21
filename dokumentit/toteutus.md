# Toteutusdokumentti

## Käyttötarkoitus

Sovelluksen ensisijainen käyttötarkoitus on kirjoituisvirheiden korjaus. Sovellus tunnistaa englanninkielisestä syötetystä tekstistä kirjoitusvirheet ja antaa niille korjausehdotukset. Toisena toimintona sovellus laskee kahden merkkijonon editointietäisyyden.

## Toteutus

Sovellus on toteuttu **Pythonilla** ja riippuvuuksien hallinta **Poetrylla**. Sovelluksen toiminta perustuu [trie-tietorakenteen](https://en.wikipedia.org/wiki/Trie) ja [Damerau–Levenshtein -etäisyyden](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance) hyödyntämiseen. 

Sovellus käyttää ensisijaisesti [Lexipedian](https://en.lexipedia.org/) Wikipedian artikkeleista koostamaa sanastoa. Lexipedian sanasto on järjestetty sen mukaan, kuinka usein sana on esiintynyt Wikipedian artikkeleissa. Useimmin esiintyvät sanat esiintyvät listassa ensimmäisenä. Otin sovelluksen käyttöön 200 000 yleisintä, enintään 25 merkin pituista sanaa. Typistin Pythonin avulla sanastosta pois Lexipedian tiedot sanan esiintyvyydestä ym. informaatiosta, ja karsin lisäksi sanoista muut kuin englannin kielisiä kirjaimia tai numeroita sisältävät sanat:  
<pre>
sana = rivi.replace("\n", "").split(" ")[0].lower()  
for kirjain in sana: 
    if kirjain not in list(string.ascii_lowercase) and kirjain not in list(string.digits) and kirjain not in  ["'", "-"]:
</pre>
Lopuksi loin sanastosta uuden tiedoston, jota sovellus käyttää. Trie-tietorakenteeseen lukiessa sovellus tallentaa solmuun tiedon sanan esiintyvyydestä, jota hyödynnetään parhaan korjausehdotuksen valinnassa.

Sovelluksen kirjoitusvirheen korjaustoiminto perustuu Damerau-Levenshtein -etäisyyden ja editointietäisyyden laskutoiminto Levenshtein -etäisyyden mittaamiseen. Kirjoitusvirheen korjaustoiminto toimii siten, että sovellus tarkistaa ensiksi, löytyykö tekstisyötteen sanat (tai sana) trie-puuhun tallennetusta sanastosta. Jos sanastosta ei löydy jotain sanaa, laskee sovellus rekursiivisesti trie-puuta ja Damerau-Levenshtein -etäisyyttä hyödyntäen sanalle korjausehdotuksia. Tietyn (tällä hetkellä alle kuuden) maksimieditointietäisyyden puitteissa sanat lisätään korjausehdotuksiksi listaan. Lopuksi sovellus valitsee korjausehdotuksista sen sanan, jolla on pienin editointietäisyys ja pienin sijoitus. 

Sovellus käsittelee tällä hetkellä sanoja pienillä kirjaimilla, sovellus ei siis huomioi eroa pienten ja isojen kirjainten välillä. Sovellus käsittelee myös välimerkit osana sanaa, ja tulkitsee siis esim. lauseen perässä olevan pisteen kirjoitusvirheeksi.

## Saavutetut aika- ja tilavaativuudet 
