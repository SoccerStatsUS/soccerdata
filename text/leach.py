# Process Ltrack files from Scott Leach.



import datetime
import os

from soccerdata.alias import get_team, get_name
#from soccerdata.cache import data_cache


DIR = '/home/chris/www/soccerdata/data/leach'


def format_name(s):
    fields = [e.strip() for e in s.split(",", 1)]

    if len(fields) == 1:
        ns = fields[0]
    elif len(fields) == 2:
        ns = "%s %s" % (fields[1], fields[0])
    return get_name(ns)
        



def process_goals_file(fn, season):
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
    l = []
    directory = os.path.join(DIR, 'goals')
    for fn in os.listdir(directory):
        p = os.path.join(directory, fn)
        season = fn.split(".")[0]
        goals = process_goals_file(p, season)
        l.extend(goals)
    return l
        

if __name__ == "__main__":
    print process_goals()
    
    
