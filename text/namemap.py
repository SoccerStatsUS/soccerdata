import datetime
import os


p = '/home/chris/www/soccerdata/data/mappings/team_name'


def correct_date(s, start=True):

    if '/' in s:
        month, day, year = [int(e) for e in s.split('/')]
        d = datetime.datetime(year, month, day)
    else:
        year = int(s)
        if start:
            d = datetime.datetime(year, 1, 1)
        else:
            d = datetime.datetime(year, 12, 31)

    return d

    

    

def load():
    files = os.listdir(p)

    l = []
    
    for e in files:
        px = os.path.join(p, e)
        l.extend(process_name_map_file(px))
    return l
            
def process_name_map_file(p):
    f = open(p)
    
    nm = []
    
    for line in f:
        if line.strip() and not line.startswith("*"):
            fields = line.split(',')
            if len(fields) == 3:
                from_name, to_name, start = fields
                end = start
            elif len(fields) == 4:
                from_name, to_name, start, end = fields
            else:
                import pdb; pdb.set_trace()

            start = correct_date(start, start=True)
            end = correct_date(end, start=False)

            nm.append({
                    'from_name': from_name.strip(),
                    'to_name': to_name.strip(),
                    'start': start,
                    'end': end,
                    })
    return nm


if __name__ == "__main__":
    print load()
