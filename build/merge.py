from soccerdata.mongo import generic_load, soccer_db, insert_rows, insert_row


def merge():
    merge_games()
    merge_goals()




def merge_games():
    soccer_db.games.drop()
    merge_mls()
    #merge_nasl()
    merge_fbleague()
    merge_aleague()


def merge_fbleague():
    insert_rows(soccer_db.games, soccer_db.fbleague_games.find())

def merge_mls():
    # Better to start with scaryice games?
    insert_rows(soccer_db.games, soccer_db.scaryice_games.find())
    #insert_rows(soccer_db.games, soccer_db.mlssoccer_games.find())

def merge_nasl():
    insert_rows(soccer_db.games, soccer_db.nasl_games.find())    

def merge_aleague():
    insert_rows(soccer_db.games, soccer_db.aleague_games.find())    

def merge_goals():
    insert_rows(soccer_db.goals, soccer_db.scaryice_goals.find())


if __name__ == "__main__":
    merge()
