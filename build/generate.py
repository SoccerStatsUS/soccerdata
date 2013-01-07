
from soccerdata.mongo import soccer_db, insert_rows, generic_load

from standings import get_standings

from collections import defaultdict



# I think I should just generate standings directly from soccer_db.games.
# And then check those against downloaded standings.


make_stat_tuple = lambda name, d: (name, d['team'], d['season'], d['competition'])


def generate():
    # Generate standings
    #generate_standings(soccer_db.games, soccer_db.standings)
    #generate_lineup_stats(soccer_db.mls_reserve_lineups.find())

    generate_db_stats()



def generate2():
    generate_all_standings()

    generate_competition_stats()
    

def make_state_code_dict():

    d = {}
    for e in soccer_db.states.find():
        if e['abbreviation']:
            d[e['abbreviation']] = e['name']

    return d



def generate_competition_stats():

    def competition_generate(competition):
        x = generate_stats(soccer_db.goals.find({'competition': competition}), soccer_db.lineups.find({"competition": competition}))
        generic_load(soccer_db.stats, lambda: x.values())

    competition_generate('FIFA World Cup')
    competition_generate('FIFA Club World Cup')
    competition_generate('FIFA Confederations Cup')


    competition_generate('Olympic Games')
    competition_generate('Copa America')
    competition_generate('MLS Cup Playoffs')
    competition_generate('MLS Reserve League')
    competition_generate('Eastern Soccer League (1928-1929)')
    competition_generate('AFA Cup')
    competition_generate('U.S. Open Cup')
    competition_generate('International Soccer League')
    competition_generate('Canadian Championship')

    competition_generate('CONCACAF Champions League')
    competition_generate('CONCACAF Champions\' Cup')
    competition_generate('North American SuperLiga')

    competition_generate('American League of Professional Football')
    competition_generate('Liga MX')

    #competition_generate('North American Soccer League')

    

                        

def generate_db_stats():
    
    def standard_generate(source):
        x = generate_stats(soccer_db['%s_goals' % source].find(), soccer_db['%s_lineups' % source].find())
        generic_load(soccer_db['%s_stats' % source], lambda: x.values())

    # This presents the problem of generating stats for games that have not been merged yet.
    # It seems like a much better idea to filter by competition and generate stats after merge.

        """
    standard_generate('nafbl')
    #standard_generate('mls_reserve')
    standard_generate('chris')

    standard_generate('american_cup')
    standard_generate('lewis_cup')
    standard_generate('open_cup')

    #standard_generate('usa')
    #standard_generate('world_cup')
    standard_generate('usl_leach')
    standard_generate('concacaf')

    standard_generate('mexico')

    standard_generate('small')

    standard_generate('ussf2')

    standard_generate('isl')

    standard_generate('tours')

    standard_generate('fifa')

    standard_generate('city')

    standard_generate('esl')
    standard_generate('asl2')
    """

    #x = generate_stats(soccer_db['mls_soccernet_goals'].find({'season': '2012'}), soccer_db['mls_soccernet_lineups'].find({"season": "2012"}))
    #generic_load(soccer_db['mls_soccernet_stats'], lambda: x.values())




def generate_all_standings():
    """Generate rolling standings for a given competition."""
    # Don't generate based on collection (definitely will overcount games.

    def sg(source):
        stg = generate_standings(soccer_db['%s_games' % source].find())
        generic_load(soccer_db['%s_standings' % source], lambda: stg.values())


    def sg2(competition):
        stg = generate_standings2(competition)
        generic_load(soccer_db.standings, lambda: stg)


    sg2('International Soccer League')
    sg2('Eastern Soccer League (1928-1929)')
    sg2('Major League Soccer')
    sg2('North American Soccer League')
    sg2('American Soccer League (1921-1933)')
    sg2('MLS Reserve League')
    sg2('MLS Cup Playoffs')
    sg2('U.S. Open Cup')
    sg2('Hyundai A-League')
    sg2('Canadian Championship')
    sg2('Liga MX')

    """
    sg('lewis_cup')
    sg('open_cup')
    sg('mls_reserve')
    sg('american_cup')
    sg('tours')
    sg('small')
    sg('usa')
    sg('concacaf')
    sg('esl')
    sg('mls_playoffs')


    sg('melvin')

    sg('fifa')
    """

    #stg = generate_standings(soccer_db.mls_soccernet_games.find({'season': '2012'}))
    #generic_load(soccer_db.mls_soccernet_standings, lambda: stg.values())

    #stg = generate_standings(soccer_db.nafbl_games.find({'season': '1895-1896'}))
    #generic_load(soccer_db.nafbl_standings, lambda: stg.values())

    #stg = generate_standings(soccer_db.nafbl_games.find({'season': '1895-1896'}))
    #generic_load(soccer_db.nafbl_standings, lambda: stg.values())



class Standing(object):
    def __init__(self, game, team, standing=None):
        self.team = team
        self.date = game['date']
        self.competition = game['competition']
        self.season = game['season']

        if standing:
            self.wins = standing.wins
            self.ties = standing.ties
            self.losses = standing.losses
            self.goals_for = standing.goals_for
            self.goals_against = standing.goals_against
        else:
            self.wins = self.ties = self.losses = self.goals_for = self.goals_against = 0

        # Not really handling these anywhere yet.
        self.shootout_wins = self.shootout_losses = 0

        ht, at, h, a = [game[k] for k in ['team1', 'team2', 'team1_score', 'team2_score']]

        if team == ht:
            gf, ga = h, a
        else:
            ga, gf = h, a

        self.goals_for += gf or 0
        self.goals_against += ga or 0

        if h == None or a == None:
            return

        if h == a:
            self.ties += 1
        elif ht == team and h > a:
            self.wins += 1
        elif at == team and a > h:
            self.wins += 1
        else:
            self.losses += 1


    def to_dict(self):
        return {
            'team': self.team,
            'date': self.date,
            'competition': self.competition,
            'season': self.season,
            'wins': self.wins,
            'losses': self.losses,
            'ties': self.ties,
            'shootout_wins': self.shootout_wins,
            'shootout_losses': self.shootout_losses,
            'games': self.wins + self.losses + self.ties,
            'goals_for': self.goals_for,
            'goals_against': self.goals_against,
            'final': False,
            }
                
            

def generate_standings2(competition):

    standing_dict = defaultdict(list)

    # This exists so we can find standings with arbitrary datetimes.
    # Seems like this whole thing might be better structured as a dict of lists?

    def generate_team_standing(game, team):

        key = (team, competition, game['season'])

        if key in standing_dict:
            standing = standing_dict[key][-1]
            new_standing = Standing(game, team, standing)
        else:
            new_standing = Standing(game, team)

        standing_dict[key].append(new_standing)

            


    for game in soccer_db.games.find({'competition': competition}).sort('date', 1):

        generate_team_standing(game, game['team1'])
        generate_team_standing(game, game['team2'])

    standings = []
    for lst in standing_dict.values():
        standings.extend([e.to_dict() for e in lst])
    return standings



            
    

        
        
        


def generate_standings(games):
    # Need to remove idea of home team.


    def insert_game(team, game):
        t = (team, game['competition'], game['season'])
        if t not in d:
            d[t] = {
                'team': team,
                'competition': t[1],
                'season': t[2],
                'wins': 0,
                'ties': 0,
                'losses': 0,
                'shootout_wins': 0,
                'shootout_losses': 0,
                'games': 0,
                'goals_for': 0,
                'goals_against': 0,
                }

        d[t]['games'] += 1
        key = get_key(team, game)
        d[t][key] += 1

        if team == game['team1']:
            gf, ga = game['team1_score'], game['team2_score']
        else:
            gf, ga = game['team2_score'], game['team1_score']

        try:
            d[t]['goals_for'] += gf or 0
            d[t]['goals_against'] += ga or 0
        except:
            import pdb; pdb.set_trace()

    def get_key(team, game):
        ht, at, h, a = [game[k] for k in ['team1', 'team2', 'team1_score', 'team2_score']]
        if h == a:
            return 'ties'
        if ht == team and h > a:
            return 'wins'
        if at == team and a > h:
            return 'wins'
        return 'losses'
        
        

    d = {}
    for game in games:
        insert_game(game['team1'], game)
        insert_game(game['team2'], game)

    return d




def generate_stats(goals=[], lineups=[]):
    """
    Generate a stat dict from goals, lineups
    """
    # Need to add:
    # cards, 
    # game events
    

    sd = {}

    def add_item(t, key, amount=1):
        """
        Add goal, lineup, etc to the stat dict.
        """

        # Generate empty stat objects.
        if t not in sd:
            name, team, season, competition = t
            if not name:
                "Name not in tuple %s" % unicode(t)
                return

            sd[t] = {
                'name': name,
                'team': team,
                'season': season,
                'competition': competition,
                'goals': 0,
                'assists': 0,
                'games_played': 0,
                'games_started': 0,
                'minutes': 0,
                }

        if t[0] == 'Omar Bravo' and t[1] == 'UANL':
            print sd[t]


        # Increment the appropriate key.
        sd[t][key] += amount


    for goal in goals:
        t = make_stat_tuple(goal['goal'], goal)
        add_item(t, 'goals')

        for assist in goal['assists']:
            t = make_stat_tuple(assist, goal)
            add_item(t, 'assists')

    # This is where things are breaking for Omar Bravo.
    for lineup in lineups:
        t = make_stat_tuple(lineup['name'], lineup)

        # Empty lineup 
        if lineup['on'] == 0 and lineup['off'] == 0:
            pass
        else:
            if lineup['on'] == 0:
                add_item(t, 'games_started')
            add_item(t, 'games_played')

            if lineup['off'] is not None and lineup['on'] is not None:
                try:
                    minutes = lineup['off'] - lineup['on']
                    add_item(t, 'minutes', minutes)
                except TypeError:
                    print lineup
            else:
                print "Missing minute data for appearance."
        

    return sd

    

             
if __name__ == "__main__":
    generate()

