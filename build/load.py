from soccerdata.mongo import generic_load, soccer_db

from soccerdata.scrapers import fbleague, rsssf, mls
from soccerdata.text import lineups

from soccerdata import scrapers
from soccerdata import text

def first_load():
    """
    Load all data.
    """

    # Base data.
    load_standings()
    load_teams()
    load_drafts()

    # Scores, stats.
    load_asl()
    load_nasl()
    load_apsl()
    load_mls()
    load_partial()
    load_mls_reserve()
    load_usl()
    load_nasl2()
    load_usa()
    load_world_cup()
    load_ncaa()

    # Scraped data
    #load_soccernet()
    #load_kicker()
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
    generic_load(soccer_db.chris_teams, syaml.load_teams)


def load_drafts():
    from soccerdata.text import drafts
    print "Loading drafts.\n"
    generic_load(soccer_db.chris_drafts, drafts.load_drafts)


def load_partial():
    from soccerdata.text import partial
    print "Loading partial stats.\n"
    generic_load(soccer_db.partial_stats, partial.process_partial_stats)

    
def load_asl():
    from soccerdata.text import awards
    from soccerdata.text import asl

    print "Loading ASL awards.\n"
    generic_load(soccer_db.asl_awards, awards.process_american_cup_awards)
    generic_load(soccer_db.asl_awards, awards.process_us_open_cup_awards, delete=False)
    generic_load(soccer_db.asl_awards, awards.process_asl2_awards, delete=False)
    generic_load(soccer_db.asl_awards, awards.process_lewis_cup_awards, delete=False)

    print "Loading ASL games.\n"
    generic_load(soccer_db.asl_games, asl.process_games)


def load_nasl():
    """
    Load stats from the old nasl and misl.
    """
    from soccerdata.text import stats
    from soccerdata.text import awards
    from soccerdata.text import nasl

    print "Loading NASL stats.\n"
    generic_load(soccer_db.nasl_stats, stats.process_nasl_stats)

    print "Loading NASL awards.\n"
    generic_load(soccer_db.nasl_awards, awards.process_nasl_awards)

    print "Loading NASL games.\n"
    generic_load(soccer_db.nasl_games, nasl.process_games)


    


def load_apsl():
    """
    Load stats and games from the APSL and WSA.
    """
    from soccerdata.text import apsl, awards
    print "loading apsl stats"
    generic_load(soccer_db.apsl_stats, apsl.process_apsl_stats)

    generic_load(soccer_db.apsl_awards, awards.process_wsa_awards)
    

    print "loading apsl scores"
    generic_load(soccer_db.apsl_games, apsl.process_apsl_scores)




def load_mls():
    """
    Load mls data
    Includes stats from mlssoccer.com, 
    hand-compiled coach playing stats,
    and player bios.
    """
    from soccerdata.text import awards
    from soccerdata.text import stats
    from soccerdata.scrapers import mls

    print "Loading MLS awards.\n"
    generic_load(soccer_db.mls_awards, awards.process_mls_awards)

    print "Loading mls bio stats.\n"
    generic_load(soccer_db.mls_stats, mls.scrape_all_bio_stats_mlssoccer)

    print "Loading coach playing stats.\n"
    # Load coach stats that are missing from mlossoccer.com
    generic_load(soccer_db.mls_stats, stats.process_mls_coach_stats, delete=False)

    print "Loading MLSsoccer.com player bios.\n"
    generic_load(soccer_db.mls_bios, mls.scrape_all_bios_mlssoccer)

    # MLS lineup data 1996-2010
    print "Loading scaryice score data.\n"
    generic_load(soccer_db.mls_games, lineups.load_all_games_scaryice)

    print "Loading scaryice goal data.\n"
    generic_load(soccer_db.mls_goals, lineups.load_all_goals_scaryice)
    
    print "Loading scaryice lineup data.\n"
    generic_load(soccer_db.mls_lineups, lineups.load_all_lineups_scaryice)

    return

    print "Loading MLSsoccer.com game data.\n"
    generic_load(soccer_db.mls_games, mls.scrape_all_games_mlssoccer)



def load_mls_reserve():
    """
    Load data from the MLS Reserve League (2011 - )
    """
    from soccerdata.text import reserve

    generic_load(soccer_db.mls_reserve_games, reserve.process_scores)
    generic_load(soccer_db.mls_reserve_lineups, reserve.process_lineups)
    generic_load(soccer_db.mls_reserve_goals, reserve.process_goals)



def load_nasl2():

    def load_scores():
        from soccerdata.scrapers import nasl
        generic_load(soccer_db.nasl2_games, nasl.scrape_scores)

    def load_stats():
        from soccerdata.text import nasl
        generic_load(soccer_db.nasl2_stats, nasl.process_stats)

    print "Loading 2011 NASL games."
    load_scores()
    print "Loading 2011 NASL stats."
    load_stats()


def load_usl():

    """
    Load usl stats and nasl stats.
    """
    from soccerdata.text import stats, awards  

    print "Loading usl stats.\n"
    generic_load(soccer_db.usl_stats, stats.process_usl_stats)

    print "Loading usl awards.\n"
    generic_load(soccer_db.usl_awards, awards.process_usl_awards)


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



def load_ncaa():
    from soccerdata.text import awards

    print "Loading NCAA awards.\n"
    generic_load(soccer_db.ncaa_awards, awards.process_ncaa_awards)


def load_usa():
    from soccerdata.text import usa
 
    print "loading usa games"
    generic_load(soccer_db.usa_games, usa.process_usa_games)

    print "loading usa goals"
    generic_load(soccer_db.usa_goals, usa.process_usa_goals)

    print "loading usa lineups"
    generic_load(soccer_db.usa_lineups, usa.process_usa_lineups)


def load_world_cup():
    from soccerdata.scrapers import fifa
    generic_load(soccer_db.fifa_games, fifa.scrape_all_world_cup_games)
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
