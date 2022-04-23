from ui.ui import UI
from services.vocabulary_service import Sanastopalvelu
from datastructures.trie import TrieSolmu
from datastructures.damerau_levenshtein import DamerauLevenshtein

def main():
    sanasto = "../vocabulary/200k_wiktionary_words.txt"
    trie = TrieSolmu()
    damerau_levenshtein = DamerauLevenshtein()
    sanasto_palvelu = Sanastopalvelu(trie, damerau_levenshtein, sanasto)
    kayttoliittyma = UI(sanasto_palvelu)
    kayttoliittyma.kaynnista()

if __name__=='__main__':
    main()
    