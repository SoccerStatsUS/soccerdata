#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup, HTMLParseError
import cPickle
import datetime
import logging
import os
import time
import urllib2

from soccer.utils import get_contents

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
    """
    player = {
        "name": "Cristiano Ronaldo",
        "birthdate": "5 February 1985",
        "birthplace": "Funchal, Madeira, Portugal",
        "height": "1.86 m (6 ft 1 in)",
        }


    # Need to swap out directory for mongo.
    DATA_DIR = '/home/chris/www/soccer/data/bios/'
    FILE_PREFIX = None

    # Url for a player
    PLAYER_URL = None
    
    # Url for a game
    GAME_URL = None

    # Logger.
    LOGGER = logger

    def __init__(self):
        pass

    
    # These should use mongo.
    @property
    def profiles_path(self):
        return os.path.join(self.DATA_DIR, '%s.%s' % (self.FILE_PREFIX, 'profiles'))

    @property
    def stats_path(self):
        return os.path.join(self.DATA_DIR, '%s.%s' % (self.FILE_PREFIX, 'stats'))
    
    @property
    def max_path(self):
        return os.path.join(self.DATA_DIR, '%s.%s' % (self.FILE_PREFIX, 'max'))


    # Why not just use a python lock object instead of these four items.
    def lock_path(self, type):
        return os.path.join(self.DATA_DIR, '%s.%s.%s' % (self.FILE_PREFIX, type, 'lock'))

    def is_locked(self, type):
        return os.path.exists(self.lock_path(type))

    def create_lock(self, type):
        f = open(self.lock_path(type), 'w')
        f.close()

    def unlock(self, type):
        os.remove(self.lock_path(type))


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


    # I don't think these are necessary anymore.
    def load_profiles(self):
        if os.path.isfile(self.profiles_path):
            f = open(self.profiles_path)
            d = cPickle.load(f)
            f.close()
            return d
        else:
            return {}

    def save_profiles(self, d):
        d1 = self.load_profiles()
        f = open(self.profiles_path, 'w')
        d1.update(d)
        cPickle.dump(d1, f)
        f.close()

    def load_stats(self):
        if os.path.isfile(self.stats_path):
            f = open(self.stats_path)
            d = cPickle.load(f)
            f.close()
            return d
        else:
            return {}

    def save_stats(self, d):
        d1 = self.load_profiles()
        f = open(self.stats_path, 'w')
        d1.update(d)
        cPickle.dump(d1, f)
        f.close()
    

    # What is the point of search_profiles?
    # Instead of inserting or something rather safe, it's
    # just keeping all of profiles in memory and saving them periodically.
    # There's really no need for any of this stuff.
    def search_profiles(self, count=300):
        """
        """

        if self.is_locked('bio'):
            return

        # Get created profiles and stats.
        self.create_lock('bio')
        profiles = self.load_profiles()
        stats = self.load_stats()
        
        start = self.get_max()
        end = start + count
        
        # Search for x profiles 
        i = 0
        print "processing from %s to %s" % (start, end)
        for num in range(start, end):
            i += 1
            time.sleep(1.5)
            
            try:
                # Fetch the page.
                soup = self.open_bio(num)
                # Parse the data.
                scraped = self.scrape_player(soup)
                # Save the data and try to scrape the stats.
                # Possibly separate the scraping part.
                if 'name' in scraped:
                    profiles[num] = scraped
                    s = self.scrape_stats(soup)
                    if s:
                        stats[num] = s
                        
            except HTMLParseError:
                print "Couldn't parse %s" % num
                logger.debug("%s couldn't parse %s" % (self.FILE_PREFIX, num))
            except urllib2.HTTPError:
                print "Received HTTP Error for %s" % num
                logger.error("%s received HTTP Error for %s" % (self.FILE_PREFIX, num))
                self.unlock('bio')
                return d

            # Save profiles every twenty fifth item.
            # Why not just save every item?
            if i % 25 == 0:
                current = start + i
                print "Downloading %s" % (current)
                self.set_max(current)
                self.save_profiles(profiles)
                self.save_stats(stats)

        # Save at the end of processing.
        self.set_max(end)
        self.save_profiles(profiles)
        self.save_stats(stats)
        self.unlock('bio')


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
        

    
