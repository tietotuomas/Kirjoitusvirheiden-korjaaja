class DamerauLevenshtein:

    def luo_matriisi(self, sarakkeet: int, rivit: int):
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

        matriisi = self.luo_matriisi(
            len(oikea_sana)+1, len(tarkistettava_sana)+1)

        for rivi in range(1, len(tarkistettava_sana)+1):
            for sarake in range(1, len(oikea_sana)+1):
                # jos kirjaimet eivät ole samoja, kopioidaan iteroitavaan soluun pienin arvo
                # "ylemmästä", "vasemmasta" tai "vinottain vasemalla" olevasta solusta
                # ja lisätään siihen 1
                # print(oikea_sana[sarake-1], tarkistettava_sana[rivi-1], rivi, sarake)
                if oikea_sana[sarake-1] != tarkistettava_sana[rivi-1]:
                    matriisi[rivi][sarake] = min(
                        matriisi[rivi-1][sarake],
                        matriisi[rivi][sarake-1]) + 1
                # jos kirjaimet ovat samoja, kopioidaan matriisissa vinoittain vasemmalla oleva luku
                else:
                    matriisi[rivi][sarake] = matriisi[rivi-1][sarake-1]


        # # palautetaan matriisin oikean alakulman arvo, joka on siis sanojen pienin editointietäisyys
       
        return matriisi

    def laske_damerau_levensthein_etaisyys(self, oikea_sana: str, tarkistettava_sana: str):
        matriisi = self.luo_matriisi(
            len(oikea_sana)+1, len(tarkistettava_sana)+1)

        for rivi in range(1, len(tarkistettava_sana)+1):
            for sarake in range(1, len(oikea_sana)+1):
                # jos kirjaimet eivät ole samoja, kopioidaan iteroitavaan soluun pienin arvo
                # "ylemmästä", "vasemmasta" tai "vinottain vasemalla" olevasta solusta
                # ja lisätään siihen 1
                # print(oikea_sana[sarake-1], tarkistettava_sana[rivi-1], rivi, sarake)
                if oikea_sana[sarake-1] != tarkistettava_sana[rivi-1]:
                    matriisi[rivi][sarake] = min(
                        matriisi[rivi-1][sarake],
                        matriisi[rivi][sarake-1]) + 1
                # jos kirjaimet ovat samoja, kopioidaan matriisissa vinoittain vasemmalla oleva luku
                else:
                    matriisi[rivi][sarake] = matriisi[rivi-1][sarake-1]
                # self.tulosta_matriisi(matriisi)
                # print("")

                if rivi-1 > 0 and sarake-1 > 0 and tarkistettava_sana[rivi-1] == oikea_sana[sarake-2]\
                        and tarkistettava_sana[rivi-2] == oikea_sana[sarake-1]\
                    and oikea_sana[sarake-1] != tarkistettava_sana[rivi-1]:
                    matriisi[rivi][sarake] = min(
                        matriisi[rivi][sarake], matriisi[rivi-2][sarake-2]+1)

                    #     and edellinen_kirjain == sana[sarake-1] and sana[sarake-1] != kirjain:
                    # nykyinen_rivi[sarake] = min(
                    #     nykyinen_rivi[sarake], toissa_rivi[sarake-2] + 1)

        # # palautetaan matriisin oikean alakulman arvo, joka on siis sanojen pienin editointietäisyys
        
        return matriisi

        # Etsii virheelliselle sanalle Damerau-Levenshtein -etäisyyksiä käymällä koko Trie-puun läpi
    def etsi_korjaukset(self, trie, sana):

        # ensimmäinen rivi täytetään oikean sanan+1 pituusindekseillä
        nykyinen_rivi = range(len(sana) + 1)
        # alustetaan pienimmäksi Damerau-Levenshtein -etäisyydeksi 5
        pienin = 5
        # luodaan tyhjä tuloslista
        tulos = []

        # käydään läpi kaikki Trie-puuhun tallennetut kirjaimet/haarat
        for kirjain in trie.lapset:
            self.etsi_rekursiivisesti(trie.lapset[kirjain], kirjain, None,
                                      sana, nykyinen_rivi, None, tulos, pienin)
        # palauttaa tulokset tuple-listana;
        # ensimmäinen alkio sisältää sanan,
        # toinen alkio Damerau-Levenshtein -etäisyyden,
        # kolmas alkio sijoituksen
        return tulos

    def etsi_rekursiivisesti(self, solmu, kirjain, edellinen_kirjain,
                             sana, edellinen_rivi, toissa_rivi, tulos, pienin):

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

            # Transpoosi eli Dameraus-osuuus - tarkistetaan,
            # kannattaako vierekkäisten kirjaimien vaihto
            if edellinen_kirjain and sarake-1 > 0 and kirjain == sana[sarake-2]\
                    and edellinen_kirjain == sana[sarake-1] and sana[sarake-1] != kirjain:
                nykyinen_rivi[sarake] = min(
                    nykyinen_rivi[sarake], toissa_rivi[sarake-2] + 1)

        # Jos kirjain on sanan päättävä kirjain ja
        # sanan pienin Damerau-Levenshtein -etäisyys on yhtä pieni
        # tai pienempi kuin listan pienin etäisyys (korkeintaan 5),
        # lisätään sana tuloksiin
        if solmu.sana is not None and nykyinen_rivi[-1] <= pienin:
            pienin = nykyinen_rivi[-1]
            tulos.append((solmu.sana, nykyinen_rivi[-1], solmu.sijoitus))

        edellinen_kirjain = kirjain

        for kirjain in solmu.lapset:
            self.etsi_rekursiivisesti(solmu.lapset[kirjain], kirjain,
                                      edellinen_kirjain, sana, nykyinen_rivi,
                                      edellinen_rivi, tulos, pienin)


if __name__ == '__main__':
    d = DamerauLevenshtein()

    print(d.levenstheinin_etaisyys("afntsatci", "fantastic"))
