from cnnsi import CNNSIPlayerScraper
from nbcsports import NBCSportsPlayerScraper
from soccernet import SoccernetPlayerScraper
from soccerbase import SoccerbasePlayerScraper


def load_profiles(source):
    d = {
        'cnnsi': CNNSIPlayerScraper,
        'nbcsports': NBCSportsPlayerScraper,
        'soccernet': SoccernetPlayerScraper,
        'soccerbase': SoccerbasePlayerScraper,
        }
    if source in d:
        scraper = d[source]()
        return scraper.load_profiles()
    else:
        raise
        
