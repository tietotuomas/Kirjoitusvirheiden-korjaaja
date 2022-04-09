import unittest
from services.vocabulary_service import Sanastopalvelu
from services.trie import TrieSolmu


class TestSanastopalvelu(unittest.TestCase):

    def setUp(self):
        self.sanastopalvelu = Sanastopalvelu()

    def test_konstruktori_luo_trie_tietorakenteen(self):
        self.assertIsInstance(self.sanastopalvelu.trie, TrieSolmu)

    def test_konstruktori_kutsun_jalkeen_trie_tietorakenne_on_tyhja(self):
        self.assertEqual(len(self.sanastopalvelu.trie.lapset), 0)


class TestSanastopalveluTarkistaTeksti(unittest.TestCase):

    def setUp(self):
        self.sanastopalvelu = Sanastopalvelu()
        sanat = ["123", "ok", "yes", "no", "dirt", "dirty",
                 "dirtier", "dirtiest", "jeff", "bezos"]
        for sana in sanat:
            self.sanastopalvelu.trie.lisaa_sana(sana)

    def test_teksti_dirt_on_virheeton(self):
        self.assertEqual(self.sanastopalvelu.tarkista_teksti("dirt"), "")

    def test_kirjainkoolla_ei_ole_valia_tekstin_oikeellisuuden_tarkistamisessa(self):
        self.assertEqual(self.sanastopalvelu.tarkista_teksti("DiRt"), "")

    def test_teksti_dirty_dirtier_dirtiest_on_virheeton(self):
        self.assertEqual(self.sanastopalvelu.tarkista_teksti(
            "dirty dirtier dirtiest"), "")

    def test_tekstin_dirty_dirtyer_dirtyest_kaksi_viimeista_sanaa_merkataan_virheelliseksi_ja_korjataan(self):
        self.assertEqual(self.sanastopalvelu.tarkista_teksti(
            "dirty dirtyer dirtyest"), "dirty dirtyer* dirtyest*\n\nTarkoititko:\ndirty dirtier dirtiest ?\n")

    def test_tekstin_hello_world_sanat_merkataan_virheelliseksi_mutta_ei_korjata(self):
        self.assertEqual(self.sanastopalvelu.tarkista_teksti(
            "hello world"), "hello* world*\n\nTarkoititko:\nhello* world* ?\n")

class TestSanastopalveluLueSanasto(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sanastopalvelu = Sanastopalvelu()
        cls.sanastopalvelu.lue_sanasto()

    def test_lue_sanasto_kutsun_jalkeen_trie_tietorakenne_ei_tyhja(self):
        self.assertNotEqual(self.sanastopalvelu.trie, {})

    def test_lue_sanasto_kutsun_jalkeen_trie_tietorakenteen_juuressa_oikea_maara_haaroja(self):
        # eli englanninkieliset aakkoset

        # print(len(self.sanastopalvelu.trie.lapset))
        # for kirjain in self.sanastopalvelu.trie.lapset:
        #     print(kirjain)
        self.assertEqual(len(self.sanastopalvelu.trie.lapset), 26)

    def test_lue_sanaston_jalkeen_trie_tietorakenteessa_on_sanaston_ensimmainen_sana_a(self):
        self.assertEqual(self.sanastopalvelu.tarkista_teksti("a"), "")
        self.assertTrue(self.sanastopalvelu.trie.onko_sana_olemassa("a"))

    def test_lue_sanaston_jalkeen_trie_tietorakenteessa_on_sanaston_viimeinen_sana_zzz(self):
        self.assertEqual(self.sanastopalvelu.tarkista_teksti("zythum"), "")
        self.assertTrue(self.sanastopalvelu.trie.onko_sana_olemassa("zythum"))

    def test_lue_sanaston_jalkeen_trie_tietorakenteessa_ei_ole_sanastoon_kuulumatonta_sanaa_ohjelmointi(self):
        self.assertFalse(self.sanastopalvelu.trie.onko_sana_olemassa("ohjelmointi"))
