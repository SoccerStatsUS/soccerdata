
# Process Bethlehem Steel scores.
import re


class Processor(object):

    def __init__(self):
        self.season = None
        self.games = []


    def process_line(line):
        line = line.strip()
        if not line:
            return
        
        if line.startswith("Bethlehem Steel"):
            season = line.split("Steel")[1]
            self.season = season.strip()

        else:
            date, game_data = line.split("-", 1)

            month, day, year = date.split("/")

            y = int(year) + 1900
            
            try:
                d = datetime.datetime(y, int(month), int(day))
            except:
                print line
                return

            fields = [game_data.split('\t')]
            fields = [e for e in fields if e]
            
            if not len(fields) == 3:
                print line
                return

            location, competition, resultss = fields
            result1, result2 = results.split(',')

            re.match("
            
        
