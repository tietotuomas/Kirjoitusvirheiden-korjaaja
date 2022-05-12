import unittest
from unittest.mock import Mock
from services.damerau_levenshtein import DamerauLevenshtein
from services.vocabulary_service import Sanastopalvelu
from datastructures.trie import TrieSolmu

# Testataan luokkaa eristetysti mockatuilla riippuvuuksilla


class TestMockattuSanastoPalvelu(unittest.TestCase):
    def setUp(self):
        self.trie_mock = Mock()
        self.dameraulevenshtein_mock = Mock()
        self.tiedosto_mock = Mock()

        self.sanastopalvelu = Sanastopalvelu(
            self.trie_mock, self.dameraulevenshtein_mock, self.tiedosto_mock)

    def test_korjaa_sana_palauttaa_pienimman_editointietaisyyden_sanan(self):
        self.dameraulevenshtein_mock.etsi_korjaukset.return_value = [
            ("suurin", 100, 1), ("mock", 42, 2), ("pienin", 1, 3)]
        pienin_etaisyys = self.sanastopalvelu.korjaa_sana("testi")
        self.assertEqual(pienin_etaisyys, "pienin")

    def test_korjaa_sana_palauttaa_pienimman_sijoituksen_sanan_jos_editointietaisyys_sama(self):
        self.dameraulevenshtein_mock.etsi_korjaukset.return_value = [
            ("it", 1, 13), ("its", 1, 27), ("is", 2, 6)]
        pienin_sijoitus = self.sanastopalvelu.korjaa_sana("itd")
        self.assertEqual(pienin_sijoitus, "it")

    def test_korjaa_sana_palauttaa_alkuperaisen_sanan_jos_korjausehdotuksia_ei_loydy(self):
        self.dameraulevenshtein_mock.etsi_korjaukset.return_value = []
        original = self.sanastopalvelu.korjaa_sana("original")
        self.assertEqual(original, "original")

    def test_tarkista_teksti_palauttaa_tyhjan_merkkijonon_jos_virheita_ei_loydy(self):
        self.trie_mock.onko_sana_olemassa.return_value = True
        tyhja_merkkijono = self.sanastopalvelu.tarkista_teksti(
            "No mistakes in this sentence")
        self.dameraulevenshtein_mock.etsi_korjaukset.assert_not_called()
        self.assertEqual("", tyhja_merkkijono)

    def test_tarkista_teksti_kutsuu_metodia_onko_sana_olemassa_sanojen_lukumaaran_verran(self):
        self.trie_mock.onko_sana_olemassa.return_value = True
        self.sanastopalvelu.tarkista_teksti(
            "There are seven words in this sentence")
        self.assertEqual(self.trie_mock.onko_sana_olemassa.call_count, 7)

    def test_tarkista_teksti_palauttaa_tahdella_merkityt_sanat_jos_virheita_loytyy(self):
        self.trie_mock.onko_sana_olemassa.return_value = False
        self.dameraulevenshtein_mock.etsi_korjaukset.return_value = [
            ("korjaus", 1, 1)]
        virheelliset_sanat = self.sanastopalvelu.tarkista_teksti(
            "Mistakes in this senctence")
        self.assertIn("*", virheelliset_sanat)

    def test_tarkista_teksti_palauttaa_korjatut_sanat_jos_virheita_loytyy(self):
        self.trie_mock.onko_sana_olemassa.return_value = False
        self.dameraulevenshtein_mock.etsi_korjaukset.return_value = [
            ("korjaus", 1, 1)]
        virheelliset_sanat = self.sanastopalvelu.tarkista_teksti(
            "Mistakes in this senctence")
        self.assertIn("korjaus", virheelliset_sanat)

    def test_tarkista_teksti_kutsuu_metodia_etsi_korjaukset_virheellisten_sanojen_lukumaaran_verran(self):
        self.trie_mock.onko_sana_olemassa.side_effect = [
            True, True, True, False, True, True, True]
        self.dameraulevenshtein_mock.etsi_korjaukset.return_value = [
            ("fixed", 1, 1)]
        self.sanastopalvelu.tarkista_teksti(
            "There is a mistaek in this sentence")
        self.assertEqual(
            self.dameraulevenshtein_mock.etsi_korjaukset.call_count, 1)

    def test_laske_editointietaisyydet_palauttaa_tuplen(self):
        self.dameraulevenshtein_mock.laske_damerau_levensthein_etaisyys.return_value = [
            [1, 2], [3, 4]]
        self.dameraulevenshtein_mock.laske_levensthein_etaisyys.return_value = [
            [1, 2], [3, 4]]
        self.assertIsInstance(
            self.sanastopalvelu.laske_editointietaisyydet("1", "2"), tuple)

    def test_laske_editointietaisyydet_kumpaakin_laskentametodia_kerran(self):
        self.dameraulevenshtein_mock.laske_damerau_levensthein_etaisyys.return_value = [
            [1, 2], [3, 4]]
        self.dameraulevenshtein_mock.laske_levensthein_etaisyys.return_value = [
            [1, 2], [3, 4]]
        self.sanastopalvelu.laske_editointietaisyydet("1", "2")
        self.assertEqual(
            self.dameraulevenshtein_mock.laske_damerau_levensthein_etaisyys.call_count, 1)
        self.assertEqual(
            self.dameraulevenshtein_mock.laske_levensthein_etaisyys.call_count, 1)

# Testataan sanastopalvelua oikeilla riippuvuuksilla,
# mutta käytetään rajattua testisanastoa lukematta sanasto-tiedostoa


class TestSanastopalveluTarkistaTeksti(unittest.TestCase):

    def setUp(self):
        self.sanasto = "ei sanastoa"
        self.trie = TrieSolmu()
        self.dl = DamerauLevenshtein()
        self.sanastopalvelu = Sanastopalvelu(self.trie, self.dl, self.sanasto)

        sanat = ["ok", "no", "yes", "dirt", "dirty",
                 "dirtier", "dirtiest", "representational", "well-being"]
        i = 0
        for sana in sanat:
            i += 1
            self.sanastopalvelu.trie.lisaa_sana(sana, i)

    def test_teksti_dirt_on_virheeton(self):
        self.assertEqual(self.sanastopalvelu.tarkista_teksti("dirt"), "")

    def test_kirjainkoolla_ei_ole_merkitysta_tekstin_oikeellisuuden_tarkistamisessa(self):
        self.assertEqual(self.sanastopalvelu.tarkista_teksti("DiRt"), "")

    def test_teksti_dirty_dirtier_dirtiest_on_virheeton(self):
        self.assertEqual(self.sanastopalvelu.tarkista_teksti(
            "dirty dirtier dirtiest"), "")

    def test_tekstin_dirty_dirtyer_dirtyest_kaksi_viimeista_sanaa_merkataan_virheelliseksi_ja_korjataan(self):
        self.assertEqual(self.sanastopalvelu.tarkista_teksti(
            "dirty dirtyer dirtyest"), "dirty dirtyer* dirtyest*\n\nTarkoititko:\ndirty dirtier dirtiest ?\n")

    def test_liikaa_sanaston_sanoista_eroavia_sanoja_ei_yritetä_korjata(self):
        self.assertEqual(self.sanastopalvelu.tarkista_teksti(
            "ylioppilastutkintotodistus ja ylioppilastutkintolautakunta"),
            "ylioppilastutkintotodistus* ja* ylioppilastutkintolautakunta*\n\nTarkoititko:\nylioppilastutkintotodistus* ok ylioppilastutkintolautakunta* ?\n")

# Testataan sanastopalvelun sanaston lukua


class TestSanastopalveluLueSanasto(unittest.TestCase):
    # classmethodin avulla sanasto luetaan vain kerran
    @classmethod
    def setUpClass(cls):
        cls.sanasto = "../vocabulary/english3.txt"
        cls.trie = TrieSolmu()
        cls.dl = DamerauLevenshtein()
        cls.sanastopalvelu = Sanastopalvelu(cls.trie, cls.dl, cls.sanasto)
        cls.sanastopalvelu.lue_sanasto()

    def test_lue_sanasto_kutsun_jalkeen_trie_tietorakenne_ei_tyhja(self):
        self.assertNotEqual(len(self.sanastopalvelu.trie.lapset), 0)

    def test_lue_sanasto_kutsun_jalkeen_trie_tietorakenteen_juuressa_oikea_maara_haaroja(self):
        # eli englanninkieliset aakkoset
        # print(len(self.sanastopalvelu.trie.lapset))
        # for kirjain in self.sanastopalvelu.trie.lapset:
        #     print(kirjain)
        self.assertEqual(len(self.sanastopalvelu.trie.lapset), 26)

    def test_lue_sanaston_jalkeen_trie_tietorakenteessa_on_sanaston_ensimmainen_sana_a(self):
        self.assertEqual(self.sanastopalvelu.tarkista_teksti("a"), "")
        self.assertTrue(self.sanastopalvelu.trie.onko_sana_olemassa("a"))

    def test_lue_sanaston_jalkeen_trie_tietorakenteessa_on_sanaston_viimeinen_sana_zythum(self):
        self.assertEqual(self.sanastopalvelu.tarkista_teksti("zythum"), "")
        self.assertTrue(self.sanastopalvelu.trie.onko_sana_olemassa("zythum"))

    def test_lue_sanaston_jalkeen_trie_tietorakenteessa_ei_ole_sanastoon_kuulumattomia_sanoja(self):
        self.assertFalse(
            self.sanastopalvelu.trie.onko_sana_olemassa("ohjelmointi"))
        self.assertFalse(
            self.sanastopalvelu.trie.onko_sana_olemassa("123"))
        self.assertFalse(
            self.sanastopalvelu.trie.onko_sana_olemassa("kekkonen"))
