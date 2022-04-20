## Viikko 5  
Käytetyt tunnit: 9

Osoittautui, että kirjoitusvirheiden korjaamiseksi toteuttamani, Levenshteinin etäisyyttä ja trie-puuta hyödyntävä algoritmini ei ehkä toiminut kaikissa tilanteissa halutulla tavalla. Minulla oli aikasemmin ohjelman kanssa suorituskykyongelmia ja yritin rajoittaa trie-puun haarojen läpi käymistä maksimi-editointietäisyyttä hyödyntäen. Tällainen menettely saattaa antaa epätoivottuja tuloksia rekursiivisessä etsinnässä ja parhaat tulokset jäävätkin saamatta.

Muutin algoritmin toimintalogiikkaa nyt niin, että virheellistä sanaa verrataan valitun sanaston kaikkiin sanoihin, tai siis trie-puu käydään läpi jokaista solmua myöten. Korjaustoiminto on nyt hitaampi, mutta nykyisellä sanastolla ei kuitenkaan toivottoman hidas.
