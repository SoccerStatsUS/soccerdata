import datetime
import itertools

from BeautifulSoup import BeautifulSoup

from soccerdata.teams import get_team
from soccerdata.utils import scrape_soup, get_contents

# Need to comment this!



def get_all_players():
    """
    Get urls for all player bios.
    """
    players_url = "http://www.mlssoccer.com/players/%s/%s"
    urls = {}
    for letter in letters:
        # Count up until we get no urls.
        for n in itertools.count(1):
            url = players_url % (letter, n)
            d = get_player_urls_from_page(url)
            urls.update(d)
            if d == {}:
                break
    return urls.items()


def scrape_player_bio(url):
    soup = scrape_soup(url)
    


def get_player_urls_from_page(url):
    """
    Scrape player urls from a given page.
    """
    # Need to run this fresh sometimes to get new player urls.
    # Could also potentially avoid this problem by scraping players
    # from game stats.
    
    soup = scrape_soup(url) #, static=False)

    tds = soup.findAll("td", "mpl-player active")
    anchors = []
    for td in tds:
        anchors.extend(td.findAll("a"))
    d = {}
    for e in anchors:
        # Probably need to do this better.
        try:
            key = str(e.contents[0])
            value = str(e['href']).split("/")[-1]
            d[key] = value
        except UnicodeEncodeError:
            print str(e['href'])
    return d




def scrape_all_games():
    l = []
    years = range(1996, 2011)
    for year in years:
        l.extend(scrape_games(year))
    return l

def scrape_games(year):
    if year >= datetime.date.today().year:
        static = False
    else:
        static = True

    url = 'http://www.mlssoccer.com/schedule?month=all&year=%s&club=all&competition_type=all' % year
    soup = scrape_soup(url, static)
    l = scrape_games_first_pass(soup)
    return MLSScoresProcessor().process_rows(l)

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

            home_score, away_score = scores.split("-")

            return {
                'type': 'game',
                'status': status,
                'home_team': home_team,
                'away_team': away_team,
                'location': location,
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
            self.current_date = unicode(d['date'])

        else:
            nd = {
                'date': self.current_date,
                }
            
            for k, v in d.items():
                nd[k] = unicode(v)
            self.games.append(nd)

    def process_rows(self, dl):
        for d in dl:
            self.process_row(d)
        return self.games



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

years = range(1996, 2011)

season_types = "REG", "PS"


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

    
            


def scrape_all_stats():
    """
    Scrape all mls stats.
    """
    stats = []
    for season_type in season_types:
        for team_id in team_ids:
            for year in years:
                url = 'http://www.mlssoccer.com/stats/season?season_year=%s&season_type=%s&team=%s' % (year, season_type, team_id)
                stats.extend(scrape_team_stats(url, year, season_type))
    return stats


def scrape_team_stats(url, year, season_type):
    """
    Scrape team stats for a given year.
    season_type is playoff or regular.
    """
    
    if season_type == "PS":
        competition = 'MLS Playoffs'
    else:
        competition = 'MLS'


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
            fields = [get_contents(e) for e in tr.findAll("td")]
            name, team, position, games_played, games_started, minutes, goals, assists, shots, shots_on_goal, _,_,_,_,_,_ = fields

            stats.append({
                    'competition': competition,
                    'year': year,
                    'season': unicode(year),
                    'name': name,
                    'team': get_team(team),
                    'position': position,
                    'games_started': games_started,
                    'games_played': games_played,
                    'minutes': minutes,
                    'goals': goals,
                    'assists': assists,
                    'shots': shots,
                    'shots_on_goal': shots_on_goal,
                })

    return stats






    
# Should move this into an alias object.
# Good enough names.
team_names = {
    "dal": "FC Dallas",
    "clb": "Columbus Crew",
    "col": "Colorado Rapids",
    "chi": "Chicago Fire",
    "chv": "Chivas USA",
    "dc": "D.C. United",
    "hou": "Houston Dynamo",
    "kc": "Kansas City Wizards",
    "la": "Los Angeles Galaxy",
    "ne": "New England Revolution",
    "ny": "New York Red Bulls",
    "phi": "Philadelphia Union",
    "rsl": "Real Salt Lake",
    "sea": "Seattle Sounders",
    "sje": "San Jose Earthquakes",
    "tor": "Toronto FC",
    "mia": "Miami Fusion",
    "tb": "Tampa Bay Mutiny",
    }
    
 
# Scrape mlssoccer stats.
   
stat_mapping = {
    '#': 'number',
    'POS': 'position',
    'Player': 'name',
    'GP': 'games_played',
    'GS': 'games_started',
    'MIN': 'minutes',
    'G': 'goals',
    'GWG': 'game_winning_goals',
    'A': 'assists',
    'SHT': 'shots',
    'SOG': 'shots_on_goal',
    'OFF': 'offsides',
    'PG': 'penalty_goals',
    'PA': 'penalty_attempts',
    'FC': "fouls_committed",
    "FS": 'fouls_suffered',
    'YC': "yellow_cards",
    "RC": "red_cards",
    }

'''
def all_stats():
    l = []
    for team in team_names:
        s = team_stats(team)


def team_stats(team):
    for year in range(1996, 2010):
        stats = scrape_stats(team, year)
        for stat in stats:
            print stat
            parse_stat(stat)


def to_int(s):
    s = s.replace(",", '')
    if s:
        return int(s)
    else:
        return 0



def parse_stat(d):
    # Return player stat dict.
    
    nd = {}
    for key, value in d.items():

        if key not in ("POS", "Player", "team", "year"):
            nvalue = to_int(value)
        else:
            nvalue = value
            
        nkey = stat_mapping.get(key, key)
        nd[nkey] = nvalue

    # Goalkeeper statistics; not sure this is necessary.
    for key in ("shutouts", "goals_allowed", "shots_faced", 
                "saves", "penalties_allowed", "penalties_faced"):
        nd[key] = 0

    return nd
        


def scrape_stats(team, year):
    
    Scrape stats for a team for a given year.
    """
    url = "http://www.mlssoccer.com/stats/club/%s/overall/%s/reg" % (team, year)
    
    # This may be an encoding problem.
    soup = scrape_soup(url).replace("&#039;", "'")

    table = soup.findAll("table", "stats statsleaders sortable-c4-desc players")
    if not table:
        return []


    field_stats = table[0]
    
    # At least one page doesn't have goalkeeper stats.  
    # Whoops, mlssoccer.com
    try:
        gk_stats = table[1]
    except IndexError:
        gk_stats = []
    
    # ?
    header = field_stats.findAll("thead")[0] # the second entry is team totals
    individual_stats = field_stats.findAll("tbody")[0]
    
    l = []

    keys = [e.contents[0] for e in header.findChildren("th")]

    def process_row(row):
        if hasattr(row, 'findChildren'):

            # Work around for terrible mlssocer.com data integrity.
            try:
                stats = [get_contents(e) for e in row.findChildren("td")]
            except:
                # Remove this when possible.
                import pdb; pdb.set_trace()


            d = dict(zip(keys, stats))
            
            # This comment does not help.
            # A few players don't have urls for some reason.
            player_name = d['Player']

            # Huh? Seems wrong.
            if hasattr(player_name, 'contents'):
                d['Player'] = player_name.contents[0]

            for key, value in d.items():
                # Get rid of BeautifulSoup cruft
                # Didn't I create the keys?
                # I think I can just do this when the value is created.
                key = str(key)
                value = str(value)
                d[key] = value

            d.update({
                    'team': team,
                    'year': year
                    })
            return d
        else:
            return {}


    stats = [process_row(row) for row in individual_stats]
    return [e for e in stats if e]
        
    


'''
