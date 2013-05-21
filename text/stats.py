#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


# Load stats from excel files.

import os


DIR = '/home/chris/www/soccerdata/data/stats'

if not os.path.exists(DIR):
    DIR = "/Users/chrisedgemon/www/soccerdata/data/stats"


def process_mls_2012_stats():
    return process_stats("mls.stats.2012.csv", "Major League Soccer", source='mlssoccer.com')


def process_mls_coach_stats():
    return process_stats("mls_coaches.csv", "Major League Soccer", source='mlssoccer.com')

def process_nasl_stats():
    return process_stats("nasl.csv", format_name=False, source='nasljerseys.com')

def process_misl_stats():
    return process_stats("misl.csv", format_name=False, source='nasljerseys.com')

def process_pdl_stats():
    l = []
    for e in range(2003, 2013):
        l.extend(process_stats("pdl/%s" % e, "USL Premier Developmental League"))
    return l


def process_usl_stats():
    l = []


    l.extend(process_stats("usl1_19972005.csv", "USL First Division"))
    l.extend(process_stats("usl1_20062007.csv", "USL First Division"))
    l.extend(process_stats("usl1_20082009.csv", "USL First Division"))
    l.extend(process_stats("psl_stats.csv", "USL Second Division"))
    l.extend(process_stats("usl2_20052009.csv", "USL Second Division"))
    l.extend(process_stats("usl2/2011", "USL Pro"))
    l.extend(process_stats("usl2/2012", "USL Pro"))
    
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
    if '*' in name:
        import pdb; pdb.set_trace()
    name = name.replace("*", "")
    return name.strip()



def process_stats(fn, competition=None, format_name=True, source=None):

    def preprocess_line(line):
        # Should probably just process these text files.
        line = line.replace('\xa0', '')
        line = line.replace('\xc2', '')
        
        # Remove *'s from nasl stats.
        line = line.replace("*", "")
        line = line.strip()
        return line


    def stat_fixes(d):
        # Incorrect line in naslmisl.csv
        if d.get('name') == 'Santiago Formoso':
            if d.get('games_played') == 'D':
                d.update({'games_played': '5', 'goals': '0'})
        return d
                         
    def process_line(line):
        line = preprocess_line(line)

        if not line:
            return {}

        fields = line.split('\t')
        d = dict(zip(header, fields))
        d = stat_fixes(d)
        

        if 'name' not in d:
            return {}

        if not d['name']:
            return {}


        if format_name:
            d['name'] = process_name(d['name'])

        if competition is not None:
            d['competition'] = competition

        if source is not None:
            d['source'] = source

        if 'year' in d:
            d['season'] = d.pop('year')
        else:
            try:
                d['season'] = d['season']
            except:
                import pdb; pdb.set_trace()



        if 'games' in d:
            d['games_played'] = d.pop('games')
            
        for k in 'games_played', 'games_started', 'minutes', 'goals', 'assists', 'shots', 'shots_on_goal', \
                'blocks', 'fouls_committed', 'fouls_suffered', 'offsides', 'pk_goals', 'pk_attempts', 'pks_drawn', \
                'pks_committed':
            if k in d:
                v = d[k]
                v = v.strip()

                if v in ('', '-'):
                    v = 0
                elif v == '?':
                    v = None
                else:
                    try:
                        d[k] = int(v)
                    except ValueError:
                        print v

            if 'position' in d:
                d.pop('position')
            if 'points' in d:
                d.pop('points')

        d['position'] = ''
        return d

    path = os.path.join(DIR, fn)
    lines = open(path).read().strip().split('\n')
    header = lines[0].split('\t')
    l = [process_line(line) for line in lines[1:]]
    return [e for e in l if e]


if __name__ == "__main__":
    print process_mls_stats()
    
