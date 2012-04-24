import datetime
import re
import sys


# More cup data here:
# http://www.rsssf.com/tablesu/usa-allcuphist.html




def process_line(line):
    r = re.search('(?P<date>\d+\s+.*?\s+\d+)?\s+(?P<team1>.*)\s+(?P<score>\d-\d)\s+(?P<team2>.*)', line)
    d = r.groupdict()
    
    if d['date']:
        date = datetime.datetime.strptime(d['date'].strip(), "%Y %b %d")
    else:
        date = None

    home_score, away_score = [int(e) for e in d['score'].split('-')]
    home_team = d['team1'].split('(')[0].strip()
    away_team = d['team2'].split('(')[0].strip()
    
    return {
        'competition': 'U.S. Open Cup',
        'home_team': home_team,
        'away_team': away_team,
        'home_score': home_score,
        'away_score': away_score,
        'date': date,
        }

def process_finals():
    lines = open("open_cup_finals").read().split('\n')
    l = []
    for line in lines:
        if line:
            d = process_line(line)
            print d
            if d['date'] == None:
                d['date'] = l[-1]['date']
            l.append(d)
    return l

if __name__ == "__main__":
    print process_finals()
