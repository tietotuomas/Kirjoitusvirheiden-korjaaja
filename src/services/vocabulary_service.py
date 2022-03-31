import os
from services.trie import Trie

class Sanastopalvelu:

    def __init__(self):
        self.trie = Trie()

        print("LUETAAN SANASTO")
        self.lue_sanasto()

    def lue_sanasto(self):
        kansio = os.path.dirname(__file__)
        engl_sanasto = os.path.join(kansio, "..\\vocabulary\\words.txt")

        with open(engl_sanasto, encoding="utf8") as sanasto:
            # laskuri = 0
            for sana in sanasto:
                sana = sana.lower().replace("\n", "")
                if not self.trie.onko_sana_olemassa(sana):
                    self.trie.lisaa_sana(sana)
                # laskuri += 1
                # if laskuri > 100:
                #     break
        # print(sana)
        # print(self.trie.juuri["a"]["a"]["l"]["t"])

    def tarkista_teksti(self, teksti: str):
        sanalista = teksti.lower().split()
        virheeton = True
        indeksi = 0
        while indeksi < len(sanalista):
            if not self.trie.onko_sana_olemassa(sanalista[indeksi]):
                virheeton = False
                sanalista[indeksi] = sanalista[indeksi] + "*"
            indeksi += 1
        if virheeton:
            return ""
        if len(sanalista) > 1:
            sanalista[0] = sanalista[0].capitalize()
        return " ".join(sanalista)
        