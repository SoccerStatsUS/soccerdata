import datetime

from soccerdata.utils import scrape_url, get_contents


from BeautifulSoup import BeautifulSoup


    

winter_leagues = [
    ('primera', 1928),
    ('premier_league_en', 2001),
    ('serie_a', 1970),
    ('bundesliga', 2001),
    ('ligue_1', 2001),
    ('eredivisie', 2001),
    ('portuguese_liga', 2008),
    ]

summer_leagues = [
    ('premier_league_ru', 2009),
    ]


winter_league_url = lambda name, year: 'http://www.fbleague.com/en/league/%s/%s_%s/' % (name, year, year + 1)
summer_league_url = lambda name, year: 'http://www.fbleague.com/en/league/%s/%s/' % (name, year)


def scrape_all_seasons():
    import time
    l = []
    for url in all_season_urls():
        l.extend(scrape_season(url))
        time.sleep(15)
    return l


def all_season_urls():
    urls = []

    for league, year in winter_leagues:
        while year < datetime.date.today().year:
            urls.append(winter_league_url(league, year))
            year += 1

    for league, year in summer_leagues:
        while year < datetime.date.today().year:
            urls.append(summer_league_url(league, year))
            year += 1        
            
    return urls


def scrape_season(url):
    html = scrape_url(url)
    soup = BeautifulSoup(html)

    tables = soup.findAll("table", "wholex")
    tables = tables[2:] # First two are different.

    def process_table(table):
        trs = table.findAll("tr")
        matchday = trs[0]
        l = []
        for tr in trs[1:]:
            date, home, away, score = [get_contents(e) for e in tr.findAll("td")]
            home_score, away_score = score.split('-')
            dt = lambda s: datetime.datetime.strptime (s, "%d %b %Y")    
            l.append({
                    'date': dt(date),
                    'home': home.strip(),
                    'away': away.strip(),
                    'home_score': int(home_score),
                    'away_score': int(away_score),
                    
                    })
        return l
                
    l = []
    raised = False # has this process raised an error yet?
    for table in tables:
        try:
            l.extend(process_table(table))
            # Make sure that once we've failed to process a table,
            # all subsequent tables also fail.
            if raised:
                raise
            
        except ValueError:
            # Thrown while parsing date, home, away, score
            # Presumably there are no more score tables.
            raised = True
    return l

