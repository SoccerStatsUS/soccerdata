import datetime
import os

from soccerdata.utils import pounds_to_kg, inches_to_cm


# Scrape bios compiled by me.
# These should be turned into YAML and this code discarded.

DIR = '/home/chris/www/soccerdata/data/people'



def process_name(s):
    """
    All names should be in normal form. 
    None of this last name first nonsense.
    """

    if ',' not in s:
        return s

    # Multiple comma names.
    mapping = {
        'Da Silva-Sarafim, Jr, Edivaldo': 'Da Silva-Sarafim Jr, Edivaldo',
        'Novas, Lomonaca, Ignacio': 'Novas, Ignacio',
        'Kato, Hajime,': 'Kato, Hajime',
        'Kolba, JR., Thoms': 'Kolba Jr., Thomas',
        'Fragoso-Gonzalez, Jr, Pedro': 'Fragoso-Gonzalez Jr, Pedro',
        }

    if s in mapping:
        s = mapping[s]

    last, first = name = s.split(',') # Assume no 2-comma names.    
    name = first + ' ' + last    
    return name.strip()


def load_all_bios():
    """
    Load all bio files.
    This is just MLS/USL bios compiled by me a long time ago.
    """
    files = os.listdir(DIR)
    l = []
    for f in files:
        p = os.path.join(DIR, f)
        l.extend(load_bios(p))
    return l
        

def load_bios(p):
    """
    Load bio data.
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

        if 'feet' in d:
            cm = inches_to_cm(feet=d['feet'], inches=d['inches'])
            d['height'] = cm

        if 'pounds' in d:
            d['weight'] = pounds_to_kg(d['pounds'])
            

        for e in 'year', 'month', 'day', 'feet', 'inches', 'pounds', '':
            if e in d:
                d.pop(e)

        return d

    lines = open(p).read().strip().split('\n')
    header = lines[0].split('\t')
    bios = [process_line(line) for line in lines[1:]]
    return [e for e in bios if e]


def bios_yaml(p):
    # Convert bios to yaml.
    import yaml
    s = yaml.dump(load_all_bios())
    f = open(p, 'w')
    f.write(s)
    f.close()


if __name__ == "__main__":
    print bios_yaml()
    



    

        
        
