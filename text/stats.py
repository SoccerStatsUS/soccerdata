# Load MLS stats that I kept up to 2004.

import os

from soccerdata.cache import data_cache

DIR = '/home/chris/www/soccerdata/data/stats'

if not os.path.exists(DIR):
    DIR = "/Users/chrisedgemon/www/soccerdata/data/stats"


def process_mls_stats():
    return process_stats("mls_stats.csv", "Major League Soccer")

def process_nasl_stats():
    return process_stats("naslmisl.csv", format_name=False)

#@data_cache
def process_usl_stats():
    l = []
    l.extend(process_stats("usl1_19972005.csv", "USL First Division"))
    l.extend(process_stats("usl1_20062007.csv", "USL First Division"))
    l.extend(process_stats("usl1_20082009.csv", "USL First Division"))
    l.extend(process_stats("psl_stats.csv", "USL Second Division"))
    l.extend(process_stats("pdl_stats.csv", "USL Premier Developmental League"))
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
        last, first = [e.strip() for e in s.split(',')] # Assume no 2-comma names.    
    except:
        import pdb; pdb.set_trace()
    name = first + ' ' + last
    return name.strip()



def process_stats(fn, competition=None, format_name=True):

    def fixes(d):
        # Incorrect line in naslmisl.csv
        if d.get('name') == 'Santiago Formoso':
            if d.get('games_played') == 'D':
                d.update({'games_played': '5', 'goals': '0'})
        return d
                         
    def process_line(line):
        # clean this up.

        if not line.strip():
            return {}

        fields = line.split('\t')
        d = dict(zip(header, fields))
        d = fixes(d)
        

        if 'name' not in d:
            return {}

        if not d['name']:
            return {}
        


        if format_name:
            d['name'] = process_name(d['name'])

        if competition is not None:
            d['competition'] = competition

        d['team'] = d['team']

        if 'year' in d:
            d['season'] = d.pop('year')
        else:
            d['season'] = d['season']



        if 'games' in d:
            d['games_played'] = d.pop('games')
            
        for k in 'games_played', 'games_started', 'minutes', 'goals', 'assists', 'shots', 'shots_on_goal', \
                'blocks', 'fouls_committed', 'fouls_suffered', 'offsides', 'pk_goals', 'pk_attempts', 'pks_drawn', \
                'pks_committed':
            if k in d:
                v = d[k]
                # Blank character showing up in naslmisl.csv
                v = v.replace('\xc2\xa0', '')

                if v in ('', '-'):
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
    l = [process_line(line) for line in lines[1:]]
    return [e for e in l if e]


if __name__ == "__main__":
    print process_nasl_stats()
    
