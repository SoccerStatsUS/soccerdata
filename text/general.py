

# For processing general format score/lineup data.

# These look something like
# 3/29/2008; FC Dallas; 3-1 (aet); Chivas Guadalajara; Laredo, TX; Alex Prus; 130000
# Ruben Luna 3, Ruben Luna 10, Hugo Sanchez 92; Chicharito 19
# FC Dallas: Matt Jordan, Chris Gbandi, Clarence Goodson, George John, Zach Loyd, Brek Shea, Oscar Pareja, Leonel Alvarez, Ronnie O'Brien, Jason Kreis, Carlos Ruiz

import datetime
import os
import re

class GeneralProcessor(object):
    """
    An object to feed lines of text to.
    Retains a basic memory
    """

    DATE_RE = re.compile("(\d+)/(\d+)/(\d+)")
    DATE_TIME_RE = re.compile("(\d+)/(\d+)/(\d+) (\d+)z")

    def __init__(self):
        self.competition = None
        self.season = None

        self.current_game = None
        self.score_type = "standard"
        self.century = None # Manage dates like 3/23/10

        self.games = []
        self.goals = []
        self.misconduct = []
        self.appearances = []


    def process_line(self, line):


        if not line.strip():
            return

        # Comment
        if line.startswith("*"):
            return

        if line.startswith("Competition:"):
            self.competition = line.split("Competition:")[1].strip()
            return


        if line.startswith("Century"):
            self.century = int(line.split("Competition:")[1].strip())
            return


        if line.startswith("Score type:"):
            self.score_type = line.split("Score type:")[1].strip()
            return


        if line.startswith("Season:"):
            self.season = line.split("Season:")[1].strip()
            return


        if line.startswith("Red Card:"):
            return self.process_misconduct(line)

        if ":" in line:
            possible_team = line.split(":")[0]
            try:
                if possible_team in (self.current_game['team1'], self.current_game['team2']):
                    return self.process_lineup(line)
            except:
                import pdb; pdb.set_trace()

        fields = line.split(";")
        if fields:
            time_string = fields[0].strip()
            mdt = self.DATE_RE.match(time_string)
            if mdt:
                return self.process_game_fields(fields)


            md = self.DATE_RE.match(time_string)
            if md:
                return self.process_game_fields(fields)
                
        try:
            team1_goals, team2_goals = line.split(";")
        except:
            import pdb; pdb.set_trace()
        self.process_goals(team1_goals, team2_goals)
                

        
    def process_misconduct(self, line):
        pass


    def process_game_fields(self, fields):
        # Game fields are of this form:
        # 1. Date
        # 2. Team1, score
        # 3. Team2, score

        time_string = fields[0].strip()

        m = self.DATE_TIME_RE.match(time_string)
        if m:
            month, day, year, start = m.groups()
        else:
            try:
                month, day, year = self.DATE_RE.match(time_string).groups()
            except:
                import pdb; pdb.set_trace()
            start = None

        try:
            year = int(year)
            if year < 1800:
                if self.century:
                    year = year + self.century
                else:
                    import pdb; pdb.set_trace()

            d = datetime.date(year, int(month), int(day))
        except:
            import pdb; pdb.set_trace()

            
        # Some scores are separated by colons.
        if self.score_type == "colon-delimited":
            delimiter = ":"
        else:
            delimiter = "-"


        if self.score_type in ('standard', 'colon-delimited'):
            try:
                team1, score, team2 = fields[1:4]

                if score == 'w/o':
                    winner = team1
                    team1_score = team2_score = None
                else:
                    team1_score, team2_score = [int(e) for e in score.split(delimiter)]
                    winner = None
            except:
                import pdb; pdb.set_trace()

            remaining = fields[4:]
        
        elif self.score_type == 'byteam':
            score_re = re.compile('(.*?)(\d+)')
            try:
                team1, team1_score = score_re.match(fields[1]).groups()
            except:
                import pdb; pdb.set_trace()

            try:
                team2, team2_score = score_re.match(fields[2]).groups()
            except:
                import pdb; pdb.set_trace()

            remaining = fields[3:]

        else:
            import pdb; pdb.set_trace()

        # Attendance is always the last item.
        if remaining:
            try:
                attendance = int(remaining[-1])
                remaining = remaining[:-1]
            except ValueError:
                attendance = None
        else:
            attendance = None


        location = referee = None

        if len(remaining) == 1:
            location = remaining[0].strip()

        elif len(remaining) == 2:
            location, referee = [e.strip() for e in remaining]

        g = {
            'competition': self.competition,
            'date': d,
            'season': self.season,

            'team1': team1.strip(),
            'team2': team2.strip(),
            'team1_score': int(team1_score),
            'team2_score': int(team2_score),
            'winner' None
            'home_team': None,

            'location': location,
            'referee': referee,
            'attendance': attendance,
            }

        self.current_game = g
        self.games.append(g)

    def process_lineup(self, line):


        def process_appearance(s, team):
            if '(' not in s:
                return [{
                    'player': s.strip(),
                    'on': 0,
                    'off': 90,
                    'team': team,
                    'competition': self.competition,
                    'date': self.current_game['date']
                    }]

            else:
                starter, subs = s.split("(")
                subs = subs.replace(")", "")
                sub_items = subs.split(",")

                #import pdb; pdb.set_trace()

                return []


        team, players = line.split(":", 1)
        lineups = []
        for e in split_outside_parens(players):
            lineups.extend(process_appearance(e, team))

        self.appearances.extend(lineups)
            


    def process_goals(self, team1_goals, team2_goals):

        def process_item(s, team):

            m = re.match('(.*?)(\d+)', s)
            if m:
                remainder, minute = m.groups()
                minute = int(minute)
            else:
                remainder = s
                minute = None

            if '(' in remainder:
                goal, assists = remainder.split('(')
                try:
                    assists = [e.strip() for e in assists.replace(')', '').split(',')]
                except:
                    import pdb; pdb.set_trace()
                goal = goal.strip()

            else:
                goal = remainder.strip()
                assists = []


            return {
                'team': team,
                'competition': self.competition,
                'date': self.current_game['date'],
                'goal': goal,
                'minute': minute,
                'assists': assists,
                }


        goals = []

        for e in split_outside_parens(team1_goals):
            goals.append(process_item(e, self.current_game['team1']))
 
        for e in split_outside_parens(team2_goals):
            goals.append(process_item(e, self.current_game['team2']))

        self.goals.extend(goals)

            


def process_file(p):
    f = open(p)
    gp = GeneralProcessor()
    for line in f:
        gp.process_line(line)

    return (gp.games, gp.goals, gp.misconduct, gp.appearances)
        

def process_general_file(fn):
    p = os.path.join("/home/chris/www/soccerdata/data/general", fn)
    return process_file(p)


def split_outside_parens(s, delimiter=','):
    in_paren = False
    l = []
    ns = ''

    for char in s:
        if char == '(':
            in_paren = True
        if char == ')':
            in_paren = False

        if char == delimiter and not in_paren:
            l.append(ns)
            ns = ''
        else:
            ns += char

    l.append(ns)
    return l
                    

        
        
if __name__ == "__main__":
    d = "/home/chris/www/soccerdata/data/general"
    for fn in os.listdir(d):
        p = os.path.join(d, fn)
        if os.path.isfile(p) and not fn.endswith("~"):
            print process_general_file(fn)
    #print process_general_file("harmarville.txt")
    