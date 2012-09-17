# Process game data for the original NASL.
# Need to simplify, export, and remove this.


import datetime
import os

from soccerdata.cache import data_cache
from soccerdata.mongo import soccer_db

DIR = '/home/chris/www/soccerdata/data/stats'
stats_filename = os.path.join(DIR, 'nasl.txt')
games_filename = '/home/chris/www/soccerdata/data/games/domestic/country/usa/leagues/nasl.csv'


foreign_map = {
    'Varzim': 'Varzim S.C.',
    'varzim': 'Varzim S.C.',
    'Hertha': 'Hertha BSC',
    'hertha': 'Hertha BSC',
    'Bangu': 'Bangu AC',
    'bangu': 'Bangu AC',
    'apollon': 'Apollon Limassol',
    'Apollon': 'Apollon Limassol',
    'lanerossi': 'Vicenza Calcio',
    'Lanerossi': 'Vicenza Calcio',
    'Monterrey': 'CF Monterrey',
    'Vera Cruz': 'Veracruz',
    'Coventry': 'Coventry City FC',
    'hapoel': 'Hapoel Tel Aviv F.C.',
    'Hapoel': 'Hapoel Tel Aviv F.C.',
    'Hearts': 'Heart of Midlothian F.C.',

}

simple_map = {
    'Baltimore': 'Baltimore Bays',
    'Calgary': 'Calgary Boomers',
    #'Chicago': 'Chicago Mustangs',
    'California': 'California Surf',
    'Cleveland': 'Cleveland Stokers',
    'Dallas': 'Dallas Tornado',
    #'Detroit': 'Detroit Cougars',
    #'Detroit': 'Detroit Express',
    'Edmonton': 'Edmonton Drillers',
    'Golden Bay': 'Golden Bay Earthquakes',
    'Kansas City': 'Kansas City Spurs',
    'Tampa Bay': 'Tampa Bay Rowdies',
    'Seattle': 'Seattle Sounders',
    'Portland': 'Portland Timbers',
    'Rochester': 'Rochester Lancers',
    'Jacksonville': 'Jacksonville Tea Men',
    'Tulsa': 'Tulsa Roughnecks',
    'Fort Lauderdale': 'Fort Lauderdale Strikers',

    'Hartford': 'Hartford Bicentennials',
    'Connecticut': 'Connecticut Bicentennials',
    'Colorado': 'Colorado Caribous',
    'San Jose': 'San Jose Earthquakes',
    'Team America': 'Team America',
    'St. Louis': 'St. Louis Stars',
    'Las Vegas': 'Las Vegas Quicksilver',
    'New England': 'New England Tea Men',
    'San Antonio': 'San Antonio Thunder',
    'Denver': 'Denver Dynamos',
    'Team Hawaii': 'Team Hawaii',
    
    
}


# Map of ambiguous names, these apply to multiple teams, but
# should be preempted by the season_map.
ambig_map = {

    'Boston': 'Boston Minutemen',
    'Detroit': 'Detroit Express',
    'Houston': 'Houston Hurricane',
    'Los Angeles': 'Los Angeles Aztecs',
    'New York': 'New York Cosmos',
    'Toronto': 'Toronto Blizzard',
    'Vancouver': 'Vancouver Whitecaps',
    'Washington': 'Washington Diplomats',
    'San Diego': 'San Diego Sockers',
    'Chicago': 'Chicago Sting',
    'Montreal': 'Montreal Manic',
    'Memphis': 'Memphis Rogues',
    'Minnesota': 'Minnesota Kicks',
    'Miami': 'Miami Toros',
    'Philadelphia': 'Philadelphia Atoms',
    'Atlanta': 'Atlanta Chiefs',
    }


simple_map.update(ambig_map)



season_map = {
    (1968, 'Boston'): 'Boston Beacons',
    (1968, 'Detroit'): 'Detroit Cougars',
    (1968, 'Houston'): 'Houston Stars',
    (1968, 'Los Angeles'): 'Los Angeles Wolves',
    (1968, 'New York'): 'New York Generals',
    (1968, 'Oakland'): 'Oakland Clippers',
    (1968, 'San Diego'): 'San Diego Toros',
    (1976, 'San Diego'): 'San Diego Jaws',
    (1968, 'Toronto'): 'Toronto Falcons',
    (1968, 'Vancouver'): 'Vancouver Royals',
    (1968, 'Washington'): 'Washington Whips',
    (1978, 'Oakland'): 'Oakland Stompers',
    (1981, 'Washington'): 'Washington Diplomats',
    (1971, 'Montreal'): 'Montreal Olympique',
    (1972, 'Montreal'): 'Montreal Olympique',
    (1973, 'Montreal'): 'Montreal Olympique',
    (1978, 'Philadelphia'): 'Philadelphia Fury',
    (1979, 'Philadelphia'): 'Philadelphia Fury',
    (1980, 'Philadelphia'): 'Philadelphia Fury',
    (1984, 'Minnesota'): 'Minnesota Strikers',
    (1972, 'Miami'): 'Miami Gatos',
    (1968, 'Atlanta'): 'Atlanta Chiefs',
    (1969, 'Atlanta'): 'Atlanta Chiefs',
    (1970, 'Atlanta'): 'Atlanta Chiefs',
    (1971, 'Atlanta'): 'Atlanta Chiefs',
    (1972, 'Atlanta'): 'Atlanta Chiefs',
     
    }


# Just fill this out by referencing Wikipedia.
team_map = {
}

competition_map = {
    'NASL': 'North American Soccer League',
    'NASL Playoffs': 'North American Soccer League Playoffs',
    'USA': 'United Soccer Association',
    'NPSL': 'National Professional Soccer League',
    'NPSL Playoffs': 'National Professional Soccer League Playoffs',
    }





def get_full_name(name, season):
    """
    Figure out the full team name based on the season.
    """
    if name in foreign_map:
        return foreign_map[name]

    # For teams with unambiguous names (e.g. Dallas, San Jose, Golden Bay.
    key = (int(season), name)
    if key in season_map:
        return season_map[key]

    if name in simple_map:
        return simple_map[name]

        
    print "(NASL) failed to get name for %s" % name
    return name
    

# This is for the New NASL!!!
# This should be split off into a separate file!!!
def process_stats():
    """
    Process stats for the new NASL.
    """
    f = open(stats_filename)
    lst = []
    for line in f:

        fields = line.split("  ") # 2 spaces
        fields = [e.strip() for e in fields if e.strip()]
        name, team, goals, assists, shots, yc, rc, minutes = fields
        name = name.split(")")[1].strip()
        lst.append({
                'competition': "North American Soccer League (2011-)",
                'season': '2011',
                'name': name,
                'team': team,
                'position': '',
                'goals': int(goals),
                'assists': int(assists),
                'shots': int(shots),
                'yellow_cards': int(yc),
                'red_cards': int(rc),
                'minutes': int(minutes),
                })
                
    return lst



def process_games():
    f = open(games_filename)
    l = []
    gp = GameProcessor()
    for line in f:
        g = gp.consume_row(line)
        if g:
            l.append(g)
    return l



class GameProcessor(object):
    def __init__(self):
        self.year = None
        self.month = None
        self.day = None
        

    def consume_row(self, row):
        fields = row.split('\t')
        if len(fields) != 11:
            import pdb; pdb.set_trace()

        competition, season, team, month, day, opponent, location, score, notes, goals, attendance = fields

        # Skipping minigame for now.
        if day in ('M', 'SO', 'OT', 'SO-M'):
            return {}

        # Not played.
        if score == 'np':
            return {}

        
        # Process day before month.
        if day.strip():
            try:
                day = int(day)
            except:
                import pdb; pdb.set_trace()
            # Adjust month if we fall into a new month.
            if day < self.day:
                self.month += 1
            self.day = day

        if month.strip():
            self.month = int(month)

        self.year = int(season)

        try:
            d = datetime.datetime(self.year, self.month, self.day)
        except:
            import pdb; pdb.set_trace()

        team_score,  opponent_score = [int(e) for e in score.split(',')]

        competition = competition_map[competition]

        team = get_full_name(team, season)
        opponent = get_full_name(opponent, season)
            
        if location == 'h':
            home_team = team
            home_score = team_score
            away_team = opponent
            away_score = opponent_score
        else:
            home_team = opponent
            home_score = opponent_score
            away_team = team
            away_score = team_score

        if not attendance.strip():
            attendance = None
        else:
            attendance = int(attendance)

        return {
            'competition': competition,
            'season': season,
            'date': d,
            'team1': home_team,
            'team2': away_team,
            'team1_score': home_score,
            'team2_score': away_score,
            'home_team': home_team,
            'attendance': attendance,
            'source': 'NASL - A Complete Record of the North American Soccer League',
            }



if __name__ == "__main__":
    print process_games()
