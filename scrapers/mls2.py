import datetime

from soccerdata.utils import scrape_soup, get_contents, pounds_to_kg, inches_to_cm
from soccerdata.cache import data_cache, set_cache


# Scraping for new style mls games.


def scrape_game_roster(url):
        soup = scrape_soup(url, fix_tags=True, refresh=True)
        import pdb; pdb.set_trace()

        return []
    








if __name__ == "__main__":
    scrape_game_roster('http://www.mlssoccer.com/matchcenter/2012-04-01-col-v-chi/rosters')
