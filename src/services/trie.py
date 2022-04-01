class Trie:
    def __init__(self):
        self.juuri = {"*": "*"}

    def lisaa_sana(self, sana):
        solmu = self.juuri
        for kirjain in sana:
            if kirjain not in solmu:
                solmu[kirjain] = {}

            solmu = solmu[kirjain]
        solmu["*"] = "*"

    def onko_sana_olemassa(self, sana):
        solmu = self.juuri
        for kirjain in sana:
            if kirjain not in solmu:
                return False
            solmu = solmu[kirjain]
        return "*" in solmu
