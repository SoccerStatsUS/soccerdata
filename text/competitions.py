
import os


COMPETITIONS_DIR = '/home/chris/www/soccerdata/data/competitions/'

def load_competitions():
    l = []
    files = ['domestic']
    for fn in files:
        p = os.path.join(COMPETITIONS_DIR, fn)
        f = open(p)
        for line in f:
            if line.strip():
                fields = [e.strip() for e in line.split(';')]
                name, abbreviation, ctype, scope, area = fields
                l.append({
                        'name': name,
                        'abbreviation': abbreviation,
                        'ctype': ctype,
                        'scope': scope,
                        'area': area,
                        })
    

    return l
