
import re

from soccerdata.utils import scrape_soup, get_contents

# List of all players.


def scrape_player_urls():
    generic_scrape_player_urls('http://nasljerseys.com/Players/Players_Roster.htm')


def scrape_indoor_player_urls():
    generic_scrape_player_urls('http://nasljerseys.com/MISL/Players/MISL_Roster.htm')

def generic_scrape_player_urls()url:
    """
    Scrape all player urls located at a given url.
    """

    soup = scrape_soup(url)
    table = soup.find("table", "MsoTableGrid")

    urls = []
    for e in table.findAll('a'):
        try:
            urls.append(e['href'])
        except KeyError:
            print e

    root_url = url.rsplit('/', 1)[0]

    return ["%s/%s" % (root_url, e) for e in urls]


def scrape_player_bios():
    l = []
    for url in scrape_player_urls():
        bio = scrape_player_bio(url)
        if bio:
            l.append(bio)
    return l



def scrape_player_bio(url):
    soup = scrape_soup(url)
    t = soup.find("table", "PlayersName")
    if not t:
        t = soup.find("table", "MsoTableGrid")

    name = t.find("td").contents[0]
    try:
        born_string = t.find("td").contents[3].contents[0]
    except:
        import pdb; pdb.set_trace()
    born_string = born_string.replace("Born:", '')
    if not born_string.strip():
        return {}

    r = re.match("(?P<location>.*?)(?P<date>\w+ \d+, \d+)", born_string)
    if r:
        print r.groups()
    else:
        print "NO MATCH %s" % url


if __name__ == "__main__":
    #print scrape_player_bio('http://www.nasljerseys.com/Players/W/West.Alan.htm')
    print scrape_player_bios()
