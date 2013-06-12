
from collections import defaultdict


from soccerdata.mongo import soccer_db, insert_rows, generic_load
from standings import get_standings




# I think I should just generate standings directly from soccer_db.games.
# And then check those against downloaded standings.


make_stat_tuple = lambda name, d: (name, d['team'], d['season'], d['competition'])


def generate():
    pass


def generate2():
    generate_competition_standings()
    generate_competition_stats()

    #generate_mongo_indexes()

# Delete this. Not working here - moving to build.sh
def generate_mongo_indexes():
    from mongo import soccer_db
    soccer_db.games.ensure_index("date")
    

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

    competition_generate('FIFA Club World Cup')

    competition_generate('Intercontinental Cup')
    competition_generate('Interamerican Cup')
    competition_generate('Recopa Sudamericana')
    competition_generate('SURUGA Bank Championship')
    competition_generate('La Copita del Mundo')

    competition_generate('FIFA World Cup')
    competition_generate('FIFA Confederations Cup')
    competition_generate('World Cup Qualifying')
    competition_generate('Olympic Games')

    competition_generate('International Friendly')

    competition_generate('Gold Cup')    
    competition_generate('CONCACAF Championship')
    competition_generate('Copa Centroamericana')
    competition_generate('Caribbean Cup')
    competition_generate('Copa America')
    competition_generate('Copa Merconorte')
    competition_generate('Copa Mercosur')

    competition_generate('CONCACAF Champions League')
    competition_generate('CONCACAF Cup Winners Cup')
    competition_generate('CONCACAF Giants Cup')
    #competition_generate('CONCACAF Champions\' Cup')
    competition_generate('North American SuperLiga')
    competition_generate('Copa Interclubes UNCAF')
    competition_generate('CFU Club Championship')

    competition_generate('Copa Libertadores')
    competition_generate('Copa Sudamericana')
    competition_generate('Copa CONMEBOL'),
    competition_generate('Copa Masters CONMEBOL'),

    competition_generate('MLS Cup Playoffs')
    competition_generate('MLS Reserve League')

    competition_generate('AFA Cup')
    competition_generate('U.S. Open Cup')
    competition_generate('Canadian Championship')

    competition_generate('American League of Professional Football')
    competition_generate('Eastern Soccer League (1928-1929)')
    competition_generate('International Soccer League')
    competition_generate('USSF Division 2 Professional League')

    competition_generate('Liga MX')
    competition_generate('Liga MX Liguilla')
    competition_generate('Campeón de Campeones')

    competition_generate('Campeonato Brasileiro Série A')
    competition_generate('Categoría Primera A')

    competition_generate('Chinese Super League')

    competition_generate('American Soccer League (1934-1983)')

    competition_generate('Mundialito')

    competition_generate('Women\'s Professional Soccer')
    competition_generate('Women\'s United Soccer Association')
    #competition_generate('North American Soccer League')


def generate_competition_standings():
    """Generate rolling standings for a given competition."""
    # Don't generate based on collection (definitely will overcount games.

    def sg2(competition):
        stg = generate_standings(competition)
        generic_load(soccer_db.standings, lambda: stg)


    sg2('FIFA Club World Cup')
    sg2('Intercontinental Cup')
    sg2('Interamerican Cup')
    sg2('Recopa Sudamericana')
    sg2('SURUGA Bank Championship')
    sg2('La Copita del Mundo')

    sg2('Copa Libertadores')
    sg2('Copa Sudamericana')
    sg2('Copa CONMEBOL')
    sg2('Copa Masters CONMEBOL')

    sg2('CONCACAF Champions League')
    sg2('Copa Interclubes UNCAF')
    sg2('CFU Club Championship')
    sg2('CONCACAF Cup Winners Cup')
    sg2('CONCACAF Giants Cup')
    sg2('North American Superliga')

    sg2('Women\'s Professional Soccer')
    sg2('National Women\'s Soccer League')
    sg2('Women\'s Premier Soccer League Elite')
    sg2('Women\'s Premier Soccer League')
    sg2('Women\'s United Soccer Association')


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
                
            

def generate_standings(competition):

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
                #"Name not in tuple %s" % str(t)
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
            print(sd[t])


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
                    print(lineup)
            else:
                pass
                #print("Missing minute data for appearance.")
        

    return sd

    

             
if __name__ == "__main__":
    generate()

