

class UI:

    """
    Tekstikäyttöliittymä
    """

    TERVEHDYS_TEKSTI = "Tervetuloa käyttämään kirjoitusvirheiden korjaaja-sovellusta!\n"
    KOMENTO_TEKSTI = "\nAnna komento: "
    KOMENNOT = {
        "1": "Syötä englanninkielinen sana: ",
        "2": "Syötä englanninkielinen lause: ",
        "3": "Lopeta"
    }

    EI_VIRHEITA_TEKSTI = "Sovellus ei löytänyt tekstistä virheitä\n"
    KORJATTU_MJONO_TEKSTI = "Korjausehdotus: "
    VIRHEELLINEN_TEKSTI = "Virheellinen komento"
    LOPETUS_TEKSTI = "Sovellus sulkeutuu"

    def kaynnista(self):
        print(self.TERVEHDYS_TEKSTI)

        while True:
            for komento in self.KOMENNOT:
                print(f"{komento}: {self.KOMENNOT[komento]}")
            syote = input(self.KOMENTO_TEKSTI)

            if syote == "3":
                print(self.LOPETUS_TEKSTI)
                break
            elif syote == "1":
                self._lue_sana()
            elif syote == "2":
                self._lue_lause()
            else:
                print(self.VIRHEELLINEN_TEKSTI)
                continue

    def _lue_sana(self):
        sana = input(self.KOMENNOT["1"])
        print(f"{self.EI_VIRHEITA_TEKSTI}")

    def _lue_lause(self):
        lause = input(self.KOMENNOT["2"])
        print(f"{self.EI_VIRHEITA_TEKSTI}")
