

class UI:
    """Tekstikäyttöliittymä 
    """

    def __init__(self, sanastopalvelu):
        self.sanastopalvelu = sanastopalvelu

    TERVEHDYS_TEKSTI = "Tervetuloa käyttämään kirjoitusvirheiden korjaaja-sovellusta!\n"
    KOMENTO_TEKSTI = "\nAnna komento: "
    KOMENNOT = {
        "1": "Syötä englanninkielinen teksti: ",
        "2": "Lopeta"
    }

    EI_VIRHEITA_TEKSTI = "Sovellus ei löytänyt tekstistä virheitä\n"
    KORJATTU_MJONO_TEKSTI = "Korjausehdotus: \n"
    VIRHEELLINEN_TEKSTI = "Virheellinen komento"
    LOPETUS_TEKSTI = "Sovellus sulkeutuu"

    def kaynnista(self):

        print(self.TERVEHDYS_TEKSTI)

        while True:
            for komento in self.KOMENNOT:
                print(f"{komento}: {self.KOMENNOT[komento]}")
            syote = input(self.KOMENTO_TEKSTI)

            if syote == "2":
                print(self.LOPETUS_TEKSTI)
                break
            if syote == "1":
                self._lue_sana()
            else:
                print(self.VIRHEELLINEN_TEKSTI)
                continue

    def _lue_sana(self):
        sana = input(self.KOMENNOT["1"])
        print(f"{self.EI_VIRHEITA_TEKSTI}")
        self.sanastopalvelu.lue_sanasto()

