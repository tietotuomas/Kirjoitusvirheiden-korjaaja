import unittest
from services.damerau_levenshtein import DamerauLevenshtein
from datastructures.trie import TrieSolmu


class TestDamerauLevenshteinDistances(unittest.TestCase):

    def setUp(self):
        self.dl = DamerauLevenshtein()

    def test_levenstheinin_etaisyys_palauttaa_oikeita_editointietaisyyksia(self):
        matriisi = self.dl.laske_damerau_levensthein_etaisyys("hello", "hello")
        self.assertEqual(matriisi[-1][-1], 0)
        matriisi = self.dl.laske_damerau_levensthein_etaisyys("world", "wolrd")
        self.assertEqual(matriisi[-1][-1], 1)
        matriisi = self.dl.laske_damerau_levensthein_etaisyys("yes", "yep")
        self.assertEqual(matriisi[-1][-1], 1)
        matriisi = self.dl.laske_damerau_levensthein_etaisyys("yes", "yse")
        self.assertEqual(matriisi[-1][-1], 1)
        matriisi = self.dl.laske_damerau_levensthein_etaisyys(
            "afntsatci", "fantastic")
        self.assertEqual(matriisi[-1][-1], 3)
        matriisi = self.dl.laske_damerau_levensthein_etaisyys(
            "engineer", "architecht")
        self.assertEqual(matriisi[-1][-1], 8)


class TestDamerauLevenshteinWithTrie(unittest.TestCase):

    def setUp(self):
        self.dl = DamerauLevenshtein()
        self.trie = TrieSolmu()
        sanat = ["ok", "no", "yes", "dirt", "dirty",
                 "dirtier", "dirtiest", "representational", "well-being"]
        i = 0
        for sana in sanat:
            i += 1
            self.trie.lisaa_sana(sana, i)

    def test_etsi_korjaukset_palauttaa_listan(self):
        tulos = self.dl.etsi_korjaukset(self.trie, "word")
        self.assertIsInstance(tulos, list)

    def test_etsi_korjaukset_palauttama_lista_sisaltaa_kolme_osaisia_tupleja(self):
        tulos = self.dl.etsi_korjaukset(self.trie, "word")
        self.assertIsInstance(tulos[0], tuple)

    def test_etsi_korjaukset_palauttaman_listan_tuple_sisaltaa_merkkijonon_ja_kaksi_kokonaislukua(self):
        tulos = self.dl.etsi_korjaukset(self.trie, "word")
        self.assertIsInstance(tulos[0][0], str)
        self.assertIsInstance(tulos[0][1], int)
        self.assertIsInstance(tulos[0][2], int)

    def test_etsi_korjaukset_palauttaa_oikeat_sanat_ja_editointietaisyydet_ja_sijoitukset(self):
        tulos = self.dl.etsi_korjaukset(self.trie, "yep")
        self.assertIn(("ok", 3, 1), tulos)
        self.assertIn(("no", 3, 2), tulos)
        self.assertIn(("yes", 1, 3), tulos)
        self.assertNotIn(("representational", 14, 8), tulos)

    def test_etsi_korjaukset_palauttaa_oikean_editointietaisyyden_kun_tarvitaan_transpoosia(self):
        # levenstheinin etaisyys (ei transpoosia) sanojen välillä on 2
        matriisi = self.dl.laske_levensthein_etaisyys("yes", "yse")
        self.assertEqual(matriisi[-1][-1], 2)
        tulos = self.dl.etsi_korjaukset(self.trie, "yse")
        print(tulos)
        self.assertIn(("yes", 1, 3), tulos)
