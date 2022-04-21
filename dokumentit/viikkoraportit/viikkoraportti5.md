## Viikko 5  
Käytetyt tunnit: 14 (ml. vertaisarviointiin käytetyt tunnit)

Osoittautui, että kirjoitusvirheiden korjaamiseksi toteuttamani, Levenshteinin etäisyyttä ja trie-puuta hyödyntävä algoritmini ei ehkä toiminut kaikissa tilanteissa halutulla tavalla. Minulla oli aikasemmin ohjelman kanssa suorituskykyongelmia ja yritin rajoittaa trie-puun haarojen läpi käymistä maksimi-editointietäisyyttä hyödyntäen. Tällainen menettely saattaa antaa epätoivottuja tuloksia rekursiivisessä etsinnässä ja parhaat tulokset jäävätkin saamatta. Muutin algoritmin toimintalogiikkaa nyt niin, että virheellistä sanaa verrataan valitun sanaston kaikkiin sanoihin, tai siis trie-puu käydään läpi jokaista solmua myöten. 

Otin lisäksi käyttöön uuden sanaston, joka on järjestetty sanojen esiintyvyyden mukaan. Lisäsin tiedon esiintyvyydestä Trie-puun solmuun. Tästä lisää [toteutusdokumentissa](https://github.com/tietotuomas/Kirjoitusvirheiden-korjaaja/blob/main/dokumentit/toteutus.md).


