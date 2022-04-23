import os


class Sanastopalvelu:

    def __init__(self, trie, dameraulevenshtein, tiedosto):
        self.trie = trie
        self.dameraulevenshtein = dameraulevenshtein
        self.tiedosto = tiedosto

    def lue_sanasto(self):
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
        ehdotukset = self.dameraulevenshtein.etsi_korjaukset(
            self.trie, korjattava_sana)
        if ehdotukset:
            korjattava_sana = min(ehdotukset, key=lambda t: (t[1], t[2]))[0]
        return korjattava_sana

    def tarkista_teksti(self, teksti: str):
        sanalista = teksti.lower().split()
        korjattu_sanalista = teksti.lower().split()
        virheeton = True
        i = 0
        while i < len(sanalista):
            if not self.trie.onko_sana_olemassa(sanalista[i]):
                virheeton = False
                korjattu_sanalista[i] = self.korjaa_sana(sanalista[i])
                sanalista[i] = sanalista[i] + "*"

            i += 1
        if virheeton:
            return ""
        return f"{' '.join(sanalista)}\n\nTarkoititko:\n{' '.join(korjattu_sanalista)} ?\n"

    def laske_editointietaisyys(self, ensimmainen_mjono: str, toinen_mjono: str):
        etaisyys = self.dameraulevenshtein.levenstheinin_etaisyys(
            ensimmainen_mjono, toinen_mjono)
        return f"Merkkijonojen {ensimmainen_mjono} ja {toinen_mjono} välinen editointietäisyys on {etaisyys}"
