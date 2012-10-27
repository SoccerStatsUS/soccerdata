

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
        self.sources = []

        self.current_game = None
        self.score_type = "standard"
        self.century = None # Manage dates like 3/23/10

        self.date_style = 'month first'

        self.games = []
        self.goals = []
        self.misconduct = []
        self.appearances = []


    def process_line(self, line):
        """
        Do a lot of processing.
        """
        
        line = line.strip()


        if not line:
            return

        # Represents a comment.
        if line.startswith("*"):
            return

        # Game without a date.
        # Need to implement this.
        if line.startswith(";"):
            return

        # Set the previous game as a minigame.
        if line.startswith("Minigame"):
            try:
                self.games[-1]['minigame'] = True
                return
            except:
                import pdb; pdb.set_trace()
                x = 5

        if line.startswith("Forfeit"):
            self.games[-1]['forfeit'] = True
            return


        if line.startswith("Date-style"):
            self.date_style = line.split("Date-style:")[1].strip()
            return



        # Change the number of minutes.
        if line.startswith("Minutes:"):
            return

        # Change the number of minutes.
        if line.startswith("Indoor"):
            return


        # Set the competition.
        if line.startswith("Competition:"):
            self.competition = line.split("Competition:")[1].strip()
            return


        # Set the round.
        if line.startswith("Round"):
            return

        # Set the round.
        if line.startswith("Roster"):
            return


        if line.lower().startswith("substitutes not used:"):
            return

        if line.startswith("Group"):
            return

        if line.startswith("Description"):
            return


        # Add a source.
        if line.startswith("Source:"):
            source = line.split("Source:")[1].strip()
            self.games[-1]['sources'].append(source)
            return

        if line.startswith('BlockSource:'):
            source = line.split("BlockSource:")[1].strip()
            self.sources = [source]
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



        # A terrible solution
        # This destroys goal processing.
        # Nevertheless something like this would be good.
        # Fields was being thrown off by a trailing ;
        # This makes that not happen without fixing the
        # underlying problem.
        #if line.endswith(';'):
        #    line = line[:-1]

        fields = line.split(";")
            

        if '26/09/1943' in line:
            pass #import pdb; pdb.set_trace()


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
            try:
                #if self.current_game['date'] == datetime.datetime(2011, 11, 6):
                #    import pdb; pdb.set_trace()

                if possible_team in (self.current_game['team1'], self.current_game['team2']):
                    lineups = self.process_lineup(line)
                    self.appearances.extend(lineups)
                    return 

            except:
                import pdb; pdb.set_trace()


        # Why is this check necessary?
        if fields:

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

        # Goals is the final fallback.
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

        team1_result = team2_result = None

        # Get the date and time.
        time_string = fields[0].strip()

        # Assume start time not included.
        start = None

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
                try:
                    year = int(time_string)
                    month = day = 1
                except ValueError:
                    import pdb; pdb.set_trace()



        # 
        try:
            year = int(year)
            if year < 1800:
                year += self.century
            d = datetime.datetime(year, int(month), int(day))
        except:
            d = None
            #import pdb; pdb.set_trace()
            x = 5

            
        # Some scores are separated by colons.
        if self.score_type == "colon-delimited":
            delimiter = ":"
        else:
            delimiter = "-"

        if len(fields) < 2:
            import pdb; pdb.set_trace()
            
        if fields[2] == ' L-4':
            pass
            # import pdb; pdb.set_trace()


        result_unknown = False

        if self.score_type in ('standard', 'colon-delimited'):
            try:
                team1, score, team2 = fields[1:4]

                score = score.lower().strip()

                if '(aet)' in score:
                    score = score.replace('(aet)', '')

                if '(asdet)' in score:
                    score = score.replace('(asdet)', '')


                # Eventually will indicate a blank score.
                # We're not prepared to handle this, so leave the function.
                if score == 'w/o':
                    print "skipping: %s" % score
                    winner = team1
                    return

                elif score == '?':
                    team1_score = team2_score = None
                    result_unknown = True
                elif score in ('n/p', 'np'):
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
            try:
                team1, team1_score = score_re.match(fields[1]).groups()
            except:
                import pdb; pdb.set_trace()

            try:
                team2, team2_score = score_re.match(fields[2]).groups()
            except:
                import pdb; pdb.set_trace()


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


        location = referee = ''

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
            'date': d,

            'team1': team1.strip(),
            'team2': team2.strip(),
            'team1_score': team1_score,
            'team2_score': team2_score,
            'team1_result': team1_result,
            'team2_result': team2_result,
            'home_team': home_team,
            'neutral': neutral,

            'result_unknown': result_unknown,

            'location': location,
            'referee': referee,
            'linesmen': linesmen,
            'attendance': attendance,
            'minigame': False,
            'forfeit': False,
            'sources': self.sources[:],
            }

        self.current_game = g
        self.games.append(g)


    def process_lineup(self, line):

        def process_appearance(s, team):
            # Currently just skipping the item if there were subs.
            # Off should be "end", then normalized later.

            # Will implement captains later.
            s = s.replace('(c)', '')

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
                }

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

                """
                if len(sub_items) == 1:
                    m = re.match("(.*)( \d+)", sub_items[0])
                    if m:
                        sub, minute = m.groups()
                        minute = int(minute)
                        sub = process_name(sub)
                    else:
                        print "No minute sub for %s" % s
                        minute = None
                        sub = process_name(sub_items[0])
                    return [{
                            'name': starter,
                            'on': 0,
                            'off': minute,
                            'team': team,
                            'competition': self.competition,
                            'date': self.current_game['date'],
                            'season': self.season,

                            },
                            {
                            'name': sub,
                            'on': minute,
                            'off': 90,
                            'team': team,
                            'competition': self.competition,
                            'date': self.current_game['date'],
                            'season': self.season,
                            }]
                """
                #if len(sub_items) >= 2:
                if True:
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

                    #print "Handling multiple sub_items %s" % len(sub_items)
                    #print sub_items


                return []



        # Remove trailing marks.
        line = line.strip()
        if line[-1] in ('.', ','):
            line = line[:-1]

        team, players = line.split(":", 1)
        lineups = []

        # Need to separate separate fields to get spearate sections.
        for e in split_outside_parens(players, ',;'):
            lineups.extend(process_appearance(e, team))

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
                try:
                    assists = [e.strip() for e in assists.replace(')', '').split(',')]
                except:
                    import pdb; pdb.set_trace()
                goal = goal.strip()

            else:
                goal = remainder.strip()
                assists = []

            if goal.strip() == '':
                import pdb; pdb.set_trace()


            return {
                'team': team,
                'competition': self.competition,
                'date': self.current_game['date'],
                'goal': goal,
                'minute': minute,
                'assists': assists,
                'season': self.season,
                }


        goals = []

        #if self.current_game['date'] == datetime.date(1929, 3, 31):
        #    import pdb; pdb.set_trace()

        for e in split_outside_parens(team1_goals):
            try:
                goals.append(process_item(e, self.current_game['team1']))
            except:
                import pdb; pdb.set_trace()
 
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

    return (gp.games, gp.goals, gp.misconduct, gp.appearances)
        

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
    
