import os
import datetime
import re

DIR = '/home/chris/www/soccerdata/data/'

if not os.path.exists(DIR):
    DIR = "/Users/chrisedgemon/www/soccerdata/data/"



wsa_team_map  = {
    'San Diego': 'San Diego Nomads',
    'Los Angeles': 'Los Angeles Heat',
    'San Jose': 'San Jose Earthquakes',
    'California': 'California Kickers',
    'San Francisco Bay': 'San Francisco Bay Blackhawks',
    'Edmonton': 'Edmonton Brickmen',
    ('1985', 'Seattle'): 'FC Seattle',
    ('1986', 'Seattle'): 'Seattle Storm',
    ('1987', 'Seattle'): 'Seattle Storm',
    ('1988', 'Seattle'): 'Seattle Storm',
    ('1989', 'Seattle'): 'Seattle Storm',
    ('1985', 'Portland'): 'FC Portland',
    ('1986', 'Portland'): 'FC Portland',
    ('1987', 'Portland'): 'FC Portland',
    ('1988', 'Portland'): 'FC Portland',
    ('1989', 'Portland'): 'Portland Timbers',
    'Victoria': 'Victoria Riptide',
    'Hollywood': 'Hollywod Kickers',
    }

apsl_team_map =  {
    'Colorado': 'Colorado Foxes',
    'Fort Lauderdale': 'Fort Lauderdale Strikers',
    'Ft. Lauderdale': 'Fort Lauderdale Strikers',
    'Tampa Bay': 'Tampa Bay Rowdies',
    'Orlando': 'Orlando Lions',
    'Miami': 'Miami Freedom',
    'Washington S': 'Washington Stars',
    'Boston': 'Boston Bolts',
    'Maryland': 'Maryland Bays',
    'New Jersey': 'New Jersey Eagles',
    'Washington D': 'Washington Diplomats',
    'Albany': 'Albany Capitals',
    'San Francisco Bay': 'San Francisco Bay Blackhawks',
    'Penn-Jersey': 'Penn-Jersey Spirit',
    'Salt Lake': 'Salt Lake Sting',
    'Toronto': 'Toronto Blizzard',
    'Vancouver': 'Vancouver 86ers',
    'Los Angeles': 'Los Angeles Salsa',
    'Montreal': 'Montreal Impact',
    }

team_map = {
    'Western Soccer Alliance': wsa_team_map,
    'Western Soccer Alliance Playoffs': wsa_team_map,
    'American Professional Soccer League': apsl_team_map,
    'American Professional Soccer League Playoffs': apsl_team_map,
    'Professional Cup': apsl_team_map,
    'CONCACAF Champions Cup': apsl_team_map,
    'Friendly': {},

}

    
    
    
class TextProcessor(object):

    position_map = {
        'D': 'Defender',
        'F': 'Forward',
        'M': 'Midfielder',
        'GK': 'Goalkeeper',
        'y': '',
        '': '',
        None: '',
        }
    
    def __init__(self):
        self.competition = None
        self.season = None
        self.team = None
        self.stats = []
        self.games = []


    def preprocess_line(self, line):
        line = line.strip()
        # Not sure what was wrong with these lines.
        d = {
            'Ronnie  Morriss        F': 'Ronnie Morriss        F',
            'John  Lee              F': 'John Lee   F',
            'John  Clare            D': 'John Clare  D',
            'Dino Lopez  -1         D    6/6     555  1  0/0': 'Dino Lopez -1         D    6/6     555  1  0/0',
            'John  Maessner         F   11/8    828   0': 'John Maessner         F   11/8    828   0', 

            }

        return d.get(line, line)


    def set_state_flags(self, line):
        if line.startswith("Competition:"):
            self.competition = line.split("Competition:")[1].strip()
            return True
            
        elif line.startswith("Season:"):
            self.season = line.split("Season:")[1].strip()
            return True

        elif line.startswith("Team:"):
            self.team = line.split("Team:")[1].strip()
            return True

        return False




    def process_roster_line(self, line):
        line = self.preprocess_line(line)



        if self.set_state_flags(line):
            return {}

        elif not line:
            return {}

        else:
            fields = line.split("  ", 1)
            if len(fields) == 2:
                name, position = [e.strip() for e in fields]
            elif len(fields) == 1:
                name = line.strip()
                position = ''
            else:
                import pdb; pdb.set_trace()

            self.stats.append({
                'competition': self.competition,
                'season': self.season,
                'team': self.team,
                'name': name,
                'position': self.position_map[position.strip()]
                })




    def process_stat_line(self, line):
        line = self.preprocess_line(line)

        if self.set_state_flags(line):
            return {}

        elif not line:
            return {}

        else:
            fields = [e.strip() for e in line.split("  ") if e and e.strip()]
            
            position = ''
            yellow_cards = red_cards = None
            if len(fields) == 4:
                name, gsgp, minutes, goals = fields
            elif len(fields) == 5:
                if "/" in fields[1]:
                    name, gsgp, minutes, goals, ycrc = fields
                else:
                    name, position, gsgp, minutes, goals = fields
            elif len(fields) == 6:
                name, position, gsgp, minutes, goals, ycrc = fields
                try:
                    yellow_cards, red_cards = [int(e) for e in ycrc.split("/")]
                except:
                    import pdb; pdb.set_trace()
            else:
                import pdb; pdb.set_trace()
                raise

            name = name.replace('-1', '').replace('-*', '').strip()

            games_started, games_played = [int(e) for e in gsgp.split("/")]
            
            self.stats.append({
                'competition': self.competition,
                'season': self.season,
                'team': self.team,
                'name': name,
                'position': self.position_map[position.strip()],
                'minutes': int(minutes),
                'goals': int(goals),
                'games_started': games_started,
                'games_played': games_played,
                'yellow_cards': yellow_cards,
                'red_cards': red_cards,
                })


    def process_score_line(self, line):
        line = self.preprocess_line(line)

        if self.set_state_flags(line):
            return {}

        elif not line:
            return {}

        else:
            r = re.match("(\d+/\d+/\d+)(.*?)\s+([HA])\s+(\d+\-\d+)(.*)", line)
            if not r:
                print line
                return {}

            date_string, opponent, homeaway, score, _ = r.groups()
            team_score, opponent_score = [int(e) for e in score.split('-')]

            month, day, year = date_string.split('/')
            year = "19%s" % year
            d = datetime.datetime(int(year), int(month), int(day))

            opponent = opponent.strip()
            td = team_map[self.competition]
            key = (self.season, opponent) 
            if key in td:
                opponent = td[key]
            else:
                opponent = td.get(opponent, opponent)


                

            if homeaway == 'H':
                home_team = self.team
                away_team = opponent
                home_score = team_score
                away_score = opponent_score
            elif homeaway == 'A':
                home_team = opponent
                away_team = self.team
                home_score = opponent_score
                away_score = team_score
            else:
                raise

            self.games.append({
                'competition': self.competition,
                'season': self.season,
                'home_team': home_team,
                'away_team': away_team,
                'home_score': home_score,
                'away_score': away_score,
                'date': d
                })
                

            



def process_apsl_stats():
    p = os.path.join(DIR, "stats", "apsl.txt")
    f = open(p)
    t = TextProcessor()
    for line in f:
        t.process_stat_line(line)

    p = os.path.join(DIR, "stats", "apsl_rosters.txt")
    f = open(p)
    for line in f:
        t.process_roster_line(line)

    return t.stats


def process_apsl_scores():
    p = os.path.join(DIR, "scores", "apsl.txt")
    f = open(p)
    t = TextProcessor()
    for line in f:
        t.process_score_line(line)

    return t.games


        

        
if __name__ == "__main__":
    print process_apsl_stats()
            
        
