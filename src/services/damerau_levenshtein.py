import numpy


class DamerauLevenshtein:

    # laskee kahden sanan välisen levenstheinin etäisyyden
    def levenstheinin_etaisyys(self, oikea_sana: str, tarkistettava_sana: str):

        oikea_sana_listana = list(oikea_sana)
        tarkistettava_sana_listana = list(tarkistettava_sana)
        # luodaan matriisi etäisyyden laskemista varten)
        matriisi = numpy.zeros((len(tarkistettava_sana)+1, len(oikea_sana)+1))
        # ensimmäinen rivi täytetään oikean sanan+1 pituusindekseillä
        matriisi[0] = list(range(len(oikea_sana_listana) + 1))
        # ensimmäinen sarake täytetään tarkistettavan sanan+1 pituusindekseillä
        matriisi[:, 0] = list(range(len(tarkistettava_sana_listana) + 1))

        for sarake in range(1, len(oikea_sana_listana)+1):
            for rivi in range(1, len(tarkistettava_sana_listana)+1):
                # jos kirjaimet eivät ole samoja, kopioidaan iteroitavaan soluun pienin arvo
                # "ylemmästä", "vasemmasta" tai "vinottain vasemalla" olevasta solusta
                # ja lisätään siihen 1
                if oikea_sana_listana[sarake-1] != tarkistettava_sana_listana[rivi-1]:
                    matriisi[rivi, sarake] = min(
                        matriisi[rivi-1, sarake], matriisi[rivi, sarake-1], matriisi[rivi-1, sarake-1]) + 1
                # jos kirjaimet ovat samoja, kopioidaan matriisissa vinoittain vasemmalla oleva luku
                else:
                    matriisi[rivi, sarake] = matriisi[rivi-1, sarake-1]

        # palautetaan matriisin oikean alakulman arvo, joka on siis sanojen pienin editointietäisyys
        return matriisi[len(tarkistettava_sana)][len(oikea_sana)]

    # Etsii virheelliselle sanalle Damerau-Levenshtein -etäisyyksiä käymällä koko Trie-puun läpi
    def etsi_korjaukset(self, trie, sana):

        # ensimmäinen rivi täytetään oikean sanan+1 pituusindekseillä
        nykyinen_rivi = range(len(sana) + 1)

        tulos = []

        # käydään läpi kaikki Trie-puuhun tallennetut kirjaimet/haarat
        for kirjain in trie.lapset:
            self.etsi_rekursiivisesti(trie.lapset[kirjain], kirjain, None, sana, nykyinen_rivi, None,
                                      tulos)
        # palauttaa tulokset tuple-listana; ensimmäinen alkio sisältää sanan, toinen alkio Damerau-Levenshtein -etäisyyden
        return tulos

    def etsi_rekursiivisesti(self, solmu, kirjain, edellinen_kirjain, sana, edellinen_rivi, toissa_rivi, tulos):

        sarakkeet = len(sana) + 1
        nykyinen_rivi = [edellinen_rivi[0] + 1]

        # vertaillaan editointietäisyyttä implisiittisessä matriisissa
        for sarake in range(1, sarakkeet):
            # vasen solu
            lisays_hinta = nykyinen_rivi[sarake - 1] + 1
            # ylempi solu
            poisto_hinta = edellinen_rivi[sarake] + 1

            # vasen yläkulma
            # jos eri kirjain, lisätään vaihtohintaan 1
            if sana[sarake - 1] != kirjain:
                vaihto_hinta = edellinen_rivi[sarake - 1] + 1
            else:
                vaihto_hinta = edellinen_rivi[sarake - 1]

            nykyinen_rivi.append(min(lisays_hinta, poisto_hinta, vaihto_hinta))

            # Transpoosi eli Dameraus-osuuus - tarkistetaan, kannattaako vierekkäisten kirjaimien vaihto
            if edellinen_kirjain and sarake-1 > 0 and kirjain == sana[sarake-2] and edellinen_kirjain == sana[sarake-1] and sana[sarake-1] != kirjain:
                nykyinen_rivi[sarake] = min(
                    nykyinen_rivi[sarake], toissa_rivi[sarake-2] + 1)

        # Jos kirjain on sanan päättävä kirjain, lisätään sana ja sen pienin Damerau-Levenshtein -etäisyys tuloksiin
        if solmu.sana is not None:
            print(solmu.sana)
            tulos.append((solmu.sana, nykyinen_rivi[-1]))

        edellinen_kirjain = kirjain

        for kirjain in solmu.lapset:
            self.etsi_rekursiivisesti(solmu.lapset[kirjain], kirjain, edellinen_kirjain, sana, nykyinen_rivi, edellinen_rivi,
                                      tulos)

    # maksimi_etäisyyttä hyödyntävä variaatio, joka ei välttämättä toimi oikein ja joka ei sisällä transpoosia eli Damerau-osuutta

    # def etsi_korjaukset_max(self, trie, sana, maksimi_etaisyys):
    #     # Etsii virheelliselle sanalle todennäköisimmät vaihtoehdot editointietäisyyden perusteella

    #     # ensimmäinen rivi täytetään oikean sanan+1 pituusindekseillä
    #     nykyinen_rivi = range(len(sana) + 1)

    #     tulos = []

    #     for kirjain in trie.lapset:

    #         self.etsi_rekursiivisesti(trie.lapset[kirjain], kirjain, sana, nykyinen_rivi,
    #                                   tulos, maksimi_etaisyys)

    #     return tulos

    # def etsi_rekursiivisesti_max(self, solmu, kirjain, sana, edellinen_rivi, tulos, maksimi_etaisyys):

    #     sarakkeet = len(sana) + 1
    #     nykyinen_rivi = [edellinen_rivi[0] + 1]

    #     for sarake in range(1, sarakkeet):

    #         lisays_hinta = nykyinen_rivi[sarake - 1] + 1
    #         poisto_hinta = edellinen_rivi[sarake] + 1
    #         # transpoosiHinta ?

    #         if sana[sarake - 1] != kirjain:
    #             vaihto_hinta = edellinen_rivi[sarake - 1] + 1
    #         else:
    #             vaihto_hinta = edellinen_rivi[sarake - 1]

    #         nykyinen_rivi.append(min(lisays_hinta, poisto_hinta, vaihto_hinta))

    #     if nykyinen_rivi[-1] <= maksimi_etaisyys and solmu.sana is not None:
    #         tulos.append((solmu.sana, nykyinen_rivi[-1]))

    #     if min(nykyinen_rivi) <= maksimi_etaisyys:
    #         for kirjain in solmu.lapset:
    #             self.etsi_rekursiivisesti(solmu.lapset[kirjain], kirjain, sana, nykyinen_rivi,
    #                                       tulos, maksimi_etaisyys)
