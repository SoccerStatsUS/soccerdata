#!/usr/bin/env python

# Need to redo a bunch of DC United Goal entries from around 2003 and 2004.  Format is Adu (34;85), which is not useable...

# Load data from scrayice's lineup files.

import datetime
import os
import re
import sys


file_mapping = {
    "CHI": u'Chicago Fire',
    "CHV": u'Chivas USA',
    "COL": u'Colorado Rapids',
    "CLB": u'Columbus Crew',
    "DC": u'D.C. United',
    "DAL": u'FC Dallas',
    "HOU": u'Houston Dynamo',
    "KC": u'Kansas City Wizards',
    "LA": u'Los Angeles Galaxy',
    "MIA": u'Miami Fusion',
    "NE": u'New England Revolution',
    "NY": u'New York Red Bulls',
    "PHI": u'Philadelphia Union',
    "RSL": u'Real Salt Lake',
    "SJ": u'San Jose Earthquakes',
    "SEA": u'Seattle Sounders',
    "TB": u'Tampa Bay Mutiny',
    "TOR": u'Toronto FC',
 }    

get_date = lambda s: datetime.datetime.strptime (s, "%Y-%m-%d")



LINEUPS_DIR = "/home/chris/www/soccerdata/data/lineups/"

def get_competition(name):
    try:
        int(name)
        return 'MLS'
    except ValueError:
        return 'other'

def get_scores(fn):
    """
    Get scores from scaryice's lineups table for a given file.
    """

    # OH NO! Fucking make the scores work correctly.

    def process_line(line):
        if not line.strip():
            return {}

        items = line.strip().split("\t")
        match_type, date_string, location, opponent, score, result, _, goals, lineups = items

        date = get_date(date_string)

        home_score, away_score = [int(e) for e in score.split('-')]


            

        if location == 'H':
            home_team = team_name
            away_team = opponent
        elif location == 'A':
            away_team = team_name
            home_team = opponent
        elif location == 'N':
            # Not sure how to handle these.
            home_team = team_name
            away_team = opponent
        else:
            raise

        
        return {
            'competition': get_competition(match_type),
            'date': date,
            'year': date.year,
            'season': unicode(date.year),
            'home_team': home_team,
            'away_team': away_team,
            'home_score': home_score,
            'away_score': away_score,
            'location': location,
            }

    p = os.path.join(LINEUPS_DIR, fn)
         
    team_name = file_mapping[fn.replace(".csv", '')]
    scores = [process_line(line) for line in open(p).readlines()]
    scores = [e for e in scores if e]
    return scores

def load_all_games():
    l = []
    for key in file_mapping.keys():
        fn = "%s.csv" % key
        l.extend(get_scores(fn))
    return l


def get_goals(filename):
    

    def process_line(line):
        if not line.strip():
            return {}

        items = line.strip().split("\t")
        match_type, date_string, location, opponent, score, result, _, goals, lineups = items
        
        date = get_date(date_string)

        def process_goal(e):
            e = e.strip()

            if not e:
                return {}
            # looks like this
            # Kosecki (Razov) 76; Kotschau (unassisted) 87'

            match = re.search("(?P<name>.*?)\s+(\d+\s+)?\(.*?\)\s+(?P<minute>\d+)", e)

            # Handle "Preki (3)" et al.
            # Currently handling "Preki (47+ pen) here, by lopping off \) from re.
            # should separate.
            if not match:
                match = re.search("(?P<name>.*?)\s+(\d+\s+)?\((?P<minute>\d+)", e)

            # Handle "Okafor 16" et al.
            if not match:
                match = re.search("(?P<name>.*?)\s+(\d+\s+)?(?P<minute>\d+)", e)

            non_goals = [
                'Own Goal',
                "o.g.",
                'og',
                'own goal',
                '(forfeit)',
                ]

            for ng in non_goals:
                if e.startswith(ng):
                    return {}

            if not match:
                import pdb; pdb.set_trace()

            try:
                player = match.groups()[0]
                minute = int(match.groups()[2])
            except:
                import pdb; pdb.set_trace()

            return {
                'competition': get_competition(match_type),
                'team': team_name,
                'date': date,
                'year': date.year,
                'player': player,
                'minute': minute,
                }


        l = [process_goal(e) for e in goals.split(';')]
        return [e for e in l if e]

    p = os.path.join(LINEUPS_DIR, filename)
         
    team_name = file_mapping[filename.replace(".csv", '')]

    l = []
    for line in open(p).readlines():
        l.extend(process_line(line))
    return l


def load_all_goals():
    l = []
    for key in file_mapping.keys():
        fn = "%s.csv" % key
        l.extend(get_goals(fn))
    return l


        




# This stuff is overly complex.





class Lineup(object):
    def __init__(self, line, file):
        fn = file.split(".")[0]

        self.line = line

        self.lineup = self._format_lineup(line.split("\t")[8])
        self.scores = line.split("\t")[7]

        
        self.players = [e.strip() for e in self.lineup.split(",")]

        self.game = self._get_game()
        self.player_failures = set()
        self.games_played = []



    def _format_lineup(self, line):
        """Replace commas inside parens with semicolons;
        Also verify that all commas are closed."""
        s = ''
        in_paren = False
        for char in line:
            if char == "(":
                if in_paren:
                    print line
                    return ''
                else:
                    in_paren = True
            if char == ")":
                if not in_paren:
                    print line
                    return ''
                else:
                    in_paren = False
            if in_paren and char == ",":
                # Trying to filter out stray commas
                # inserted between names and times.
                try:
                    int(s[-2:])
                    s += ";"
                except ValueError:
                    pass
                    
            # Fix incidental semicolons
            elif not in_paren and char == ";":
                s += ","
            else:
                s += char

        if s.endswith("."):
            s = s[:-1]

        return s

    def _format_scores(self, scores):
        s = ''
        in_paren = False
        
        for char in scores:
            if char == "(":
                if in_paren:
                    raise
                else:
                    in_paren = True

            if char == ")":
                if not in_paren:
                    raise
                else:
                    in_paren = False

            if char in (",", ";"):
                if in_paren:
                    s += ","
                else:
                    s += char
            else:
                s += char

        
        # If you use a comman instead of a semicolon to 
        # separate goal entries.
        s2 = ''
        for char in s:
            if char == ',':
                try:
                    int(s2[-2:])
                    s2 += ';'
                except ValueError:
                    s2 += ','
            else:
                s2 += char
                
        return s2
        
                
                


    def _get_game(self):
        number, date, home_away, opponent, score, result, record, scorers, lineup = self.line.split('\t')
        

        try:
            team_score, opponent_score = score.split("-")
        except:
            import pdb; pdb.set_trace()

        if home_away == 'H':
            home_team = self.team
            home_score = team_score
            away_team = opponent_team
            away_score = opponent_score
        else:
            home_team = opponent_team
            home_score = opponent_score
            away_team = self.team
            away_score = team_score

        dt = get_date(date)

        games = Game.objects.filter(date=dt, home_team=home_team, away_team=away_team)

        if games.count() > 1:
            raise
        elif games.count() == 1:
            game = games[0]
        else:
            game = Game.objects.create(date=dt, 
                                       neutral=False,
                                       home_team=home_team,
                                       home_score=home_score,
                                       away_team=away_team,
                                       away_score=away_score)
        return game



    def interpret_sub(self, sub):
        minute_re = re.compile("(?P<minute>\d+)[\+\?]?")
        r = minute_re.search(sub)
        if r:
            minute_s = r.groups()[0]
            minute = int(minute_s)
            sub_name = sub.split(minute_s)[0].strip()
            return sub_name, minute
        else:
            if "?" in sub:
                sub_name = sub.split("?")[0]
                return sub_name, -1
            elif "sent off in shootout" in sub:
                return '', 200
            elif "sent off during shootout" in sub:
                return '', 200
            elif "sent off after final whistle" in sub:
                return '', 200

        import pdb; pdb.set_trace()
        pass


    def sub_fixes(self, sub):
        # Fix 
        if sub == "J Gomez 78" and self.team.id == 15:
            return 'Julian Gomez 78'
        return sub
        
        
    def process_games(self):
        if self.game is None:
            return

        for player in self.players:
            if player == "":
                pass

            # Deal with one weirdo sub [sub:(Mickey Kydes ???), NY]
            elif player.startswith("sub:"):
                pass


            elif "(" in player:
                players = []
                false_sub = False
                sub_times = [0]
                nplayer = player.replace(")", "")
                
                # Sometimes subs are like (p1 32) (p2 64)
                if nplayer.count("(") > 1:
                    starter = nplayer.split("(")[0]
                    subs = nplayer.split("(")[1:]
                # Usually they are like (p1 32; p2 64)
                else:
                    starter, subs = nplayer.split("(")
                    subs = subs.split(";")
                players.append(self.get_person(starter))
                
                for sub in subs:
                    sub = self.sub_fixes(sub)

                    false_sub = "sent off" in sub
                    if "ejection" in sub:
                        false_sub = True
                    if "injured" in sub:
                        false_sub = True
                        min = 90
                    else:
                        n, min = self.interpret_sub(sub)
                        if not false_sub:
                            players.append(self.get_person(n))
                    sub_times.append(min)

                if not false_sub:
                    sub_times.append(90)

                for i, player in enumerate(players):
                    on = sub_times[i]
                    off = sub_times[i+1]
                    try:
                        self.create_game_played(player, on, off)
                    except:
                        import pdb; pdb.set_trace()
                        print self.lineup
                        print players
                        pass
            else:
                try:
                    self.create_game_played(self.get_person(player))
                except:
                    import pdb; pdb.set_trace()
                    pass

    def figure_player(self, n):
        n = n.strip()
        
        if n.lower() in ("unassisted", "pk", "own goal"):
            return


        if "," in n:
            last, first = [e.strip() for e in n.split(",")]
        elif "." in n:
            first, last = [e.strip() for e in n.split(".")]
        else:
            last = n
            first = ''
            

        players = self.get_players()
        matches = [e for e in players if last in e]

        if len(matches) == 0:
            import pdb; pdb.set_trace()

        if len(matches) == 1:
            return matches[0]

        else:
            better_matches = [e for e in matches if e.startswith(first)]
            if len(better_matches) == 1:
                return better_matches[0]
            else:
                better_matches = [e for e in matches if e.endswith(last)]
                if len(better_matches) == 1:
                    return better_matches[0]


        import pdb; pdb.set_trace()
        
        


        print n
        print players
        print
        return


    def process_goals(self):
        if self.game is None:
            return

        if not self.scores:
            return

        gr = GoalRecord(game=self.game, team=self.team, description=self.scores)
        gr.save()
        return

        minute_re = re.compile("(?P<minute>\d+)\+?")
        scorers = self.scores.split(";")
        for scorer in scorers:
            try:
                minute_s = minute_re.search(scorer).groups()[0]
            except:
                import pdb; pdb.set_trace()
            nscorer = scorer.replace(minute_s, '')
            if "(" not in nscorer:
                self.figure_player(nscorer)
            else:
                try:
                    g, a = nscorer.split("(")
                except:
                    import pdb; pdb.set_trace()
                a = a.replace(")", "")

                assisters = []
                pieces = [e.strip() for e in assisters]
                for i, n in enumerate(pieces):
                    next_piece = pieces[i]
                    if len(n) == 1:
                        pass
                    elif len(next_piece) == 1:
                        name = "%s, %s" % (n, next_piece)
                        assisters.append(name)
                    else:
                        assisters.append(n)

                try:
                    assert len(assisters) <= 2
                except AssertionError:
                    import pdb; pdb.set_trace()

                self.figure_player(g)
                for e in assisters:
                    self.figure_player(e)

            


if __name__ == "__main__":
    process_file(sys.argv[1])
            
        
            


    

