# Process Golden Age ASL scores.
# Stats not working yet.

import datetime
import re

from soccerdata.alias import get_team, get_name

games_filename = '/home/chris/www/soccerdata/data/scores/asl.csv'


# These should be merged into get_team?
team_map = {
    'J&P Coats': 'J & P Coats',
    'NY Giants': 'New York Giants',
    'Fleischer': 'Fleisher Yarn',
    'Fleischer Yarn': 'Fleisher Yarn',
}

competition_map = {
    'ASL': 'American Soccer League (1921-1933)',
    'US Open Cup': 'Lamar Hunt U.S. Open Cup',
    'ASA Cup': 'American Cup',
    'AFA Cup': 'American Cup',
    }


def get_standings_dict():
    """
    Get a dict of all standings.
    """
    # This is used for mapping team names, but is probably not a good idea.

    from soccerdata.mongo import soccer_db

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
    Get the relevant team name based on the competition and season a team played in.
    Basically, convert New York to New York Giants, or whatever is appropriate.
    """
    # Check aliases first.
    # This is really not a good system at all.
    name = team_map.get(name, name)

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
    """
    Process the games text.
    Returns a list of dicts representing game results.
    """

    def __init__(self):
        self.year = None
        self.month = None
        self.day = None
        

    def consume_row(self, row):
        fields = row.strip().split('\t')

        # What is field # 10?
        if len(fields) == 10:
            print "TENS!!!"
            print row
            fields = fields[:9]

        if len(fields) == 9:
            team, season, competition, month, day, opponent, location, score, goals = fields
        elif len(fields) == 8:
            team, season, competition, month, day, opponent, location, score = fields
            goals = []
        else:
            # Is this happening?
            print fields
            import pdb; pdb.set_trace()
            return {}

        
        # Figure out what year a game was played in. (dates are only partially entered for convenience)
        sx = season # Clean up the season a bit; 
        for e in 'Fall', 'Spring', 'Playoffs', 'First Half', 'Second Half':
            sx = sx.replace(e, '')

        if '-' in season:
            try:
                start_year, end_year = [int(e) for e in sx.split('-')]
            except:
                import pdb; pdb.set_trace()
        else:
            start_year = end_year = int(re.match('^(\d+).*$', sx).groups()[0])

        # Skipping minigames for now.
        if day in ('M', 'SO', 'OT', 'SO-M'):
            return {}

        # Not played.
        if score == 'np':
            return {}

        
        # Process day before month. (huh? why?)
        if day.strip():
            self.day = int(day)

        if month.strip():
            self.month = int(month)

            if self.month >= 8:
                self.year = start_year
            else:
                self.year = end_year

        d = datetime.datetime(self.year, self.month, self.day)

        if score in ('forfeit loss', 'forfeit win', 'awarded', ''):
            return {}

        team_score,  opponent_score = [int(e) for e in score.split(',')]

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


