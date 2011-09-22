#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
import json
import re
import urllib2

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
    return lines

def get_infobox_lines(lines):
    start = end = None
    for i, line in enumerate(lines):
        if not start and re.match("\s*{{\s*[Ii]nfobox", line) :
            start = i
        if not end and re.match("\s*}}", line):
            end = i
    return lines[start:end]


def process_line(line):
    # seems like there are at least three kinds of lines.
    # 1. raw data.
    # 2. templates
    # 3. links (with alternate names sometimes)
    # 4. hybrid.
    pass


def process_key_value_line(line):
    if not line.startswith("|"):
        return None

    k, v = [e.strip() for e in line.split("=", 1)]
    return (k, v)


def scrape_team(url):
    return {
        'name': clubname,
        'image': image,
        'fullname': fullname,
        'founded': founded,
        'ground': ground,
        'website': website,
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


def scrape_player(url):
    return {
        'fullname': fullname,
        'name': name,
        'image': image,
        'birthdate': dateofbirth,
        'birthplace': birthplace,
        'height': height,
        'position': position,
        }


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
        
            


def get_categories(lines):
    categories = []
    for line in lines:
        m = re.match("\[\[Category:\s*(?P<name>.*?)\]\]", line)
        if m:
            category = m.groups()[0].strip()
            categories.append(category)
    return categories


def sc():
    return get_categories(scrape_new("Jason_Kreis"))
        

    
    


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


# Just some sample urls for testing wikipedia.
player_urls = [
    'Arsène_Wenger',
    'Wayne_Rooney',
    'Landon_Donovan',
    ]


def scrape_stadium(name):
    wiki_name = name.replace(" ", "_")
    url = "http://en.wikipedia.org/wiki/%s" % wiki_name
    data = scrape_url(url)
    soup = BeautifulSoup(data)
    infobox = soup.find("table", "infobox vcard")

    name = infobox.find("th", "fn org").contents[0]
    nickname = infobox.find("span", "nickname").contens[0]

    attrs = {}
    for tr in infobox.findAll("tr"):
        th = tr.find("th")
        td = tr.find("td")
        if th and td:
            key = get_contents(th).lower()
            value = get_contents(td)
            attrs[key] = value

        
    return {
        'name': name,
        'nickname': nicknamem,
        'location': attrs.get('Location'),
        'opened': attrs.get('Opened'),
        'capacity': attrs.get('Capacity'),
        }
        


def scrape_team(name):
    wiki_name = name.replace(" ", "_")
    url = "http://en.wikipedia.org/wiki/%s" % wiki_name
    data = scrape_url(url)
    soup = BeautifulSoup(data)
    infobox = soup.find("table", "infobox vcard")

    attrs = {}
    for tr in infobox.findAll("tr"):
        th = tr.find("th")
        td = tr.find("td")
        if th and td:
            key = get_contents(th).lower()
            value = get_contents(td)

            m = re.match(".*? (?P<year>\d{4}).*", value)            
            if key == "founded":
                if m:
                    value = m.groups()[0]
                else:
                    value = ''

            try:
                attrs[key] = value
            except:
                import pdb; pdb.set_trace()


    return {
        'name': attrs["full name"],
        'short_name': '',
        'city': '',
        'founded': attrs['founded'],
        'defunct': "dissolved" in attrs,
        }


def scrape_player(name):
    wiki_name = name.replace(" ", "_")
    url = "http://en.wikipedia.org/wiki/%s" % wiki_name
    data = scrape_url(url)
    soup = BeautifulSoup(data)
    infobox = soup.find("table", "infobox vcard")

    if not infobox:
        return {}

    import pdb; pdb.set_trace()

    return {}


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
        




    
