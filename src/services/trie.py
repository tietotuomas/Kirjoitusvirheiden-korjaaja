class Trie:
    def __init__(self):
        self.juuri = {"*":"*"}

    def lisaa_sana(self, sana):
        solmu = self.juuri
        # print("solmu nyt", solmu)
        for kirjain in sana:
            # print("kirjain nyt", kirjain)
            if kirjain not in solmu:
                solmu[kirjain] = {}
                # print("uusi kirjain", solmu)

            solmu = solmu[kirjain]
            # print("lapsi", solmu)
        solmu["*"] = "*"

    def onko_sana_olemassa(self, sana):
        solmu = self.juuri
        for kirjain in sana:
            if kirjain not in solmu:
                return False
            solmu = solmu[kirjain]
        return "*" in solmu

# trie = Trie()
# words = ["wait", "waiter", "shop", "shopper"]
# for word in words:
#   trie.lisaa_sana(word)
# print(trie.juuri["w"]["a"]["i"]["t"])

# print(trie.onko_sana_olemassa("wait")) #True
# print(trie.onko_sana_olemassa("")) #True
# print(trie.onko_sana_olemassa("waite")) #False
# print(trie.onko_sana_olemassa("shop")) #True
# print(trie.onko_sana_olemassa("shoppp")) #False
