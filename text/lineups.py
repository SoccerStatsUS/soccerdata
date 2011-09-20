#!/usr/bin/env python

# Need to redo a bunch of DC United Goal entries from around 2003 and 2004.  Format is Adu (34;85), which is not useable...

# Looks like this should probably just be redone.

import datetime
import os
import re
import sys



LINEUPS_DIR = "/home/chris/www/soccer/data/lineups/"



translation_map = {
    'Stoichkov': 'Stoitchkov'
}

team_mapping = {
    "Chicago": u'Chicago Fire',
    "Chivas USA": u'Chivas USA',
    "Colorado": u'Colorado Rapids',
    "Columbus": u'Columbus Crew',
    "DC United": u'D.C. United',
    "Dallas": u'FC Dallas',
    "FC Dallas": u'FC Dallas',
    "Houston": u'Houston Dynamo',
    "Kansas City": u'Kansas City Wizards',
    "Los Angeles": u'Los Angeles Galaxy',
    "Miami": u'Miami Fusion',
    "New England": u'New England Revolution',
    "New York": u'New York Red Bulls',
    "MetroStars": u'New York Red Bulls',
    "Metrostars": u'New York Red Bulls',
    "Philadelphia": u'Philadelphia Union',
    "Real Salt Lake": u'Real Salt Lake',
    "San Jose": u'San Jose Earthquakes',
    "Seattle": u'Seattle Sounders',
    "Tampa Bay": u'Tampa Bay Mutiny',
    "Toronto": u'Toronto FC',
 }


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



def process_files():
    files = os.listdir(LINEUPS_DIR)
    #for fn in files[3:]:
    for fn in files:
        print fn
        p = os.path.join(LINEUPS_DIR, fn)
        process_lineup(p)

def process_file(fn):
    p = os.path.join(LINEUPS_DIR, fn)
    process_lineup(p)


def process_lineup(p):
    fn = os.path.split(p)[1]
    f = open(p)
    for line in f:
        line = line.strip()
        if line:
            lineup = Lineup(line, fn)
            lineup.process_games()
            lineup.process_goals()
    f.close()


class Lineup(object):
    def __init__(self, line, file):
        fn = file.split(".")[0]
        self.team = Team.objects.get(short_name=file_mapping[fn])

        self.line = line

        self.lineup = self._format_lineup(line.split("\t")[8])
        self.scores = line.split("\t")[7]

        
        self.players = [e.strip() for e in self.lineup.split(",")]

        self.game = self._get_game()
        self.player_failures = set()
        self.games_played = []

    def get_players(self):
        # Fixme
        return [str(e.player) for e in self.games_played]
        return [e.player.name for e in self.games_played]


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
        
        if opponent not in team_mapping:
            #print opponent
            return None

        opponent_team = Team.objects.get(short_name=team_mapping[opponent])
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


    def get_person(self, name):
        name = name.strip()
        try:
            p = Person.objects.get_person(name)
            return p
        except:
            self.player_failures.add(name)

        
    def create_game_played(self, player, on=0, off=90):
        gp = GameAppearance(game=self.game,
                            team=self.team,
                            player=player,
                            on=on,
                            off=off)
        gp.save()
        self.games_played.append(gp)


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
            
        if last in translation_map:
            last = translation_map[last]

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
            
        
            


    

