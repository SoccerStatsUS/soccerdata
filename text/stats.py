# Load MLS stats that I kept up to 2004.

import os

p = '/home/chris/www/soccerdata/data/mls_stats.csv'

if os.path.exists(p):
    STATS_PATH
else:
    STATS_PATH = "/Users/chrisedgemon/www/soccerdata/data/mls_stats.csv"


def process_stats(file):
    lines = open(file).read().strip().split('\n')
    header = lines[0].split('\t')

    stats = []
    for line in lines[1:]:
        fields = line.split('\t')
        d = dict(zip(header, fields))
        if ',' in d['name']:
            last, first = name = d['name'].split(',') # Assume no 2-comma names.
            name = first + ' ' + last
            d['name'] = name.strip()
            
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

            d.pop('position')
            d.pop('points')
            stats.append(d)
    return stats
        
if __name__ == "__main__":
    stats = process_stats(STATS_PATH)
    for e in stats:
        print e['name']
    

