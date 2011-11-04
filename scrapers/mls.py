import datetime

from soccerdata.utils import scrape_soup, get_contents, pounds_to_kg, inches_to_cm
from soccerdata.cache import data_cache, set_cache

# Team ids to look through.
team_ids = [
    1207,
    2079,
    436,
    454,
    1326,
    1903,
    1897,
    1230,
    6226,
    928,
    399,
    5513,
    1581,
    1899,
    1131,
    3500,
    421,
    1806,
    2077,
    1708
    ]

# Stat years to scrape.
years = range(1996, 2012)




def scrape_all_games_mlssoccer():

    l = []
    years = range(1996, 2012)
    for year in years:
        l.extend(scrape_games(year))

    return l

@data_cache
def scrape_games(year):
    """
    Scrape all game data from a scoreboard.
    """

    # If the year is this year, re-scrape.
    if year >= datetime.date.today().year:
        refresh = True
    else:
        refresh = False

    url = 'http://www.mlssoccer.com/schedule?month=all&year=%s&club=all&competition_type=all' % year
    soup = scrape_soup(url, refresh=refresh)
    l = scrape_games_first_pass(soup)
    games =  MLSScoresProcessor().process_rows(l)
    return games


@data_cache
def scrape_all_bios_mlssoccer():
    """
    Scrape all players that are linked to by a stats link.
    Should comprise almost all players who have played in MLS.
    (Currently coaches are not linked, plus mlssoccer.com is
    just not consistently good at stats.
    """
    
    bios = []
    visited = set()
    for stat in scrape_all_stats_mlssoccer():
        url = stat['url']
        if url and url not in visited:
            visited.add(url)
            bios.append(scrape_player_bio(url))

    # Should I handle this better?
    # Maybe. not sure it's worth it.
    return [e for e in bios if e]


@data_cache
def scrape_all_bio_stats_mlssoccer():

    
    stats = []
    visited = set()
    for stat in scrape_all_stats_mlssoccer():
        url = stat['url']
        if url and url not in visited:
            visited.add(url)
            stats.append(scrape_stats_from_bio(url))

    # Should I handle this better?
    # Maybe. not sure it's worth it.
    return [e for e in stats if e]


@data_cache
def scrape_all_stats_mlssoccer():
    """
    Scrape all mls stats.
    """

    # This currently looks at all possible teams / years
    # and scrapes them, so there are a lot of unsuccessful
    # attempts.

    stats = []
    for team_id in team_ids:
        for year in years:
            season = unicode(year)
            url = 'http://www.mlssoccer.com/stats/season?season_year=%s&season_type=REG&team=%s' % (year, team_id)
            stats.extend(scrape_team_stats(url, season))
    return stats



@data_cache
def scrape_player_bio(url):
    """
    Scrapes player biographical information.
    """
    # We need to also get season stat information
    # because mlssoccer.com merges team stats on
    # their stat pages for some reason.

    soup = scrape_soup(url, sleep=2)

    try:
        name = get_contents(soup.find("div", "header_title").find("h1"))
    except:
        # Some players don't have header_titles?
        # e.g. Chris Eylander?
        # Not sure at all why.
        print "No result for %s" % url
        return {}

    

    fields = [get_contents(e) for e in soup.find("div", "player-info").findAll("li")]
    d = dict([e.strip().split(":") for e in fields])

    height = weight = birthdate = birthplace = None

    # Need to actually parse these, especially birthdate.
    if "Height" in d:
        height = d['Height']
        height = height.replace("&nbsp;", "").replace("\"", "")

        height = [e.strip() for e in height.split("'")]

        assert len(height) == 2

        # height[1] is probably an empty string.
        if not height[1]:
            height[1] = 0

        feet, inches = [int(e) for e in height]
        height = inches_to_cm(inches=inches, feet=feet)
        
                  
    if 'Weight' in d:
        weight = d['Weight']
        if "lbs." in weight:
            weight = int(weight.replace("lbs.", ''))
            weight = pounds_to_kg(weight)
            

    if 'Birth Date' in d:
        birthdate_string = d['Birth Date']
        if birthdate_string:
            birthdate = datetime.datetime.strptime(birthdate_string,  "%a, %m/%d/%Y")


    if 'Birthplace' in d:
        birthplace = d['Birthplace']

    return {
        'name': name,
        'height': height,
        'weight': weight,
        'birthdate': birthdate,
        'birthplace': birthplace,
        }

@data_cache
def scrape_stats_from_bio(url):
    print 'working'
    bio = scrape_player_bio(url)

    soup = scrape_soup(url, sleep=2)

    tables = soup.findAll("table", 'views-table')

    career, season_stats = tables[0], tables[1:]

    l = []

    fields_set = set()

    if not season_stats:
        return {}

    try:
        keys = [get_contents(e).lower() for e in season_stats[0].findAll("th")] + ['season']
    except:
        import pdb; pdb.set_trace()

    for t in season_stats:
        season = get_contents(t.previousSibling.previousSibling).replace("Season Statistics", "").strip()

        trs = t.findAll("tr")

        for tr in trs:
            fields = [get_contents(e) for e in tr.findAll("td")]
            if len(fields) == 13:
                if fields[0] in ('MLS Regular Season', 'MLS Playoffs'):
                    t = tuple(fields + [season])
                    fields_set.add(t)

    for fields in sorted(fields_set):

        d = dict(zip(keys, fields))

        field_mapping = {
                'gp': 'games_played',
                'gs': 'games_started',
                'g': 'goals',
                'min': 'minutes',
                'a': 'assists',
                'sht': 'shots',
                'sog': 'shots_on_goal',
                'fc': 'fouls committed',
                'off': 'offsides',
                'y': 'yellow_cards',
                'r': 'red_cards',
                'club': 'team',
                }

        competition_dict = {
            'MLS Regular Season': 'Major League Soccer',
            'MLS Playoffs': 'Major League Soccer Playoffs',
            }

        nd = {}
        for k, v in d.items():
            key = field_mapping.get(k, k)
            nd[key] = v

        nd['competition'] = competition_dict[nd['competition']]

        if 'name' in bio:
            nd['name'] = bio['name']
            l.append(nd)
        else:
            pass




    return l
            
        
def scrape_games_first_pass(soup):
    """
    Generates date and game objects,
    in the order that they are listed.
    """
    

    def process_row(row):
        """
        Return either an empty object, a date, or a game.
        """
        # This is a header row.
        if row.findAll("th"):
            return {}

        # Date row
        if not row.findAll("td"):
            date = row.contents[0]
            return {
                'type': 'date',
                'date': date
                }
        
        # Game row
        else:
            tds = [e for e in row.findAll("td", text=True) if e.strip()]

            # Game does not conform to standard final game structure, so
            # skip it.
            if len(tds) != 6:
                return {}

            status, home_team, scores, away_team, location, _ = tds

            # Consider altering this so that we have future schedules also?

            # Game is probably unplayed.
            if status != "Final":
                return {}

            try:
                home_score, away_score = [int(e) for e in scores.split("-")]
            except:
                return {}

            return {
                'type': 'game',
                'home_team': unicode(home_team),
                'away_team': unicode(away_team),
                'location': unicode(location),
                'home_score': home_score,
                'away_score': away_score
                }


    schedule_div = soup.find("div", 'schedule-page')
    rows = schedule_div.findAll(["h3", "tr"])
    
    # Rows with blanks
    raw_rows = [process_row(row) for row in rows]
    return [e for e in raw_rows if e]


# Create a helper function for this.
class MLSScoresProcessor(object):

    def __init__(self):
        self.current_date = None
        self.games = []

    def process_row(self, d):
        """
        Returns None.
        Consumes a dictionary and changes internal state based on it.
        """
        
        if d['type'] == 'date':
            dt = unicode(d['date'])
            self.current_date = datetime.datetime.strptime(dt, "%A, %B %d, %Y")

        else:
            nd = {
                'date': self.current_date,
                'competition': 'Major League Soccer',
                'season': unicode(self.current_date.year)
                }

            nd.update(d)
            nd.pop('type')
            self.games.append(nd)

    def process_rows(self, dl):
        for d in dl:
            self.process_row(d)
        return self.games



# Probably makes more sense to cross check against all-time.
# http://www.mlssoccer.com/stats/alltime?page=118

# This fucker is giving season stats, so we have to scrape individual players apparently.
# Anybody that appears twice, scrape their individual page.

# Find duplicates

# KC doesn't seem to be working.

def find_duplicates(lst):
    # Remove duplicate items,
    # then scrape player names.

    # Use a counter?
    s = set()
    duplicates = Counter()
    new_l = []
    for e in l:
        t = (e['name'], e['season'])

    for e in l:
        if e not in duplicates:
            new_l.append(e)

    for dupe in duplicates:
        stats = scrape_player(dupe)
        stats = [e for e in stats if e['year'] == dupe['year']]
        new_l.extend(stats)

    return new_l


@data_cache
def scrape_player_stats(url):

    def process_stat(tr):
        fields = [get_contents(e) for e in tr.findAll("td")]
        # Probably a header row.
        if not fields:
            return {}
        

        if len(fields) == 13:
            try:
                year, team, games_played, games_started, goals, minutes, assists, shots, shots_on_goal, fouls_committed, offsides, yellow_cards, red_cards = fields
                year = int(year)
            except:
                competition, team, games_played, games_started, goals, minutes, assists, shots, shots_on_goal, fouls_committed, offsides, yellow_cards, red_cards = fields
                year = 0
                try:
                    int(games_started)
                except:
                    return {}

        else:
            return {}
            

        return {
            'competition': 'Major League Soccer',
            'season': 'regular season %s' % year,
            'name': bio['name'],
            'team': team,
            'games_started': games_started,
            'games_played': games_played,
            'minutes': minutes,
            'goals': goals,
            'assists': assists,
            'shots': shots,
            'shots_on_goal': shots_on_goal,
            }

    soup = scrape_soup(url)

    bio = scrape_player_bio(url)
    stats = []
    stat_tables = soup.findAll("div", 'stats-table')
    for table in stat_tables:
        trs = table.findAll('tr')
        for tr in trs:
            stats.append(process_stat(tr))

    return [e for e in stats if e]

    return stats

            
def process_stat(tr, competition, season):
    fields = [get_contents(e) for e in tr.findAll("td")]
    name, team, position, games_played, games_started, minutes, goals, assists, shots, shots_on_goal, _,_,_,_,_,_ = fields

    a = tr.find("a")
    if a:
        url = a['href']
        full_url = "http://mlssoccer.com" + url
    else:
        full_url = ''


    return {
        'competition': competition,
        'season': season,
        'name': name,
        'url': full_url,
        'team': team,
        'position': position,
        'games_started': games_started,
        'games_played': games_played,
        'minutes': minutes,
        'goals': goals,
        'assists': assists,
        'shots': shots,
        'shots_on_goal': shots_on_goal,
        }


@data_cache
def scrape_team_stats(url, season):
    """
    Scrape team stats for a given year.
    season_type is playoff or regular.
    """

    soup = scrape_soup(url)
    
    # Can't find a stats table.
    stats_table = soup.find("div", "stats-table")
    if not stats_table:
        print "No stats table: %s" % url
        return []

    # Can't find rows.
    stats_trs = stats_table.findAll("tr")
    if len(stats_trs) == 0:
        print "No rows: %s" % url
        return []


    else:
        stats = []
        for tr in stats_trs[1:]: #Skip header.
            competition = 'MLS'
            stats.append(process_stat(tr, competition, season))

    return stats


if __name__ == "__main__":
    #print scrape_stats_from_bio('http://www.mlssoccer.com/players/joseph-nane')
    #print scrape_stats_from_bio('http://www.mlssoccer.com/players/freddy-adu')
    print scrape_all_bio_stats_mlssoccer()
    #print "\n".join([str(e) for e in main()])

    
