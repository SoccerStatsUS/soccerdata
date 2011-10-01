import bson
import pymongo
import random
import requests
import time
import urllib2

from BeautifulSoup import BeautifulSoup


# This should be implemented with redis instead of mongo!
# Automate installation of mongo and redis?
# Document!

# Turn this into cacheing infrastructure.

connection = pymongo.Connection()

# Should be connection.cache
scraper_db = connection.scraper

cache_db = connection.cache

# Should be db.page_cache

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


def dict_to_str(d):
    opts = ["%s=%s" % (str(k), str(v)) for (k, v) in d.items()]
    return "?" + "&".join(opts)


def set_cache(cache_id, value):
    """
    Don't scrape this url. Use this value instead.
    """
    cache_db.data_cache.insert({
            "cache_id": cache_id,
            "value": value
            })



def get_cache(cache_id):
    d = cache_db.data_cache.find_one({
            'cache_id': cache_id
            })
    if d:
        return d['value']
    return None
                                    
    


#def scrape_post(url, options_dict):
def scrape_post():
    # Scrape a post url.
    # This doesn't really make sense, but this is how
    # Mediotiempo does it.

    url = 'http://www.mediotiempo.com/ajax/ajax_jornadas.php'

    options_dict = {
        'id_liga' :1,
        'id_torneo':303,
        'jornada':6,
        }

    options_string = dict_to_str(options_dict)


    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', USER_AGENT)]
    data = opener.open(url, options_string).read()

    # Oh no more shit.
    # This is from mediotiempo.com/ajax/ajax_jornadas.php?id_liga=1&id_torneo=229&jornada=5
    # Tired of struggling with mediotiempo so I'm skipping over it for now.
    # But definitely need to address these problems.
    data = data.replace("\xed", "")

    
    return data

def scrape_post_soup():
    data = scrape_post()
    return BeautifulSoup(data)




def scrape_url(url, refresh=False, encoding=None, sleep=0):
    """
    Scrape a url, or just use a version saved in mongodb.
    """
    # Might want to allow a list of encodings.
    if encoding is None:
        encoding = 'utf-8'

    # Should be cache_db.page_cache
    pages_collection = scraper_db.pages


    if refresh is False:
        result = pages_collection.find_one({"url": url })
    else:
        result = None

    if result is None:
        time.sleep(sleep)
        print "downloading %s" % url
        # Work on this logic.
        
        # Requests is not returning correct data.
        # e.g. http://www.fifa.com/worldcup/archive/edition=84/results/matches/match=3051/report.html
        # gets trash back.
        #data = requests.get(url, headers=[('User-Agent', USER_AGENT)]).read()

        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', USER_AGENT)]
        data = opener.open(url).read()

        # Mediotiempo taught us these, but they're possibly used other places.
        # This seems to show up several places, usually in document.writes.
        # I think it's addressing an internet explorer bug.
        data = data.replace("</scr'+'ipt>", "</script>")
        data = data.replace("</scr' + 'ipt", "</script")
        data = data.replace("</scr'+'ipt>", "</script>")
        data = data.replace("</SCRI' + 'PT>", "</SCRIPT>")


        # Oh shit! There was some bad unicode data in eu-football.info
        # Couldn't find an encoding so I'm just killing it.
        # Looked to be involved with goolge analytics.
        data = data.replace("\xf1\xee\xe7\xe4\xe0\xed\xee", "")

        # Save the data.
        unicode_data = data.decode(encoding)
        pages_collection.insert({"url": url, "data": unicode_data})
    else:
        print "pulling %s from cache." % url
        unicode_data = result['data']
    return unicode_data

# Bad idea.
def scrape_soup(*args, **kwargs):
    html = scrape_url(*args, **kwargs)
    return BeautifulSoup(html)



class SelfRegulatingScraper(object):
    def __init__(self, url_list):
        # What if we don't want to use a list?
        self.url_list = url_list
        self.visited_urls = set()

    def scrape_url():
        random.choice(url_list)
