# So far just using this for world cup data.

from BeautifulSoup import BeautifulSoup

from soccerdata.utils import scrape_url, get_contents


def scrape_world_cup_game():
    url = 'http://news.bbc.co.uk/sport2/hi/football/world_cup_2010/matches/match_38/default.stm'
    data = scrape_url(url)
    
