#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime
import json
import re

from soccerdata.utils import get_contents, scrape_url

# This, like RSSSF, is sort of on the border between text scrapers and html scrapers
# Since they don't need anything from the scrapers field, however (since scrape_url is in
# utils), they should probably be in text.
# Should probably also change the name of scrape_url

# FIXME
# Need tests IN PARTICULAR for wiki to verify that it's 
# scraping different formats correctly.

# This is probably a better url pattern to use!
# This does not display any navigation, just the article text.
# http://en.wikipedia.org/w/index.php?action=render&title=Helsinki


#OH SHIT NEW WIKI SCRAPING ON THE WAY.

def scrape_new(query):
    url = 'http://en.wikipedia.org/w/api.php?format=json&action=query&titles=%s&rvprop=content&prop=revisions' % query
    response = json.loads(scrape_url(url))
    revisions = response['query']['pages'].keys()
    assert len(revisions) == 1
    revision = revisions[0]
    text = response['query']['pages'][revision]['revisions'][0]['*']
    lines = text.split('\n')

    rm = re.search("#REDIRECT\s+\[\[(?P<link>.*?)\]\]", lines[0])
    if rm:
        return scrape_new(rm.groups()[0])


    return lines

def get_infobox_lines(lines):
    start = end = None
    for i, line in enumerate(lines):
        if not start and re.match("\s*{{\s*[Ii]nfobox", line) :
            start = i
        if not end and re.match("\s*}}", line):
            end = i
    return lines[start:end]

def process_key_value(line):
    if not line.startswith("|"):
        return None

    line = line[1:]

    k = line.split("=", 1)[0].strip()
    v = process_value(line.split("=", 1)[1])

    return (k, v)

def process_value(value):
    # seems like there are at least three kinds of lines.
    # 1. raw data.
    # 2. templates
    # 3. links (with alternate names sometimes)
    # 4. hybrid.

    value = value.strip()

    # [[Santiago Bernab\xe9u Stadium|Estadio Santiago Bernab\xe9u]]
    link_m = re.match("\[\[(?P<link>.*?)\|.*?\]\]$", value)
    if link_m:
        link_name = link_m.groups()[0]
        processed = link_name.replace(" ", "_")
        return {
            'link': processed,
            }


    link_m2 = re.match("\[\[(?P<link>.*?)\]\]$", value)
    if link_m2:
        link_name = link_m2.groups()[0]
        processed = link_name.replace(" ", "_")
        return {
            'link': processed,
            }




    date_re = re.search("Start date and years ago\|(?P<year>\d+)\|(?P<month>\d+)\|(?P<day>\d+)", value)
    if date_re:
        year, month, day = [int(e) for e in date_re.groups()]
        return datetime.datetime(year, month, day)


    date_re2 = re.search("{{birth date and age\|(?P<year>\d+)\|(?P<month>\d+)\|(?P<day>\d+)", value)
    if date_re2:
        year, month, day = [int(e) for e in date_re2.groups()]
        return datetime.datetime(year, month, day)

    # Can't figure this one out.
    height_re = re.match("{{height|m=(?P<m>\d+)\.\d+}}", value)
    if height_re:        
        return value
        m, cm = [int(e) for e in height_re.groups()]
        return cm + (100 * m)
    
                             



    # ' Real Madrid Club de F\xfatbol<ref name="Real Madrid Club de F\xfatbol"/>
    ref_m = re.search("(?P<text>.*?<.*?>)", value)
    if ref_m:
        return ref_m.groups()[0].strip()


    return value.strip()
        



def get_categories(lines):
    categories = []
    for line in lines:
        m = re.match("\[\[Category:\s*(?P<name>.*?)\]\]", line)
        if m:
            category = m.groups()[0].strip()
            categories.append(category)
    return categories



        
        
        




def scrape_list(url):
    return []

def scrape_team(url):
    lines = scrape_new(url)
    infobox_lines = get_infobox_lines(lines)
    processed = [process_key_value(line) for line in infobox_lines]
    d = dict([e for e in processed if e])
    
    return {
        'name': d['clubname'],
        'image': d['image'],
        'fullname': d['fullname'],
        'founded': d['founded'],
        'ground': d['ground'],
        'website': d['website'],
        }

def scrape_stadium(url):
    return {
        'fullname': stadium_name,
        'name': name,
        'image': image,
        'location': location,
        'coordinates': coordinates,
        'opened': opened,
        'closed': closed,
        'dimensions': dimensions,
        'architect': architect,
        'cost': cost,
        'tenants': tenants,
        'capacity': capacity,
        }


def scrape_person(url):
    lines = scrape_new(url)
    infobox_lines = get_infobox_lines(lines)
    processed = [process_key_value(line) for line in infobox_lines]
    d = dict([e for e in processed if e])

    if not d:
        print url
        return

    if 'pronunciation' in d:
        return


    try:
        name = d.get('playername') or d.get('name') or d['fullname']
        birthdate = d.get('dateofbirth') or d['birth_date']
        birthplace = d.get('cityofbirth') or d.get('birth_place') or d['countryofbirth']
    except:
        import pdb; pdb.set_trace()

    try:
        return {
        'name': name,
        'full_name': d.get('fullname') or d['name'],
        'image': d['image'],
        'birthdate': birthdate,
        'birthplace': birthplace,
        'height': d['height'],
        'position': d['position'],
        }

    except:
        import pdb; pdb.set_trace()
        x = 5


def scrape_list(url):
    lines = [e for e in lines if line != '|-']
    header = '!Rank!!Stadium!!Capacity!!City!!Country!!Home Team(s)'
    header = header.split('!!')
    l = []
    for line in lines:
        line = line.replace("|=", "")
        attrs = line.split("||")
        d = dict(zip(header, attrs))
        l.append(d)
    return l


def scrape_competition(url):
    x = {
        'logo': logo,
        'founded': founded,
        'region': region,
        }
    return {
        'title': title,
        'year': year,
        'num_teams': num_teams,
        'champions': champions,
        'runner-up': runner_up,
        }




def scrape_category_page(url):
    pass
        

def sc():
    return get_categories(scrape_new("Jason_Kreis"))
        

    
# This ain't good.    


world_cup_years = [
    1930,
    1934,
    1938,
    1950,
    1954,
    1958,
    1962,
    1966,
    1970,
    1974,
    1978,
    1982,
    1986,
    1990,
    1994,
    1998,
    2002,
    2006,
    2010,
    ]






def scrape_player_tables(url):
    data = scrape_url(url)

    # This obviously won't work on other pages...
    data = data.split("Rosters include reserves, alternates, and preselected")[0]
    soup = BeautifulSoup(data)

    tables = soup.findAll('table')
    nested_tables = [e.find('table') for e in tables]
    nested_tables = [e for e in nested_tables if e]

    l = []
    for e in nested_tables:
        l.extend(scrape_player_table(e))
    return l
    
def scrape_player_table(soup):


    def process_row(tr):
        # Would be a very good idea to pull the url out, if possible.
        # Would be nice to pull the url out,
        # but hard to figure out which is the player url.
        # [e['href'] for e in tr.findAll("a")]

        # Header row.
        if tr.find("th"):
            return {}

        tds = [get_contents(e) for e in tr.findAll("td")]
        fields = [unicode(e) for e in tds if e.strip()]

        # I'm not confident that this is 
        # going to reliably return the best
        # answer.

        birthdate = None
        
        # Obviously not the tables we're looking for.
        if len(fields) in [0, 1, 2]:
            print fields
            return {}

        elif len(fields) == 3:
            _, name, club = fields
        
        elif len(fields) == 4:
            _, _, name, club = fields


        elif len(fields) == 5:
            _, _, name, birthdate, club = fields

        elif len(fields) == 6:
            _, _, name, birthdate, caps, club = fields

        elif len(fields) == 7:
            _, _, name, birthdate, caps, goals, club = fields

        else:
            import pdb; pdb.set_trace()

        return {
            'name': name,
            'birthdate': birthdate,
            }
        
    trs = soup.findAll("tr")    
    players = [process_row(tr) for tr in trs]
    return [e for e in players if e]


def scrape_world_cup_players():
    # Need to get player urls!
    l = []
    for year in world_cup_years:
        url = 'http://en.wikipedia.org/wiki/%s_FIFA_World_Cup_squads' % year
        players = scrape_player_tables(url)
        l.extend(players)
    return l
        




#
# Old code for scraping mls players.
# can be used for scraps then discarded.    

# I do like this header.
# req.add_header('User-Agent', "Chores/1.0 +http://www.socceroutsider.com")


letters = "abcdefghijklmnopqrstuvwxyz"

def clean_html(text):
    return get_contents(text).replace("&#160;", " ")


# This seems to just be a wikipedia player scraper, which should be in wiki.py
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
            return get_contents(value)
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

