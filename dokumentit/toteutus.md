# Toteutusdokumentti

## Käyttötarkoitus

Sovelluksen ensisijainen käyttötarkoitus on kirjoitusvirheiden korjaus. Sovellus tunnistaa englanninkielisestä syötetystä tekstistä kirjoitusvirheet ja antaa niille korjausehdotukset. Toisena toimintona sovellus laskee kahden merkkijonon editointietäisyyden.

## Toteutus

Sovellus on toteuttu **Pythonilla** ja riippuvuuksien hallinta **Poetrylla**. Sovelluksen toiminta perustuu [trie-tietorakenteen](https://en.wikipedia.org/wiki/Trie) ja [Damerau–Levenshtein -etäisyyden](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance) hyödyntämiseen. Kts myös [muut lähteet](https://github.com/tietotuomas/Kirjoitusvirheiden-korjaaja/edit/main/dokumentit/toteutus.md#lis%C3%A4%C3%A4-dameraulevenshtein--et%C3%A4isyydest%C3%A4-ja-sen-hy%C3%B6dynt%C3%A4misest%C3%A4-kirjoitusvirhedeiden-korjaamisessa).

Sovelluksen käyttöliittymä, sovelluslogiikka ja tallennuslogiikka on eriytetty kerrosarkkitehtuurin hengessä omiksi kokonaisuuksikseen. Sovelluksen hakemistorakenne on seuraavanlainen:

![Hakemistorakenne](/dokumentit/rakenne.png)


[Ui.py](/src/ui/ui.py) sisältää sovelluksen tekstipohjaisen käyttöliittymän.   
[Vocabulary_service.py](/src/services/vocabulary_service.py):n Sanastopalvelu-luokka yhdistää käyttöliittymän tietorakenteisiin/algoritmeihin ja sisältää logiikkaa merkkijonojen korjaamiseen ja oikeellisuuden tarkastamiseen.  
[Damerau_levenshtein.py](/src/services/damerau_levenshtein.py) sisältää Damerau-Levenshteinin etäisyyteen mittaamisen pohjautuvat algoritmit.  
[Trie.py:n](/src/datastructures/trie.py) TrieSolmu-luokka mallintaa Trie-tietorakenteen (puun) solmua. Ensimmäinen solmu toimii puun juurena.  
[Index.py](/src/index.py)-tiedosto käynnistää sovelluksen ja sisältää riippuvuuksien injektoinnit.  

Vocabulary-kansiosta löytyy sovelluksen ensisijaisesti käyttämä [sanasto](/src/vocabulary/modified_wiktionary.txt), testien käyttämiä sanastoja sekä muita sanastoja, joita on hyödynnetty ensisijaisen sanaston rakentamisessa.

[Trie_performance_testing.py](/src/datastructures/trie_performance_testing.py) sisältää erikseen käynnistettävän suorituskykytestin trie-tietorakenteelle. Yksikkötestien hakemistorakenne mukailee sovelluksen rakennetta, käyttöliittymää ei testata.

### Sanaston luominen

Sovellus käyttää ensisijaisesti [Lexipedian](https://en.lexipedia.org/) Wikipedian artikkeleista koostamaa sanastoa. Lexipedian sanasto on järjestetty sen mukaan, kuinka usein sana on esiintynyt Wikipedian artikkeleissa. Useimmin esiintyvät sanat esiintyvät listassa ensimmäisenä. Latasin sovelluksen käyttöön 200 000 yleisintä, enintään 25 merkin pituista sanaa. Typistin Pythonin avulla sanastosta pois Lexipedian numeeriset tiedot sanan esiintyvyydestä ym. informaatiosta, ja karsin lisäksi sanoista muut kuin englanninkielisiä kirjaimia tai numeroita sisältävät sanat:  
<pre>
sana = rivi.replace("\n", "").split(" ")[0].lower()  
for kirjain in sana: 
    if kirjain not in list(string.ascii_lowercase) and kirjain not in list(string.digits) and kirjain not in  ["'", "-"]:
</pre>

Koska sanasto sisälsi edelleen huomattavan määrän hyvin harvinaisia sanoja tai lyhenteitä, jatkoin edelleen sanojen karsimista ohjelmallisesti. Vertasin Lexipedian sanastoa toiseen samankokoiseen 194 000 sanaa sisältävään [sanastoon](http://www.gwicks.net/dictionaries.htm). Loin uuden listan, johon talletin sanat vain jos ne löytyivät kummastakin sanastosta. Tässä hyödynsin rakentamaani Trie-tietorakennetta, jolloin operaatio onnistui nopeasti.
<pre>
if self.trie.onko_sana_olemassa(sana):
    uusi_sanasto.append(sana)
</pre>

Karsin samalla mm. kolmatta sanastoa hyödyntäen lyhyitä sanoja, jotka ovat erityisesti aiheuttaneet ei-toivottuja tuloksia sanojen korjauksessa.
<pre>
if sijoitus > 15000 and sijoitus < 200000 and len(sana) <= 2:
    continue
</pre>

Hyödynsin vielä 10000:en yleisimmän sanan [sanastoa](https://englishgrammarhere.com/vocabulary/10000-most-common-words-in-english/) sijoitusten määrittelyssä. Lopuksi kirjoitin sanastosta uuden [tiedoston](/src/vocabulary/modified_wiktionary.txt), jota sovellus käyttää. Kun sovellus lukee tiedoston sanat Trie-tietorakenteeseen, tallennetaan solmuun myös tieto sanan esiintyvyydestä ([self.sijoitus](/src/datastructures/trie.py)), jota hyödynnetään parhaan korjausehdotuksen valinnassa ([def korjaa_sana](/src/services/vocabulary_service.py)).

### Korjaustoiminto

Sovelluksen kirjoitusvirheen korjaustoiminto toimii seuraavalla seuraavalla tavalla:  

Aluksi Sanastopalvelun [tarkista_teksti](/src/services/vocabulary_service.py) tarkistaa käyttäjän syötteen sana kerrallaan. Metodi tarkistaa, löytyykö sana Trie-tietorakenteesta kutsumalla TrieSolmun [onko_sana_olemassa](/src/datastructures/trie.py) -metodia. Jos sanastosta ei löydy jotain sanaa, kutsuu [tarkista_teksti](/src/services/vocabulary_service.py) saman luokan [korjaa_sana](/src/services/vocabulary_service.py) -metodia, joka kutsuu puolestaan DamerauLevenshtein-luokan [etsi_korjaukset](/src/services/damerau_levenshtein.py) -algoritmia. 

[Etsi_korjaukset](/src/services/damerau_levenshtein.py) etsii [etsi_rekursiivisesti](/src/services/damerau_levenshtein.py)-metodia kutsuen (Trie-tietorakennetta ja Damerau-Levenshtein -etäisyyttä hyödyntäen) sanalle korjausehdotuksia, jotka lisätään [korjaa_sana](/src/services/vocabulary_service.py)-metodille palautettavaan listaan. Damerau-Levenshtein -etäisyyksiä lasketaan kaksiuloitteisein taulukon avulla. Trie-puun ansiosta jokaista sanaa ei tarvitse vertailla kirjain kirjaimelta, koska etuliitteenä olevaa merkkijonoa ja sille laskettuja tuloksia voidaan hyödyntää. Esimerkiksi tilanteessa (haarassa) car -> **car**t -> **cart**oon -> **cartoon**s, cart-sanalle pitää laskea vain yksi uusi rivi, vaikka sanan pituus on 4. Cartoons-sanallekin pitää laskea vain yksi uusi rivi, vaikka sanan pituus on 8. 

Korjausehdotuksia karsitaan pitämällä kirjaa korjausehdotus-listan pienimmästä edintointietäisyydestä. Lopuksi [korjaa_sana](/src/services/vocabulary_service.py) valitsee korjausehdotuksista sen sanan, jolla on pienin editointietäisyys. Jos kahdella tai usemmalla sanalla on sama editointietäisyys &ndash; kuten usein on &ndash;  valitaan korjaushedotuksista se sana, jolla on pienin sijoitus. 

## Saavutetut aika- ja tilavaativuudet 
[Trie-tietorakenteen](/src/datastructures/trie.py) aika- ja tilavaativuus on yhtä merkkijonoa käsitellessä luokkaa **O(n)**, jossa n on merkkijonon pituus. Koko sanaston lisääminen Trie-tietorakenteeseen on kuitenkin luokkaa **O(mn)**, jossa m on sanastojen sanojen lukumäärä ja n sanojen keskimääräinen pituus.  

Damerau-Levenshteinin etäisyyttä hyödyntävän [etsi_korjaukset O(m)](/src/services/damerau_levenshtein.py) * [etsi_rekursiivisesti O(n)](/src/services/damerau_levenshtein.py) -algoritmin aika- ja tilavaativuus on luokkaa **O(mn)**, jossa n on korjattavan sanan pituus ja m solmujen määrä Trie-tietorakenteessa. Tästä johtuen sovellus hidastelee erityisesti pitkien korjattavien sanojen kohdalla, ja toisaalta sovellusta on "helppo" nopeuttaa sanastoa (eli solmujen määrää) karsimalla. Sovelluksen nykyisessä versiossa Trie-tietorakenteeseen luodaan noin **237 000** solmua, jotka sisältävät noin **96 000** sanaa.   

Korjaustoimintoon liittyvä korjausehdotusten vertailu suoritetaan [Sanastopalvelun](/src/services/vocabulary_service.py) puolella ajassa **O(n)**, eli myös koko [korjaustoiminnon](https://github.com/tietotuomas/Kirjoitusvirheiden-korjaaja/edit/main/dokumentit/toteutus.md#korjaustoiminto) aikavaativuus- ja tilavaativuus on **O(mn)**. 

## Parannuskohteet

Sovellus käsittelee sanoja pienillä kirjaimilla, sovellus ei siis huomioi eroa pienten ja isojen kirjainten välillä. Lisäksi sovellus käsittelee pilkun ja pisteen osana sanaa, ja tulkitsee siis esim. lauseen perässä olevan kirjoitusvirheeksi.

Sanan valintaa korjausehdotuslistasta voisi hienosäätää. Esimerkiksi joidenkin useasti esiintyvien (eli pienen sijoituksen) sanojen valinta olisi parempi/todennäköisempi vaihtoehto, vaikka tällaisen sanan editointietäisyys olisikin yksikön verran suurempi kuin jonkin toisen, harvinaisemman sanan editointietäisyys. Korjaustoimintoa voisi edelleen kehittää niin, että (esim. korjausehdotus-listasta sanaa valittaessa) sovellus tarkastelisi tyypillisimpiä kirjoitusvirheitä tai sitä, mitkä sanat esiintyvät useiten englanninkielisessä tekstissä yhdessä. Sanastoakin voisi edelleen parannella tarkoituksenmukaisemmaksi.

Kooditasolla parantamisen varaa voisi olla ainakin metodien yksi vastuu -periaatteen noudattamisessa. Jotkin metodit voisi jakaa moneen eri osaan. Toisaalta esimerkiksi melko pitkän [etsi_rekursiivisesti](/src/services/damerau_levenshtein.py)-metodin jakaminen osiin tuntuisi epäintuitiiviselta, vaikka mm. sanan lisäyksen tuloslistaan voisi hyvin eriyttää omaksi metodikseen.

Sovellusta voisi myös nopeuttaa: Erityisesti karsimalla harvinaisempia sanoja pois sanastosta, ja ehkä myös hitusen niin, että korjausehdotuksia ei kerättäisi erilliseen tulostaulukoon vertailtavaksi.

### Lisää Damerau–Levenshtein -etäisyydestä ja sen hyödyntämisestä kirjoitusvirheiden korjaamisessa
https://www.baeldung.com/cs/levenshtein-distance-computation  
http://fuzzy-string.com/Compare/  
https://youtu.be/AY2DZ4a9gyk  
https://blog.paperspace.com/implementing-levenshtein-distance-word-autocomplete-autocorrect/
