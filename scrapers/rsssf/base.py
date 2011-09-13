#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


import datetime
import re
import urllib2
from BeautifulSoup import BeautifulSoup


# Need to split up pages into separate whatevers.
# Need to figure out how to parse by year.
# Probably need ot install simplejson



BAD_CHARS = {
    '\xe1': 'á',
    '\xe0': 'à',
    '\xe7': 'ç',
    '\xe8': 'è',
    '\xe9': 'é',
    '\xed': 'í',
    '\xf3': 'ó',
    '\xfa': 'ú',
    '\xfc': 'ü',
    '\xf1': 'ñ',
    '\xc1': 'Á',
    '\xc9': 'É',
    '\xd3': 'Ó',
    '\x96': '-',
    '\x92': '’',
    '\xb4': '´',
    '\xeb': 'ë',
    }

BAD_TWO_CHARS = {
    '\xc3\xb3': 'ó',
    '\xc3\xa1': 'á',
    '\xc3\xa8': 'è',
    '\xc3\xa7': 'ç',
}

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
    table_ends = []

    UNIVERSAL_REPLACE = []

    RE_CUTOFFS = []

    BASE_CUTOFFS = [

        # These need to be ahead of the First Leg.
        "First Legs", 
        "First Leg", 
        "First leg",

        "Second Legs",
        "Second Leg", 
        "Second leg", 

        "Third Leg Minigame",
        "Third Legs", 
        "Third Leg", 
        "Third leg", 

        "First Round",
        "Second Round",
        "Third Round",

        'Preliminary Round',
        'Qualifying Match',

        "Quarterfinals",
        "Semifinals",
        'Final',
        ]
    CUTOFFS = []
    SUB_LINES = {}

    def __init__(self):
        pass

    def get_html(self, url):
        html = urllib2.urlopen(url).read()
        s = ''
        for char in html:
            if char in BAD_CHARS:
                s += BAD_CHARS[char]
            else:
                s += char

        for k, v in BAD_TWO_CHARS.items():
            html = html.replace(k, v)

        return s



    def preprocess_line(self, line, year):

        for old, new in self.UNIVERSAL_REPLACE:
            line = line.replace(old, new)

        for rx in self.RE_CUTOFFS:
            s = re.search(rx, line)
            if s:
                line = s.groups()[0]
                

        for e in self.BASE_CUTOFFS + self.CUTOFFS:
            if line.startswith(e):
                return line.split(e, 1)[1]

        if year in self.SUB_LINES and line in self.SUB_LINES[year]:
            return self.SUB_LINES[year][line]
        else:
            return line


    def parse_page(self, url, year):
        html = self.get_html(url)
        
        pre_text = html.split("<pre>")[1].split("</pre>")[0]

        if self.table_start:
            start = pre_text.index(self.table_start)
        else:
            start = 0

        end = len(pre_text)
        for e in self.table_ends:
            if e in pre_text[start:]:
                end = min(end, pre_text[start:].index(e) + start) # Don't forget to adjust for pre_text[start:]!!


        table = pre_text[start:end]

        lines = [e for e in table.split("\n") if e.strip()]
        
        scores = []
        date = None
        date_year = year

        for line in lines:
            line = line.strip()
            pline = self.preprocess_line(line, year)
            date = self.get_date(pline, date, date_year)
            if date:
                date_year = date.year
            result = self.process_line(pline, date)
            if result:
                scores.append(result)


        return scores


    def get_date(self, line, date, year):
        # This is the standard get_date; however,
        # Year should really only be used as a hint for finding the first date.
        # After that, it's better to use the previous date's year.
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

            # Set the year correctly?
            if date and month_number < date.month:
                year = date.year + 1

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

        # Dodge penalty shootout results that look like
        # Giggs (scored)        1-0      O'Hara (saved)        1-0
        # resembling scores...
        if "(scored)" in line or "(missed)" in line:
            return None

            
        game_re = re.compile("(.*?)(\d-\d)(.*)")
        if game_re.search(line):
            # Italy sometimes puts the dates of games at the end of a line.
            # Need to pull allow customizing of the process line function?

            home_team, score, away_team = game_re.search(line).groups()

            # Strip out comments in the away side info.
            # Need to add facility that detects pk score.
            s = re.search("\[\w+\s\d+\]", away_team)
            if s:
                away_team = away_team.split("[")[0]


            if line.count("-") > 1:
                print line

            try:
                home_score, away_score = [int(e) for e in score.split("-")]
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


