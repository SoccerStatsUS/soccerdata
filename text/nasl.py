
import datetime
import os

from soccerdata.cache import data_cache
from soccerdata.mongo import soccer_db

DIR = '/home/chris/www/soccerdata/data/stats'
stats_filename = os.path.join(DIR, 'nasl.txt')
games_filename = '/home/chris/www/soccerdata/data/scores/nasl.csv'


final_map = {
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

team_map = {
    'Golden Bay': 'San Jose',
    'Hartford': 'Connecticut',

}

competition_map = {
    'NASL': 'North American Soccer League',
    'NASL Playoffs': 'North American Soccer League Playoffs',
    'USA': 'United Soccer Association',
    'NPSL': 'National Professional Soccer League',
    'NPSL Playoffs': 'National Professional Soccer League Playoffs',
    }



def get_standings_dict():
    # Oh shit relying on standings when it shouldn't...
    # We've got a weird kind of reference here.


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
    """
    Figure out the full team name based on the season and competition.
    """
    if name in final_map:
        return final_map[name]

    name = team_map.get(name, name)

    competition = competition.replace("Playoffs", '').strip()

    key = (competition, season)
    names = sd.get(key, [])

    for e in names:
        if e.startswith(name):
            return e
        
    print "(NASL) failed to get name for %s" % name
    return name
    

    



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
                'minutes': int(minutes)
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

        if not attendance.strip():
            attendance = None
        else:
            attendance = int(attendance)

        return {
            'competition': competition,
            'season': season,
            'date': d,
            'team1': 'home_team',
            'team2': 'away_team',
            'team1_score': home_score,
            'team2_score': away_score,
            'home_team': home_team,
            'attendance': attendance,
            }
            
            



if __name__ == "__main__":
    print process_games()
