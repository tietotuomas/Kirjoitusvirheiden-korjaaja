import numpy

class Levenstein:

    def levensteinin_etaisyys(self, oikea_sana: str, tarkistettava_sana: str):    

        oikea_sana_listana = [kirjain for kirjain in oikea_sana]
        tarkistettava_sana_listana = [kirjain for kirjain in tarkistettava_sana]

        #luodaan matriisi etäisyyden laskemista varten
        # self.luo_matriisi(oikea_sana=oikea_sana, kirjoitettu_sana=kirjoitettu_sana)
        matriisi = numpy.zeros((len(tarkistettava_sana)+1, len(oikea_sana)+1))
        print(matriisi)

        # ensimmäinen rivi täytetään oikean sanan+1 pituusindekseillä
        matriisi[0] = [numero for numero in range(len(oikea_sana_listana)+1)]
        # ensimmäinen sarake täytetään tarkistettavan sanan+1 pituusindekseillä
        matriisi[:, 0] = [numero for numero in range(len(tarkistettava_sana_listana)+1)]

        print(matriisi)

        for sarake in range(1, len(oikea_sana_listana)+1):
            for rivi in range(1, len(tarkistettava_sana_listana)+1):
                print(oikea_sana_listana[sarake-1], " = ", tarkistettava_sana_listana[rivi-1])
                # jos kirjaimet eivät ole samoja, kopioidaan iteroitavaan soluun pienin arvo 
                # "ylemmästä", "vasemmasta" tai "vinottain vasemalla" olevasta solusta ja lisätään siihen 1
                if oikea_sana_listana[sarake-1] != tarkistettava_sana_listana[rivi-1]:
                    matriisi[rivi,sarake] = min(matriisi[rivi-1, sarake], matriisi[rivi, sarake-1], matriisi[rivi-1, sarake-1]) + 1
                # jos kirjaimet ovat samoja, kopioidaan matriisissa vinoittain vasemmalla oleva luku
                else: 
                    matriisi[rivi,sarake] = matriisi[rivi-1, sarake-1]
                    
        print(matriisi)

        # palautetaan matriisin oikean alakulman arvo, joka on siis sanojen pienin editointietäisyys
        return matriisi[len(tarkistettava_sana)][len(oikea_sana)]
   
    # def luo_matriisi(self, oikea_sana: str, kirjoitettu_sana: str):

if __name__ == "__main__":
    l = Levenstein()
    print(l.levensteinin_etaisyys("life", "living"))
