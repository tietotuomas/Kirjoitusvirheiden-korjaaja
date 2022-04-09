import os
from services.trie import TrieSolmu
from services.levenshtein_distance import Levenshtein

class Sanastopalvelu:

    def __init__(self):
        self.trie = TrieSolmu()
        self.levenshtein = Levenshtein()

    def lue_sanasto(self):
        kansio = os.path.dirname(__file__)
        engl_sanasto = os.path.join(kansio, "..\\vocabulary\\english3.txt")

        with open(engl_sanasto, encoding="utf8") as sanasto:
            for sana in sanasto:
                sana = sana.lower().replace("\n", "")
                self.trie.lisaa_sana(sana)

    def korjaa_sana(self, korjattava_sana:str):
        ehdotukset = self.levenshtein.etsi_korjaukset(self.trie, korjattava_sana, 3)
        if ehdotukset:
            korjattava_sana = min(ehdotukset, key = lambda t: t[1])[0]
        return korjattava_sana

    def tarkista_teksti(self, teksti: str):
        sanalista = teksti.lower().split()
        korjattu_sanalista = teksti.lower().split()
        virheeton = True
        i = 0
        while i < len(sanalista):
            if not self.trie.onko_sana_olemassa(sanalista[i]):
                virheeton = False
                sanalista[i] = sanalista[i] + "*"
                korjattu_sanalista[i] = self.korjaa_sana(sanalista[i])
            i += 1
        if virheeton:
            return ""
        return f"{' '.join(sanalista)}\n\nTarkoititko:\n{' '.join(korjattu_sanalista)} ?\n"

    def laske_editointietaisyys(self, ensimmainen_mjono: str, toinen_mjono: str):
        etaisyys = self.levenshtein.levenstheinin_etaisyys(ensimmainen_mjono, toinen_mjono)
        return f"Merkkijonojen {ensimmainen_mjono} ja {toinen_mjono} välinen editointietäisyys on {int(etaisyys)}"
