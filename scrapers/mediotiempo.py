# encoding: utf-8

from BeautifulSoup import BeautifulSoup
from urllib import urlencode
import urllib2

team_url = "http://www.mediotiempo.com/ajax/ajax_equipo.php"

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
    
