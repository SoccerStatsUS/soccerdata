from soccerdata.mongo import soccer_db, insert_rows

from standings import get_standings

# I think I should just generate standings directly from soccer_db.games.
# And then check those against downloaded standings.


def generate():
    # Generate
    generate_standings()
    generate_stats()
    generate_transfers()


def generate_standings():
    # Load seasons so we know which
    # we have to generate standings for.
    seasons = set()
    coll = soccer_db.games
    for doc in coll.find():
        t = (doc['competition'], doc['season'])
        seasons.add(t)

    for t in seasons:
        competition, season = t
        d = {'competition': competition, 'season': season}
        games = [e for e in coll.find(d)] # Cursor to list.
        standings = get_standings(games, competition, season)
        insert_rows(soccer_db.standings, standings)


def generate_stats():
    pass


def generate_transfers():
    pass
    

if __name__ == "__main__":
    generate_standings()

