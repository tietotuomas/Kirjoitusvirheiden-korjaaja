## Viikko 5  
Käytetyt tunnit: 24 (ml. vertaisarviointiin käytetyt noin 4 tuntia)

Osoittautui, että kirjoitusvirheiden korjaamiseksi toteuttamani, Levenshteinin etäisyyttä ja trie-puuta hyödyntävä algoritmini ei ehkä toiminut kaikissa tilanteissa halutulla tavalla. Minulla oli aikasemmin ohjelman kanssa suorituskykyongelmia ja yritin rajoittaa trie-puun haarojen läpi käymistä maksimi-editointietäisyyttä hyödyntäen. Tällainen menettely saattaa antaa epätoivottuja tuloksia rekursiivisessä etsinnässä ja parhaat tulokset jäävätkin saamatta. Muutin algoritmin toimintalogiikkaa nyt niin, että virheellistä sanaa verrataan valitun sanaston kaikkiin sanoihin, tai siis trie-puu käydään läpi jokaista solmua myöten. 

Otin lisäksi käyttöön uuden sanaston, joka on järjestetty sanojen esiintyvyyden mukaan. Lisäsin tiedon esiintyvyydestä Trie-puun solmuun. Tästä lisää [toteutusdokumentissa](https://github.com/tietotuomas/Kirjoitusvirheiden-korjaaja/blob/main/dokumentit/toteutus.md).

Näiden lisäksi parantelin hieman käyttöliittymää ja uudistin isolla kädellä projektin testausta. Korjailin tai poistin vanhoja testejä, ja kirjoitin uusia riippuvuuksia eliminoivia testejä Mock-kirjaston avulla. Tulin testejä kirjoittaessa havainnollistaakseni itselleni testien hyödyllisyyden - löysin vihdoinkin bugin, joka on tuottanut sanoille toisinaan virheellisiä editointietäisyyksiä. Käytin tuntikausia DamerauLevenshtein-luokan debuggaamiseen, mutta testejä kirjoittaessa osoittautui, että virhe olikin Sanastopalvelu-luokan puolella: virheelliseksi merkatut sanat lähtivät DamerauLevenshtein-luokan käsiteltäväksi \*-merkki perässään. Tarkoitukseni oli siis alunperin merkata virheelliset sanat tähdellä vain tulostuksiin, jotka näkyvät käyttäjälle...

Tällä viikolla syvensin edelleen ymmärrystäni Damerau-Levenshteinin-etäisyyden implementoinnista, erityisesti Damerau-osuudesta. Testejä kirjoittaessa opin täysin uuuttakin asiaa. Pythonin Mock-kirjasto oli minulle uusi tuttavuus, vaikka tekniikka sinänsä jokseenkin tuttu (Javan puolelta). Joihinkin uusiin assert-metodeihin tuli myös tutustuttua.

Ensi viikolla aion viimeistellä projektin vaatimusten mukaisesti "valmiiksi". Tehtävää on vielä ainakin projektin dokumentaatiossa ja koodin kommentoinnissa, joka on nyt varsin epäyhtenäistä. Testejäkin on ehkä vielä vähänlaisesti, _kattavan yksikkötestauksen_ voi toki tulkita monella tavalla. Erityisesti voisin parantaa Damerau-Levenshteinin-luokan testausta: lisää testejä, joissa ainakin osassa trie-riippuvuus Mock-kirjastolla eliminoituna. Lisäksi tarkoituksenani on rakentaa workflow + badget yksikkötestejä varten. Jos aikaa jää, niin parantelen sovelluksen toissijaista toimintoa eli kahden merkkijonon välistä Levenshteinin etäisyyden laskentaa (ilmoittamalla samassa yhteydessä myös Damerau-Levehnshteinin etäisyyden).

Viimeisillä viiko(i)lla olisi sitten mahdollisuus hienosäätää esimerkiksi sanan valintaa korjaustoiminnossa ja kenties karsia oudoimpia sanoja pois sanastosta.


