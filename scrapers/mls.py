import datetime
import itertools

from BeautifulSoup import BeautifulSoup

from soccerdata.utils import scrape_soup, get_contents



def to_int(s):
    s = s.replace(",", '')
    if s:
        return int(s)
    else:
        return 0


def get_all_players():
    players_url = "http://www.mlssoccer.com/players/%s/%s"
    urls = {}
    for letter in letters:
        for n in itertools.count(1):
            url = players_url % (letter, n)
            d = get_players_from_page(url)
            urls.update(d)
            if d == {}:
                break
    return urls.items()


def get_players_from_page(url):
    soup = scrape_soup(url, static=False)

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
    """
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
        
    


    
