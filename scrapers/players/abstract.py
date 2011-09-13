#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup, HTMLParseError
import cPickle
import datetime
import logging
import os
import time
import urllib2

LOG_DIR = "/home/chris/www/soccer/logs"
LOG_FORMAT = "%(asctime)s\t%(process)d\t%(levelname)s\t%(filename)s\t%(message)s"

logger = logging.getLogger('scraper')
logger.setLevel(logging.DEBUG)

to_file = logging.FileHandler(
    os.path.join(LOG_DIR, 'scraper'))
to_file.setFormatter(logging.Formatter(LOG_FORMAT))

logger.addHandler(to_file)


def get_contents(l):
    if not hasattr(l, 'contents'):
        s = l
    else:
        s = ""
        for e in l.contents:
            s += get_contents(e)
    return s.strip()



class AbstractGameScraper(object):

    def __init__(self):
        pass


class AbstractPlayerScraper(object):
    DATA_DIR = '/home/chris/www/soccer/data/bios/'
    FILE_PREFIX = None
    PLAYER_URL = None
    GAME_URL = None
    LOGGER = logger

    def __init__(self):
        pass

    @property
    def profiles_path(self):
        return os.path.join(self.DATA_DIR, '%s.%s' % (self.FILE_PREFIX, 'profiles'))

    @property
    def stats_path(self):
        return os.path.join(self.DATA_DIR, '%s.%s' % (self.FILE_PREFIX, 'stats'))
    
    @property
    def max_path(self):
        return os.path.join(self.DATA_DIR, '%s.%s' % (self.FILE_PREFIX, 'max'))


    # Why not just use a python lock object?
    def lock_path(self, type):
        return os.path.join(self.DATA_DIR, '%s.%s.%s' % (self.FILE_PREFIX, type, 'lock'))

    def is_locked(self, type):
        return os.path.exists(self.lock_path(type))

    def create_lock(self, type):
        f = open(self.lock_path(type), 'w')
        f.close()

    def unlock(self, type):
        os.remove(self.lock_path(type))


    def get_max(self):
        if os.path.isfile(self.max_path):
            return int(open(self.max_path).read())
        else:
            return 0

    def set_max(self, num):
        f  = open(self.max_path, 'w')
        f.write(str(num))
        f.close()

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
    
    def search_profiles(self, count=300):
        if self.is_locked('bio'):
            return

        self.create_lock('bio')
        profiles = self.load_profiles()
        stats = self.load_stats()
        
        start = self.get_max()
        end = start + count
        
        i = 0
        print "processing from %s to %s" % (start, end)
        for num in range(start, end):
            i += 1
            time.sleep(1.5)
            try:
                soup = self.open_bio(num)
                scraped = self.scrape_player(soup)
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

            if i % 25 == 0:
                current = start + i
                print "Downloading %s" % (current)
                self.set_max(current)
                self.save_profiles(profiles)
                self.save_stats(stats)

        self.set_max(end)
        self.save_profiles(profiles)
        self.save_stats(stats)
        self.unlock('bio')

    def scrape_player(self, soup):
        return NotImplementedError

    def scrape_stats(self, soup):
        return None


    def clean_list(self, l):
        return [e.strip() for e in l if e.strip()]        

    def preprocess_bio_html(self, html):
        return html

    def preprocess_game_html(self, html):
        return html.replace('&nbsp;', '')

    def open_bio(self, id):
        url = self.PLAYER_URL % id
        html = urllib2.urlopen(url).read()
        nhtml = self.preprocess_bio_html(html)
        return BeautifulSoup(nhtml)    

    def open_game_page(self, id):
        url = self.GAME_URL % id
        html = urllib2.urlopen(url).read()
        nhtml = self.preprocess_game_html(html)
        return BeautifulSoup(nhtml)
        

    
