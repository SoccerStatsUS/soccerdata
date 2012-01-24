from soccerdata import mongo

import datetime

# What is this for?

def check():
    # Verify
    check_standings()
    check_goals()
    check_people()
    check_games()
    check_lineups()
    check_stats()


def check_standings():
    """
    Check that standings are valid.
    """
    for s in mongo.soccer_db.standings.find():

        # Check that total games is equal to the sum of wins, losses, etc.
        games = s['games']
        try:
            games2 = s['wins'] + s['losses'] + (s['ties'] or 0) + (s['shootout_wins'] or 0) + (s['shootout_losses'] or 0)
        except:
            import pdb; pdb.set_trace()
        if games != games2:
            print "Games do not match for: %s" % s
        


def check_people():
    # Not sure what kind of consistency checking is necessary here.
    pass

def check_games():
    """
    """

    game_fields = [
        'home_team',
        'away_team',
        'home_score',
        'away_score',
        'date',
        'season',
        'competition'
        ]

    for game in mongo.soccer_db.games.find():
        for field in game_fields:
            try:
                assert field in game
            except:
                print "% missing fields from game %s" % game
                continue
            #assert(type(game['date']) == datetime.date)
            #assert(type(away_score) == int)
            #assert(type(home_score) == int)

            


def check_lineups():
    pass

def check_goals():
    pass

    
def check_stats():
    pass


if __name__ == "__main__":
    check()
