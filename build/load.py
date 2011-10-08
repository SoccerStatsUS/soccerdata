from soccerdata.mongo import generic_load, soccer_db

from soccerdata.scrapers import fbleague, fifa, nasl, rsssf, mls
from soccerdata.text import lineups

def load():
    """
    Load all data.
    """

    # Offline data
    load_yaml()
    load_chris()
    load_scaryice()

    # Scraped data
    load_mls()
    #load_nasl()
    #load_soccernet()

    #load_mediotiempo()
    #load_wiki()
    
    #load_fifa()



def load_yaml():
    from soccerdata.text import syaml
    print "Loading teams.\n"
    generic_load(soccer_db.yaml_teams, syaml.load_teams)


def load_chris():
    print "Loading chris text bios.\n"
    from soccerdata.text import bios, salaries, drafts, stats
    generic_load(soccer_db.chris_bios, bios.merged_bios)

    print "Loading chris stats.\n"
    generic_load(soccer_db.chris_stats, stats.process_all_chris_stats)

    print "Loading MLS salary data.\n"
    generic_load(soccer_db.mls_salaries, salaries.load_salaries)

    print "Loading mls draft data.\n"
    generic_load(soccer_db.mls_drafts, drafts.load_drafts)

    # Need to load other league stats.


def load_scaryice():
    # MLS lineup data 1996-2010
    print "Loading scaryice score data.\n"
    generic_load(soccer_db.scaryice_games, lineups.load_all_games_scaryice)

    print "Loading scaryice goal data.\n"
    generic_load(soccer_db.scaryice_goals, lineups.load_all_goals_scaryice)

    print "Loading scaryice lineup data.\n"
    generic_load(soccer_db.scaryice_lineups, lineups.load_all_lineups_scaryice)


def load_mls():
    print "Loading MLSsoccer.com player bios\n"
    generic_load(soccer_db.mls_bios, mls.scrape_all_bios_mlssoccer)

    print "Loading MLSsoccer.com stats\n"
    #generic_load(soccer_db.mls_stats, mls.scrape_all_stats_mlssoccer)

    print "Loading MLSsoccer.com game data.\n"
    #generic_load(soccer_db.mls_games, mls.scrape_all_games_mlssoccer)




def load_nasl():
    # 2011 NASL scores.
    print "Loading 2011 NASL games."
    generic_load(soccer_db.nasl_games, nasl.scrape_scores)


def load_soccernet():
    from soccerdata.scrapers import soccernet
    generic_load(soccer_db.soccernet_games, lambda: soccernet.scrape_all_league_games('usa.1'))
    generic_load(soccer_db.soccernet_goals, lambda: soccernet.scrape_all_league_goals('usa.1'))
    #generic_load(soccer_db.soccernet_lineups, lambda: soccernet.scrape_all_league_lineups('usa.1'))



def load_mediotiempo():
    pass

def load_wiki():
    pass

# European and other data.


def load_fbleague():
    # Various European league scores.
    print "Loading fbleague game scores."
    generic_load(soccer_db.fbleague_games, fbleague.scrape_all_seasons)


def load_aleague():
    from soccerdata.scrapers import australia
    # Australian A-league.
    print "Loading A-league.com game scores."
    generic_load(soccer_db.aleague_games, australia.scrape_all_games)


# International

def load_fifa():
    # World cup games from 1930 to 2006.
    print "Loading fifa world cup games."
    generic_load(soccer_db.fifa_games, fifa.scrape_all_world_cup_games)

    generic_load(soccer_db.fifa_goals, fifa.scrape_all_world_cup_goals)



def load_eufootball():
    from soccerdata.scrapers import eufootball
    # All-time European national team games.
    print "Loading eufootball.com game scores."
    generic_load(soccer_db.eufootball_games, eufootball.scrape_all_games)    


# Not using these.
def load_statto():
    # Various historical scores.

    generic_load(soccer_db.world_cup_games, statto.scrape_all_games)    






if __name__ == "__main__":
    load()
