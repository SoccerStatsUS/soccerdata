import bson
import pymongo
import random
import requests
import urllib2

from BeautifulSoup import BeautifulSoup


# These are meant to be site-wide utilities

connection = pymongo.Connection()
db = connection.scraper
collection = db.pages

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.A.B.C Safari/525.13'



# merge this.
def get_contents(l):
    """
    Fetch the contents from a soup object.
    """
    # Good recursive function.
    if not hasattr(l, 'contents'):
        s = l
    else:
        s = ""
        for e in l.contents:
            s += get_contents(e)
    return s.strip()


def scrape_url(url, static=True, encoding=None):
    """
    Scrape a url, or just use a version saved in mongodb.
    """
    # Might want to allow a list of encodings.
    if encoding is None:
        encoding = 'utf-8'

    scrape_db = connection.scraper
    pages_collection = scrape_db.pages

    if static is True:
        result = collection.find_one({"url": url })
    else:
        result = None

    if result is None:
        print "downloading %s" % url
        # Work on this logic.
        
        # Requests is not returning correct data.
        # e.g. http://www.fifa.com/worldcup/archive/edition=84/results/matches/match=3051/report.html
        # gets trash back.
        #data = requests.get(url, headers=[('User-Agent', USER_AGENT)]).read()

        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', USER_AGENT)]
        data = opener.open(url).read()
        unicode_data = data.decode(encoding)
        pages_collection.insert({"url": url, "data": unicode_data})
    else:
        print "pulling %s from cache." % url
        data = result['data']
    return data

def scrape_soup(url):
    return BeautifulSoup(scrape_url(url))



class SelfRegulatingScraper(object):
    def __init__(self, url_list):
        # What if we don't want to use a list?
        self.url_list = url_list
        self.visited_urls = set()

    def scrape_url():
        random.choice(url_list)
