from ui.ui import UI
from services.vocabulary_service import Sanastopalvelu

def main():
    sanasto_palvelu = Sanastopalvelu()
    kayttoliittyma = UI(sanasto_palvelu)
    kayttoliittyma.kaynnista()

if __name__=='__main__':
    main()