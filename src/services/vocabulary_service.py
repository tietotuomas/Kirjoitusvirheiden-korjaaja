import os

class Tiedostonlukija:

    def lue_sanasto(self):
        kansio = os.path.dirname(__file__)
        engl_sanasto = os.path.join(kansio, "..\\vocabulary\words.txt")

        with open(engl_sanasto) as sanasto:
            laskuri = 0
            for rivi in sanasto:
                rivi = rivi.replace("\n", "")
                print("Rivi", rivi)
                laskuri += 1
                if laskuri > 10:
                    break
