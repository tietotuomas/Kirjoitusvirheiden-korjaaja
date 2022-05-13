class DamerauLevenshtein:
    """
    Luokka tarjoaa toiminnallisuudet editointietäisyyksien laskemiseen
    sekä virheellisen sanan korjausehdotuslistan muodostamiseen. Toiminnallisuudet
    perustuvat Damerau-Levenshtein -etäisyyden hyödyntämiseen.
    """

    def _luo_matriisi(self, sarakkeet: int, rivit: int):
        """
        Luo kaksiuloitteisen taulukon eli matriisin, jonka koko on
        (n+1) * (m+1), missä n ja m ovat merkkijonojen pituudet.
        Täyttää matriisin ensimmäisen vaakarivin ensimmäisen (oikean) sanan
        pituusindekseillä+1 ja ensimmäisen pystyrivin toisen (tarkistettavan)
        sanan pituusindekseillä+1. Alustaa muiden solujen arvoksi nolla.

        Esim. kahdelle kolmen merkin pituiselle sanalle muodostettu matriisi:

        0 1 2 3
        1 0 0 0
        2 0 0 0
        3 0 0 0

        Args:
            sarakkeet: oikean merkkijonon pituus + 1
            rivit: tarkistettavan merkkijonon pituus +1

        Returns:
            Kaksiulotteisen taulukon, joka on täytetty yllä kuvatulla tavalla.

        """
        matriisi = []

        for rivi in range(rivit):
            matriisi.append([])
            for sarake in range(sarakkeet):
                if rivi == 0:
                    matriisi[rivi].append(sarake)
                elif sarake == 0:
                    matriisi[rivi].append(rivi)
                else:
                    matriisi[rivi].append(0)

        return matriisi

    def laske_levensthein_etaisyys(self, oikea_sana: str, tarkistettava_sana: str):
        """
        Täyttää metodin luo_matriisi alustaman matriisin rivi kerrallaan
        levehnstein-etäisyyteen perustuen. Editointietäisyys luetaan matriisin
        viimeisestä solusta.

        Levensteinin etäisyyttä laskettaessa sallittuja operaatioita ovat
        yhden merkin lisääminen, poistaminen tai korvaaminen toisella merkillä.

        Args:
            oikea_sana: Käyttäjän syöttämä ensimmäinen merkkijono, johon vertailua tehdään.
            tarkistettava_sana: Käyttäjän syöttämä toinen merkkijono, jota vertaillaan
            ensimmäiseen merkkijonoon.

        Returns:
            Kokonaan täytetyn kaksiulotteisen taulukon eli matriisin levehnstein-etäisyyteen
            perustuen.
        """

        matriisi = self._luo_matriisi(
            len(oikea_sana)+1, len(tarkistettava_sana)+1)

        for rivi in range(1, len(tarkistettava_sana)+1):
            for sarake in range(1, len(oikea_sana)+1):
                if oikea_sana[sarake-1] != tarkistettava_sana[rivi-1]:
                    matriisi[rivi][sarake] = min(matriisi[rivi-1][sarake-1],
                                                 matriisi[rivi-1][sarake],
                                                 matriisi[rivi][sarake-1]) + 1
                else:
                    matriisi[rivi][sarake] = matriisi[rivi-1][sarake-1]

        return matriisi

    def laske_damerau_levensthein_etaisyys(self, oikea_sana: str, tarkistettava_sana: str):
        """
        Täyttää metodin luo_matriisi alustaman matriisin rivi kerrallaan
        damerau-levehnstein-etäisyyteen perustuen. Editointietäisyys luetaan matriisin
        viimeisestä solusta.

        Damerau-levensteinin etäisyyttä laskettaessa sallittuja operaatioita ovat
        yhden merkin lisääminen, poistaminen, korvaaminen toisella merkillä tai kahden
        vierekkäisen merkin paikan vaihtaminen.

        Args:
            oikea_sana: Käyttäjän syöttämä ensimmäinen merkkijono, johon vertailua tehdään.
            tarkistettava_sana: Käyttäjän syöttämä toinen merkkijono, jota vertaillaan
            ensimmäiseen merkkijonoon.

        Returns:
            Kokonaan täytetyn kaksiulotteisen taulukon eli matriisin levehnstein-etäisyyteen
            perustuen.
        """

        matriisi = self._luo_matriisi(
            len(oikea_sana)+1, len(tarkistettava_sana)+1)

        for rivi in range(1, len(tarkistettava_sana)+1):
            for sarake in range(1, len(oikea_sana)+1):
                if oikea_sana[sarake-1] != tarkistettava_sana[rivi-1]:
                    matriisi[rivi][sarake] = min(matriisi[rivi-1][sarake-1],
                                                 matriisi[rivi-1][sarake],
                                                 matriisi[rivi][sarake-1]) + 1
                else:
                    matriisi[rivi][sarake] = matriisi[rivi-1][sarake-1]

                if rivi-1 > 0 and sarake-1 > 0 and tarkistettava_sana[rivi-1] == \
                        oikea_sana[sarake-2] and tarkistettava_sana[rivi-2] == oikea_sana[sarake-1]\
                        and oikea_sana[sarake-1] != tarkistettava_sana[rivi-1]:
                    matriisi[rivi][sarake] = min(
                        matriisi[rivi][sarake], matriisi[rivi-2][sarake-2]+1)

        return matriisi

    def etsi_korjaukset(self, trie, sana):
        """
        Etsii virheellisille sanalle korjausehdotuksia. Laskee virheelliselle
        sanalle Damerau-Levenshtein -etäisyyksiä käymällä läpi Trie-puuhun
        ladatun sanaston kutsumalla metodia etsi_rekursiivisesti. Alustaa matriisin
        ensimmäisen rivin, tyhjän tulostaulukon ja muuttujan pienin (5), jota suurempia
        editointietäisyyden omaavia sanoja ei lisätä tulostaulukkoon.

        Args:
            trie: TrieSolmu-luokkaan tallennettu sanasto.
            sana: Virheellinen sana, jolle etsitään korjausehdotuksia.

        Returns:
            Palauttaa korjausehdotukset kolmialkioisia tupleja
            sisältävänä taulukkona:
            ensimmäinen alkio sisältää sanan eli itse korjausehdotuksen,
            toinen alkio kertoo Damerau-Levenshtein -etäisyyden virheelliseen sanaan verrattuna,
            kolmas alkio kertoo sanan sijoituksen.
        """

        nykyinen_rivi = range(len(sana) + 1)

        pienin = 5

        tulos = []

        for kirjain in trie.lapset:
            self._etsi_rekursiivisesti(trie.lapset[kirjain], kirjain, None,
                                       sana, nykyinen_rivi, None, tulos, pienin)
        return tulos

    def _etsi_rekursiivisesti(self, solmu, kirjain, edellinen_kirjain,
                              sana, edellinen_rivi, toissa_rivi, tulos, pienin):
        """
        Laskee virheelliselle sanalle Damerau-Levenshtein -etäisyyksiä käymällä läpi Trie-puuhun
        ladatun sanaston kirjain tai merkki kerrallaan. Käy haarat rekursiivisesti läpi
        kutsumalla itseään.

        Damerau-levensteinin etäisyyden mukaisesti tarkistettavat operaatiot ovat
        yhden merkin lisääminen, poistaminen, korvaaminen toisella merkillä tai kahden
        vierekkäisen merkin paikan vaihtaminen.

        Jos solmu sisältää sanan päättävän kirjaimen ja ko. sanan Damerau-Levenshtein -etäisyys
        on yhtä pieni tai pienempi kuin tuloslistan pienin etäisyys (kuitenkin korkeintaan 5),
        lisätään sana tulostaulukkoon.

        Args:
            solmu: trie-puun solmu
            kirjain: vertailuvuorossa oleva kirjain
            edellinen_kirjain: edellisenä vuorossa ollut kirjain,
            siis trie-puussa nykyisen kirjaimen vanhempi
            sana: virheellinen sana, johon sanaston sanoja verrataan
            edellinen_rivi: matriisin edellinen, "ylempi" rivi
            toissa_rivi: edellistä riviä edeltänyt rivi
            tulos: tulostaulukko, johon potentiaaliset korjausehdotukset lisätään
            tuplena (sana, etaisyys, sijoitus)
            pienin: kokonaisluku, joka pitää kirjaa tulostaulukon pienimmästä editointietäisyydestä

        """

        sarakkeet = len(sana) + 1
        nykyinen_rivi = [edellinen_rivi[0] + 1]
        for sarake in range(1, sarakkeet):

            lisays_hinta = nykyinen_rivi[sarake - 1] + 1

            poisto_hinta = edellinen_rivi[sarake] + 1

            if sana[sarake - 1] != kirjain:
                vaihto_hinta = edellinen_rivi[sarake - 1] + 1
            else:
                vaihto_hinta = edellinen_rivi[sarake - 1]

            nykyinen_rivi.append(min(lisays_hinta, poisto_hinta, vaihto_hinta))

            if edellinen_kirjain and sarake-1 > 0 and kirjain == sana[sarake-2]\
                    and edellinen_kirjain == sana[sarake-1] and sana[sarake-1] != kirjain:
                nykyinen_rivi[sarake] = min(
                    nykyinen_rivi[sarake], toissa_rivi[sarake-2] + 1)

        if solmu.sana is not None and nykyinen_rivi[-1] <= pienin:
            pienin = nykyinen_rivi[-1]
            tulos.append((solmu.sana, nykyinen_rivi[-1], solmu.sijoitus))

        edellinen_kirjain = kirjain

        for lapsi in solmu.lapset:
            self._etsi_rekursiivisesti(solmu.lapset[lapsi], lapsi,
                                       edellinen_kirjain, sana, nykyinen_rivi,
                                       edellinen_rivi, tulos, pienin)
