from BeautifulSoup import BeautifulSoup
import re
import urllib2

from soccerdata.utils import get_contents, scrape_url


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





    
