from soccerdata.mongo import generic_load, soccer_db

from soccerdata.scrapers import fbleague, rsssf, mls
from soccerdata.text import asl
from soccerdata.text import lineups
from soccerdata.text import standings

from soccerdata import scrapers
from soccerdata import text


def clear_all():
    from soccerdata.settings import STAT_TABLES, SOURCES, SINGLE_SOURCES
    for e in STAT_TABLES:
        soccer_db['%s' % e].drop()

    for s in SOURCES:
        for e in STAT_TABLES: 
            soccer_db['%s_%s' % (s, e)].drop()

    for e in SINGLE_SOURCES:
        soccer_db[e].drop()


def load_games_standard(coll, fn):
    from soccerdata.text import games
    games, goals, fouls, lineups = games.process_games_file(fn)
    generic_load(soccer_db['%s_games' % coll], lambda: games, delete=False)
    generic_load(soccer_db['%s_lineups' % coll], lambda: lineups, delete=False)
    generic_load(soccer_db['%s_fouls' % coll], lambda: fouls, delete=False)
    generic_load(soccer_db['%s_goals' % coll], lambda: goals, delete=False)



def first_load():
    """
    Load all data.
    """
    clear_all()

    load_bios()
    load_places()
    load_competitions()
    load_teams()

    load_positions()
    load_drafts()
    #load_news()
    load_nasl2()

    load_friendlies()

    load_concacaf()



    load_usa()

    load_cups()
    load_name_maps()
    load_stadium_maps()

    load_isl()

    load_apsl()

    load_asl2()

    load_usl()


    #load_ncaa()

    load_small_tournaments()

    load_nasl()

    load_nafbl()

    load_city()


    load_asl()
    load_mls()    



    return

    # Fix this first.
#load_leach()    


    # soccernet / recent stats.


    # USMNT


    # All World Cups.
    load_world_cup()



    load_analysis()


def generate_cities():
    print "Generating cities."

    state_code_dict = make_state_code_dict()

    state_name_set = set([e['name'] for e in soccer_db.states.find()])
    country_name_set = set([e['name'] for e in soccer_db.countries.find()])

    def make_city(s):

        country = state = None

        if ',' in s:
            pieces = s.split(',')
            end = pieces[-1].strip()
            

            if end in state_code_dict:
                state = state_code_dict[end]

            elif end in state_name_set:
                state = end

            elif end in country_name_set:
                country = end

        if country or state:
            name = ','.join(pieces[:-1])
        else:
            name = s

        return {
            'name': name,
            'country': country,
            'state': state,
            }
            

    
    cities = set()

    for e in soccer_db.bios.find():
        cities.add(e.get('birthplace'))
        cities.add(e.get('deathplace'))


    for e in soccer_db.games.find():
        cities.add(e['location'])

    cities.remove(None)
    city_dicts = [make_city(e) for e in sorted(cities)]




            
def load_name_maps():
    from text import namemap
    generic_load(soccer_db.name_maps, namemap.load)


def load_stadium_maps():
    from text import stadiummap
    generic_load(soccer_db.stadium_maps, stadiummap.load)


def load_news():
    from text import news
    generic_load(soccer_db.news, news.load)



def load_bios():
    print "Loading ASL Bios"
    print soccer_db.bios.count()
    generic_load(soccer_db.bios, asl.process_bios)

    print "Loading MLSsoccer.com player bios.\n"
    generic_load(soccer_db.bios, mls.scrape_all_bios_mlssoccer)
    print soccer_db.bios.count()



def second_load():
    # This is for data that should not be loaded
    # until after we have merged all data.
    # e.g. wikipedia team bios based on game results.
    
    # These provide no data to any other items.

    #load_yaml() # Could be loaded earlier, but not really thematically
    #load_wiki()
    pass






def load_places():
    from text import places
    generic_load(soccer_db.countries, places.load_countries)
    generic_load(soccer_db.states, places.load_states)
    generic_load(soccer_db.state_populations, places.load_state_populations)
    generic_load(soccer_db.stadiums, places.load_stadiums)





def load_isl():
    # Load both isl leagues - 1926 and 1960-1965
    load_games_standard('isl', 'domestic/country/usa/leagues/isl')
    load_games_standard('isl', 'domestic/country/usa/leagues/isl2')
    load_standings('isl', 'domestic/country/usa/isl')



def load_usa():
    from soccerdata.text import halloffame

    #load_general('usa', 'international/usmnt/gold_cup')
    #load_general('usa', 'international/usmnt/world_cup')
    for e in [1880, 1910, 1980, 2000, 2010]:
        load_games_standard('usa', 'international/country/usa/%s' % e)

    load_games_standard('usa', 'international/country/usa/gold')
    load_games_standard('usa', 'international/country/usa/world_cup')

    generic_load(soccer_db.usa_awards, halloffame.load_hall_of_fame)



def load_cups():
    load_games_standard('american_cup', 'domestic/country/usa/cups/american')
    load_games_standard('american_cup', 'domestic/country/usa/cups/american2')
    load_games_standard('lewis_cup', 'domestic/country/usa/cups/lewis')

    for e in range(191, 202):
        load_games_standard('open_cup', 'domestic/country/usa/cups/open/%s0' % e)




def load_small_tournaments():

    load_games_standard('small', 'domestic/country/canada/cups//championship')
    load_games_standard('small', 'domestic/country/canada/cups//early')
    load_games_standard('small', 'domestic/country/usa/tournaments/carolina')
    load_games_standard('small', 'domestic/country/usa/tournaments/dynamo')
    load_games_standard('small', 'international/misc/us_cup')
    load_games_standard('small', 'international/misc/bicentennial')



def load_mls():
    load_games_standard('mls_reserve', 'domestic/country/usa/leagues/mls_reserve')

    load_mls_data()
    load_mls_lineups()


    load_soccernet_league('mls_soccernet', 'usa.1')

def load_nafbl():

    # Also loading ALoPF and SNESL

    load_games_standard('nafbl', 'domestic/country/usa/leagues/alpf')

    load_games_standard('nafbl', 'domestic/country/usa/leagues/nafbl1')
    load_games_standard('nafbl', 'domestic/country/usa/leagues/nafbl2')

    load_standings('nafbl', 'domestic/country/usa/early')


def load_city():

    load_standings('city', 'domestic/city/slsl')
    load_standings('city', 'domestic/city/cosmo')



def load_friendlies():

    for e in [70, 75, 78, 80, 82]:
        load_games_standard('tours', 'domestic/country/usa/friendly/19%s' % e)

    for e in range(190, 201):
        load_games_standard('tours', 'domestic/country/usa/friendly/tours/%s0' % e)






# Custom 


def load_modern():
    load_mls()
    load_apsl()
    load_usl()
    load_leach()    
    load_nasl2()
    load_concacaf()


def load_early():

    load_general('american_cup', 'cups/american_cup')

    load_general('american_cup', 'international/usmnt/usa_very_early')


def load_midwest():
    for e in range(191, 202):
        load_general('open_cup', 'cups/open/%s0' % e)

    load_general('midwest', 'leagues/isl')
    load_general('midwest', 'teams/benmillers.txt')
    load_general('midwest', 'teams/bricklayers.txt')
    load_general('midwest', 'teams/harmarville.txt')
    load_general('midwest', 'teams/benmillers.txt')
    load_general('midwest', 'teams/morgan')
    load_general('midwest', 'teams/scullin.txt')
    load_general('midwest', 'teams/stix.txt')


    






    

def load_competitions():
    from soccerdata.text import competitions
    print "Loading competitions.\n"
    generic_load(soccer_db.competitions, competitions.load)


def load_teams():
    from soccerdata.text import teams
    print "Loading teams.\n"
    generic_load(soccer_db.teams, teams.load)


def load_drafts():
    from soccerdata.text import drafts
    print "Loading drafts.\n"
    generic_load(soccer_db.drafts, drafts.load_drafts)
    generic_load(soccer_db.picks, drafts.load_picks)



def load_positions():
    from soccerdata.text.positions import process_positions
    print "Loading positions.\n"
    generic_load(soccer_db.positions, process_positions)


def load_asl2():
    from soccerdata.text import partial
    print "Loading partial stats.\n"
    generic_load(soccer_db.asl2_stats, partial.process_partial_stats)
    load_standings('asl2', 'domestic/country/usa/asl2')


def load_analysis():
    from soccerdata.text import ratings
    print "Loading ratings.\n"
    generic_load(soccer_db.analysis_ratings, ratings.get_ratings)
    

    
def load_asl():
    from soccerdata.text import awards

    load_standings('asl', 'domestic/country/usa/asl')

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

    load_standings('nasl', 'domestic/country/usa/nasl')


    


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

    load_games_standard('apsl', 'domestic/country/usa/playoffs/apsl')
    load_games_standard('apsl', 'domestic/country/usa/playoffs/wsa')
    load_games_standard('apsl', 'domestic/country/usa/cups/apsl_professional')

    load_standings('apsl', 'domestic/country/usa/apsl')
    load_standings('apsl', 'domestic/country/usa/wsa')
    load_standings('apsl', 'domestic/country/usa/lssa')
    
    print "loading apsl scores"
    #generic_load(soccer_db.apsl_games, apsl.process_apsl_scores)


def load_standings(coll, fn):

    generic_load(soccer_db['%s_standings' % coll], lambda: standings.process_standings(fn))


def load_leach():
    from soccerdata.text import leach
    generic_load(soccer_db.usl_leach_goals, leach.process_goals)
    generic_load(soccer_db.usl_leach_games, leach.process_games)
    generic_load(soccer_db.usl_leach_lineups, leach.process_lineups)


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

    load_standings('mls', 'domestic/country/usa/mls')

    print "Loading MLS awards.\n"
    generic_load(soccer_db.mls_awards, awards.process_mls_awards)
    generic_load(soccer_db.mls_awards, awards.process_mls_cup_awards)

    print "Loading mls bio stats.\n"
    generic_load(soccer_db.mls_stats, mls.scrape_all_bio_stats_mlssoccer)

    print "Loading coach playing stats.\n"
    # Load coach stats that are missing from mlossoccer.com
    generic_load(soccer_db.mls_stats, stats.process_mls_coach_stats, delete=False)





def load_mls_lineups():
    # Load scaryice lineup data.

    # MLS lineup data 1996-2010
    print "Loading scaryice score data.\n"
    generic_load(soccer_db.mls_games, lineups.load_all_games_scaryice)

    print "Loading MLS playoff data.\n"
    load_games_standard('mls', 'domestic/country/usa/playoffs/mls')

    print "Loading scaryice goal data.\n"
    generic_load(soccer_db.mls_goals, lineups.load_all_goals_scaryice)
    
    print "Loading scaryice lineup data.\n"
    generic_load(soccer_db.mls_lineups, lineups.load_all_lineups_scaryice)





def load_nasl2():

    print "Loading 2010 USSF D2 stats."
    from soccerdata.text import nasl
    load_games_standard('ussf2', 'domestic/country/usa/leagues/ussfd2')
    load_standings('ussf2', 'domestic/country/usa/ussf2')

    print "Loading 2011 NASL stats."
    from soccerdata.text import nasl
    generic_load(soccer_db.nasl2_stats, nasl.process_stats)

    print "Loading 2011 NASL games."
    load_games_standard('nasl2', 'domestic/country/usa/leagues/nasl2011')

    load_standings('nasl2', 'domestic/country/usa/nasl2')



def load_usl():

    """
    Load usl stats and nasl stats.
    """
    from soccerdata.text import stats, awards  

    print "Loading usl stats.\n"
    generic_load(soccer_db.usl_stats, stats.process_usl_stats)

    print "Loading usl awards.\n"
    generic_load(soccer_db.usl_awards, awards.process_usl_awards)

    load_standings('usl', 'domestic/country/usa/usl/pro')
    load_standings('usl', 'domestic/country/usa/usl/12')
    load_standings('usl', 'domestic/country/usa/usl/pdl')
    load_standings('usl', 'domestic/country/usa/usl/premier')
    load_standings('usl', 'domestic/country/usa/usl/usl_pro')
    load_standings('usl', 'domestic/country/usa/usl/usl0')
    load_standings('usl', 'domestic/country/usa/usl/usisl')
    load_standings('usl', 'domestic/country/usa/usl/select')


def load_soccernet_league(name, code):
    from soccerdata.scrapers import soccernet
    generic_load(soccer_db['%s_goals' % name], lambda: soccernet.scrape_all_league_goals(code))
    generic_load(soccer_db['%s_games' % name], lambda: soccernet.scrape_all_league_games(code))
    generic_load(soccer_db['%s_lineups' % name], lambda: soccernet.scrape_all_league_lineups(code))

    load_standings('nasl2', 'domestic/country/usa/nasl2')


def load_concacaf():

    load_games_standard('concacaf', 'domestic/confederation/concacaf/superliga')
    load_games_standard('concacaf', 'domestic/confederation/concacaf/giantscup')

    for e in '6789':
        load_games_standard('concacaf', 'domestic/confederation/concacaf/champions_cup/19%s0' % e)

    load_games_standard('concacaf', 'domestic/confederation/concacaf/champions_cup/2000')
        
    load_soccernet_league('concacaf', 'concacaf.champions')


def load_ncaa():
    from soccerdata.text import awards

    print "Loading NCAA awards.\n"
    generic_load(soccer_db.ncaa_awards, awards.process_ncaa_awards)


def load_world_cup():
    from soccerdata.scrapers import fifa
    generic_load(soccer_db.fifa_games, fifa.scrape_all_world_cup_games)
    generic_load(soccer_db.fifa_goals, fifa.scrape_all_world_cup_goals)
    generic_load(soccer_db.fifa_lineups, fifa.scrape_all_world_cup_lineups)


def load_kicker():
    from soccerdata.scrapers import kicker
    generic_load(soccer_db.kicker_games, kicker.scrape_all_kicker_seasons)


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
