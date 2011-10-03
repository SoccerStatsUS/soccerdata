from soccerdata.mongo import soccer_db, insert_rows

from standings import get_standings

# I think I should just generate standings directly from soccer_db.games.
# And then check those against downloaded standings.


def generate():
    # Generate standings
    generate_standings(soccer_db.scaryice_games, soccer_db.standings)


    generate_stats()
    generate_transfers()


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






def generate_stats():
    pass


def generate_transfers():
    pass
    

if __name__ == "__main__":
    generate_standings()

