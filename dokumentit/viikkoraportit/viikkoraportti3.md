Viikko 3
Käytetyt tunnit: 10

Muokkasin sovelluksen rakennetta ja riippuvuuksia. Loin luokat Sanastopalvelu ja Trie. Sanastopalvelu lukee sanaston ja tallentaa sen Trie-puuhun. Tarkastelin eri vaihtoehtoja Trie-tietorakenteen luomiseen ja päädyin ainakin alustavasti käsittelemään "solmuja" sanakirjan avulla. En siis toteuttanut erikseen solmu-oliota. 

Muokkasin hieman myös sovelluksen tekstikäyttöliittymää, sovellus tarkastaa nyt syötteen aina samalla tavalla. Erillisiä vaihtoehtoja sanan ja lauseen tarkastamiselle ei enää ole. Tällä hetkellä sovellus tarkistaa tekstin ja merkkaa virheelliset sanat (sanat, joita ei löydy sanastosta) *-merkillä. Korjaustoimintoa ei ole vielä toteutettu. 

Syvensin tällä viikolla tietämystäni Trie-tietorakenteesta, vaikka viime viikolta olikin jo pohjia. Opin lisää myös Pylintistä, Poetrysta ja Pythonin unit testeistä. Uutena asiana lisäsin projektiin coverage-työkalun. Tästä lisää testausdokumentissa. 

Kohtasin joitakin ongelmia projektinhallinnassa. Windows-koneeni ei jostain syystä enää tunnistanut Poetrya, mutta uudelleen asentaminen auttoi. Toinen vielä ratkaisematon (mutta ei niin kriittinen) ongelma koskee sanasto-tiedostoa, jota käytän. Sanasto sisältää nyt paljon epätyypillisiä sanoja ja lyhenteitä. Saatan vaihtaa sanaston projektin aikana. Lisäksi korjaustoiminnon toteuttamisessa mietityttää tällä hetkellä mm. välimerkkien käsittely.

Ensi viikolla olisi tarkoitus lähteä toteuttamaan varsinaista kirjoitusvirheen korjaustoimintoa Damerau–Levenshtein -etäisyyteen perustuen.
