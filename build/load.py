from mongo import generic_load, soccer_db


def load():
    # load
    load_people()
    load_games()
    load_goals()
    load_lineups()
    load_salaries()
    load_drafts()
    load_lists()
    load_stats()




def load_people():
    """
    Loads my MLS and USL bios.
    """
    # Add:
    # wikipedia bios
    # cnnsi bios.
    # soccernet bios
    from text import bios
    generic_load(soccer_db.chris_bios, bios.load_bios)



def load_games():
    from text import lineups, mls
    from scrapers import fbleague, fifa, nasl, rsssf

    # These are working.
    # General
    #generic_load(soccer_db.world_cup_games, statto.scrape_all_games)

    # World cups 1930 to 2006
    #generic_load(soccer_db.world_cup_games, fifa.scrape_all_world_cup_games)

    # MLS soccer game results to 1996
    generic_load(soccer_db.mlsoccer_games, mls.scrape_all_games)
    # MLS scores from 1996 to 2010
    generic_load(soccer_db.scaryice_games, lineups.load_all_scores)
    # NASL scores for 2011
    generic_load(soccer_db.nasl_games, nasl.scrape_scores)
    # Some European scores, primarily Spanish.
    generic_load(soccer_db.fbleague_games, fbleague.scrape_all_seasons)
    # Europe
    # generic_load(soccer_db.cnnsi_games, cnnsi.scrape_all_games)
    # generic_load(soccer_db.rsssf_mls_games, rsssf.mls.scrape_all_games)
    # generic_load(soccer_db.rsssf_spain_games, rsssf.mls.scrape_spain_games)
    # generic_load(soccer_db.rsssf_australia_games, rsssf.mls.scrape_australia_games)


# Goals

def load_goals():
    from scrapers import fifa
    from text import lineups

    # Working:
    #generic_load(soccer_db.world_cup_goals, fifa.scrape_all_world_cup_goals)

    #Todo:
    # generic_load(soccer_db.scaryice_goals, fifa.lineups.load_all_goals)




def load_lineups():
    # No lineups ready yet.
    pass


def load_salaries():
    print "Loading mls salaries."
    from text import salaries
    generic_load(soccer_db.mls_salaries, salaries.load_salaries)



def load_drafts():
    print "Loading mls drafts."
    from text import drafts
    generic_load(soccer_db.mls_drafts, drafts.load_drafts)


def load_lists():
    # MVP winners etc.
    pass

def load_stats():
    pass
