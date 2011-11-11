
import datetime
import os

from soccerdata.cache import data_cache
from soccerdata.mongo import soccer_db

DIR = '/home/chris/www/soccerdata/data/stats'
games_filename = '/home/chris/www/soccerdata/data/scores/asl.csv'



competition_map = {
    'ASL': 'American Soccer League (1921-1933)',
    'US Open Cup': 'Lamar Hunt U.S. Open Cup',
    'ASA Cup': 'American Cup',
    'AFA Cup': 'American Cup',
    }

from soccerdata.mongo import soccer_db
def get_standings_dict():
    d = {}
    for e in soccer_db.standings.find():
        key = (e['competition'], e['season'])
        if key not in d:
            d[key] = [e['name']]
        else:
            d[key].append(e['name'])
    return d

sd = get_standings_dict()


def get_full_name(name, competition, season):
    competition = competition.replace("Playoffs", '').strip()
    try:
        names = sd[(competition, season)]
    except:
        return name
    for e in names:
        if e.startswith(name):
            return e
        
    print "failed on %s" % name
    return name
    


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
        fields = row.strip().split('\t')

        if len(fields) == 10:
            fields = fields[:9]

        if len(fields) == 9:
            team, season, competition, month, day, opponent, location, score, goals = fields
        elif len(fields) == 8:
            team, season, competition, month, day, opponent, location, score = fields
            goals = []
        else:
            print fields
            return {}

        sx = season.replace("Fall", '').replace('Spring', '').replace('Playoffs', '').replace('Playoff', '').strip()
        if '-' in season:
            start_year, end_year = [int(e) for e in sx.split('-')]
        else:
            start_year = end_year = int(sx)

        # Skipping minigame for now.
        if day in ('M', 'SO', 'OT', 'SO-M'):
            return {}

        # Not played.
        if score == 'np':
            return {}

        
        # Process day before month.
        if day.strip():
            self.day = int(day)

        if month.strip():
            self.month = int(month)

            if self.month >= 8:
                self.year = start_year
            else:
                self.year = end_year

        try:
            d = datetime.datetime(self.year, self.month, self.day)
        except:
            import pdb; pdb.set_trace()

        if score in ('forfeit loss', 'forfeit win', 'awarded', ''):
            return {}

        try:
            team_score,  opponent_score = [int(e) for e in score.split(',')]
        except:
            import pdb; pdb.set_trace()

        competition = competition_map.get(competition, competition)

        team = get_full_name(team, competition, season)
        opponent = get_full_name(opponent, competition, season)
            
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

        return {
            'competition': competition,
            'season': season,
            'date': d,
            'home_team': home_team,
            'away_team': away_team,
            'home_score': home_score,
            'away_score': away_score,
            }
            
            



if __name__ == "__main__":
    print process_games()


