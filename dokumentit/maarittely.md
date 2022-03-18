# Määrittelydokumentti

## Aihe ja toteutus

Aiheenani on kirjoitusvirheiden korjaus. Tarkoituksenani on siis laatia sovellus, joka tunnistaa englanninkielisestä syötetystä tekstistä kirjoitusvirheet ja antaa niille korjausehdotukset. Jos aika riittää, toteutan sovellukseen myös ominaisuuden suomenkielisten syötteiden korjaamiseen. Suomenkielisten sanojen korjaaminen on runsaasta taivutuksesta johtuen todennäköisesti haastavampaa, ja lähden siksi toteuttamaan ensisijaisesti englanninkielisten sanojen korjaajaa. Käyttöliittymän toteutan tekstipohjaisena. Syötteeksi annetaan sana tai lause. Syötteen antamisen jälkeen sovellus ehdottaa korjauksia mahdollisiin kirjoitusvirheisiin.

## Ohjelmointikielet

Toteutan projektini **Pythonilla**. Tarvittaessa voin vertaisarvioida myös **Javalla** koodattuja projekteja.

## Algoritmit ja tietorakenteet

Laadin sanaston hallintaa varten [trie-tietorakenteen](https://en.wikipedia.org/wiki/Trie). Kirjoitusvirheiden korjausta varten toteutan myös [Damerau–Levenshtein -etäisyyttä](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance) hyödyntyvän algoritmin.

## Aika- ja tilavaativuudet

Trie-tietorakenteen aika- ja tilavaativuus on O(n). Iteratiiviset, Damerau–Levenshtein -etäisyyttä hyödyntävät algoritmit näyttävät yleisesti (esim. [baeldung, kappale 5](https://www.baeldung.com/cs/levenshtein-distance-computation)) pääsevän aika- ja tilavaativuuteen O(nm), jossa n ja m ovat vertailtavien merkkijonojen pituuksia. Lähden tältä pohjalta tavoittelemaan algoritmilleni aika- ja tilavaativuutta O(nm).

## Kieli

Toteutan sovelluksen käyttöliittymän, koodin, kommentoinnin ja dokumentaation suomeksi.

## Opinto-ohjelma

Tietojenkäsittelytieteen kandidaatti (TKT).


