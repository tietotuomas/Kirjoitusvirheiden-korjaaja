class UI:
    """Tekstikäyttöliittymä
    """

    def __init__(self, sanastopalvelu):
        self.sanastopalvelu = sanastopalvelu
        self.ohje = True

    TERVEHDYS_TEKSTI = "\nTervetuloa käyttämään kirjoitusvirheiden korjaaja -sovellusta!\n"
    KOMENTO_TEKSTI = "\nValitse komento syöttämällä numero: "
    KOMENNOT = {
        "1": "Syötä englanninkielinen teksti",
        "2": "Laske kahden merkkijonon välinen editointietäisyys",
        "3": "Lopeta"
    }

    EI_VIRHEITA_TEKSTI = "Sovellus ei löytänyt tekstistä virheitä\n"
    SANASTO_LUKU_TEKSTI = "Sovellus lukee sanastoa...\n"
    INFO_TEKSTI = "\nSovellus ei tunnista välimerkeistä kuin heittomerkin (') ja väliviivan (-).\n"\
        "Esimerkiksi piste ja pilkku tulkitaan aina kirjoitusvirheeksi.\n"
    KORJATTU_MJONO_TEKSTI = "Tähdellä merkatut sanat vaikuttavat virheelliseltä: "
    VIRHEELLINEN_TEKSTI = "Virheellinen komento\n"
    EI_KORJAUKSIA_TEKSTI = "Sovellus ei pystynyt korjaamaan tähdellä merkattuja sanoja\n"
    ENSIMMAINEN_MERKKIJONO = "Syötä ensimmäinen merkkijono: "
    TOINEN_MERKKIJONO = "Syötä toinen merkkijono: "
    DAMERAU_LEVENSHTEIN = "Merkkijonojen {ensimmainen_sana} ja {toinen_sana} välinen Damerau-Levenshtein-etäisyys on"
    LEVENSHTEIN = "Merkkijonojen {ensimmainen_sana} ja {toinen_sana} välinen Levenshtein-etäisyys on"
    LOPETUS_TEKSTI = "Sovellus sulkeutuu"

    def kaynnista(self):

        print(self.TERVEHDYS_TEKSTI)
        print(self.SANASTO_LUKU_TEKSTI)
        self.sanastopalvelu.lue_sanasto()

        while True:
            for komento in self.KOMENNOT:
                print(f"{komento}: {self.KOMENNOT[komento]}")
            syote = input(self.KOMENTO_TEKSTI)

            if syote == "3":
                print(self.LOPETUS_TEKSTI)
                break
            elif syote == "2":
                self._lue_merkkijonot()
            elif syote == "1":
                self._lue_teksti()
            else:
                print(self.VIRHEELLINEN_TEKSTI)
                continue

    def _lue_teksti(self):
        if self.ohje:
            print(self.INFO_TEKSTI)
            self.ohje = False
        teksti = input(self.KOMENNOT["1"]+": ")

        palaute = self.sanastopalvelu.tarkista_teksti(teksti)
        if palaute:
            print(self.KORJATTU_MJONO_TEKSTI)
            if "*" in palaute.split("Tarkoititko:")[1]:
                print(palaute)
                print(self.EI_KORJAUKSIA_TEKSTI)
            else:
                print(palaute)
        else:
            print(f"{self.EI_VIRHEITA_TEKSTI}")

    def _lue_merkkijonot(self):
        ensimmainen_sana = input(self.ENSIMMAINEN_MERKKIJONO)
        toinen_sana = input(self.TOINEN_MERKKIJONO)
        damerau_levenshtein, levenshtein = self.sanastopalvelu.laske_editointietaisyys(
            ensimmainen_sana, toinen_sana)

        self._tulosta_matriisi(levenshtein, False)
        self._tulosta_matriisi(damerau_levenshtein, True)

        print(self.DAMERAU_LEVENSHTEIN.format(ensimmainen_sana=ensimmainen_sana, toinen_sana=toinen_sana),
              damerau_levenshtein[len(toinen_sana)][len(ensimmainen_sana)])
        print(self.LEVENSHTEIN.format(ensimmainen_sana=ensimmainen_sana, toinen_sana=toinen_sana),
              levenshtein[len(toinen_sana)][len(ensimmainen_sana)])
        print("")

    def _tulosta_matriisi(self, matriisi, onko_damearau):
        vali = " "
        for lista in matriisi:
            for numero in lista:
                if numero > 9:
                    vali = "  "
                    break
        print("")
        for rivi in range(len(matriisi)):
            for sarake in range(len(matriisi[rivi])):
                print(matriisi[rivi][sarake], end=vali)
            if len(matriisi) // 2 == rivi:
                if onko_damearau:
                    print(" "*10, "Damerau-Levenshtein matriisi", end="")
                else:
                    print(" "*10, "Levenshtein matriisi", end="")
            print("")
        print("")
