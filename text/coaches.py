# Should change this to positions.py

import datetime
import re

from soccerdata.alias import get_team, get_name

POSITIONS_PATH = '/home/chris/www/soccerdata/data/transactions/positions'

class PositionParser(object):
    """
    Parse position text file.
    e.g. Bruce Arena, Head Coach, DC United, 1996, 1998
    """
    # Empty person, position, or team fields will be repeated from the previous line.

    def __init__(self):
        self.person = None
        self.position = None
        self.team = None

    def process_date_string(self, s):
        s = s.strip()
        if not s:
            return None

        m = re.match("(\d+)/(\d+)/(\d+)", s) # something like 12/31/1989
        if m:
            month, day, year = [int(e) for e in m.groups()]
        else:
            month, day, year = 1, 1, int(s) # default to the first day of the year.
        
        return datetime.datetime(year, month, day)


    def process_line(self, line):
        # Does date handling and fills in empty fields if necessary.
        fields = line.split(",")
        person, position, team = [e.strip() for e in fields[:3]]

        start = end = None
        if len(fields) > 3:
            start = self.process_date_string(fields[3])
        if len(fields) > 4:
            end = self.process_date_string(fields[4])
            # Set end at the end of the year if appropriate.
            if end and end.month == 1 and end.day == 1:
                end = datetime.datetime(end.year + 1, end.month, end.day) - datetime.timedelta(days=1)

        if person:
            self.person = person
        if position:
            self.position = position
        if team:
            self.team = get_team(team)

        return {
            'person': get_name(self.person),
            'name': self.position,
            'team': get_team(self.team),
            'start': start,
            'end': end,
            }


def process_position_file(fn):
    """Process a file."""
    p = PositionParser()
    return [p.process_line(e) for e in open(fn)]

process_positions = lambda: process_position_file(POSITIONS_PATH)

if __name__ == "__main__":
    print process_positions()



            
