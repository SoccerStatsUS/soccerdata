import datetime

from soccerdata.utils import scrape_url, get_contents


from BeautifulSoup import BeautifulSoup


winter_leagues = [
    ('primera', 1928, 'La Liga'),
    ('premier_league_en', 2001, 'Premier League'),
    ('serie_a', 1970, 'Serie A'),
    ('bundesliga', 2001, 'Bundesliga'),
    ('ligue_1', 2001, 'Ligue 1'),
    ('eredivisie', 2001, 'Eredivisie'),
    ('portuguese_liga', 2008, 'Portuguese Liga'),
    ]

summer_leagues = [
    ('premier_league_ru', 2009, 'Russian Premier League'),
    ]


winter_league_url = lambda name, year: 'http://www.fbleague.com/en/calendar/%s/%s_%s/' % (name, year, year + 1)
summer_league_url = lambda name, year: 'http://www.fbleague.com/en/calendar/%s/%s/' % (name, year)


# Unused.
def get_name(s):
    for slug, year, name in winter_leagues:
        if slug == s:
            return name

    for slug, year, name in summer_leagues:
        if slug == s:
            return name

    raise
        


def scrape_all_seasons():
    """
    Scrape all fbleague.com seasons.
    """
    l = []
    for url, season, competition in all_season_urls():
        season = scrape_season(url, competition, season)
        l.extend(season)
    return l


def all_season_urls():
    """
    Get all seasons urls for fbleague.
    """
    urls = []

    for slug, year, competition in winter_leagues:
        while year < datetime.date.today().year:
            season = "%s-%s" % (year, year + 1)
            t = (winter_league_url(slug, year), season, competition)
            urls.append(t)
            year += 1

    for slug, year, competition in summer_leagues:
        while year < datetime.date.today().year:
            season = str(year)
            t = (summer_league_url(slug, year), season, competition)
            urls.append(t)
            year += 1        
            
    return urls


def scrape_season(url, competition, season):
    """
    Scrape a single season.
    """

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
                    'home_team': home.strip(),
                    'away_team': away.strip(),
                    'home_score': int(home_score),
                    'away_score': int(away_score),
                    'competition': competition,
                    'season': season,
                    'url': url,
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

