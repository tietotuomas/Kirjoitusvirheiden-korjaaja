import unittest
from services.damerau_levenshtein import DamerauLevenshtein
from datastructures.trie import TrieSolmu


class TestDamerauLevenshteinLaskeEtaisyydet(unittest.TestCase):

    def setUp(self):
        self.dl = DamerauLevenshtein()

    def test_luo_matriisi_palauttaa_kaksiulotteisen_taulukon(self):
        sana1 = "o"
        sana2 = "k"
        matriisi = self.dl._luo_matriisi(len(sana1)+1, len(sana2)+1)
        self.assertIsInstance(matriisi, list)
        self.assertIsInstance(matriisi[0], list)
        self.assertIsInstance(matriisi[1], list)
        self.assertEqual(len(matriisi), 2)

    def test_luo_matriisi_alustaa_matriisin_oikein(self):
        self.assertEqual(self.dl._luo_matriisi(4, 4), [[0, 1, 2, 3], [
                         1, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0]])
        self.assertEqual(self.dl._luo_matriisi(2, 8), [[0, 1], [1, 0], [
                         2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]])
        self.assertEqual(self.dl._luo_matriisi(0, 0), [])
        self.assertEqual(self.dl._luo_matriisi(1, 1), [[0]])

    def test_laske_damerau_levensthein_etaisyys_palauttaa_oikeita_editointietaisyyksia(self):
        matriisi = self.dl.laske_damerau_levensthein_etaisyys("hello", "hello")
        self.assertEqual(matriisi[-1][-1], 0)
        # transpoosi
        matriisi = self.dl.laske_damerau_levensthein_etaisyys("world", "wolrd")
        self.assertEqual(matriisi[-1][-1], 1)
        matriisi = self.dl.laske_damerau_levensthein_etaisyys("yes", "yep")
        self.assertEqual(matriisi[-1][-1], 1)
        # transpoosi
        matriisi = self.dl.laske_damerau_levensthein_etaisyys("yes", "yse")
        self.assertEqual(matriisi[-1][-1], 1)
        matriisi = self.dl.laske_damerau_levensthein_etaisyys(
            "afntsatci", "fantastic")
        self.assertEqual(matriisi[-1][-1], 3)
        matriisi = self.dl.laske_damerau_levensthein_etaisyys(
            "engineer", "architecht")
        self.assertEqual(matriisi[-1][-1], 8)

    def test_laske_levensthein_etaisyys_palauttaa_oikeita_editointietaisyyksia(self):
        matriisi = self.dl.laske_levensthein_etaisyys("hello", "hello")
        self.assertEqual(matriisi[-1][-1], 0)
        matriisi = self.dl.laske_levensthein_etaisyys("world", "wolrd")
        # etäisyyteen 1 tarvittaisiin transpoosia
        self.assertEqual(matriisi[-1][-1], 2)
        matriisi = self.dl.laske_levensthein_etaisyys("yes", "yep")
        self.assertEqual(matriisi[-1][-1], 1)
        matriisi = self.dl.laske_levensthein_etaisyys("yes", "yse")
        # etäisyyteen 1 tarvittaisiin transpoosia
        self.assertEqual(matriisi[-1][-1], 2)
        matriisi = self.dl.laske_levensthein_etaisyys(
            "afntsatci", "fantastic")
        # etäisyyteen 3 tarvittaisiin transpoosia
        self.assertEqual(matriisi[-1][-1], 6)
        matriisi = self.dl.laske_levensthein_etaisyys(
            "engineer", "architecht")
        self.assertEqual(matriisi[-1][-1], 8)


class TestDamerauLevenshteinEtsiKorjauksetTrienKanssaTestiSanastolla(unittest.TestCase):

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
        # levenstheinin etäisyys (ei transpoosia) sanojen välillä on 2
        matriisi = self.dl.laske_levensthein_etaisyys("yes", "yse")
        self.assertEqual(matriisi[-1][-1], 2)
        tulos = self.dl.etsi_korjaukset(self.trie, "yse")
        # mutta metodin käyttämä damerau-levenstheinin etäisyys on 1
        self.assertIn(("yes", 1, 3), tulos)
