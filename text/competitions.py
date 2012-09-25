
import os


COMPETITIONS_DIR = '/home/chris/www/soccerdata/data/competitions/'

def load_competitions():
    l = []
    files = ['new']
    for fn in files:
        p = os.path.join(COMPETITIONS_DIR, fn)
        f = open(p)
        for line in f:
            if line.startswith('*'):
                continue

            if line.strip():
                fields = [e.strip() for e in line.split(';')]
                try:
                    name, abbreviation, code, international, ctype, level, scope, area = fields
                except:
                    import pdb; pdb.set_trace()

                if international.strip() == 'international':
                    ib = True
                else:
                    ib = False

                if level == '':
                    level = None
                else:
                    level = int(level)


                l.append({
                        'name': name,
                        'abbreviation': abbreviation,
                        'code': code,
                        'international': ib,
                        'ctype': ctype,
                        'level': level,
                        'scope': scope,
                        'area': area
                        })
    

    return l
