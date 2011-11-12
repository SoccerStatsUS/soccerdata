
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
    mls_reserve_stats = generate_stats(soccer_db.mls_reserve_goals.find(), soccer_db.mls_reserve_lineups.find())
    generic_load(soccer_db.mls_reserve_stats, lambda: mls_reserve_stats.values())

    world_cup_stats = generate_stats(soccer_db.fifa_goals.find(), soccer_db.fifa_lineups.find())
    generic_load(soccer_db.fifa_stats, lambda: world_cup_stats.values())

    standings = generate_standings(soccer_db.mls_reserve_games.find())
    generic_load(soccer_db.mls_reserve_standings, lambda: standings.values())

    standings = generate_standings(soccer_db.usa_games.find())
    generic_load(soccer_db.usa_standings, lambda: standings.values())

    usa_stats = generate_stats(soccer_db.usa_goals.find(), soccer_db.usa_lineups.find())
    generic_load(soccer_db.usa_stats, lambda: usa_stats.values())


    


def generate_standings(games):

    def insert_game(team, game):
        t = (team, game['competition'], game['season'])
        if t not in d:
            d[t] = {
                'name': team,
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

        if team == game['home_team']:
            gf, ga = game['home_score'], game['away_score']
        else:
            gf, ga = game['away_score'], game['home_score']

        d[t]['goals_for'] += gf
        d[t]['goals_against'] += ga

    def get_key(team, game):
        ht, at, h, a = [game[k] for k in ['home_team', 'away_team', 'home_score', 'away_score']]
        if h == a:
            return 'ties'
        if ht == team and h > a:
            return 'wins'
        if at == team and a > h:
            return 'wins'
        return 'losses'
        
        

    d = {}
    for game in games:
        insert_game(game['away_team'], game)
        insert_game(game['home_team'], game)

    return d
        

def generate_stats(goals=[], lineups=[]):
    # Generate stat dict.
    # 
    sd = {}

    def add_item(t, key, amount=1):
        if t not in sd:
            name, team, season, competition = t
            if not name:
                print t
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

        sd[t][key] += amount


    for goal in goals:
        t = make_stat_tuple(goal['goal'], goal)
        add_item(t, 'goals')

        for assist in goal['assists']:
            t = make_stat_tuple(assist, goal)
            add_item(t, 'assists')

    for lineup in lineups:
        t = make_stat_tuple(lineup['name'], lineup)

        # Empty lineup 
        if lineup['on'] == 0 and lineup['off'] == 0:
            pass
        else:
            if lineup['on'] == 0:
                add_item(t, 'games_started')
            add_item(t, 'games_played')
            try:
                minutes = lineup['off'] - lineup['on']
                add_item(t, 'minutes', minutes)
            except TypeError:
                print lineup
        

    return sd

    

             
if __name__ == "__main__":
    generate()

