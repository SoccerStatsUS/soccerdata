#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


from BeautifulSoup import BeautifulSoup, HTMLParseError
import cPickle
import datetime
import logging
import os
import time
import urllib2

from soccerdata.utils import get_contents

# This logging could definitely be improved...
LOG_DIR = "/home/chris/www/soccer/logs"
LOG_FORMAT = "%(asctime)s\t%(process)d\t%(levelname)s\t%(filename)s\t%(message)s"

logger = logging.getLogger('scraper')
logger.setLevel(logging.DEBUG)

to_file = logging.FileHandler(
    os.path.join(LOG_DIR, 'scraper'))
to_file.setFormatter(logging.Formatter(LOG_FORMAT))

logger.addHandler(to_file)


# Is this doing anything?
class AbstractGameScraper(object):
    """
    What should a game look like?
    
    Currently I'm thinking something like this:

    FIXME: use this to make a real life test.
    game = {
        "date": "Aug. 17\n10 pm",
        "location": "Estadio Olímpico Universitário",
        "home_team": "Pumas UNAM (MEX)",
        "away_team": "FC Dallas (USA)",
        "home_score": "0",
        "away_score": "1",
        "competition": "CONCACAF Champions League",
        "round": "Group Stage",
        "notes": "",
        "source": "http://www.mlssoccer.com/ccl/schedule2011",
        }

    All fields would be required, except possibly round and notes.
    Sometimes it is also possible for home_score or away_score to 
    not have values, like when a game is cancelled or postponed.
    """        
    

    def __init__(self):
        pass


class AbstractPlayerScraper(object):
    # What is the purpose of the AbstractPlayerScraper?
    # Presumably it should define an interface of what constitutes
    # acceptable player information.
    # It probably doesn't need to be involved with saving any data
    # or with maintaining any knowledge of what it's supposed to be
    # scraping. That can be managed elsewhere.

    """
    What is a player?

    player = {
        "name": "Cristiano Ronaldo",
        "birthdate": "5 February 1985",
        "birthplace": "Funchal, Madeira, Portugal",
        "height": "1.86 m (6 ft 1 in)",
        }
    """


    # Url for a player
    PLAYER_URL = None
    
    # Url for a game
    GAME_URL = None

    # Logger.
    LOGGER = logger

    def __init__(self):
        pass

    
    # These should use mongo.
    # Right? Are we going to use mongo on this side? What for exactly?
    def get_max(self):
        """
        Get maximum id searched.
        """
        # Probably, rather than simply counting upward, we should define a search space
        # and access urls as semi-randomized intervals.
        if os.path.isfile(self.max_path):
            return int(open(self.max_path).read())
        else:
            return 0

    def set_max(self, num):
        """
        Set maximum id searched.
        """
        f  = open(self.max_path, 'w')
        f.write(str(num))
        f.close()

    def scrape_player(self, soup):
        """
        Given a BeautifulSoup object, returns a dict of player bio data.
        """
        raise NotImplementedError


    def scrape_stats(self, soup):
        """
        Given a BeautifulSoup object, returns a dict of player stats data.
        """
        raise NotImplementedError


    def strip_list(self, l):
        """
        Strip items in a list.
        """
        return [e.strip() for e in l if e.strip()]        


    def preprocess_bio_html(self, html):
        """
        Clean up html
        """
        return html


    def preprocess_game_html(self, html):
        """
        Clean up html
        """
        html = html.replace('&nbsp;', '')
        return html


    def open_bio(self, id):
        """
        Load bio html as a BeautifulSoup object.
        """
        url = self.PLAYER_URL % id
        html = urllib2.urlopen(url).read()
        nhtml = self.preprocess_bio_html(html)
        return BeautifulSoup(nhtml)    


    def open_game_page(self, id):
        """
        Load game html as a BeautifulSoup object.
        """
        url = self.GAME_URL % id
        html = urllib2.urlopen(url).read()
        nhtml = self.preprocess_game_html(html)
        return BeautifulSoup(nhtml)
        

    
