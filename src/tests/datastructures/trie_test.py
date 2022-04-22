import unittest
from datastructures.trie import TrieSolmu


class TestTrieEmpty(unittest.TestCase):

    def setUp(self):
        self.trie = TrieSolmu()

    def test_konstruktori_luo_tyhjan_juuren(self):
        self.assertIsInstance(self.trie.lapset, dict)
        self.assertEqual(len(self.trie.lapset), 0)

    def test_konstruktorin_kutsumisen_jalkeen_sana_attribuutti_on_tyhja(self):
        self.assertIsNone(self.trie.sana)

    def test_konstruktorin_kutsumisen_jalkeen_sijoitus_attribuutti_on_tyhja(self):
        self.assertIsNone(self.trie.sijoitus)

    def test_lisaa_sana_tallentaa_sanan_oikein(self):
        self.trie.lisaa_sana("word", 1)
        self.assertIn('w', self.trie.lapset)
        # yksi haara, w
        self.assertEqual(1, len(self.trie.lapset))
        self.assertEqual(self.trie.lapset['w'].lapset['o'].lapset['r'].lapset['d'].sana, "word")
        self.assertEqual(self.trie.lapset['w'].lapset['o'].lapset['r'].lapset['d'].sijoitus, 1)

    def test_onko_sana_olemassa_palauttaa_true_lisatylle_sanalle(self):
        self.trie.lisaa_sana("word", 1)
        self.assertTrue(self.trie.onko_sana_olemassa("word"))

    def test_onko_sana_olemassa_palauttaa_false_lisaamattomalle_sanalle(self):
        self.assertFalse(self.trie.onko_sana_olemassa("word"))
        self.trie.lisaa_sana("word", 1)
        self.assertFalse(self.trie.onko_sana_olemassa("nonexistent"))


class TestTrieFilled(unittest.TestCase):

    def setUp(self):
        self.trie = TrieSolmu()
        sanat = ["ok", "no", "yes", "dirt", "dirty",
                 "dirtier", "dirtiest", "representational", "well-being"]
        i = 0
        for sana in sanat:
            i += 1
            self.trie.lisaa_sana(sana, i)

    def test_sana_ok_on_olemassa(self):
        self.assertTrue(self.trie.onko_sana_olemassa("ok"))

    def test_sana_dirt_on_olemassa(self):
        self.assertTrue(self.trie.onko_sana_olemassa("dirt"))

    def test_sana_dirty_on_olemassa(self):
        self.assertTrue(self.trie.onko_sana_olemassa("dirty"))

    def test_sana_well_being_on_olemassa(self):
        self.assertTrue(self.trie.onko_sana_olemassa("well-being"))

    def test_sana_application_ei_ole_olemassa(self):
        self.assertFalse(self.trie.onko_sana_olemassa("application"))

    def test_sana_dir_ei_ole_olemassa(self):
        self.assertFalse(self.trie.onko_sana_olemassa("dir"))

    def test_sana_dirtyer_ei_ole_olemassa(self):
        self.assertFalse(self.trie.onko_sana_olemassa("dirtyer"))

    def test_tyhja_merkkijono_ei_ole_olemassa(self):
        self.assertFalse(self.trie.onko_sana_olemassa(""))
