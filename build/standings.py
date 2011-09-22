# A standings object. Used to generate standings.
# Doing this wrong?


def get_standing(games):
    return Standing(games).standings()

class Standing(object):

    def __init__(self, games):
        # Games is probably a cursor object!
        self.games = games

        self.wins = self.get_wins(games)
        self.losses = self.get_losses(games)
        self.ties = self.get_ties(games)
        self.goals_for = self.get_for(games)
        self.goals_against = self.get_against(games)


    def get_results(self, games):
        from collections import defaultdict
        wins = defaultdict(int)
        losses = defaultdict(int)
        ties = defaultdict(int)
        goals_for = defaultdict(int)
        goals_against = defaultdict(int)
        for game in games:
            h, a = game['home_score'], game['away_score']
            try:
                ht, at = game['home_team'], game['away_team']
            except:
                import pdb; pdb.set_trace()
            
            goals_for[ht] += h
            goals_against[ht] += a

            goals_for[at] += a
            goals_against[at] += h

            if h == a:
                ties[ht] += 1
                ties[at] += 1
            elif h > a:
                wins[ht] += 1
                losses[at] += 1
            else:
                losses[ht] += 1
                wins[at] += 1
        return wins, losses, ties, goals_for, goals_against

    def get_wins(self, games):
        return self.get_results(games)[0]

    def get_losses(self, games):
        return self.get_results(games)[1]

    def get_ties(self, games):
        return self.get_results(games)[2]
                
    def get_for(self, games):
        return self.get_results(games)[3]

    def get_against(self, games):
        return self.get_results(games)[4]

    def standings(self):
        l = []
        for team in sorted(self.wins.keys()):
            t = (team, self.wins[team], self.losses[team], self.ties[team], self.goals_for[team], self.goals_against[team])
            l.append(t)
        return l

    def print_standings(self):
        print "\n\n\n"
        header = ["name", "wins", "losses", "ties", "goals for", "goals against"]
        print "\t".join(header)
        for e in self.standings():
                try:
                    "\t".join([str(a) for a in e])
                except UnicodeEncodeError:
                    print "CANNOT PRINT ASCII ERROR"

            
