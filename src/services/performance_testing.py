import os
import datetime
from trie import TrieSolmu


def lue_sanasto_trie():
    trie = TrieSolmu()
    kansio = os.path.dirname(__file__)
    engl_sanasto = os.path.join(kansio, "..\\vocabulary\\words.txt")

    with open(engl_sanasto, encoding="utf8") as sanasto:
        for sana in sanasto:
            sana = sana.lower().replace("\n", "")
            trie.lisaa_sana(sana)

    return trie


def lue_sanasto_lista():
    sanalista = []
    kansio = os.path.dirname(__file__)
    engl_sanasto = os.path.join(kansio, "..\\vocabulary\\words.txt")

    with open(engl_sanasto, encoding="utf8") as sanasto:
        for sana in sanasto:
            sana = sana.lower().replace("\n", "")
            sanalista.append(sana)
    return sanalista


def onko_sana_olemassa_lista(sana: str, lista: list):
    return sana in lista


def onko_sana_olemassa_trie(sana: str, trie: TrieSolmu):
    return trie.onko_sana_olemassa(sana)


def lue_testisanasto():
    sanalista = []
    sanalista_virheilla = []
    kansio = os.path.dirname(__file__)
    engl_sanasto = os.path.join(kansio, "..\\vocabulary\\1-1000.txt")
    with open(engl_sanasto, encoding="utf8") as sanasto:
        for sana in sanasto:
            sana = sana.lower().replace("\n", "")
            sanalista.append(sana)
            sanalista_virheilla.append(sana + "kirjoitusvirhe")
    return sanalista, sanalista_virheilla


if __name__ == '__main__':
    tuhat_yleisinta_sanaa, tuhat_yleisinta_sanaa_virheilla = lue_testisanasto()

    alku = datetime.datetime.now()
    lista = lue_sanasto_lista()
    print("Sanaston lukeminen listaan:", datetime.datetime.now() - alku)

    alku = datetime.datetime.now()
    trie = lue_sanasto_trie()
    print("Sanaston lukeminen trie-puuhun:", datetime.datetime.now() - alku)

    alku = datetime.datetime.now()
    for sana in tuhat_yleisinta_sanaa:
        loytyyko = onko_sana_olemassa_lista(sana, lista)
        if not loytyyko:
            print("UPS! Sanaa", sana, "ei löytynyt!")
    print("Tuhannen yleisimmän sanan etsintä listan avulla:",
          datetime.datetime.now() - alku)

    alku = datetime.datetime.now()
    for sana in tuhat_yleisinta_sanaa:
        loytyyko = onko_sana_olemassa_trie(sana, trie)
        if not loytyyko:
            print("UPS! Sanaa", sana, "ei löytynyt!")
    print("Tuhannen yleisimmän sanan etsintä trie-puun avulla:",
          datetime.datetime.now() - alku)

    alku = datetime.datetime.now()
    for sana in tuhat_yleisinta_sanaa_virheilla:
        loytyyko = onko_sana_olemassa_lista(sana, lista)
    print("Tuhannen yleisimmän sanan ja tuhannen tietorakenteesta löytymättömän sanan etsintä listan avulla:",
          datetime.datetime.now() - alku)

    alku = datetime.datetime.now()
    for sana in tuhat_yleisinta_sanaa_virheilla:
        loytyyko = onko_sana_olemassa_trie(sana, trie)
    print("Tuhannen yleisimmän sanan ja tuhannen tietorakenteesta löytymättömän sanan etsintä trie-puun avulla:",
          datetime.datetime.now() - alku)
