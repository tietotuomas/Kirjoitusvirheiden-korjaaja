import unittest
from services.trie import TrieSolmu


class TestTrieEmpty(unittest.TestCase):

    def test_konstruktori_luo_tyhjan_juuren(self):
        self.trie = TrieSolmu()
        self.assertEqual(len(self.trie.lapset), 0)

class TestTrieFilled(unittest.TestCase):

    def setUp(self):
        self.trie = TrieSolmu()
        sanat = ["123", "ok", "yes", "no", "dirt", "dirty",
                 "dirtier", "dirtiest", "jeff", "bezos"]
        for sana in sanat:
            self.trie.lisaa_sana(sana)

    def test_sana_dirt_on_olemassa(self):
        self.assertTrue(self.trie.onko_sana_olemassa("dirt"))

    def test_sana_dirty_on_olemassa(self):
        self.assertTrue(self.trie.onko_sana_olemassa("dirty"))

    def test_sana_123_on_olemassa(self):
        self.assertTrue(self.trie.onko_sana_olemassa("123"))

    def test_sana_bezos_on_olemassa(self):
        self.assertTrue(self.trie.onko_sana_olemassa("bezos"))

    def test_sana_musk_ei_ole_olemassa(self):
        self.assertFalse(self.trie.onko_sana_olemassa("musk"))

    def test_sana_dir_ei_ole_olemassa(self):
        self.assertFalse(self.trie.onko_sana_olemassa("dir"))

    def test_sana_dirti_ei_ole_olemassa(self):
        self.assertFalse(self.trie.onko_sana_olemassa("dirti"))

    def test_sana_bezoz_ei_ole_olemassa(self):
        self.assertFalse(self.trie.onko_sana_olemassa("bezoz"))
