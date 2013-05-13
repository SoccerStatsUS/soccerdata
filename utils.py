import hashlib
import leveldb
import os
import random
import time
from urllib import urlencode
import urllib2

from BeautifulSoup import BeautifulSoup

db = leveldb.LevelDB("/home/chris/leveldb/page")

# USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.A.B.C Safari/525.13'
USER_AGENT = 'Mozilla/5.0 (Windows NT 5.1; rv:8.0; en_us) Gecko/20100101 Firefox/8.0'


def get_id():
    return hashlib.md5(str(time.time())).hexdigest()


class IDCounter(object):
    """
    A generic counter used for getting unique, sequential game id's.
    """
    
    def __init__(self):
        self.id = 1

    def get(self):
        v = self.id
        self.id += 1
        return v


def list_paths(root):
    l = []
    for dirname, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.endswith('.py') and fn != '__init__.py':
                l.append(os.path.join(dirname, fn))
    return l


def import_path(p):
    #assert p.endswith('.py')
    #m = p[:-3].replace('/', '.')

    # Use importlib instead?
    #iname = "%s.%s.%s" % (istub, region, xn)
    #m = importlib.import_module(iname)


    return __import__(p, fromlist=["dummy value"]) # __import requires non-empty fromlist to import submodules (foo.bar.baz)
        

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
def scrape_post(url, options):
    # Scrape a post url.
    # This doesn't really make sense, but this is how
    # Mediotiempo does it.

    options_string = dict_to_str(options)

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


def scrape_url(url, refresh=False, encoding=None, sleep=5, fix_tags=False, url_data={}):
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
            
            #try:
            data = db.Get(url)
            print "pulling %s from page cache" % url
            #except leveldb.LevelDBError:
            #db.Delete(url)
        except KeyError:
            pass

    if data is None:
        time.sleep(sleep)
        print "downloading %s" % url

        # Requests is not returning correct data.
        # e.g. http://www.fifa.com/worldcup/archive/edition=84/results/matches/match=3051/report.html
        # gets trash back.
        #data = requests.get(url, headers=[('User-Agent', USER_AGENT)]).read()

        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', USER_AGENT)]
        if url_data:
            post = urlencode(url_data)
            import pdb; pdb.set_trace()
            data = opener.open(url, data=post).read()
        else:
            data = opener.open(url).read()
        db.Put(url, data)

    # jesus christ.
    data = data.replace("</scr'+'ipt>", "</script>")
    data = data.replace("</scr' + 'ipt", "</script")
    data = data.replace("</scr'+'ipt>", "</script>")
    data = data.replace("</SCRI' + 'PT>", "</SCRIPT>")
    data = data.replace("</scri'+'pt>", "</script>")
    data = data.replace('"RowHeader""', '"RowHeader"')
    data = data.replace("<meta content=  </div>", "<meta></div>")
    data = data.replace("<meta charset=  </div>", "<meta></div>")
    data = data.replace("<p style=  </div>", "<p></div>")


    # Seeing this problem with mlssoccer.com for some reason.
    if fix_tags:
        data = data.replace("&lt;", '<')
        data = data.replace("&gt;", '>')


    # Missing quotation mark. (http://soccernet.espn.go.com/match?id=331193&cc=5901)
    data = data.replace('href=http', 'href="http')

    # Bad tag.
    data = data.replace("<font size=  </div>", "</div>")

    # Oh shit! There was some bad unicode data in eu-football.info
    # Couldn't find an encoding so I'm just killing it.
    # Looked to be involved with goolge analytics.
    data = data.replace("\xf1\xee\xe7\xe4\xe0\xed\xee", "")

    # http://www.mlssoccer.com/schedule?month=all&year=1996&club=all&competition_type=all
    data = data.replace('<img alt="" src="/sites/league/files/eljimador_300x100.gif" style="border: medium none; width: 300px; height: 100px;" <img', "<img")

    data = data.replace("""onclick="this.href=this.href+'?ref=espn_deportes&refkw=deportes+tickets'""", '')
    
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
