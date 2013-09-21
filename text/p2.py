
import datetime

# Process positions.



def process_file(p, position, delimiter=','):

    f = open(p)
    
    data = []

    for line in f:
        p = process_line(line, delimiter)
        if p:
            p['name'] = position
            data.append(p)

    return data
        


def process_line(line, delimiter):
    if not line.strip() or line.startswith('*'):
        return {}

    if line.startswith('Source'):
        return {}
        

    try:
        name, team, start, end = line.split(delimiter)
    except:
        import pdb; pdb.set_trace()

    if end.strip():
        if end.strip() == 'present':
            dtend = None
        elif '/' not in end:
            dtend = datetime.datetime(int(end), 12, 31)
            
        else:
            month, day, year = [int(e) for e in end.split('/')]
            try:
                dtend = datetime.datetime(year, month, day)
            except:
                import pdb; pdb.set_trace()

    else:
        dtend = None

    if '/' not in start:
        dtstart = datetime.datetime(int(start), 1, 1)
    else:
        try:
            month, day, year = [int(e) for e in start.split('/')]
        except:
            import pdb; pdb.set_trace()
        dtstart = datetime.datetime(year, month, day)

    return {
        'person': name.strip(),
        'team': team.strip(),
        'start': dtstart,
        'end': dtend,
        }

            

if __name__ == "__main__":
    process_file("/home/chris/www/soccerdata/data/jobs/world/england", 'Head Coach')
    print(process_file("/home/chris/www/soccerdata/data/jobs/usa/d1/mls/head", 'Head Coach', delimiter=';'))

