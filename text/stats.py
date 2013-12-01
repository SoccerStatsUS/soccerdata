#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


# Load stats from excel files.

import os

from soccerdata.settings import ROOT_DIR

STANDARD_DIR = os.path.join(ROOT_DIR, 'soccerdata/data/stats')


def process_misl_stats():
    return process_stats("indoor/misl", format_name=False, source='nasljerseys.com')

def process_nwsl_stats():
    nwsl_dir = os.path.join(ROOT_DIR, 'nwsl-data/data/stats')
    return process_stats("2013", format_name=False, source='nasljerseys.com', root=nwsl_dir, delimiter=';')

def process_mls_2012_stats():
    return process_stats("d1/2012", source='MLSSoccer.com')

def process_mls_coach_stats():
    return process_stats("d1/mls.coaches", source='MLSSoccer.com')


def process_nasl_stats():
    return process_stats("d1/nasl", source='nasljerseys.com')

def process_misl_stats():
    return process_stats("indoor/misl", source='nasljerseys.com')


def process_usl1_stats():
    l = []
    l.extend(process_stats("d2/19972005"))

    #for e in '06', '07', '08', '09', '11', '12':
    for e in '06', '07', '08', '09':
        l.extend(process_stats("d2/20%s" % e))

    return l

def process_usl2_stats():
    l = []
    l.extend(process_stats("d3/psl", "USL Second Division"))
    l.extend(process_stats("d3/20052009", "USL Second Division"))
    for e in range(2010, 2013):
        l.extend(process_stats("d3/%s" % e, "USL Pro"))

    return l

def process_pdl_stats():
    l = []
    for e in range(2003, 2013):
        l.extend(process_stats("d4/%s" % e)) 
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





class StatsProcessor(object):
    

    def __init__(self, delimiter='\t'):
        self.delimiter = delimiter
        self.header = None
        self.competition = None
        self.season = None
        self.source = None
        self.team = None

        self.format_name = False

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
            self.competition = line.split('Competition:')[1]
            return

        if line.startswith('Season:'):
            self.season = line.split('Season:')[1]
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


        if self.season and not d.get('season'):
            d['season'] = self.season

        if self.competition and not d.get('competition'):
            d['competition'] = self.competition


        if 'year' in d:
            d['season'] = d.pop('year')

        """
        else:
            try:
                d['season'] = d['season']
            except:
                import pdb; pdb.set_trace()
        """



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
                        print(v)

            if 'position' in d:
                d.pop('position')
            if 'points' in d:
                d.pop('points')

        d['position'] = ''
        #return d
        self.data.append(d)



def process_stats(fn, format_name=True, source=None, root=STANDARD_DIR, delimiter="\t"):
    sp = StatsProcessor(delimiter)
    path = os.path.join(root, fn)
    lines = open(path).read().strip().split('\n')    

    for line in lines:
        sp.process_line(line)

    return [e for e in sp.data if e]

    

def process_stats_old(fn, format_name=True, source=None, root=STANDARD_DIR, delimiter="\t"):

    header = competition = None


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

        if line.startswith('Key:'):
            header = line.split('Key:')[1]
            return

        if line.startswith('Competition:'):
            competition = line.split('Competition:')[1]
            return

        line = preprocess_line(line)

        if not line:
            return {}



        fields = line.split(delimiter)
        d = dict(zip(header, fields))
        d = stat_fixes(d)
        

        if 'name' not in d:
            return {}

        if not d['name']:
            return {}


        if format_name:
            d['name'] = process_name(d['name'])

        #if competition is not None:
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
                        print(v)

            if 'position' in d:
                d.pop('position')
            if 'points' in d:
                d.pop('points')

        d['position'] = ''
        return d



    #header = lines[0].split(delimiter)

    path = os.path.join(root, fn)
    lines = open(path).read().strip().split('\n')

    l = [process_line(line) for line in lines[1:]]

    import pdb; pdb.set_trace()

    return [e for e in l if e]



if __name__ == "__main__":
    #print(process_nwsl_stats())
    process_mls_2012_stats()
    process_mls_coach_stats()
    process_nasl_stats()
    process_misl_stats()
    process_usl1_stats()
    process_usl2_stats()
    process_pdl_stats()
