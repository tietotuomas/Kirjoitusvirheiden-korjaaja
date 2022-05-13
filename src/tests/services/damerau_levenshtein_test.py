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
        # etäisyyteen 3 tarvittaisiin transpoosi
        self.assertEqual(matriisi[-1][-1], 6)
        matriisi = self.dl.laske_levensthein_etaisyys(
            "engineer", "architecht")
        self.assertEqual(matriisi[-1][-1], 8)

# Testataan korjaustoimintoa rajatulla testisanastolla


class TestDamerauLevenshteinEtsiKorjaukset(unittest.TestCase):

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

# Testataan korjaustoiminnon palauttamia etäisyyksiä sana kerrallaan


class TestDamerauLevenshteinEtsiKorjauksetEtaisyydet(unittest.TestCase):

    def setUp(self):
        self.trie = TrieSolmu()
        self.dl = DamerauLevenshtein()
        self.sijoitus = 0

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_a_ja_an(self):
        self.trie.lisaa_sana("a", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(self.trie, "an")[0][1], 1)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_an_ja_a(self):
        self.trie.lisaa_sana("an", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(self.trie, "a")[0][1], 1)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_test_ja_est(self):
        self.trie.lisaa_sana("test", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(self.trie, "est")[0][1], 1)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_test_ja_ests(self):
        self.trie.lisaa_sana("test", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(self.trie, "ests")[0][1], 2)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_test_ja_esst(self):
        self.trie.lisaa_sana("test", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(self.trie, "esst")[0][1], 2)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_test_ja_tests(self):
        self.trie.lisaa_sana("test", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(self.trie, "tests")[0][1], 1)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_test_ja_tets(self):
        self.trie.lisaa_sana("test", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(self.trie, "tets")[0][1], 1)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_car_ja_cars(self):
        self.trie.lisaa_sana("car", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(self.trie, "cars")[0][1], 1)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_car_ja_acr(self):
        self.trie.lisaa_sana("car", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(self.trie, "acr")[0][1], 1)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_car_ja_cartoon(self):
        self.trie.lisaa_sana("car", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(
            self.trie, "cartoon")[0][1], 4)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_hero_ja_zero(self):
        self.trie.lisaa_sana("hero", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(self.trie, "zero")[0][1], 1)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_hero_ja_hreo(self):
        self.trie.lisaa_sana("hero", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(self.trie, "hreo")[0][1], 1)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_hero_ja_heroes(self):
        self.trie.lisaa_sana("hero", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(self.trie, "heroes")[0][1], 2)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_algorithm_ja_alogrytm(self):
        self.trie.lisaa_sana("algorithm", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(
            self.trie, "alogrytm")[0][1], 3)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_alogrytm_ja_algorithm(self):
        self.trie.lisaa_sana("alogrytm", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(
            self.trie, "algorithm")[0][1], 3)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_fantastic_ja_afntsatci(self):
        self.trie.lisaa_sana("fantastic", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(
            self.trie, "afntsatci")[0][1], 3)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_tyhjalla_syotteella(self):
        self.trie.lisaa_sana("empty", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(
            self.trie, "")[0][1], 5)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_ylioppilastutkintolautakunta_ja_yliooopilastutkintolautakunta(self):
        self.trie.lisaa_sana("ylioppilastutkintolautakunta", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(
            self.trie, "yliooopilastutkintolautakunta")[0][1], 2)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_ylioppilastutkintolautakunta_ja_yliopplilaastutkintoklautakunta(self):
        self.trie.lisaa_sana("ylioppilastutkintolautakunta", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(
            self.trie, "yliopplilaastutkintoklautakunta")[0][1], 3)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_ylioppilastutkintolautakunta_ja_yloipplilaastutkintoklautakunta(self):
        self.trie.lisaa_sana("ylioppilastutkintolautakunta", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(
            self.trie, "yloipplilaastutkintoklautakunta")[0][1], 4)

    def test_etsi_korjaukset_palauttaa_oikean_damerau_levenshtein_etaisyyden_ylioppilastutkintolautakunta_ja_yloipplilaastutkintoklautakuntaa(self):
        self.trie.lisaa_sana("ylioppilastutkintolautakunta", self.sijoitus)
        self.assertEqual(self.dl.etsi_korjaukset(
            self.trie, "yloipplilaastutkintoklautakuntaa")[0][1], 5)
