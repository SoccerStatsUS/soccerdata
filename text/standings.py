
import os



from soccerdata.cache import data_cache

from soccerdata.alias import get_team

DIR = '/home/chris/www/soccerdata/data/'

if not os.path.exists(DIR):
    DIR = "/Users/chrisedgemon/www/soccerdata/data/"


def process_standings_file(filename):
    
    return lambda: process_standings(filename)


def process_standings(filename):
    # Load standings from standings file.

    p = os.path.join(DIR, "standings", filename)
    f = open(p)
    lines = f.read().split('\n')

    def process_line(line):
        line = line.strip()
        if not line:
            return {}

        fields = line.split("\t")

        goals_for = goals_against = None
        shootout_wins = shootout_losses = None

        if len(fields) < 8:
            import pdb; pdb.set_trace()
            print fields
            return {}

        if len(fields) == 8:
            team, competition, season, division, games, wins, ties, losses = fields
            points = None

        elif len(fields) == 9:
            team, competition, season, division, games, wins, ties, losses, points = fields

        else:
            team, competition, season, division, games, wins, ties, losses, points, goals_for, goals_against = fields[:11]

        # No data for these yet.
        if (competition, season) == ('National Premier Soccer League', '2008'):
            return {}



        if len(fields) == 12:
            shootout_wins = fields[11]
        if len(fields) == 13:
            shootout_wins, shootout_losses = fields[11:]
        
        def int_or_none(e):
            if e:
                return int(e)
            return None

        return {
            'name': get_team(team.strip()),
            'competition': competition,
            'division': division,
            'season': season,
            'games': int(games),
            'wins': int(wins),
            'ties': int_or_none(ties),
            'losses': int(losses),
            'points': int_or_none(points),
            'goals_for': int_or_none(goals_for),
            'goals_against': int_or_none(goals_against),
            'shootout_wins': int_or_none(shootout_wins),
            'shootout_losses': int_or_none(shootout_losses),
            }
        
    l = [process_line(line) for line in lines]
    return [e for e in l if e]

if __name__ == "__main__":
    print process_standings()
    
        
    
