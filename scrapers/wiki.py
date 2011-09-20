from BeautifulSoup import BeautifulSoup
import re
import urllib2

from soccerdata.utils import get_contents, scrape_url

# FIXME
# Need tests IN PARTICULAR for wiki to verify that it's 
# scraping different formats correctly.

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
        




    
