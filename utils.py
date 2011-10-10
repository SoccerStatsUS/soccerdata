import leveldb
import random
import time
import urllib2

from BeautifulSoup import BeautifulSoup

db = leveldb.LevelDB("/home/chris/leveldb/page")

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.A.B.C Safari/525.13'


def pounds_to_kg(pounds):
    if not pounds:
        return ''

    if pounds == '?':
        return ''

    kg = int(pounds) * 0.45359237
    return int(round(kg, 0))


def inches_to_cm(inches=0, feet=0):
    if not inches and not feet:
        return ''

    if inches == '?' or feet == '?':
        return ''

    feet, inches = int(feet), int(inches)
    real_inches = inches + (feet * 12)
    cm = real_inches * 2.54
    return int(round(cm, 0))


def get_contents(l, formatter=lambda s: s):
    """
    Fetch the contents from a soup object.
    """
    # We seem to be losing some spaces with this function.
    # Would be nice to turn br's into newlines.
    # cf. 

    if not hasattr(l, 'contents'):
        s = l
    else:
        s = ""

        for e in l.contents:
            s += get_contents(e)
    return formatter(s.strip())


def dict_to_str(d):
    """
    Parse url options, basically.
    """
    opts = ["%s=%s" % (str(k), str(v)) for (k, v) in d.items()]
    return "?" + "&".join(opts)


# Scrapers


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




def scrape_url(url, refresh=False, encoding=None, sleep=5):
    """
    Scrape a url, or just use a version saved in mongodb.
    """
    # Might want to allow a list of encodings.
    if encoding is None:
        encoding = 'utf-8'

    # Should be connection.cache
    data = None
    if refresh is False:
        try:
            print "pulling %s from page cache" % url
            data = db.Get(url)
        except KeyError:
            pass

    if data is None:
        time.sleep(sleep)
        print "downloading %s" % url
        # Work on this logic.


        
        # Requests is not returning correct data.
        # e.g. http://www.fifa.com/worldcup/archive/edition=84/results/matches/match=3051/report.html
        # gets trash back.
        #data = requests.get(url, headers=[('User-Agent', USER_AGENT)]).read()

        print "pulling %s from page cache." % url
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', USER_AGENT)]
        data = opener.open(url).read()

        db.Put(url, data)

    # Mediotiempo taught us these, but they're possibly used other places.
    # This seems to show up several places, usually in document.writes.
    # I think it's addressing an internet explorer bug.
    data = data.replace("</scr'+'ipt>", "</script>")
    data = data.replace("</scr' + 'ipt", "</script")
    data = data.replace("</scr'+'ipt>", "</script>")
    data = data.replace("</SCRI' + 'PT>", "</SCRIPT>")

    # Missing quotation mark. (http://soccernet.espn.go.com/match?id=331193&cc=5901)
    data = data.replace('href=http', 'href="http')

    # Bad tag.
    data = data.replace("<font size=  </div>", "</div>")

    # Oh shit! There was some bad unicode data in eu-football.info
    # Couldn't find an encoding so I'm just killing it.
    # Looked to be involved with goolge analytics.
    data = data.replace("\xf1\xee\xe7\xe4\xe0\xed\xee", "")
    
    return data



def scrape_soup(*args, **kwargs):
    html = scrape_url(*args, **kwargs)
    return BeautifulSoup(html)


class SelfRegulatingScraper(object):
    # Not used.

    def __init__(self, url_list):
        # What if we don't want to use a list?
        self.url_list = url_list
        self.visited_urls = set()

    def scrape_url():
        random.choice(url_list)
