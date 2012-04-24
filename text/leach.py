# Process Ltrack files from Scott Leach.



import datetime
import os

from soccerdata.alias import get_team, get_name
#from soccerdata.cache import data_cache


DIR = '/home/chris/www/soccerdata/data/leach'


def format_name(s):
    # Reverse a name from Donovan, Landon to Landon Donovan.
    fields = [e.strip() for e in s.split(",", 1)]

    if len(fields) == 1:
        ns = fields[0]
    elif len(fields) == 2:
        ns = "%s %s" % (fields[1], fields[0])
    return get_name(ns)


def make_team_to_competition_dict():
    # Create a dict mapping a team name and season to a competition.
    from soccerdata.mongo import soccer_db

    d = {}
    for e in soccer_db.standings.find():
        key = (e['name'], e['season'])
        if key not in d:
            d[key] = [e['competition']]
    return d


TEAM_COMPETITION_DICT = make_team_to_competition_dict()


def process_lineups_file(fn, season):
    text = open(fn).read().replace('\r', '').split('\n')
    header = text[0]
    data = text[1:]

    l = []
    
    for line in data:
        s = line.strip()
        if s:
            fields = line.split('\t')

            comp, date_string, home_team, away_team, team, name, rating, on, off, yc1, yc2, rc, yc, time, substituted, time_on, time_off, yc_time = fields

            month, day, year = [int(e) for e in date_string.split("/")]
            d = datetime.datetime(year, month, day)

            t = get_team(team)

            if comp == 'LGE':
                competitions = TEAM_COMPETITION_DICT[(t, season)]
                if len(competitions) > 1:
                    import pdb; pdb.set_trace()
                else:
                    competition = competitions[0]

            n = get_name(format_name(name))


            l.append({
                    'name': n,
                    'on': on,
                    'off': off,
                    'team': t,
                    'date': d,
                    'season': season,
                    'competition': competition,
                    })


    return l
        

def process_games_file(fn, season):
    """
    Process a games file.
    """
    text = open(fn).read().replace('\r', '').split('\n')
    header = text[0]
    data = text[1:]

    l = []
    
    for line in data:
        s = line.strip()
        if s:
            fields = line.split('\t')
            
            # 14 fields always
            date_string, home_team, away_team, home_score, away_score, attendance, competition_type, comp, comments, referee, awarded, _, _, _ = fields

            month, day, year = [int(e) for e in date_string.split("/")]
            d = datetime.datetime(year, month, day)

            team1 = get_team(home_team)
            team2 = get_team(away_team)

            if comp == 'LGE':
                competitions = TEAM_COMPETITION_DICT[(team1, season)]
                if len(competitions) > 1:
                    import pdb; pdb.set_trace()
                else:
                    competition = competitions[0]

            l.append({
                    'team1': team1,
                    'team2': team2,
                    'team1_score': int(home_score),
                    'team2_score': int(away_score),
                    'home_team': team1,
                    'competition': competition,
                    'season': season,
                    'date': d,
                    #'location': location,
                    'referee': format_name(referee),
                    })

    return l


def process_goals_file(fn, season):
    """
    Process a goal file.
    """

    text = open(fn).read().replace('\r', '').split('\n')
    header = text[0]
    data = text[1:]

    l = []

    for line in data:
        s = line.strip()
        if s:
            fields = line.split('\t')

            # 11 fields always
            player, team, _, _, date_string, minute, _, league, assist1, assist2, _ = fields

            month, day, year = [int(e) for e in date_string.split("/")]

            d = datetime.datetime(year, month, day)

            if assist1 and assist2:
                assists = [format_name(assist1), format_name(assist2)]
            elif assist1:
                assists = [format_name(assist1)]
            else:
                assists = []

            l.append({
                    'goal': format_name(player),
                    'minute': int(minute),
                    'team': get_team(team),
                    'type': 'normal',
                    'date': d,
                    'assists': assists,
                    })
    return l
                    


def process_goals():
    """
    Process all goal data from Leach.
    """
    l = []
    directory = os.path.join(DIR, 'goals')
    for fn in os.listdir(directory):
        p = os.path.join(directory, fn)
        season = fn.split(".")[0]
        data = process_goals_file(p, season)
        l.extend(data)
    return l
        



def process_games():
    """
    Process all game data from Leach.
    """
    l = []
    directory = os.path.join(DIR, 'games')
    for fn in os.listdir(directory):
        p = os.path.join(directory, fn)
        season = fn.split(".")[0]
        data = process_games_file(p, season)
        l.extend(data)
    return l
     


def process_lineups():
    """
    Process all game data from Leach.
    """
    l = []
    directory = os.path.join(DIR, 'squads')
    for fn in os.listdir(directory):
        p = os.path.join(directory, fn)
        season = fn.split(".")[0]
        data = process_lineups_file(p, season)
        l.extend(data)
    return l
        

if __name__ == "__main__":
    print process_lineups()
    #print process_games()
    #print process_goals()
    
    
