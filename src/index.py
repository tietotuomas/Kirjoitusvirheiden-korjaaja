from ui.ui import UI
from services.vocabulary_service import Tiedostonlukija

def main():
    sanasto_palvelu = Tiedostonlukija()
    kayttoliittyma = UI(sanasto_palvelu)
    kayttoliittyma.kaynnista()



if __name__=='__main__':
    main()