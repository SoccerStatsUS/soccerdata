

# Process a variety of standings files. 

# Excel style:
# Houston Stars	North American Soccer League	1968	Gulf Division	32	14	6	12	150	58	41			
# Wikipedia Style
# 3       Moctezuma       18      9       3       6       43      34      21

import os
from soccerdata.cache import data_cache

DIR = '/home/chris/www/soccerdata/data/'

if not os.path.exists(DIR):
    DIR = "/Users/chrisedgemon/www/soccerdata/data/"



def int_or_none(e):
    if e:
        try:
            return int(e)
        except:
            import pdb; pdb.set_trace()

    return None



def process_excel_standings(filename):
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
        

        return {
            'team': team,
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


def process_standings_file(p, delimiter):
    full_path = os.path.join('/home/chris/www/soccerdata/data/standings', p)
    f = open(full_path)
    sp = StandingProcessor(delimiter)
    for line in f:
        sp.process_line(line)

    return sp.standings
        
    


class StandingProcessor(object):
    """
    An object to feed lines of text to.
    Retains a basic memory
    """




    def __init__(self, delimiter):
        self.delimiter = delimiter
        self.competition = None
        self.season = None
        self.group = ''

        self.sources = []

        self.standings = []


    def process_line(self, line):
        """
        Do a lot of processing.
        """
        
        line = line.strip()

        if not line:
            return

        # Represents a comment.
        if line.startswith("*"):
            return

        # Set the competition.
        if line.startswith("Competition:"):
            self.competition = line.split("Competition:")[1].strip()
            self.group = ''
            return

        if line.startswith("Season:"):
            self.season = line.split("Season:")[1].strip()
            self.group = ''
            return

        if line.startswith("Round:"):
            #self.season = line.split("Season:")[1].strip()
            #self.group = ''
            return

        if line.startswith("Region:"):
            #self.season = line.split("Season:")[1].strip()
            #self.group = ''
            return

        # Set the round.
        if line.startswith("Group"):
            self.group = line.split("Group:")[1].strip()
            return

        # This is definitely a standing now.
        if line.strip():
            self.process_standings(line)


    def process_standings(self, line):

        fields = line.split(self.delimiter)
        fields = [e.strip() for e in fields if e.strip()]


        # This is not attractive or good.
        # A good idea to standardize standings.
        if len(fields) == 9:
            position, team, games, wins, ties, losses, points, goals_for, goals_against = fields
        elif len(fields) == 8:
            team, games, wins, ties, losses, goals_for, goals_against, points = fields
        else:
            import pdb; pdb.set_trace()
    


        shootout_wins = shootout_losses = None
        self.standings.append({
                'competition': self.competition,
                'season': self.season,
                'group': self.group,

                'team': team,

                'games': int(games),
                'wins': int(wins),
                'ties': int(ties),
                'losses': int(losses),
                'points': int_or_none(points),

                'goals_for': int_or_none(goals_for),
                'goals_against': int_or_none(goals_against),
                'shootout_wins': int_or_none(shootout_wins),
                'shootout_losses': int_or_none(shootout_losses),
                'final': True,
                })


if __name__ == "__main__":
    print process_file("/home/chris/www/soccerdata/data/standings/domestic/country/guatemala", ';')
