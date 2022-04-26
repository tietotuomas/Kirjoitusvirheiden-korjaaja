from ui.ui import UI
from datastructures.trie import TrieSolmu
from services.vocabulary_service import Sanastopalvelu
from services.damerau_levenshtein import DamerauLevenshtein


def main():
    sanasto = "../vocabulary/modified_wiktionary.txt"
    trie = TrieSolmu()
    damerau_levenshtein = DamerauLevenshtein()
    sanasto_palvelu = Sanastopalvelu(trie, damerau_levenshtein, sanasto)
    kayttoliittyma = UI(sanasto_palvelu)
    kayttoliittyma.kaynnista()


if __name__ == '__main__':
    main()
