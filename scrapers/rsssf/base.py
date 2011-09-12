import datetime
import re
import urllib2
from BeautifulSoup import BeautifulSoup


months = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12,
    }




class RSSSFParser(object):
    table_start = None
    table_end = None

    CUT_OFFS = []
    SUB_LINES = {}

    def __init__(self):
        pass


    def preprocess_line(self, line, year):
        for e in self.CUT_OFFS:
            if line.startswith(e):
                return line.split(e, 1)[1]

        if year in self.SUB_LINES and line in self.SUB_LINES[year]:
            return self.SUB_LINES[year][line]
        else:
            return line


    def parse_page(self, url, year):
        html = urllib2.urlopen(url).read()
        pre_text = html.split("<pre>")[1].split("</pre>")[0]

        if self.table_start:
            start = pre_text.index(self.table_start)
        else:
            start = 0

        if self.table_end:
            end = pre_text[start:].index(self.table_end) + start # Don't forget to adjust for pre_text[start:]!!
        else:
            end = len(pre_text)

        table = pre_text[start:end]

        lines = [e for e in table.split("\n") if e.strip()]
        
        scores = []
        date = None

        for line in lines:
            line = line.strip()
            pline = self.preprocess_line(line, year)
            date = self.get_date(pline, date, year)
            result = self.process_line(pline, date)
            if result:
                scores.append(result)


        return scores



    def get_date(self, line, date, year):
        if re.search("\[\w+\s\d+\]", line):
            sline = line.strip().replace("[", "").replace("]", "")

            try:
                month, day = sline.split(" ")
            except:
                import pdb; pdb.set_trace()

            day = int(day)
            # This is not a date.
            if day > 31:
                return None

            # Goals are formatted the same way as dates, so something like
            #   [Acasiete 87], we have to figure out which it is.
            # No way to be sure that somebody hasn't mis-entered a date.
            if len(month) > 3:
                print sline
                return None

            # Presumably not a month, but more likely to be.
            # Let's be extra careful?
            elif month not in months:
                print sline
                return None

            try:
                month_number = months[month]
            except KeyError:
                import pdb; pdb.set_trace()
            try:
                return datetime.datetime(year, month_number, int(day))
            except:
                import pdb; pdb.set_trace()
        else:
            return date


        


    def process_line(self, line,  date):
        # Not sure what to do with these weird games
        # (games that don't produce a result)
        if re.search("\sabd\s", line):
            # Game was abandoned.

            home_side, away_side = line.split("abd", 1)
            l = {
                "home_team": home_side.strip(),
                "away_team": away_side.strip(),
                "completed": False,
                "notes": "abandoned"
               }
            return None

        if re.search("\sawd\s", line):
            # Game was awarded to one side.
            home_side, away_side = line.split("awd", 1)
            l = {
                "home_team": home_side.strip(),
                "away_team": away_side.strip(),
                "completed": False,
                "notes": "awarded"
               }
            return None
            
        elif re.search("\d-\d", line):
            home_side, away_side = line.split("-", 1)
            if line.count("-") > 1:
                print line
            
            # Watch out for team names with spaces.
            home_team, home_score = home_side.rsplit(" ", 1)
            try:
                away_score, away_team = away_side.split(" ", 1)
            except:
                print line
                raise
            away_score = int(away_score)
            try:
                home_score = int(home_score)
            except:
                import pdb; pdb.set_trace()
            return {
                'home_team': home_team.strip(),
                'away_team': away_team.strip(),
                'home_score': home_score,
                'away_score': away_score,
                'date': date,
                }


        
        else: 
            return None


