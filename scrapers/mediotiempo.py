# encoding: utf-8

from urllib import urlencode

from BeautifulSoup import BeautifulSoup
from soccerdata.utils import scrape_url, scrape_soup, get_contents

team_url = "http://www.mediotiempo.com/ajax/ajax_equipo.php"



def scrape_jornadas(url):
    url = 'http://www.mediotiempo.com/jornadas.php?id_liga=1&id_torneo=303'
    soup = scrape_soup(url, encoding='iso_8859_1')

    selects = soup.findAll("select")
    jornada_select = selects[1]
    jornadas = [e['value'] for e in jornada_select.findAll("option")]

    return jornadas



def scrape_player(soup):

    import pdb; pdb.set_trace()
    x = 5
    
    




"""
AAAAHHHHHHHHHHHHHHHH
MEDIOTIEMPO IS USING POSTS FOR GETS!!!
Presumably to hide that shit from you.

a typical post:

url: mediotiempo.com/ajax/ajax_jornadas.php

post = {
    'id_liga': 1 # Mexico?
    'id_torneo': 229,
    'jornada': 5,
}
"""


unicode_mapping = [
    ('Á', '&Aacute;'),
    ('á', '&aacute;'),
    ('É', '&Eacute;'),
    ('é', '&eacute;'),
    ('Í', '&Iacute;'),
    ('í', '&iacute;'),
    ('Ó', '&Oacute;'),
    ('ó', '&oacute;'),
    ('Ñ', '&Ntilde;'),
    ('ñ', '&ntilde;'),
    ('Ú', '&Uacute;'),
    ('ú', '&uacute;'),
    ('Ü', '&Uuml;'),
    ('ü', '&uuml;'),
    ('¡', '&iexcl;'),
    #('ª', '&ordf;'),
    #('¿', '&iquest;'),
    #('º', '&ordm;'),
    ]

html_to_unicode = dict([(b, a) for (a,b) in unicode_mapping])

def convert_html_to_unicode(s):
    n = s
    for k, v in html_to_unicode.items():
        n = n.replace(k, v)
    return n

def h_to_u(s):
    try:
        return convert_html_to_unicode(s)
    except UnicodeDecodeError:
        import pdb; pdb.set_trace()
        print s

def h_to_u(s):
    return s.encode('ascii', 'xmlcharrefreplace')



def fetch_data(team, tournament, league=1):
    d = {
        "id_equipo": team,
        "id_liga": league,
        "id_torneo": tournament,
        }
    s = urlencode(d)
    r = urllib2.urlopen(team_url, s).read()
    return r.strip()
    
def parse_data(html):
    # Seems to be team data, so lineups and stuff?
    l = []
    soup = BeautifulSoup(html)
    table = soup.findAll("table", {"id": "equipo"})[0]
    trs = table.findAll("tr")[1]
    items = trs.findAll("tr")
    headers = [get_contents(e) for e in items[0].findAll("th")]
    for item in items:
        values = item.findAll("td")
        if len(values) == len(headers):
            attrs = [get_contents(e) for e in values]
            unicode_attrs = [h_to_u(e) for e in attrs]
            d = zip(headers, unicode_attrs)
            l.append(d)

    return l
    
if __name__ == "__main__":
    url = 'http://www.mediotiempo.com/jugador/marco-antonio-palacios'
    soup = scrape_soup(url, encoding='iso_8859_1')
    scrape_player(soup)
    
