# Load MLS stats that I kept up to 2004.

import os

from soccerdata.alias import get_team
from soccerdata.cache import data_cache

DIR = '/home/chris/www/soccerdata/data/stats'

if not os.path.exists(DIR):
    DIR = "/Users/chrisedgemon/www/soccerdata/data/stats"

#@data_cache
def process_all_chris_stats():

    l = []
    l.extend(process_stats("mls_stats.csv", "MLS"))
    l.extend(process_stats("pdl_stats.csv", "PDL"))
    l.extend(process_stats("psl_stats.csv", "PSL"))
    l.extend(process_stats("usl_one_stats.csv", "USL-1"))
    return l
    


def process_name(s):
    if ',' not in s:
        return s

    mapping = {
        'Da Silva-Sarafim, Jr, Edivaldo': 'Da Silva-Sarafim Jr, Edivaldo',
        'Novas, Lomonaca, Ignacio': 'Novas, Ignacio',
        'Kato, Hajime,': 'Kato, Hajime',
        'Kolba, JR., Thoms': 'Kolba Jr., Thomas',
        'Fragoso-Gonzalez, Jr, Pedro': 'Fragoso-Gonzalez Jr, Pedro',
        }

    if s in mapping:
            s = mapping[s]

    try:
        last, first = name = s.split(',') # Assume no 2-comma names.    
    except:
        import pdb; pdb.set_trace()
    name = first + ' ' + last    
    return name.strip()



def process_stats(fn, competition):

    def process_line(line):
        # clean this up.
        fields = line.split('\t')
        d = dict(zip(header, fields))
        d['name'] = process_name(d['name'])
        d['competition'] = competition
        d['season'] = d.pop('year')

        try:
            d['team'] = get_team(d['team'])
        except:
            import pdb; pdb.set_trace()
            
        for k in 'games_played', 'games_started', 'minutes', 'goals', 'assists', 'shots', 'shots_on_goal', \
                'blocks', 'fouls_committed', 'fouls_suffered', 'offsides', 'pk_goals', 'pk_attempts', 'pks_drawn', \
                'pks_committed':
            if k in d:
                v = d[k]
                if v == '':
                    v = 0
                elif v == '?':
                    pass
                else:
                    try:
                        d[k] = int(v)
                    except ValueError:
                        print v

            if 'position' in d:
                d.pop('position')
            if 'points' in d:
                d.pop('points')
        return d

    path = os.path.join(DIR, fn)
    lines = open(path).read().strip().split('\n')
    header = lines[0].split('\t')
    return [process_line(line) for line in lines[1:]]


def load_chris_stats():
    return process_stats(STATS_PATH)
        
if __name__ == "__main__":
    process_all_chris_stats()

