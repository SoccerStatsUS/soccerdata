import datetime
import re

from soccerdata.alias import get_team, get_name

POSITIONS_PATH = '/home/chris/www/soccerdata/data/transactions/positions'

class PositionParser(object):
    def __init__(self):
        self.person = None
        self.name = None
        self.team = None

    def process_date_string(self, s):
        s = s.strip()
        if not s:
            return None

        m = re.match("(\d+)/(\d+)/(\d+)", s)
        if m:
            month, day, year = [int(e) for e in m.groups()]
        else:
            month, day, year = 1, 1, int(s)
        
        try:
            return datetime.datetime(year, month, day)
        except:
            import pdb; pdb.set_trace()
            x = 5


    def process_line(self, line):
        fields = line.split(",")
        person, name, team = [e.strip() for e in fields[:3]]

        start = end = None
        if len(fields) > 3:
            start = self.process_date_string(fields[3])
        if len(fields) > 4:
            # Make the end at the end of the year.
            end = self.process_date_string(fields[4])
            # Set end at the end of the year.
            if end:
                end = datetime.datetime(end.year + 1, end.month, end.day) - datetime.timedelta(days=1)

        if person:
            self.person = person
        if name:
            self.name = name
        if team:
            self.team = get_team(team)

        return {
            'person': self.person,
            'name': get_name(self.name),
            'team': self.team,
            'start': start,
            'end': end
            }




def process_positions():
    p = PositionParser()
    f = open(POSITIONS_PATH)
    l = []
    for e in f:
        l.append(p.process_line(e))
    return l


if __name__ == "__main__":
    print process_positions()



            
