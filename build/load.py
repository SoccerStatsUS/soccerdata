from soccerdata.mongo import generic_load, soccer_db

from soccerdata.scrapers import fbleague, rsssf, mls
from soccerdata.text import lineups

from soccerdata import scrapers
from soccerdata import text


def clear_all():
    from soccerdata.settings import STAT_TABLES, SOURCES
    for e in STAT_TABLES:
        soccer_db['%s' % e].drop()

    for s in SOURCES:
        for e in STAT_TABLES: 
            soccer_db['%s_%s' % (s, e)].drop()
    

def first_load():
    """
    Load all data.
    """

    # Base data.

    clear_all()
    
    # Experiments
    #load_midwest()
    #load_early

    load_standings()




    load_positions()
    load_drafts()


    load_generals()

    # What are USL games coming from?
    load_cups()

    load_asl()
    load_mls_data()
    load_mls_lineups()
    load_mls_reserve()
    load_nasl()

    load_usl()
    load_leach()
    load_apsl()
    load_partial()



    load_ncaa()

    return

    # Fix this first.
    load_nasl2()

    # reconsider this. Or at least clean up.
    load_teams()

    # soccernet / recent stats.
    load_mls2()

    # USMNT
    load_usa()

    # All World Cups.
    load_world_cup()

    # Ideally, Gold Cup, CONCACAF Champions League, Concacaf Cup
    # World Cup Qualifiers
    load_concacaf()


    load_analysis()

def second_load():
    # This is for data that should not be loaded
    # until after we have merged all data.
    # e.g. wikipedia team bios based on game results.
    
    # These provide no data to any other items.

    #load_yaml() # Could be loaded earlier, but not really thematically
    #load_wiki()
    pass



def load_generals():
    load_general('chris', 'small_tournaments/giantscup.txt')
    load_general('chris', 'small_tournaments/bicentennial')
    load_general('chris', 'small_tournaments/canadian.txt')
    load_general('chris', 'small_tournaments/carolina.txt')
    load_general('chris', 'small_tournaments/dynamo.txt')
    load_general('chris', 'small_tournaments/superliga.txt')
    load_general('chris', 'cups/us_cup')


def load_mls_reserve():
    load_general('mls_reserve', 'leagues/mls_reserve')


def load_early():
    load_general('american_cup', 'cups/american_cup')
    load_general('american_cup', 'leagues/nafbl.txt')
    load_general('american_cup', 'leagues/alpf.txt')
    load_general('american_cup', 'international/usmnt/usa_very_early')


def load_midwest():
    for e in range(1, 8):
        load_general('open_cup', 'cups/us_open/19%s0' % e)

    load_general('open_cup', 'leagues/isl')
    load_general('open_cup', 'teams/benmillers.txt')
    load_general('open_cup', 'teams/bricklayers.txt')
    load_general('open_cup', 'teams/harmarville.txt')
    load_general('open_cup', 'teams/benmillers.txt')
    load_general('open_cup', 'teams/morgan')
    load_general('open_cup', 'teams/scullin.txt')
    load_general('open_cup', 'teams/stix.txt')


def load_cups():
    load_general('american_cup', 'cups/american_cup')
    load_general('lewis_cup', 'cups/lewis')
    load_general('open_cup', 'cups/us_open/1910')
    load_general('open_cup', 'cups/us_open/1920')
    load_general('open_cup', 'cups/us_open/1930')
    load_general('open_cup', 'cups/us_open/1940')
    load_general('open_cup', 'cups/us_open/1950')
    load_general('open_cup', 'cups/us_open/1960')
    load_general('open_cup', 'cups/us_open/1970')
    load_general('open_cup', 'cups/us_open/1980')
    load_general('open_cup', 'cups/us_open/1990')



def load_standings():
    from soccerdata.text import standings
    print "Loading chris standings.\n"

    soccer_db.standings.drop()
    f = lambda s: generic_load(soccer_db.chris_standings, standings.process_standings_file(s), delete=False)

    for e in 'mls', 'nasl', 'asl', 'wsa', 'apsl', 'cosmo', 'usl/12', 'usl/select', 'usl/pro', 'usl/premier', 'nasl0', 'lssa':
        f(e)

    



def load_general(coll, fn):
    from soccerdata.text import general
    games, goals, misconduct, lineups = general.process_general_file(fn)
    generic_load(soccer_db['%s_games' % coll], lambda: games, delete=False)
    generic_load(soccer_db['%s_lineups' % coll], lambda: lineups, delete=False)
    generic_load(soccer_db['%s_goals' % coll], lambda: goals, delete=False)

    


def load_teams():
    from soccerdata.text import syaml
    print "Loading teams.\n"
    generic_load(soccer_db.chris_teams, syaml.load_teams)


def load_drafts():
    from soccerdata.text import drafts
    print "Loading drafts.\n"
    generic_load(soccer_db.chris_drafts, drafts.load_drafts)



def load_positions():
    from soccerdata.text.positions import process_positions
    print "Loading positions.\n"
    generic_load(soccer_db.chris_positions, process_positions)


def load_partial():
    from soccerdata.text import partial
    print "Loading partial stats.\n"
    generic_load(soccer_db.partial_stats, partial.process_partial_stats)


def load_analysis():
    from soccerdata.text import ratings
    print "Loading ratings.\n"
    generic_load(soccer_db.analysis_ratings, ratings.get_ratings)
    

    
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

    print "Loading ASL stats.\n"
    generic_load(soccer_db.asl_stats, asl.process_stats)


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
    # Need to work some integrity issues on games.
    generic_load(soccer_db.nasl_games, nasl.process_games)


    


def load_apsl():
    """
    Load stats and games from the APSL and WSA.
    """
    from soccerdata.text import apsl, awards
    print "loading apsl stats"
    generic_load(soccer_db.apsl_stats, apsl.process_apsl_stats)

    generic_load(soccer_db.apsl_awards, awards.process_wsa_awards)
    generic_load(soccer_db.apsl_awards, awards.process_apsl_awards, delete=False)
    generic_load(soccer_db.apsl_awards, awards.process_usl0_awards, delete=False)

    load_general('apsl', 'playoffs/apsl_playoffs')
    load_general('apsl', 'playoffs/wsa_playoffs')

    load_general('apsl', 'cups/apsl_professional_cup')
    
    print "loading apsl scores"
    #generic_load(soccer_db.apsl_games, apsl.process_apsl_scores)



def load_leach():
    from soccerdata.text import leach
    generic_load(soccer_db.leach_goals, leach.process_goals)
    generic_load(soccer_db.leach_games, leach.process_games)
    generic_load(soccer_db.leach_lineups, leach.process_lineups)


def load_mls_data():
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


def load_mls2():
    load_soccernet_league('usa.1', 'mls2')


def load_mls_lineups():
    # Load scaryice lineup data.

    # MLS lineup data 1996-2010
    print "Loading scaryice score data.\n"
    generic_load(soccer_db.mls_games, lineups.load_all_games_scaryice)

    print "Loading scaryice goal data.\n"
    generic_load(soccer_db.mls_goals, lineups.load_all_goals_scaryice)
    
    print "Loading scaryice lineup data.\n"
    generic_load(soccer_db.mls_lineups, lineups.load_all_lineups_scaryice)



def load_mls_reserve_old():
    # Probably delete this.
    """
    Load data from the MLS Reserve League (2011 - )
    """
    from soccerdata.text import reserve

    generic_load(soccer_db.mls_reserve_games, reserve.process_scores)
    generic_load(soccer_db.mls_reserve_lineups, reserve.process_lineups)
    generic_load(soccer_db.mls_reserve_goals, reserve.process_goals)



def load_nasl2():
    # Need to remove this scraper. Completely unnecessary for NASL.

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


def load_soccernet_league(code, name):
    from soccerdata.scrapers import soccernet
    generic_load(soccer_db['%s_goals' % name], lambda: soccernet.scrape_all_league_goals(code))
    generic_load(soccer_db['%s_games' % name], lambda: soccernet.scrape_all_league_games(code))
    generic_load(soccer_db['%s_lineups' % name], lambda: soccernet.scrape_all_league_lineups(code))


def load_concacaf():
    load_soccernet_league('concacaf.champions', 'concacaf')


def load_ncaa():
    from soccerdata.text import awards

    print "Loading NCAA awards.\n"
    generic_load(soccer_db.ncaa_awards, awards.process_ncaa_awards)


def load_usa():
    from soccerdata.text import usa2
    from soccerdata.text import drafts
 
    print "loading usa games"
    generic_load(soccer_db.usa_games, usa2.process_usa_games)

    print "loading usa goals"
    generic_load(soccer_db.usa_goals, usa2.process_usa_goals)

    print "loading usa lineups"
    generic_load(soccer_db.usa_lineups, usa2.process_usa_lineups)

    generic_load(soccer_db.usa_drafts, drafts.process_usa_drafts)


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
    first_load()
