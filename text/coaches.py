import datetime
import re

from soccerdata.alias.teams import get_team

POSITIONS_PATH = '/home/chris/www/soccerdata/data/transactions/td'

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
        return datetime.datetime(year, month, day)


    def process_line(self, line):
        fields = line.split(",")
        person, name, team = [e.strip() for e in fields[:3]]

        start = end = None
        if len(fields) > 3:
            start = self.process_date_string(fields[3])
        if len(fields) > 4:
            end = self.process_date_string(fields[4])

        if person:
            self.person = person
        if name:
            self.name = name
        if team:
            self.team = get_team(team)

        return {
            'person': self.person,
            'name': self.name,
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



            
