from soccerdata.mongo import generic_load, soccer_db, insert_rows, insert_row

from soccerdata.teams import get_team


def merge():
    merge_games()
    merge_goals()
    merge_stats()





def merge_games():
    soccer_db.games.drop()
    merge_mls()
    #merge_nasl()
    merge_fbleague()
    merge_aleague()

def merge_goals():
    soccer_db.goals.drop()
    insert_rows(soccer_db.goals, soccer_db.scaryice_goals.find())

def merge_stats():
    soccer_db.stats.drop()
    insert_rows(soccer_db.stats, soccer_db.mls_stats.find())



def merge_fbleague():
    insert_rows(soccer_db.games, soccer_db.fbleague_games.find())


def merge_teams(coll, teams):
    for team in teams:
        # Is this the right place for this?
        d = team.copy()
        d['home_team'] = get_team(d['home_team'])
        d['away_team'] = get_team(d['away_team'])
        d.pop("_id")
        insert_row(coll, d)

def merge_mls():
    # Better to start with scaryice games?
    merge_teams(soccer_db.games, soccer_db.scaryice_games.find())
    #insert_rows(soccer_db.games, soccer_db.mlssoccer_games.find())

def merge_nasl():
    insert_rows(soccer_db.games, soccer_db.nasl_games.find())    

def merge_aleague():
    insert_rows(soccer_db.games, soccer_db.aleague_games.find())    



if __name__ == "__main__":
    merge()
