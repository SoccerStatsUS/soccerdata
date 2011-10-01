import datetime
import os

# Scrape bios compiled by me.

DIR = '/home/chris/www/soccerdata/people'

if not os.path.exists(DIR):
    DIR = "/Users/chrisedgemon/www/soccerdata/data/people"

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


def merged_bios():
    # Fields
    # name

    # birthdate
    # nationality

    # height/weight - later
    # position - later

    bios = {}
    for e in load_all_bios():
        name = e['name']
        birthdate = e['birthdate']
        nationality = e['nationality']

        

        if name in bios:
            bd = bios[name]
            if bd['birthdate']:
                if birthdate:
                    try:
                        assert bd['birthdate'] == birthdate
                    except:
                        #import pdb; pdb.set_trace()
                        print name
                        continue
            else:
                bd['birthdate'] = birthdate

            if bd['nationality']:
                if nationality:
                    try:
                        assert bd['nationality'] == nationality
                    except:
                        #import pdb; pdb.set_trace()
                        print name
                        continue
            else:
                bd['nationality'] = nationality
            

        else:
            bios[name] = {
                'name': name,
                'birthdate': birthdate,
                'nationality': nationality,
                }

    return bios

            
        



def load_all_bios():
    files = os.listdir(DIR)
    l = []
    for f in files:
        p = os.path.join(DIR, f)
        l.extend(load_bios(p))
    return l
        

def load_bios(p):
    """
    Load my MLS bios data.
    """

    def process_line(line):

        if not line.strip():
            return {}

        # Remove trailing newline.
        if line.endswith("\n"):
            line = line[:-1]

        # Tab separated.
        items = line.split('\t')
        d = dict(zip(header, items))
        d['name'] = process_name(d['name'])

        if d['year'] and d['month'] and d['day']:
            # Repair inconsistent year handling.
            if int(d['year']) < 100:
                d['year'] = int(d['year']) + 1900

            d['birthdate'] = datetime.datetime(int(d['year']), int(d['month']), int(d['day']))
        else:
            d['birthdate'] = None

        for e in 'year', 'month', 'day':
            if e in d:
                d.pop(e)

        return d

    lines = open(p).read().strip().split('\n')
    header = lines[0].split('\t')
    bios = [process_line(line) for line in lines[1:]]
    return [e for e in bios if e]


if __name__ == "__main__":
    merged_bios()
    



    

        
        
