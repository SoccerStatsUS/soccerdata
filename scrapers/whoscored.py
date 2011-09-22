# Oh shit this one looks like a great source of information!

import re

from soccerdata.utils import scrape_url

from BeautifulSoup import BeautifulSoup

import pymongo

connection = pymongo.Connection()
soccer_db = connection.soccer


def pick_random(coll):
    pass


def scrape_id(player_id):
    url = 'http://www.whoscored.com/Players/%s' % player_id
    return scrape_player(url)

def scrape_player(url):
    data = scrape_url(url)
    soup = BeautifulSoup(data)
    
    info_blocks = soup.findAll("dl", "player-info-block")
    name, current_team, position, age, nationality = [e.find("dd") for e in info_blocks]
    birthdate_string = re.search("<i>(?P<birthdate>.*?)</i>", age).groups[0]
    birthdate = datetime.datetime.strptime(birthdate_string, '%d-%m-%Y')    
    
    
    
