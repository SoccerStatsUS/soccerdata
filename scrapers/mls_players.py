import datetime
import itertools
import urllib2
import re

from BeautifulSoup import BeautifulSoup

from soccer.places.models import State, Country

letters = "abcdefghijklmnopqrstuvwxyz"

players_url = "http://www.mlssoccer.com/players/%s/%s"


states = [e.name for e in State.objects.all()]




def clean_html(text):
    return suppress_tags(text).replace("&#160;", " ")

def suppress_tags(b):
    s = ""
    for e in b:
        if hasattr(e, 'contents'):
            s += suppress_tags(e)
        else:
            s += e
    return s

def scrape_wiki(url):
    # Wikipedia is blocking urllib2's default header.
    # Bypass this.
    
    req = urllib2.Request(url)
    req.add_header('User-Agent', "Chores/1.0 +http://www.socceroutsider.com")
    opener = urllib2.build_opener()
    return opener.open(req).read()

class PlayerScraper(object):

    # Possible patterns that the player's birthdate could be in.
    # Scraping wikipedia can be tough.
    date_patterns = [
        "%B %d, %Y",
        "%B %d %Y",
        "%d %B, %Y",
        "%d %B %Y",
                     ]

    # Regular expression to match 1.73m, e.g.
    metric_re = re.compile("(?P<meters>\d)\.(?P<centimeters>\d+) ?m")

    def __init__(self, name):
        self.name = name
        self.info_map = self.map_infobox()

    def player_urls(self):
        u = "http://en.wikipedia.org/wiki/%s" % self.name.replace(" ", "_")
        endings = ["", "_(soccer)", "_(footballer)", "_(American_soccer)",]
        return ["%s%s" % (u, e) for e in endings]


    def get_wiki_infobox(self):
        for url in self.player_urls():
            try:
                # Have to find infobox here to avoid disambiguation pages.
                text = scrape_wiki(url)
                soup = BeautifulSoup(text)
                infobox = soup.findAll("table", {"class": "infobox vcard"})
                if infobox:
                    return infobox
            except urllib2.HTTPError:
                pass
        return ''


    def map_infobox(self):
        infobox = self.get_wiki_infobox()
        if not infobox:
            return {}

        trs = infobox[0].findAll("tr")
        d = {}
        for tr in trs:
            children = tr.findAll(["th", "td"])
            if len(children) == 2:
                try:
                    key = clean_html(children[0].contents[0])
                    value = clean_html(children[1].contents[0])
                    d[key] = value
                except IndexError:
                    # One of the key, value pair's contents was empty.
                    # Just ignore it.
                    pass
        return d


    def find_info(self):
        return [
            self.find_full_name(),
            self.find_birthdate(),
            self.find_place_of_birth(),
            self.find_height()
            ]
            
            

    def find_full_name(self):
        value = self.info_map.get("Full name")
        if value:
            return value
        else:
            return self.name

    
    def find_birthdate(self):
        def helper(data):
            for pattern in self.date_patterns:
                try:
                    s = data.strip()
                    dt = datetime.datetime.strptime(s, pattern)
                    d = datetime.date(dt.year, dt.month, dt.day)
                    return d
                except ValueError:
                    pass
            return None

        value = self.info_map.get("Date of birth")
        if value:
            return helper(value)
        else:
            return None


    def find_place_of_birth(self):
        value = self.info_map.get("Place of birth")
        if value:
            return suppress_tags(value)
        else:
            return ""

    def find_height(self):
        def helper_old(data):
            d = data.replace("(", "").replace(")", "")
            # Height is often listed in metric and imperial.
            forms = d.split(" ") 
            for f in forms:
                result = self.metric_re.search(f)
                if result:
                    m, cm = result.groups()
                    return int(m) * 100 + int(cm)

        def helper(data):
            result = self.metric_re.search(data)
            if result:
                m, cm = result.groups()
                return int(m) * 100 + int(cm)


        value = self.info_map.get("Height")
        if value:
            return helper(value)
        else:
            return 0


def get_players_from_page(url):
    text = urllib2.urlopen(url).read()
    soup = BeautifulSoup(text)
    tds = soup.findAll("td", {"class": "mpl-player active"})
    anchors = []
    for td in tds:
        anchors.extend(td.findAll("a"))
    d = {}
    for e in anchors:
        try:
            key = str(e.contents[0])
            value = str(e['href']).split("/")[-1]
            d[key] = value
        except UnicodeEncodeError:
            print str(e['href'])
    return d


def get_players():
    urls = {}
    for letter in letters:
        for n in itertools.count(1):
            url = players_url % (letter, n)
            d = get_players_from_page(url)
            urls.update(d)
            if d == {}:
                break
    return urls.items()



def scrape_person(name, slug=''):
    from soccer.players.models import Person
    usa = Country.objects.get(name="United States")
    scraped = PlayerScraper(name)
    full_name, birthdate, birthplace, height = scraped.find_info()
    p = Person(name=name, 
               mls_slug=slug, 
               height=height, 
               birthdate=birthdate,
               birthplace=birthplace,
               full_name=full_name)

    if "United States" in birthplace:
        p.nationality = usa
    for state in states:
        if state in birthplace:
            p.nationality = usa

    names = name.split(" ")
    if len(names) == 2:
        p.last_name = names[1]
    p.save()
    
    
            


    
