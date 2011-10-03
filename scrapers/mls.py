import datetime
import itertools

from BeautifulSoup import BeautifulSoup

# Probably do the team stuff when we're merging into canonical tables.
from soccerdata.alias import get_team
from soccerdata.utils import scrape_soup, get_contents, pounds_to_kg, inches_to_cm
from soccerdata.cache import data_cache, set_cache


# Need to comment this!


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


def scrape_all_stats_mlssoccer():
    """
    Scrape all mls stats.
    """
    # This currently looks at all possible teams / years
    # and scrapes them, so there are a lot of unsuccessful
    # attempts.

    stats = []
    for season_type in season_types:
        for team_id in team_ids:
            for year in years:
                season = unicode(year)
                url = 'http://www.mlssoccer.com/stats/season?season_year=%s&season_type=%s&team=%s' % (year, season_type, team_id)
                stats.extend(scrape_team_stats(url, season, season_type))
    return stats

@data_cache
def scrape_all_games_mlssoccer():

    l = []
    years = range(1996, 2011)
    for year in years:
        l.extend(scrape_games(year))

    return l



def scrape_active_players():
    """
    Scrape active mls player bios.
    """
    l = []
    for url, name in scrape_active_player_urls():
        full_url = "http://mlssoccer.com%s" % url
        l.append(scrape_player_bio(full_url))
    return l
        

def scrape_active_player_urls():
    """
    Get urls for all player bios.
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    players_url = "http://www.mlssoccer.com/players/%s"
    urls = {}
    for letter in letters:
        url = players_url % letter
        d = get_player_urls_from_page(url)
        urls.update(d)
    return sorted(urls.items())


@data_cache
def scrape_player_bio(url):
    """
    Scrapes player biographical information.
    """
    # We need to also get season stat information
    # because mlssoccer.com merges team stats on
    # their stat pages for some reason.

    soup = scrape_soup(url, sleep=5)

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
        birthdate = d['Birth Date']

    if 'Birthplace' in d:
        birthplace = d['Birthplace']

    return {
        'name': name,
        'height': height,
        'weight': weight,
        'birthdate': birthdate,
        'birthplace': birthplace,
        }



def get_player_urls_from_page(url):
    """
    Scrape player urls from a given page.
    """
    # Need to run this fresh sometimes to get new player urls.
    # Could also potentially avoid this problem by scraping players
    # from game stats.
    
    soup = scrape_soup(url) #, static=False)

    try:
        link_name_tuples = [(a['href'], get_contents(a)) for a in soup.find("div", "view-content").find("table").find("tbody").findAll("a")]
    except AttributeError:
        # Something was probably a NoneType
        return []

    # Filter out twitter links.
    link_name_tuples = [e for e in link_name_tuples if e[1]]

    return dict(link_name_tuples)




def scrape_games(year):
    """
    Scrape all game data from a scoreboard.
    """
    

    # If the year is this year, re-scrape.
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

    
            


@data_cache
def scrape_team_stats(url, season, season_type):
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

            a = tr.find("a")
            if a:
                url = a['href']
                full_url = "http://mlssoccer.com" + url
            else:
                full_url = ''


            stats.append({
                    'competition': competition,
                    'season': season,
                    'name': name,
                    'url': full_url,
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



if __name__ == "__main__":
    #print scrape_active_players()
    print scrape_all_bios_mlssoccer()

