from BeautifulSoup import BeautifulSoup
import re
import urllib2

from abstract import get_contents

DEFAULT_USER_AGENT = "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.22 Safari/532.5"

def scrape_team(name):
    wiki_name = name.replace(" ", "_")

    url = "http://en.wikipedia.org/wiki/%s" % wiki_name

    urlopener = urllib2.build_opener()
    urlopener.addheaders = [('User-agent', DEFAULT_USER_AGENT)]
    data = urlopener.open(url).read()

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





    
