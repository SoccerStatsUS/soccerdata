import urllib2

from BeautifulSoup import BeautifulSoup

from soccer.teams.models import Team
from soccer.stats.models import SeasonStat

create_url = lambda t,y: "http://www.mlssoccer.com/stats/club/%s/overall/%s/reg" % (t, y)

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
    

    stat = SeasonStat(**nd)
    stat.save()
        


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
        
    


    
