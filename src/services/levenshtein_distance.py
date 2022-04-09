import numpy

class Levenshtein:

    def levenstheinin_etaisyys(self, oikea_sana: str, tarkistettava_sana: str):

        oikea_sana_listana = [kirjain for kirjain in oikea_sana]
        tarkistettava_sana_listana = [
            kirjain for kirjain in tarkistettava_sana]
        
        # luodaan matriisi etäisyyden laskemista varten)
        matriisi = numpy.zeros((len(tarkistettava_sana)+1, len(oikea_sana)+1))
        # print(matriisi)


        # ensimmäinen rivi täytetään oikean sanan+1 pituusindekseillä
        matriisi[0] = [numero for numero in range(len(oikea_sana_listana)+1)]
        # ensimmäinen sarake täytetään tarkistettavan sanan+1 pituusindekseillä
        matriisi[:, 0] = [numero for numero in range(
            len(tarkistettava_sana_listana)+1)]

        # print(matriisi)

        for sarake in range(1, len(oikea_sana_listana)+1):
            for rivi in range(1, len(tarkistettava_sana_listana)+1):
                # print(oikea_sana_listana[sarake-1], " = ",
                #       tarkistettava_sana_listana[rivi-1])
                # jos kirjaimet eivät ole samoja, kopioidaan iteroitavaan soluun pienin arvo
                # "ylemmästä", "vasemmasta" tai "vinottain vasemalla" olevasta solusta ja lisätään siihen 1
                if oikea_sana_listana[sarake-1] != tarkistettava_sana_listana[rivi-1]:
                    matriisi[rivi, sarake] = min(
                        matriisi[rivi-1, sarake], matriisi[rivi, sarake-1], matriisi[rivi-1, sarake-1]) + 1
                # jos kirjaimet ovat samoja, kopioidaan matriisissa vinoittain vasemmalla oleva luku
                else:
                    matriisi[rivi, sarake] = matriisi[rivi-1, sarake-1]

        # print(matriisi)

        # palautetaan matriisin oikean alakulman arvo, joka on siis sanojen pienin editointietäisyys
        return matriisi[len(tarkistettava_sana)][len(oikea_sana)]



    def etsiKorjaukset(self, trie, sana, maksimiEtaisyys):
    # Etsii virheelliselle sanalle todennäköisimmät vaihtoehdot editointietäisyyden perusteella
    # maximum distance from the target word

        # ensimmäinen rivi täytetään oikean sanan+1 pituusindekseillä
        nykyinenRivi = range(len(sana) + 1)

        tulos = []

        for kirjain in trie.lapset:
            self.etsiRekursiivisesti(trie.lapset[kirjain], kirjain, sana, nykyinenRivi,
                            tulos, maksimiEtaisyys)

        return tulos


    def etsiRekursiivisesti(self, solmu, kirjain, sana, edellinenRivi, tulos, maksimiEtaisyys):

        sarakkeet = len(sana) + 1
        nykyinenRivi = [edellinenRivi[0] + 1]

        for sarake in range(1, sarakkeet):

            lisaysHinta = nykyinenRivi[sarake - 1] + 1
            poistoHinta = edellinenRivi[sarake] + 1
            # transpoosiHinta ?

            if sana[sarake - 1] != kirjain:
                vaihtoHinta = edellinenRivi[sarake - 1] + 1
            else:
                vaihtoHinta = edellinenRivi[sarake - 1]

            nykyinenRivi.append(min(lisaysHinta, poistoHinta, vaihtoHinta))

        # print("nykyinenRivi", nykyinenRivi, nykyinenRivi[-1])


        if nykyinenRivi[-1] <= maksimiEtaisyys and solmu.sana != None:
            tulos.append((solmu.sana, nykyinenRivi[-1]))

        if min(nykyinenRivi) <= maksimiEtaisyys:
            for kirjain in solmu.lapset:
                self.etsiRekursiivisesti(solmu.lapset[kirjain], kirjain, sana, nykyinenRivi,
                                tulos, maksimiEtaisyys)


