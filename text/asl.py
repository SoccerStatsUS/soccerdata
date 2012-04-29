# Process Golden Age ASL scores.
# Stats not working yet.

import datetime
import re

from soccerdata.alias import get_team, get_name

games_filename = '/home/chris/www/soccerdata/data/scores/asl.csv'
stats_filename = '/home/chris/www/soccerdata/data/stats/aslstats.csv'
bios_filename = '/home/chris/www/soccerdata/data/people/asl_bios.csv'


def get_full_name_stats(team, season):

    TEAM_HISTORY_TUPLES = [
        #Uniques
        ('B. Hakoah', [], 'Brooklyn Hakoah'),
        ('B/Newark', [], '?'),
        ('Bethlehem', [], 'Bethlehem Steel'),
        ('Brooklyn', [], 'Brooklyn Wanderers'),
        ('Fleischer', [], 'Fleisher Yarn'), # I misspelled Fleisher in Excel.
        ('Hakoah', [], 'Hakoah All-Stars'),
        ('Harrison', [], 'Harrison Soccer Club'),
        ('Hartford', [], 'Hartford Americans'),
        ('Holyoke', [], 'Holyoke Falcons'),
        ('Indiana', [], 'Indiana Flooring'),
        ('J&P Coats', [], 'J & P Coats'),
        ('NY Americans', [], 'New York Americans'),
        ('NY Giants', [], 'New York Giants'),
        ('NY Nationals', [], 'New York Nationals'),
        ('NY Yankees', [], 'New York Yankees'),
        ('New Bedford', [], 'New Bedford Whalers'),
        ('New York', [], 'New York Field Club'), # Different teams?
        ('New York FC', [], 'New York Field Club'), # Different teams?
        ('New York SC', [], 'New York Soccer Club'),
        ('Paterson', [], 'Paterson Silk Sox'),
        ('Pawtucket', [], 'Pawtucket Rangers'),
        ('Shawsheen', [], 'Shawsheen Indians'),
        ('Springfield', [], 'Springfield Babes'),
        ('Todd', [], 'Todd Shipyards F.C.'),

        #Complicateds
        # 'Bridgeport', # Bridgeport is missing or something.
        ('Boston', ['1924-1925', '1925-1926', '1926-1927', '1927-1928', '1928-1929'], 'Boston Wonder Workers'),
        ('Boston', ['1929 Fall', '1929-1930', '1931 Fall', '1931 Spring'], 'Boston Bears'),
        ('Fall River', ['1921-1922'], 'Fall River United'),
        ('Fall River', ['1922-1923', '1923-1924', '1924-1925', '1925-1926', '1926-1927', '1927-1928', '1928-1929', '1929 Fall', '1929-1930', '1930 Fall'], 'Fall River Marksmen'),
        ('Fall River', ['1931 Fall', '1931 Spring', '1932 Fall'], 'Fall River Football Club'),
        ('Jersey City', ['1921-1922'], 'Jersey City Celtics'),
        ('Jersey City', ['1925-1926'], 'Jersey City ?'), # Can't find.
        ('Jersey City', ['1928-1929'], 'Jersey City'),
        ('Newark', ['1922-1923', '1923-1924', '1924-1925', '1925-1926', '1926-1927', '1927-1928', '1928-1929', '1929 Fall', '1929-1930'], 'Newark Skeeters'),
        ('Newark', ['1930 Fall', '1931 Fall', '1931 Spring'], 'Newark Americans'),
        ('Philadelphia', ['1921-1922', '1922-1923', '1923-1924', '1924-1925', '1925-1926', '1926-1927', '1928-1929', '1929 Fall'], 'Philadelphia Field Club'),
        ('Philadelphia', ['1927-1928'], 'Philadelphia Celtic'),
        ('Providence', ['1924-1925', '1925-1926', '1926-1927', '1927-1928'], 'Providence Clamdiggers'),
        ('Providence', ['1928-1929', '1929 Fall', '1929-1930', '1930 Fall'], 'Providence Gold Bugs')
        ]

    
    team_matches = [e for e in TEAM_HISTORY_TUPLES if e[0] == team]

    if len(team_matches) == 0:
        print "Fail: %s" % team
        return team
    elif len(team_matches) == 1:
        assert team_matches[0][1] == []
        return team_matches[0][2]
    else:
        for t, seasons, full_name in team_matches:
            if season in seasons:
                return full_name

    import pdb; pdb.set_trace()
    x = 5
    


# These should be merged into get_team?
team_map = {
    'J&P Coats': 'J & P Coats',
    'NY Giants': 'New York Giants',
    'New York National Giants': 'New York Giants',
    'Fleischer': 'Fleisher Yarn',
    'Fleischer Yarn': 'Fleisher Yarn',

    'Philadelphia 1928-1929': 'Philadelphia Field Club',
    'NY Nationals': 'New York Nationals',
    'Abbot W.': 'Abbot Worsted',
    'Holley C.': 'Holley Carburetor',
    'Yonkers Th.': 'Yonkers Thistle',
    'Scullin St.': 'Scullin Steels',
    'Hispano': 'Brooklyn Hispano',
    'Bricklayers': 'Bricklayers FC',
    'NY Yankees': 'New York Yankees',
    'NY Americans': 'New York Americans',
    'Prospect H.': 'Prospect Hill FC',
    'Bethlehem': 'Bethlehem Steel',

    # These are just so the build script doesn't report an error.
    # Move these to a different object.
    'Brooklyn FC': 'Brooklyn FC',
    'Ben Millers': 'Ben Millers',
    'Pawtucket Rangers': 'Pawtucket Rangers',
    'Fall River Marksmen': 'Fall River Marksmen',
    'Providence Gold Bugs': 'Providence Gold Bugs',
    'Bridgeport Hungaria': 'Bridgeport Hungaria',
    'New York SC': 'New York SC',
    'New York Giants': 'New York Giants',
    'Newark 1929-1930': 'Newark 1929-1930',
    'Boston 1929-1930': 'Boston 1929-1930',
    'Boston Wonder Workers': 'Boston Wonder Workers',
    'Boston Bears': 'Boston Bears',
    'Brooklyn Wanderers': 'Brooklyn Wanderers',
    'Brooklyn Hakoah': 'Brooklyn Hakoah',
    'New York Nationals': 'New York Nationals',
    'New Bedford Whalers': 'New Bedford Whalers',
    'Bridgeport Bears': 'Bridgeport Bears',
    'Philadelphia 1929 Fall': 'Philadelphia 1929 Fall',
    'Bridgeport Bears': 'Bridgeport Bears',
    
}

competition_map = {
    'ASL': 'American Soccer League (1921-1933)',
    'ASA Cup': 'American Cup',
    'AFA Cup': 'American Cup',
    }

LEWIS_CUP_YEARS = set([
    '1924-1925',
    '1925-1926',
    '1926-1927',
    '1927-1928',
    '1928-1929',
    '1929-1930',
    ])


        



def process_bios():
    f = open(bios_filename)

    l = []
    for line in f:
        fields = line.split("\t") # 9 fields
        name, birthplace, bmonth, bday, byear, deathplace, dmonth, dday, dyear = fields

        if bmonth:
            try:
                birthdate = datetime.date(int(byear), int(bmonth), int(bday))
            except:
                print name, byear, bmonth, bday 
                birthdate = None
        else:
            birthdate = None
            
        if dmonth:
            try:
                deathdate = datetime.date(int(dyear), int(dmonth), int(dday))
            except:
                print name, dyear, dmonth, dday 
                deathdate = None

        else:
            deathdate = None

        l.append({
                'name': name,
                'birthdate': birthdate,
                'birthplace': birthplace,
                'deathdate': deathdate,
                'deathplace': deathplace,
                })

    return l
            
        
        


def process_stats():
    f = open(stats_filename)
    l = []
    for line in f:
        lx = load_stat(line)
        l.append(lx)
    return l



def load_stat(line):
    fields = line.split("\t")
    name, team, season = fields[:3]

    def convert(n):
        if n.strip():
            try:
                return int(n)
            except:
                import pdb; pdb.set_trace()
                x = 5
        return 0

    stats = [convert(e) for e in fields[3:]]

    season_games, cup_games, other_cup_games, season_goals, cup_goals, other_cup_goals = stats


    if "-" in season:
        start, end = season.split("-")
        season = "19%s-19%s" % (start, end)

    team_name = get_full_name_stats(team, season)

    # Get canonical name.
    name = get_name(name)
    
    l = []
    l.append({
            'name': name,
            'team': team_name,
            'season': season,
            'competition': 'American Soccer League (1921-1933)',
            'games_played': season_games,
            'goals': season_goals,
            })


    if cup_games or cup_goals:

        if season in ('1930 Fall', '1931 Spring'):
            sx = '1931'
        elif season in ('1931 Fall', '1932 Spring', '1932'):
            sx = '1932'

        else:
            try:
                sx = season.split("-")[1]
            except:
                import pdb; pdb.set_trace()

        l.append({
                'name': name,
                'team': team_name,
                'season': sx,
                'competition': 'U.S. Open Cup',
                'games_played': cup_games,
                'goals': cup_goals,
                })

    if other_cup_games or other_cup_goals:
        if season in LEWIS_CUP_YEARS:
            other_cup = "Lewis Cup"
            oc_season = season.split("-")[1]
        else:
            other_cup = "American Cup"
            oc_season = season
            print season, name, team

        l.append({
                'name': name,
                'team': team_name,
                'season': oc_season,
                'competition': other_cup,
                'games_played': other_cup_games,
                'goals': other_cup_goals,
                })
        
    return l



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


STANDINGS_DICT = get_standings_dict()

def get_full_name(name, competition, season):
    """
    Get the relevant team name based on the competition and season a team played in.
    e.g., convert New York to New York Giants
    """
    
    name = name.strip()

    # Check direct mapping first.
    if name in team_map:
        return team_map.get(name, name)

    # Get teams that played in a given season.
    ncompetition = competition.replace("Playoffs", '').strip()
    nseason = season.replace("Playoffs", '').strip()



    try:
        names = STANDINGS_DICT[(ncompetition, nseason)]
    except:
        names = []
    
    for e in names:
        if e.startswith(name):
            return e

    if nseason == '1927-1928':
        return get_full_name(name, competition, '1927-1928 First Half')


    # Need to figure out how to handle these? Bummer.
    # Seems like I'm using the wrong season.
    if nseason == '1929 First Half':
        return get_full_name(name, competition, '1928-1929 First Half')


    #import pdb; pdb.set_trace()
    print "name match failed on %s, competition: %s (%s) " % (name, competition, season)
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
            print "Ten fields for some reason?"
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
            'team1': home_team,
            'team2': away_team,
            'team1_score': home_score,
            'team2_score': away_score,
            'home_team': home_team,
            }


if __name__ == "__main__":
    print process_stats()
    #print process_bios()


