# For processing general format score/lineup data.

# These look something like
# 3/29/2008; FC Dallas; 3-1 (aet); Chivas Guadalajara; Laredo, TX; Alex Prus; 130000
# Ruben Luna 3, Ruben Luna 10, Hugo Sanchez 92; Chicharito 19
# FC Dallas: Matt Jordan, Chris Gbandi, Clarence Goodson, George John, Zach Loyd, Brek Shea, Oscar Pareja, Leonel Alvarez, Ronnie O'Brien, Jason Kreis, Carlos Ruiz

# Need to add in home_team


import datetime
import os
import re




def process_name(s):
    """Clean up a player name. Remove possible leading numbers.
    e.g. '18-Tim Howard ' -> 'Tim Howard'"""
    s = s.strip()
    m = re.match("(\d+-)?(.*)", s)
    if m:
        return m.groups()[1].strip()
    else:
        return s

class GeneralProcessor(object):
    """
    An object to feed lines of text to.
    Retains a basic memory
    """

    DATE_RE = re.compile("(\d+)/([\d\?]+)/(\d+)")
    DATE_TIME_RE = re.compile("(\d+)/(\d+)/(\d+) (\d+)z")

    def __init__(self):
        self.competition = None
        self.season = None
        self.round = ''
        self.group = ''
        self.sources = []

        self.current_game = None
        self.score_type = "standard"
        self.century = None # Manage dates like 3/23/10

        self.date = None
        self.date_style = 'month first'

        self.games = []
        self.goals = []
        self.misconduct = []
        self.appearances = []
        

        self.rosters = []


    def process_line(self, line):
        """
        Do a lot of processing.
        """
        
        line = line.strip()
        if not line:
            return


        tag_data = lambda l, t: l.split(t, 1)[1].strip()

        def process_simple_tag(line, tag, key):
            if line.startswith(tag):
                key = tag_data(line, tag)




        # Represents a comment.
        if line.startswith("*"):
            return

        # Set the previous game as a minigame.

        for e in ["Minigame", "Forfeit"]:
            if line.startswith(e):
                self.games[-1][e.lower()] = True
                return

            
        if line.startswith("Notes:"):
            self.games[-1]['notes'] = tag_data(line, "Notes:")
            return


        if line.startswith("Replay"):
            return

        if line.startswith("Date:"):
            d = line.split('Date:')[1].strip()
            if d:
                month, day, year = [int(e) for e in d.split('/')]
                self.date = datetime.datetime(year, month, day)
            else:
                self.date = None

            return


        if line.startswith("Date-style"):
            self.date_style = tag_data(line, "Date-style:")
            return



        # Change the number of minutes.
        if line.startswith("Minutes:"):
            self.current_game['minutes'] = int(tag_data(line, 'Minutes:'))
            return


        # Change the game type.
        if line.startswith("Indoor"):
            return


        # Set the competition.
        if line.startswith("Competition:"):
            self.competition = tag_data(line, "Competition:")
            self.round = self.group = self.zone = ''
            return

        if line.startswith("Season:"):
            self.season = tag_data(line, "Season:")
            self.round = self.group = self.zone = ''
            return

        # Set the round.
        if line.startswith("Round:"):
            self.round = tag_data(line, "Round:")
            if self.round.lower() == 'none':
                self.round = ''
                self.group = ''
            return

        if line.startswith("Group:"):
            self.group = tag_data(line, "Group:")
            if self.group.lower() == 'none':
                self.group = None
            return

        # Zone should be group?
        if line.startswith("Zone:"):
            self.group = tag_data(line, "Zone:")
            if self.group.lower() == 'none':
                self.group = None
            return

        # Set the round.
        if line.startswith("Roster:"):
            self.process_roster(tag_data(line, "Roster:"))
            return

        if line.lower().startswith("substitutes not used:"):
            return

        if line.startswith('Subs:'):
            return

        if line.startswith("Description"):
            return


        if line.startswith("Source:"):
            self.current_game['sources'].append(tag_data(line, "Source:"))
            return

        if line.startswith("Video:"):
            self.current_game['video'] = tag_data(line, "Video:")
            return

        if line.startswith('BlockSource:'):
            source = tag_data(line, "BlockSource:")
            if source:
                self.sources = [source]
            return


        if line.startswith("Century"):
            self.century = int(tag_data(line, "Century:"))
            return


        if line.startswith("Score type:"):
            self.score_type = tag_data(line, "Score type:")
            return



        if line.startswith("Red Card:"):
            s = tag_data(line, "Red Card:")
            self.misconduct.extend(self.process_misconduct(s))
            return 

        if line.startswith("Shootout Win"):
            self.current_game['shootout_winner'] = tag_data(line, "Shootout Win:")
            return



        # A terrible solution
        # This destroys goal processing.
        # Nevertheless something like this would be good.
        # Fields was being thrown off by a trailing ;
        # This makes that not happen without fixing the
        # underlying problem.
        #if line.endswith(';'):
        #    line = line[:-1]

        fields = line.split(";")
            

        # Checking for Brooklyn FC: GK, DF
        # Trying to handle 1/25/1990; Brooklyn FC; 2 : 1; Queens Boys
        # and not have it mistaken for a team line because of the colon?
        # Seems unnecessary.
        skip_team = False
        if ';' in line and ':' in line:
            if line.index(';') < line.index(':'):
                skip_team = True

        if ":" in line and not skip_team:
            possible_team = line.split(":")[0]
            if self.current_game == None:
                import pdb; pdb.set_trace()
                
            if possible_team in (self.current_game['team1'], self.current_game['team2']):
                lineups = self.process_lineup(line)
                self.appearances.extend(lineups)
                return 

        # Why is this check necessary?
        if fields:

            # Game without a date.
            # Need to implement this.
            # Whoops - this kills a lot of valid game results.
            if line.startswith(";") and line.count(';') > 1:
                return self.process_game_fields(fields)

            # Need to implement datetime check here.
            time_string = fields[0].strip()
            mdt = self.DATE_RE.match(time_string)
            if mdt:
                return self.process_game_fields(fields)

            md = self.DATE_RE.match(time_string)
            if md:
                return self.process_game_fields(fields)
            try:
                year = int(time_string)
                return self.process_game_fields(fields)
            except ValueError:
                pass


            if fields[0].startswith('?'):
                return self.process_game_fields(fields)

        # Goals is the final fallback.
        try:
            team1_goals, team2_goals = line.split(";")
        except ValueError:
            print line
            raise

        self.process_goals(team1_goals, team2_goals)
                

        
    def process_misconduct(self, line):

        def process_item(team, s):
            m = re.match('(.*?)(\d+)', s)
            if m:
                name = m.groups()[0].strip()
                minute = int(m.groups()[1])
            else:
                name, minute = s.strip(), None

            return {
                'competition': self.competition,
                'date': self.current_game['date'],
                'season': self.season,
                'name': name,
                'minute': minute,
                'type': 'red',
                'team': team,
                }
            

        process_side = lambda t, l: [process_item(t, e) for e in l.split(',') if e.strip()]

        if ';' in line:
            t1m, t2m = line.split(';')
            t1, t2 = self.current_game['team1'], self.current_game['team2']
            l = process_side(t1, t1m)
            l.extend(process_side(t2, t2m))

        else:
            l = process_side(None, line)




        return l
        



        


    def process_roster(self, line):

        def process_players(s):
            l = []
            fields = s.split(',')
            for f in fields:
                player = f.split('(')[0]
                l.append({
                        'competition': self.competition,
                        'season': self.season,
                        'team': team,
                        'name': player,
                        })

            return l
            

        line = line.strip()
        if line.endswith('.'):
            line = line[:-1]

        fields = line.split(";")
        if len(fields) == 2:
            start = end = None
            team, players = fields

        elif len(fields) == 4:
            team, start, end, players = fields

        else:
            import pdb; pdb.set_trace()

        self.rosters.append(process_players(players))


    def process_game_fields(self, fields):
        # Game fields are of this form:
        # 1. Date
        # 2. Team1, score
        # 3. Team2, score

        team1_result = team2_result = None

        # Get the date and time.
        time_string = fields[0].strip()

        # Assume start time not included.
        start = None


        if fields[0].strip() == '':
            # This should usually just be None. Make sure to not accidentally set dates.
            d = self.date
            

        elif '?' in fields[0]:
            try:
                _, _, year = fields[0].split('/')
                day = month = None
                d = None
            except ValueError:
                print "? problem on date", fields[0]
                d = None

        else:
            # Try datetime first, if it doesn't work, try time.
            m = self.DATE_TIME_RE.match(time_string)
            if m:
                if self.date_style == 'day first':
                    day, month, year, start = m.groups()
                else: 
                    month, day, year, start = m.groups()
            else:
                try:
                    # Where is this?
                    if self.date_style == 'day first':
                        day, month, year = self.DATE_RE.match(time_string).groups()
                    else:
                        month, day, year = self.DATE_RE.match(time_string).groups()
                except:
                    year = int(time_string)
                    month = day = 1

            year = int(year)
            if year < 1800:
                year += self.century
            d = datetime.datetime(year, int(month), int(day))
            
        # Some scores are separated by colons.
        if self.score_type == "colon-delimited":
            delimiter = ":"
        else:
            delimiter = "-"

        result_unknown = False

        if self.score_type in ('standard', 'colon-delimited'):
            try:
                team1, score, team2 = fields[1:4]

                score = score.lower().strip()
                minutes = 90

                if '(aet)' in score:
                    score = score.replace('(aet)', '')
                    minutes = 120

                if '(asdet)' in score:
                    score = score.replace('(asdet)', '')
                    minutes = 'asdet'


                # Eventually will indicate a blank score.
                # We're not prepared to handle this, so leave the function.
                if score == 'w/o':
                    print "skipping: %s" % score
                    winner = team1
                    return

                elif score == '?':
                    team1_score = team2_score = None
                    result_unknown = True
                elif score in ('n/p', 'np', 'v'):
                    team1_score = team2_score = None
                else:
                    team1_score, team2_score = [e.strip() for e in score.split(delimiter)]

                    if team1_score in 'wlt':
                        team1_result = team1_score
                        team1_score = None
                    else:
                        team1_score = int(team1_score)


                    if team2_score in 'wlt':
                        team2_result = team2_score
                        team2_score = None
                    else:
                        team2_score = int(team2_score)

                    winner = None
            except:
                import pdb; pdb.set_trace()

            remaining = fields[4:]


        # Can't handle more complex score processing with byteam
        # Intend to just drop this completely eventually.
        elif self.score_type == 'byteam':
            score_re = re.compile('(.*?)(\d+)\'?')
            team1, team1_score = score_re.match(fields[1]).groups()

            team2, team2_score = score_re.match(fields[2]).groups()

            team1_score, team2_score = int(team1_score), int(team2_score)

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


        location = ''
        referee = None

        if len(remaining) == 1:
            location = remaining[0].strip()

        elif len(remaining) == 2:
            location, referee = [e.strip() for e in remaining]

        linesmen = []
        if referee and ',' in referee:
            people = referee.split(',')
            referee = people[0].strip()
            linesmen = [e.strip() for e in people[1:]]

        if self.competition is None or self.season is None:
            import pdb; pdb.set_trace()

        
        team1 = team1.strip()
        team2 = team2.strip()

        location = location.strip()
        
        neutral = False
        home_team = None
        if location in (team1, team2):
            home_team, location = location, ''
        elif location.lower() == 'neutral':
            neutral = True

        g = {
            'competition': self.competition,
            'season': self.season,
            'round': self.round,
            'group': self.group,

            'date': d,

            'team1': team1.strip(),
            'team2': team2.strip(),
            'team1_score': team1_score,
            'team2_score': team2_score,
            'team1_result': team1_result,
            'team2_result': team2_result,
            'result_unknown': result_unknown,

            'home_team': home_team,
            'shootout_winner': None,

            'location': location,
            'neutral': neutral,

            'referee': referee,
            'linesmen': linesmen,
            'attendance': attendance,
            'minigame': False,
            'forfeit': False,
            'sources': self.sources[:],
            'notes': '',
            'video': '',
            'minutes': minutes,
            }

        self.current_game = g
        self.games.append(g)


    def process_lineup(self, line):

        def process_appearance(s, team, order):

            capts = ['(c)', '(capt)', '(capt.)', '(Capt.)', '(Capt)', '(cap)']
            for e in capts:
                s = s.replace(e, '')

            #s = s.replace('(c)', '').replace('(capt)', '').replace('(capt.)', '').replace('(capt.)', '')
            # Off should be "end", then normalized later.

            # Will implement captains later.
            s = s.replace('(c)', '')

            # Fuck. This is wrong. This is true of game plus/minus, but not appearance plus/minus.
            # Need to handle appearance minutes...
            # This is being used for determining the results of games.
            if team == self.current_game['team1']:
                goals_for, goals_against = self.current_game['team1_score'], self.current_game['team2_score']
            elif team == self.current_game['team2']:
                goals_for, goals_against = self.current_game['team2_score'], self.current_game['team1_score']
            else:
                import pdb; pdb.set_trace()


            base = {
                'team': team,
                'competition': self.competition,
                'date': self.current_game['date'],
                'season': self.season,
                'goals_for': goals_for,
                'goals_against': goals_against,
                'order': order,
                }


            # It should be possible to merge these into one.
            # It might even be possible to just remove the first half of the if clause.
            if '(' not in s:
                name = process_name(s)

                e = {
                    'name': name,
                    'on': 0,
                    'off': 90,
                    }
                e.update(base)
                return [e]

            else:

                    
                
                starter, subs = s.split("(")
                subs = subs.replace(")", "")
                sub_items = subs.split(",")

                starter = process_name(starter)                

                l = [{ 'name': starter, 'on': 0 }]
                    
                for item in sub_items:
                    m = re.match("(.*)( \d+)", item)
                    if m:
                        sub, minute = m.groups()
                        minute = int(minute)
                        sub = process_name(sub)
                    else:
                        print "No minute for sub %s" % s
                        minute = None
                        sub = process_name(sub_items[0])

                    l[-1]['off'] = minute
                    l.append({'name': sub, 'on': minute})

                l[-1]['off'] = 90
                for e in l:
                    e.update(base)

                return l




        # Remove trailing marks.
        line = line.strip()
        if line[-1] in ('.', ','):
            line = line[:-1]

        team, players = line.split(":", 1)
        lineups = []

        # Need to separate separate fields to get spearate sections.
        for order, e in enumerate(split_outside_parens(players, ',;'), start=1):
            lineups.extend(process_appearance(e, team, order))

        return lineups


            


    def process_goals(self, team1_goals, team2_goals):
        """
        Process goals for both teams.
        """

        def process_item(s, team):
            s = s.strip()
            if not s:
                return {}

            m = re.match('(.*?)(\d+)', s)
            if m:
                remainder, minute = m.groups()
                minute = int(minute)
            else:
                remainder = s
                minute = None

            if '(' in remainder:
                goal, assists = remainder.split('(')
                assists = [e.strip() for e in assists.replace(')', '').split(',')]
                goal = goal.strip()

            else:
                goal = remainder.strip()
                assists = []

            if goal.strip() == '':
                import pdb; pdb.set_trace()


            return {
                'competition': self.competition,
                'date': self.current_game['date'],
                'season': self.season,
                'goal': goal,
                'assists': assists,
                'team': team,
                'minute': minute,
                }


        goals = []

        for e in split_outside_parens(team1_goals):
            goals.append(process_item(e, self.current_game['team1']))
 
        for e in split_outside_parens(team2_goals):
            goals.append(process_item(e, self.current_game['team2']))

        self.goals.extend([e for e in goals if e])

            


def process_string(s):
    lines = s.split('\n')
    return process_lines(lines)

def process_lines(lines):
    gp = GeneralProcessor()
    for line in lines:
        gp.process_line(line)

    return (gp.games, gp.goals, gp.misconduct, gp.appearances, gp.rosters)
        

def process_games_file(fn):
    p = os.path.join("/home/chris/www/soccerdata/data/games", fn)
    return process_file(p)

def process_file(p):
    f = open(p)
    return process_lines(f)



def split_outside_parens(s, delimiters=','):
    # Supports multiple delimiters.
    in_paren = False
    l = []
    ns = ''

    for char in s:
        if char == '(':
            in_paren = True
        if char == ')':
            in_paren = False

        if char in delimiters and not in_paren:
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
    
