#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


# Load stats from excel files.

import os

from soccerdata.settings import ROOT_DIR

STANDARD_DIR = os.path.join(ROOT_DIR, 'soccerdata/data/stats')
USD1_DIR = os.path.join(ROOT_DIR, 'usd1')

NCAA_DIR = os.path.join(ROOT_DIR, 'ncaa-data')


def process_misl_stats():
    return process_stats("indoor/misl", source='nasljerseys.com')

def process_nwsl_stats():
    nwsl_dir = os.path.join(ROOT_DIR, 'nwsl-data/data/stats')
    return process_stats("2013", source='nasljerseys.com', root=nwsl_dir, delimiter=';')

def process_mls_2012_stats():
    return process_stats("d1/2012", source='MLSSoccer.com')

def process_mls_2013_stats():
    return process_stats("data/stats/mls/2013", source='MLSSoccer.com', root=USD1_DIR, delimiter=';')

def process_ncaa_stats():
    l = []
    for e in [
        'akron', 
        'berkeley',
        #'boston_college',
        #'charlotte',
        'clemson',
        'coastal_carolina',
        'conn',
        #'furman',
        'indiana',
        'maryland',
        'nc_state',
        'new_mexico',
        'notre_dame',
        'ohio_state',
        'oregon_state',
        'rutgers',
        'ucla',
        'unc',
        'wake_forest',
        ]:
        l.extend(process_stats("stats/%s" % e, format_name=True, root=NCAA_DIR, delimiter=';'))
    
    return l


def process_mls_coach_stats():
    return process_stats("d1/mls.coaches", source='MLSSoccer.com')

def process_nasl_stats():
    return process_stats("d1/nasl", source='nasljerseys.com')

def process_misl_stats():
    return process_stats("indoor/misl", source='nasljerseys.com')


def process_usl1_stats():
    l = []
    l.extend(process_stats("d2/19972005", format_name=True))

    #for e in '06', '07', '08', '09', '11', '12':
    for e in '06', '07', '09':
        l.extend(process_stats("d2/20%s" % e, format_name=True))

    l.extend(process_stats("d2/2008", format_name=True, delimiter=';'))

    return l

def process_usl2_stats():
    l = []
    l.extend(process_stats("d3/psl", format_name=True))
    l.extend(process_stats("d3/20052009", format_name=True))
    for e in range(2010, 2013):
        l.extend(process_stats("d3/%s" % e, format_name=True))

    return l

def process_pdl_stats():
    l = []
    
    for e in range(2003, 2013):
        l.extend(process_stats("d4/%s" % e, format_name=True)) 

    s = process_stats("d4/pdl_2013", delimiter=";", format_name=True)
    l.extend(s)

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

    #import pdb; pdb.set_trace()

    try:
        last, first = [e.strip() for e in s.split(',')] # Assume no 2-comma names.    

    except:
        import pdb; pdb.set_trace()
    name = first + ' ' + last

    # What is this?
    if '*' in name:
        import pdb; pdb.set_trace()
    name = name.replace("*", "")

    # Clean and remove titles
    name = name.strip().title()

    return name


class StatsProcessor(object):
    

    def __init__(self, delimiter='\t', format_name=False):
        self.delimiter = delimiter
        self.header = None
        self.competition = None
        self.season = None
        self.source = None
        self.team = None

        self.format_name = format_name

        self.data = []



    def preprocess_line(self, line):
        # Should probably just process these text files.
        line = line.replace('\xa0', '')
        line = line.replace('\xc2', '')
        
        # Remove *'s from nasl stats.
        line = line.replace("*", "")
        line = line.strip()
        return line



    def process_line(self, line):

        if not line or line.startswith('*'):
            return

        line = self.preprocess_line(line)

        if line.startswith('Key:'):
            h = line.split('Key:')[1]
            self.header = [e.strip() for e in h.split(self.delimiter)]
            return

        if line.startswith('Team:'):
            self.team = line.split('Team:')[1]
            return


        if line.startswith('Competition:'):
            self.competition = line.split('Competition:')[1].strip()
            return

        if line.startswith('Season:'):
            self.season = line.split('Season:')[1].strip()
            return

        if line.startswith('BlockSource:'):
            self.source = line.split('BlockSource:')[1]
            return

        fields = line.split(self.delimiter)



        try:
            d = dict(zip(self.header, fields))
        except:
            import pdb; pdb.set_trace()

        #d = stat_fixes(d)


        if 'name' not in d:
            return {}

        if not d['name']:
            return {}

        if self.format_name:
            d['name'] = process_name(d['name'])

        if not d.get('team'):
            d['team'] = self.team

        #if competition is not None:

        d['source'] = self.source

        if self.competition and not d.get('competition'):
            d['competition'] = self.competition

        if self.season and not d.get('season'):
            d['season'] = self.season

        if 'year' in d:
            d['season'] = d.pop('year').strip()

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
                        v = int(v)
                    except ValueError:
                        import pdb; pdb.set_trace()
                        print(v)

                d[k] = v

        d['position'] = d['points'] = ''

        self.data.append(d)



def process_stats(fn, format_name=False, source=None, root=STANDARD_DIR, delimiter="\t"):
    sp = StatsProcessor(delimiter, format_name=format_name)
    path = os.path.join(root, fn)
    lines = open(path).read().strip().split('\n')    

    for line in lines:
        sp.process_line(line)

    return [e for e in sp.data if e]



if __name__ == "__main__":
    #print(process_nwsl_stats())
    process_mls_2012_stats()
    process_mls_coach_stats()
    process_nasl_stats()
    process_misl_stats()
    process_usl1_stats()
    process_usl2_stats()
    process_pdl_stats()
