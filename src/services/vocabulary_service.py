import os


class Sanastopalvelu:
    """
    Luokka yhdistää käyttöliittymän tietorakenteisiin ja sisältää
    logiikkaa merkkijonojen korjaamiseen ja oikeellisuuden tarkastamiseen.


    Attributes:
        trie: Trie-tietorakenne.
        dameraulevenshtein: DamerauLevenshtein-luokka
        tiedosto: Sanasto-tiedoston suhteellinen sijainti
    """

    def __init__(self, trie, dameraulevenshtein, tiedosto):
        self.trie = trie
        self.dameraulevenshtein = dameraulevenshtein
        self.tiedosto = tiedosto

    def lue_sanasto(self):
        """
        Lukee sanaston self.tiedoston osoittamasta sijainnista sana kerrrallaan.
        Metodi olettaa, että sanasto on järjestetty sen mukaan,
        kuinka usein sana on esiintyy englanninkielisessä tekstissä.
        Useimmin esiintyvät sanat luetaan ensimmäisenä.
        """

        kansio = os.path.dirname(__file__)
        engl_sanasto = os.path.join(
            kansio, self.tiedosto)

        with open(engl_sanasto, encoding="utf8") as sanasto:

            sijoitus = 0
            for rivi in sanasto:
                sijoitus += 1
                sana = rivi.replace("\n", "").lower()
                self.trie.lisaa_sana(sana, sijoitus)

    def korjaa_sana(self, korjattava_sana: str):
        """
        Etsii virheelliseksi tunnistetulle sanalle korjausehdotuksia
        dameraulevenshtein.etsi_korjaukset- metodin avulla. Valitsee
        korjausehdotuksista sen sanan, jolla on pienin editointietäisyys.
        Jos kahdella tai useammalla sanalla on sama editointietäisyys,
        valitsee sanan, jolla pienempi sijoitus.

        Args:
            korjattava_sana: Virheelliseksi tunnistettu sana.

        Returns:
            Parhaimman korjausehdotuksen.
            Jos dameraulevenshtein ei anna korjausehdotuksia,
            palauttaa alkuperäisen korjaamattoman sanan.
        """
        ehdotukset = self.dameraulevenshtein.etsi_korjaukset(
            self.trie, korjattava_sana)

        if ehdotukset:
            korjattava_sana = min(ehdotukset, key=lambda t: (t[1], t[2]))[0]
        return korjattava_sana

    def tarkista_teksti(self, teksti: str):
        """
        Jakaa tekstin sanoiksi (listaksi) ja tarkistaa sana kerrallaan,
        löytyykö sana Trie-tietorakenteesta. Jos ei löydy, hakee
        sanalle korjausehdotusta kutsumalla korjaa_sana-metodia.

        Args:
            teksti: Käyttäjän syöttämä merkkijono.

        Returns:
            Palauttaa f-merkkijonomuotoisen tulostuksen,
            joka sisältää sekä alkuperäisen että korjatun tekstin.
            Virheelliset sanat merkitään tähdellä alkuperäiseen tekstiin.
            Jos teksti ei sisällä virheellisiä sanoja, palauttaa tyhjän merkkijonon.
        """
        sanalista = teksti.lower().split()
        korjattu_sanalista = teksti.lower().split()
        virheeton = True
        i = 0
        while i < len(sanalista):
            if not self.trie.onko_sana_olemassa(sanalista[i]):
                virheeton = False
                korjattu_sana = self.korjaa_sana(sanalista[i])
                if korjattu_sana != sanalista[i]:
                    korjattu_sanalista[i] = korjattu_sana
                else:
                    korjattu_sanalista[i] = korjattu_sana + "*"
                sanalista[i] = sanalista[i] + "*"

            i += 1
        if virheeton:
            return ""
        return f"{' '.join(sanalista)}\n\nTarkoititko:\n{' '.join(korjattu_sanalista)} ?\n"

    def laske_editointietaisyys(self, ensimmainen_mjono: str, toinen_mjono: str):
        """
        Kutsuu DamerauLevenshtein-luokan laske_levensthein_etaisyys- ja 
        laske_damerau_levensthein_etaisyys-metodia. Metodit palauttavat 
        kaksiulotteiset listat (matriisit). Matriisin viimeinen solu kertoo
        editointietäisyyden.

        Args:
            ensimmainen_mjono: Käyttäjän syöttämä ensimmäinen merkkijono.
            toinen_mjono: Käyttäjän syöttämä toinen merkkijono.

        Returns:
            Tuplen, joka sisältää DamerauLevenshtein-luokan rakentamat 
            kaksiuloitteiset listat (matriisit).
        """
        damerau_levenshtein = self.dameraulevenshtein.laske_damerau_levensthein_etaisyys(
            ensimmainen_mjono, toinen_mjono)
        levenshtein = self.dameraulevenshtein.laske_levensthein_etaisyys(
            ensimmainen_mjono, toinen_mjono)

        return damerau_levenshtein, levenshtein
