from soccerdata.mongo import generic_load, soccer_db

from soccerdata.scrapers import fbleague, rsssf, mls
from soccerdata.text import lineups

from soccerdata import scrapers
from soccerdata import text

def first_load():
    """
    Load all data.
    """

    load_standings()
    load_teams()
    load_nasl()
    load_apsl()
    return

    load_usl()
    load_mls()

    load_chris()
    load_scaryice()
    return

    # Scraped data
    load_soccernet()
    load_fifa()
    load_kicker()
    #load_mediotiempo()


def second_load():
    # This is for data that should not be loaded
    # until after we have merged all data.
    # e.g. wikipedia team bios based on game results.
    
    # These provide no data to any other items.

    #load_yaml() # Could be loaded earlier, but not really thematically
    #load_wiki()
    pass


def load_standings():
    from soccerdata.text import standings
    print "Loading chris standings.\n"
    generic_load(soccer_db.chris_standings, standings.process_standings)

    

def load_teams():
    from soccerdata.text import syaml
    print "Loading teams.\n"
    generic_load(soccer_db.yaml_teams, syaml.load_teams)


def load_wiki():
    pass



def load_chris():
    print "Loading chris text bios.\n"
    from soccerdata.text import bios, salaries, drafts


    print "Loading chris bios.\n"
    generic_load(soccer_db.chris_bios, bios.merged_bios)
    

    print "Loading MLS salary data.\n"
    generic_load(soccer_db.mls_salaries, salaries.load_salaries)

    print "Loading mls draft data.\n"
    generic_load(soccer_db.mls_drafts, drafts.load_drafts)



def load_scaryice():
    # MLS lineup data 1996-2010
    print "Loading scaryice score data.\n"
    generic_load(soccer_db.scaryice_games, lineups.load_all_games_scaryice)
    return

    print "Loading scaryice goal data.\n"
    generic_load(soccer_db.scaryice_goals, lineups.load_all_goals_scaryice)
    
    print "Loading scaryice lineup data.\n"
    generic_load(soccer_db.scaryice_lineups, lineups.load_all_lineups_scaryice)


def load_nasl():
    from soccerdata.text import stats

    print "Loading NASL stats.\n"
    generic_load(soccer_db.nasl_stats, stats.process_nasl_stats)


def load_apsl():
    from soccerdata.text import apsl
    print "loading apsl stats"
    generic_load(soccer_db.apsl_stats, apsl.process_apsl_stats)

    print "loading apsl scores"
    generic_load(soccer_db.apsl_games, apsl.process_apsl_scores)




def load_mls():
    from soccerdata.text import stats
    print "Loading MLSsoccer.com game data.\n"
    generic_load(soccer_db.mls_games, mls.scrape_all_games_mlssoccer)

    print "Loading chris mls stats.\n"
    generic_load(soccer_db.mls_stats, stats.process_mls_stats)


    return

    print "Loading MLSsoccer.com player bios\n"
    generic_load(soccer_db.mls_bios, mls.scrape_all_bios_mlssoccer)


    print "Loading MLSsoccer.com stats\n"
    generic_load(soccer_db.mls_stats, mls.scrape_all_stats_mlssoccer)



def load_usl():
    from soccerdata.text import stats

    def load_scores():
        from soccerdata.scrapers import nasl
        generic_load(soccer_db.usl_games, nasl.scrape_scores)

    def load_stats():
        from soccerdata.text import nasl
        generic_load(soccer_db.usl_stats, nasl.process_stats)

    print "Loading 2011 NASL games."
    load_scores()
    print "Loading 2011 NASL stats."
    load_stats()

    print "Loading usl stats.\n"
    generic_load(soccer_db.usl_stats, stats.process_usl_stats, delete=False)




def load_soccernet_league(code):
    from soccerdata.scrapers import soccernet
    generic_load(soccer_db.soccernet_games, lambda: soccernet.scrape_all_league_games(code), delete=False)
    generic_load(soccer_db.soccernet_goals, lambda: soccernet.scrape_all_league_goals(code), delete=False)
    generic_load(soccer_db.soccernet_lineups, lambda: soccernet.scrape_all_league_lineups(code), delete=False)




def load_soccernet():
    soccer_db.soccernet_games.drop()
    soccer_db.soccernet_goals.drop()
    soccer_db.soccernet_lineups.drop()
    return
    load_soccernet_league('usa.1')
    load_soccernet_league('mex.1')

def load_fifa():
    from soccerdata.scrapers import fifa
    generic_load(soccer_db.fifa_games, fifa.scrape_all_world_cup_games)
    return
    generic_load(soccer_db.fifa_goals, fifa.scrape_all_world_cup_goals)
    generic_load(soccer_db.fifa_lineups, fifa.scrape_all_world_cup_lineups)


def load_kicker():
    from soccerdata.scrapers import kicker
    generic_load(soccer_db.kicker_games, kicker.scrape_all_kicker_seasons)





def load_mediotiempo():
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
