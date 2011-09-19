import datetime
import urllib2
from BeautifulSoup import BeautifulSoup

from soccerdata.utils import scrape_url


create_url = lambda t,y: "http://www.mlssoccer.com/stats/club/%s/overall/%s/reg" % (t, y)

def scrape_scores(year):
    if year >= datetime.date.today().year:
        static = False
    else:
        static = True


    url = 'http://www.mlssoccer.com/schedule?month=all&year=%s&club=all&competition_type=all' % year
    text = scrape_url(url, static)
    soup = BeautifulSoup(text)
    l = scrape_scores_first_pass(soup)
    return MLSScoresProcessor().process_rows(l)

def scrape_scores_first_pass(soup):

    def process_row(row):
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


    # Need to scrape using the scraper object.
    schedule_div = soup.find("div", 'schedule-page')
    rows = schedule_div.findAll(["h3", "tr"])
    
    raw_rows = [process_row(row) for row in rows]
    raw_rows = [e for e in raw_rows if e]
    return raw_rows


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



        
        
                
            

    
    
    


def to_int(s):
    s = s.replace(",", '')
    if s:
        return int(s)
    else:
        return 0

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
            create_stat(stat)

def year_stats(year):
    for team in team_names.keys():
        stats = scrape_stats(team, year)
        for stat in stats:
            create_stat(stat)

# Not sure this is at all necessary.
def create_stat(d):
    nd = {}
    for key, value in d.items():
        if key not in ("POS", "Player", "team", "year"):
            nvalue = to_int(value)
        elif key == "team":
            nvalue = Team.objects.get_team(team_names[value])
        else:
            nvalue = value
            
        nkey = stat_mapping.get(key, key)
        nd[nkey] = nvalue

    for key in ("shutouts", "goals_allowed", "shots_faced", 
                "saves", "penalties_allowed", "penalties_faced"):
        nd[key] = 0
    return nd
        


def scrape_stats(team, year):
    url = create_url(team, year)

    text = urllib2.urlopen(url).read()
    text = text.replace("&#039;", "'")
    soup = BeautifulSoup(text)
    table = soup.findAll("table", {"class": "stats statsleaders sortable-c4-desc players"})
    if not table:
        return []
    field_stats = table[0]
    
    # At least one page doesn't have goalkeeper stats.  Whoops, mlssoccer.com
    try:
        gk_stats = table[1]
    except IndexError:
        gk_stats = []
    
    header = field_stats.findAll("thead")[0] # the second entry is team totals
    individual_stats = field_stats.findAll("tbody")[0]
    
    l = []

    keys = [e.contents[0] for e in header.findChildren("th")]

    for row in individual_stats:
        if hasattr(row, 'findChildren'):
            # Work around for terrible mlssocer.com data integrity.
            get_contents = lambda d: d.contents[0] if len(d) else ''
            try:
                stats = [get_contents(e) for e in row.findChildren("td")]
            except:
                import pdb; pdb.set_trace()
            d = dict(zip(keys, stats))
            
            # A few players don't have urls for some reason.
            player_name = d['Player']
            if hasattr(player_name, 'contents'):
                d['Player'] = player_name.contents[0]

            for key, value in d.items():
                # Get rid of BeautifulSoup cruft
                key = str(key)
                value = str(value)
                d[key] = value
            d['team'] = team
            d['year'] = year
            l.append(d)
    
    return l
        
    


    
