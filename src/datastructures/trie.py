class TrieSolmu:
    """
    Luokka mallintaa Trie-tietorakenteen (puun) solmua. Ensimmäinen solmu toimii puun juurena.
    Self.sana sisältää sanan ja self.sijoitus sijoituksen vain jos jokin sana päättyy ko. solmuun.
    """

    def __init__(self):
        self.sana = None
        self.sijoitus = None
        self.lapset = {}

    def lisaa_sana(self, sana: str, sijoitus: int):
        """
        Lisätään sana puuhun, kirjain (haara) kerrallaan.
        Viimeisen kirjaimen kohdalla merkataan sana ja sen sijoitus.
        """
        solmu = self
        for kirjain in sana:
            if kirjain not in solmu.lapset:
                solmu.lapset[kirjain] = TrieSolmu()

            solmu = solmu.lapset[kirjain]

        solmu.sana = sana
        solmu.sijoitus = sijoitus

    def onko_sana_olemassa(self, sana: str):
        """
        Tarkistaa, löytyykö sana puusta.
        Palauttaa True, jos löytyy. Muuten False.
        """
        solmu = self
        for kirjain in sana:
            if not kirjain in solmu.lapset:
                return False
            solmu = solmu.lapset[kirjain]
        if solmu.sana:
            return True
        return False
