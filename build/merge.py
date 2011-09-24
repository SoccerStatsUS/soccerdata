from soccerdata.mongo import generic_load, soccer_db, insert_rows, insert_row


def merge():
    merge_games()


def merge_games():
    #merge_mls()
    merge_nasl()
    merge_fbleague()
    merge_scaryice()


def merge_scaryice():
    insert_rows(soccer_db.games, soccer_db.scaryice_games.find())

def merge_fbleague():
    insert_rows(soccer_db.games, soccer_db.fbleague_games.find())

def merge_mls():
    # Better to start with scaryice games?
    # Not confident either of these are only MLS.
    insert_rows(soccer_db.games, soccer_db.mlssoccer_games.find())

def merge_nasl():
    insert_rows(soccer_db.games, soccer_db.nasl_games.find())    
