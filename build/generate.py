from soccerdata.mongo import soccer_db, insert_rows

from standings import get_standings

from collections import defaultdict

# I think I should just generate standings directly from soccer_db.games.
# And then check those against downloaded standings.


def generate():
    # Generate standings
    generate_standings(soccer_db.games, soccer_db.standings)
    generate_stats()


def generate_standings(src, dst):
    # Load seasons so we know which
    # we have to generate standings for.
    soccer_db.standings.drop()
    seasons = set()

    for doc in src.find():
        try:
            t = (doc['competition'], doc['season'])
        except:
            import pdb; pdb.set_trace()
        seasons.add(t)

    for t in seasons:
        competition, season = t
        d = {'competition': competition, 'season': season}
        games = [e for e in src.find(d)] # Cursor to list.
        standings = get_standings(games, competition, season)
        insert_rows(dst, standings)


def filled_stats():
    """
    Game, team, competition, season combinations
    that have stats already.
    """
    # Don't really need a set?
    # Can just do a list comprehension.
    stats = set()
    for e in soccer_db.stats.find():
        try:
            t = (e['name'], e['team'], e['competition'], e['season'])
        except:
            import pdb; pdb.set_trace()
    return stats
        
             
def generate_stats():
    stat_tuples = filled_stats()
    d = {}

    # Just generating goal stats.
    # Should generate lineup stats as well.
    for e in soccer_db.goals.find():
        t = (e['player'], e['team'], e['competition'], str(e['date'].year))
        if t not in stat_tuples:
            if t not in d:
                d[t] = 1
            else:
                d[t] += 1
    
    stats = []
    for (player, team, competition, season), goals in d.items():
        stats.append({
                'player': player,
                'team': team,
                'competiton': competition,
                'season': season,
                'minutes': None,
                'games_started': None,
                'games_played': None,
                'goals': goals,
                'assists': None,
                'shots': None,
                'shots_on_goal': None,
                'fouls_committed': None,
                'fouls_suffered': None,
                'yellow_cards': None,
                'red_cards': None,
                })
    
    insert_rows(soccer_db.stats, stats)
    

if __name__ == "__main__":
    generate()

