from soccerdata.mongo import generic_load, soccer_db
from soccerdata.text import bios, lineups,  salaries, drafts
from soccerdata.scrapers import fbleague, fifa, nasl, rsssf, mls

from soccerdata.scrapers import eufootball



def load():
    # Cities
    # Countries
    # Confederations
    # Leagues
    # Competitions
    # Stadiums

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

    generic_load(soccer_db.chris_bios, bios.load_bios)



def load_games():

    # These are working.
    # General
    #generic_load(soccer_db.world_cup_games, statto.scrape_all_games)

    # World cups 1930 to 2006
    #generic_load(soccer_db.world_cup_games, fifa.scrape_all_world_cup_games)

    # MLS soccer game results to 1996
    generic_load(soccer_db.mlssoccer_games, mls.scrape_all_games)
    # MLS scores from 1996 to 2010
    generic_load(soccer_db.scaryice_games, lineups.load_all_games)
    # NASL scores for 2011
    generic_load(soccer_db.nasl_games, nasl.scrape_scores)
    # Some European scores, primarily Spanish.
    generic_load(soccer_db.fbleague_games, fbleague.scrape_all_seasons)

    # All-time European national team games.
    #generic_load(soccer_db.eufootball_games, eufootball.scrape_all_games)

    # Europe
    # generic_load(soccer_db.cnnsi_games, cnnsi.scrape_all_games)
    # generic_load(soccer_db.rsssf_mls_games, rsssf.mls.scrape_all_games)
    # generic_load(soccer_db.rsssf_spain_games, rsssf.mls.scrape_spain_games)
    # generic_load(soccer_db.rsssf_australia_games, rsssf.mls.scrape_australia_games)


# Goals

def load_goals():

    # Working:
    #generic_load(soccer_db.world_cup_goals, fifa.scrape_all_world_cup_goals)

    generic_load(soccer_db.scaryice_goals, lineups.load_all_goals)



def load_lineups():
    # No lineups ready yet.
    pass


def load_salaries():
    print "Loading mls salaries."

    generic_load(soccer_db.mls_salaries, salaries.load_salaries)



def load_drafts():
    print "Loading mls drafts."

    generic_load(soccer_db.mls_drafts, drafts.load_drafts)


def load_lists():
    # MVP winners etc.
    pass

def load_stats():
    pass
