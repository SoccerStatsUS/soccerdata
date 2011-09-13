import datetime
import urllib2
import re
from BeautifulSoup import BeautifulSoup

from abstract import get_contents

# Scrape the scores of the NASL.

def scrape_scores():
    url = 'http://nasl.com/index.php?id=12'
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    table = soup.find("h1", "blockHeader").nextSibling.nextSibling
    rows = table.findAll("tr")
    results = []
    for row in rows:
        data = [get_contents(e) for e in row]
        if len(data) == 10:
            _, date, time, home, _, away, stadium, score, _, _ = data
            month, day = re.search("(?P<date>\d{1,2}/\d{2})", date).groups()[0].split("/")
            dt = datetime.datetime(2011, int(month), int(day))
            try:
                home_score, away_score = [int(e) for e in score.split("-")]
                results.append({
                        'home_team': str(home),
                        'away_team': str(away),
                        'home_score': home_score,
                        'away_score': away_score,
                        'date': dt,
                        'competition': 'NASL',
                        #'url': "", # Nasl doesn't even link these.
                        })
            # Probably a Buy Tickets link, indicating game hasn't been played yet.
            except ValueError:
                pass

    return results
