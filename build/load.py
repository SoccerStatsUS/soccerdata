from soccerdata.mongo import generic_load, soccer_db

from soccerdata.scrapers import fbleague, mls

from soccerdata.text import asl
from soccerdata.text import awards
from soccerdata.text import bios
from soccerdata.text import drafts
from soccerdata.text import lineups
from soccerdata.text import partial
from soccerdata.text import rosters
from soccerdata.text import salaries
from soccerdata.text import standings
from soccerdata.text import stats

from soccerdata import scrapers

from soccerdata.data.alias.people import check_for_name_loops


def clear_all():
    from soccerdata.settings import STAT_TABLES, SOURCES, SINGLE_SOURCES
    for e in STAT_TABLES:
        soccer_db['%s' % e].drop()

    for s in SOURCES:
        for e in STAT_TABLES: 
            soccer_db['%s_%s' % (s, e)].drop()

    for e in SINGLE_SOURCES:
        soccer_db[e].drop()


def load_games_standard(coll, fn, games_only=False):
    from soccerdata.text import games
    games, goals, fouls, lineups, rosters = games.process_games_file(fn)



    generic_load(soccer_db['%s_games' % coll], lambda: games, delete=False)

    if games_only:
        return

    generic_load(soccer_db['%s_lineups' % coll], lambda: lineups, delete=False)
    generic_load(soccer_db['%s_fouls' % coll], lambda: fouls, delete=False)
    generic_load(soccer_db['%s_goals' % coll], lambda: goals, delete=False)
    generic_load(soccer_db['%s_rosters' % coll], lambda: rosters, delete=False)




def first_load():
    """
    Load all data.
    """
    check_for_name_loops()
    clear_all()

    load_sources()
    load_bios()
    load_places()
    load_competitions()
    load_teams()

    load_salaries()
    load_positions()
    #load_news()

    load_name_maps()
    load_stadium_maps()
    load_competition_maps()

    load_drafts()
    load_games()

    #load_analysis()

def load_drafts():
    generic_load(soccer_db.drafts, drafts.load_drafts)
    generic_load(soccer_db.picks, drafts.load_picks)


def load_games():
    load_australia()    

    load_early_cups()
    load_modern_cups()


    load_fifa()

    load_asl()



    load_mls()

    load_nasl()

    load_usl()
    load_apsl()

    load_olympics()


    load_isl()
    load_canada()

    load_esl()    
    load_early_friendlies()
    load_copa_america()
    load_usmnt()

    #load_mexico()
    #load_guatemala()
    load_ncaa()
    load_nafbl()
    load_modern_friendlies()
    load_pdl()
    load_leach()    
    load_misl()
    load_city()
    load_ny()
    load_asl2()
    load_concacaf()
    load_melvin()


def load_excel_standings(coll, fn):
    """
    Load standard excel-formatted standings.
    """

    generic_load(soccer_db['%s_standings' % coll], lambda: standings.process_excel_standings(fn))


def load_new_standings(coll, fn):
    """
    Load semicolon-style standings
    """
    generic_load(soccer_db['%s_standings' % coll], lambda: standings.process_file(fn))


def generate_cities():
    """
    Generate city objects from 
    """


    print "Generating cities."

    state_code_dict = make_state_code_dict()

    state_name_set = set([e['name'] for e in soccer_db.states.find()])
    country_name_set = set([e['name'] for e in soccer_db.countries.find()])

    def make_city(s):
        """
        Format a city based on known state and country names.
        """
        # This doesn't seem to be the right place for this function.

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


def load_competition_maps():
    from text import competitionnamemap
    generic_load(soccer_db.competition_maps, competitionnamemap.load)    


def load_stadium_maps():
    from text import stadiummap
    generic_load(soccer_db.stadium_maps, stadiummap.load)


def load_sources():
    from text import sources
    generic_load(soccer_db.sources, sources.load)


def load_news():
    from text import news
    generic_load(soccer_db.news, news.load)



def load_bios():
    print "Loading ASL Bios"
    print soccer_db.bios.count()
    generic_load(soccer_db.asl_bios, bios.process_asl_bios)

    print "Loading MLSsoccer.com player bios.\n"
    generic_load(soccer_db.mls_bios, mls.scrape_all_bios_mlssoccer)
    print soccer_db.bios.count()

    print "Loading chris's compiled bios."
    generic_load(soccer_db.usl_bios, bios.load_all_bios)

    generic_load(soccer_db.misl_bios, bios.process_misl_bios)
    generic_load(soccer_db.nasl_bios, bios.process_nasl_bios)



    generic_load(soccer_db.usa_bios, bios.process_usa_bios)

    generic_load(soccer_db.mls_bios, bios.process_mls_bios)
    generic_load(soccer_db.mls_reserve_bios, bios.process_mls_reserve_bios)

    generic_load(soccer_db.asl_bios, bios.process_asl_bios2)


    generic_load(soccer_db.asl2_bios, bios.process_asl2_bios)

    generic_load(soccer_db.ussf2_bios, bios.process_ussf2_bios)
    generic_load(soccer_db.nasl2_bios, bios.process_nasl2_bios)


    generic_load(soccer_db.apsl_bios, bios.process_apsl_bios)


    generic_load(soccer_db.usl_bios, bios.process_usl2_bios)
    generic_load(soccer_db.usl_bios, bios.process_usl1_bios)




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



def load_olympics():

    #generic_load(soccer_db.olympics_rosters, lambda: rosters.process_rosters('international/olympics'))

    olympics = [1900, 1904, 1908, 1912, 1920, 1924, 1928, 1936, 
                1948, 1952, 1956, 1960, 1964, 1968, 1972,
                2008, 2012]
    olympics = [2008, 2012]

    generic_load(soccer_db.olympics_awards, awards.process_olympics_awards)

    for e in olympics:
        load_games_standard('olympics', 'international/world/olympics/%s' % e)


def load_isl():
    # Load both isl leagues - 1926 and 1960-1965
    load_games_standard('isl', 'domestic/country/usa/leagues/isl')
    load_games_standard('isl', 'domestic/country/usa/leagues/isl2')
    load_excel_standings('isl', 'domestic/country/usa/isl')
    generic_load(soccer_db.isl_awards, awards.process_isl_awards)




def load_usmnt():
    from soccerdata.text import halloffame

    #load_general('usa', 'international/usmnt/gold_cup')
    #load_general('usa', 'international/usmnt/world_cup')
    for e in [1880, 1910, 1980, 1990, 2000, 2010]:
        load_games_standard('usa', 'international/country/usa/%s' % e)

    load_games_standard('usa', 'international/country/usa/gold')
    #load_games_standard('usa', 'international/country/usa/world_cup')

    load_games_standard('usa', 'international/misc/us_cup')

    generic_load(soccer_db.usa_awards, halloffame.load_hall_of_fame)



def load_early_cups():


    generic_load(soccer_db.asl_awards, awards.process_american_cup_awards)
    generic_load(soccer_db.asl_awards, awards.process_us_open_cup_awards, delete=False)
    generic_load(soccer_db.asl_awards, awards.process_lewis_cup_awards, delete=False)

    load_games_standard('american_cup', 'domestic/country/usa/cups/american')
    load_games_standard('american_cup', 'domestic/country/usa/cups/american2')
    load_games_standard('lewis_cup', 'domestic/country/usa/cups/lewis')

    for e in range(191, 197):
        load_games_standard('open_cup', 'domestic/country/usa/cups/open/%s0' % e)#, games_only=True)


def load_modern_cups():

    for e in range(197, 202):
        load_games_standard('open_cup', 'domestic/country/usa/cups/open/%s0' % e)#, games_only=True)

def load_canada():
    load_excel_standings('apsl', 'domestic/country/canada/csl')
    load_games_standard('canada', 'domestic/country/canada/cups/championship')
    #load_games_standard('canada', 'domestic/country/canada/cups/early')
    load_games_standard('canada', 'domestic/country/canada/friendly')
    load_games_standard('canada', 'international/country/canada')

    generic_load(soccer_db.canada_stats, partial.process_csl_partial)

    generic_load(soccer_db.canada_awards, awards.process_csl_awards)
    generic_load(soccer_db.canada_awards, awards.process_canada_awards)


def load_guatemala():
    generic_load(soccer_db.guatemala_standings, lambda: standings.process_standings_file('domestic/country/guatemala', ';'))
    load_games_standard('guatemala', 'domestic/country/guatemala')




def load_mls():


    load_excel_standings('mls', 'domestic/country/usa/mls')

    print "Loading MLS awards.\n"
    generic_load(soccer_db.mls_awards, awards.process_mls_awards)
    generic_load(soccer_db.mls_awards, awards.process_mls_reserve_awards)
    generic_load(soccer_db.mls_awards, awards.process_mls_cup_awards)

    print "Loading mls bio stats.\n"
    generic_load(soccer_db.mls_stats, stats.process_mls_2012_stats)

    print "Loading MLS playoff data.\n"
    load_games_standard('mls_playoffs', 'domestic/country/usa/playoffs/mls')
    load_games_standard('mls_reserve', 'domestic/country/usa/leagues/mls/reserve')

    load_games_standard('mls', 'domestic/country/usa/leagues/mls/2011')
    load_games_standard('mls', 'domestic/country/usa/leagues/mls/2012')
    load_games_standard('mls', 'domestic/country/usa/leagues/mls/mls_attendance.csv')

    load_mls_lineups()

    #generic_load(soccer_db.mls_stats, mls.scrape_all_bio_stats_mlssoccer)
    #load_soccernet_league('mls_soccernet', 'usa.1')
    #print "Loading coach playing stats.\n"
    # Load coach stats that are missing from mlossoccer.com
    #generic_load(soccer_db.mls_stats, stats.process_mls_coach_stats, delete=False)



def load_nafbl():

    # Also loading ALoPF and SNESL


    generic_load(soccer_db.asl_awards, awards.process_nafbl_awards, delete=False)
    generic_load(soccer_db.asl_awards, awards.process_snesl_awards, delete=False)

    load_games_standard('nafbl', 'domestic/country/usa/leagues/alpf')
    load_games_standard('nafbl', 'domestic/country/usa/leagues/nafbl1')

    load_games_standard('nafbl', 'domestic/country/usa/leagues/snesl')
    load_games_standard('nafbl', 'domestic/country/usa/leagues/nafbl2')

    load_excel_standings('nafbl', 'domestic/country/usa/early')


def load_melvin():
    load_games_standard('melvin', 'domestic/country/usa/friendly/1865')
    load_games_standard('melvin', 'domestic/country/usa/friendly/1870')
    load_games_standard('melvin', 'domestic/country/usa/friendly/1875')
    load_games_standard('melvin', 'domestic/country/usa/friendly/1880')
    load_games_standard('melvin', 'domestic/country/usa/friendly/1885')
    load_games_standard('melvin', 'domestic/country/usa/friendly/1890')


def load_city():

    #oad_games_standard('city', 'city')

    load_excel_standings('city', 'domestic/city/slsl')
    load_excel_standings('city', 'domestic/city/cosmo')


def load_ny():
    load_games_standard('state', 'domestic/country/usa/leagues/metropolitan')
    load_games_standard('state', 'domestic/country/usa/friendly/1900_ny')
    generic_load(soccer_db.state_awards, awards.process_ny_awards, delete=False)

def load_early_friendlies():
    for e in range(190, 197):
        load_games_standard('tours', 'domestic/country/usa/friendly/%s0' % e)


def load_modern_friendlies():

    load_games_standard('tours', 'domestic/country/usa/friendly/carolina')
    load_games_standard('tours', 'domestic/country/usa/friendly/dynamo')

    load_games_standard('tours', 'international/misc/bicentennial')

    load_games_standard('tours', 'domestic/country/usa/friendly/mls_all_star')

    load_games_standard('tours', 'domestic/country/usa/friendly/tours/1970')
    load_games_standard('tours', 'domestic/country/usa/friendly/tours/1980')



    load_games_standard('tours', 'domestic/country/usa/friendly/1960')
    load_games_standard('tours', 'domestic/country/usa/friendly/1967')
    load_games_standard('tours', 'domestic/country/usa/friendly/1970')
    load_games_standard('tours', 'domestic/country/usa/friendly/1975')
    load_games_standard('tours', 'domestic/country/usa/friendly/1978')
    load_games_standard('tours', 'domestic/country/usa/friendly/1980')
    load_games_standard('tours', 'domestic/country/usa/friendly/1982')
    load_games_standard('tours', 'domestic/country/usa/friendly/1990')
    load_games_standard('tours', 'domestic/country/usa/friendly/2000')
    load_games_standard('tours', 'domestic/country/usa/friendly/2010')






# Custom 


def load_modern():
    load_mls()
    load_apsl()
    load_usl()
    load_leach()    
    load_concacaf()


def load_early():
    load_games_standard('usa', 'international/country/usa/1880')
    load_games_standard('american_cup', 'domestic/country/usa/cups/american')
    load_melvin()


def load_midwest():
    for e in range(191, 202):
        load_games_standard('open_cup', 'cups/open/%s0' % e)

    load_games_standard('midwest', 'leagues/isl')
    load_games_standard('midwest', 'teams/benmillers.txt')
    load_games_standard('midwest', 'teams/bricklayers.txt')
    load_games_standard('midwest', 'teams/harmarville.txt')
    load_games_standard('midwest', 'teams/benmillers.txt')
    load_games_standard('midwest', 'teams/morgan')
    load_games_standard('midwest', 'teams/scullin.txt')
    load_games_standard('midwest', 'teams/stix.txt')


    

def load_competitions():
    from soccerdata.text import competitions
    print "Loading competitions.\n"
    generic_load(soccer_db.competitions, competitions.load_competitions)


def load_teams():
    from soccerdata.text import teams
    print "Loading teams.\n"
    generic_load(soccer_db.teams, teams.load)


def load_salaries():
    soccer_db.salaries.drop()

    generic_load(soccer_db.salaries, salaries.load_salaries)

def load_positions():
    from soccerdata.text.positions import process_positions
    print "Loading positions.\n\n"
    generic_load(soccer_db.positions, process_positions)






def load_analysis():
    from soccerdata.text import ratings
    print "Loading ratings.\n"
    generic_load(soccer_db.analysis_ratings, ratings.get_ratings)
    

def load_copa_america():
    from soccerdata.text import copaamerica
    coll = 'copa_america'
    games, goals, fouls, lineups = copaamerica.process_copa_files()

    generic_load(soccer_db['%s_games' % coll], lambda: games, delete=False)
    generic_load(soccer_db['%s_lineups' % coll], lambda: lineups, delete=False)
    generic_load(soccer_db['%s_fouls' % coll], lambda: fouls, delete=False)
    generic_load(soccer_db['%s_goals' % coll], lambda: goals, delete=False)

    generic_load(soccer_db.copa_america_rosters, lambda: rosters.process_rosters('international/copa_america'))

    generic_load(soccer_db.copa_america_awards, awards.process_conmebol_awards)


    
def load_asl():

    load_excel_standings('asl', 'domestic/country/usa/asl')

    print "Loading ASL awards.\n"
    generic_load(soccer_db.asl_awards, awards.process_asl_awards, delete=False)


    print "Loading ASL games.\n"
    generic_load(soccer_db.asl_games, asl.process_games)

    print "Loading ASL stats.\n"
    generic_load(soccer_db.asl_stats, asl.process_stats)

    load_games_standard('asl', 'domestic/country/usa/leagues/asl')


def load_esl():    
    load_games_standard('esl', 'domestic/country/usa/leagues/esl')
    generic_load(soccer_db.esl_awards, awards.process_esl_awards, delete=False)



def load_asl2():

    print "Loading asl2 partial stats.\n"
    generic_load(soccer_db.asl2_stats, partial.process_asl2_partial)
    load_excel_standings('asl2', 'domestic/country/usa/asl2')

    generic_load(soccer_db.asl2_awards, awards.process_asl2_awards, delete=False)


    load_games_standard('esl', 'domestic/country/usa/leagues/asl2')





def load_nasl():
    """
    Load stats from the old nasl and misl.
    """
    from soccerdata.text import nasl

    print "Loading USA and NPSL data"
    load_excel_standings('nasl', 'domestic/country/usa/nasl0')
    generic_load(soccer_db.nasl_games, nasl.process_npsl_games)
    load_games_standard('nasl', 'domestic/country/usa/leagues/usa')
    generic_load(soccer_db.nasl_awards, awards.process_usa_awards)
    generic_load(soccer_db.nasl_awards, awards.process_npsl_awards)

    print "Loading NASL stats.\n"
    generic_load(soccer_db.nasl_stats, stats.process_nasl_stats)

    print "Loading NASL awards.\n"
    generic_load(soccer_db.nasl_awards, awards.process_nasl_awards)

    print "Loading NASL games.\n"
    # Need to work some integrity issues on games.
    generic_load(soccer_db.nasl_games, nasl.process_nasl_games)

    load_excel_standings('nasl', 'domestic/country/usa/nasl')


    


def load_apsl():
    """
    Load stats and games from the APSL and WSA.
    """
    from soccerdata.text import apsl, awards
    print "loading apsl stats"
    generic_load(soccer_db.apsl_stats, apsl.process_apsl_stats)

    print "loading apsl partial stats"
    generic_load(soccer_db.asl2_stats, partial.process_apsl_partial)

    generic_load(soccer_db.apsl_awards, awards.process_wsa_awards)
    generic_load(soccer_db.apsl_awards, awards.process_apsl_awards)
    generic_load(soccer_db.apsl_awards, awards.process_apslpc_awards)
    generic_load(soccer_db.apsl_awards, awards.process_usl0_awards)


    load_excel_standings('apsl', 'domestic/country/usa/apsl')
    load_excel_standings('apsl', 'domestic/country/usa/wsa')
    load_excel_standings('apsl', 'domestic/country/usa/lssa')
    
    print "loading apsl scores"
    generic_load(soccer_db.apsl_games, apsl.process_apsl_scores)
    load_games_standard('apsl', 'domestic/country/usa/leagues/wsa3')

    load_games_standard('apsl', 'domestic/country/usa/playoffs/apsl')
    load_games_standard('apsl', 'domestic/country/usa/playoffs/wsa')
    load_games_standard('apsl', 'domestic/country/usa/cups/apsl_professional')




def load_misl():
    """
    Load stats and games from the APSL and WSA.
    """

    load_excel_standings('misl', 'indoor/all')
    load_excel_standings('misl', 'indoor/misl')
    print "Loading NASL stats.\n"
    generic_load(soccer_db.misl_stats, stats.process_misl_stats)


def load_leach():
    from soccerdata.text import leach
    generic_load(soccer_db.usl_leach_goals, leach.process_goals)
    generic_load(soccer_db.usl_leach_games, leach.process_games)
    generic_load(soccer_db.usl_leach_lineups, leach.process_lineups)

def load_mls_lineups():
    # Load scaryice lineup data.

    # MLS lineup data 1996-2010
    print "Loading scaryice score data.\n"
    generic_load(soccer_db.mls_games, lineups.load_all_games_scaryice)


    print "Loading scaryice goal data.\n"
    generic_load(soccer_db.mls_goals, lineups.load_all_goals_scaryice)
    
    print "Loading scaryice lineup data.\n"
    generic_load(soccer_db.mls_lineups, lineups.load_all_lineups_scaryice)



def load_pdl():
    from soccerdata.text import pdl
    load_excel_standings('pdl', 'domestic/country/usa/usl/pdl')

    generic_load(soccer_db.pdl_stats, stats.process_pdl_stats)
    generic_load(soccer_db.pdl_games, pdl.load_pdl_games)

    generic_load(soccer_db.pdl_awards, awards.process_pdl_awards)

def load_usl():

    """
    Load usl stats and nasl stats.
    """
    load_games_standard('usl', 'domestic/country/usa/playoffs/usl1')
    load_games_standard('usl', 'domestic/country/usa/playoffs/usl2')

    load_games_standard('usl', 'domestic/country/usa/leagues/usl1/usl1')


    load_games_standard('usl', 'domestic/country/usa/leagues/usl2/2012')
    load_games_standard('usl', 'domestic/country/usa/leagues/usl2/2011')
    load_games_standard('usl', 'domestic/country/usa/leagues/usl2/2010')
    load_games_standard('usl', 'domestic/country/usa/leagues/usl2/2009')
    load_games_standard('usl', 'domestic/country/usa/leagues/usl2/2008')
    load_games_standard('usl', 'domestic/country/usa/leagues/usl2/2007')
    load_games_standard('usl', 'domestic/country/usa/leagues/usl2/2006')
    load_games_standard('usl', 'domestic/country/usa/leagues/usl2/2005')
    load_games_standard('usl', 'domestic/country/usa/leagues/usl2/2004')
    load_games_standard('usl', 'domestic/country/usa/leagues/usl2/2003')


    print "Loading usl stats.\n"
    generic_load(soccer_db.usl_stats, stats.process_usl_stats)

    print "Loading usl awards.\n"
    generic_load(soccer_db.usl_awards, awards.process_usl_awards)

    load_excel_standings('usl', 'domestic/country/usa/usl/pro')
    load_excel_standings('usl', 'domestic/country/usa/usl/12')

    load_excel_standings('usl', 'domestic/country/usa/usl/premier')
    load_excel_standings('usl', 'domestic/country/usa/usl/usl_pro')
    load_excel_standings('usl', 'domestic/country/usa/usl/usl0')
    load_excel_standings('usl', 'domestic/country/usa/usl/usisl')
    load_excel_standings('usl', 'domestic/country/usa/usl/select')

    print "Loading 2010 USSF D2 stats."
    load_games_standard('ussf2', 'domestic/country/usa/leagues/usl1/ussfd2')
    load_excel_standings('ussf2', 'domestic/country/usa/ussf2')

    generic_load(soccer_db.ussf2_awards, awards.process_ussf2_awards)

    print "Loading NASL2 stats."
    from soccerdata.text import nasl

    generic_load(soccer_db.nasl2_stats, nasl.process_stats)

    load_games_standard('nasl2', 'domestic/country/usa/leagues/usl1/nasl2011')
    load_games_standard('nasl2', 'domestic/country/usa/playoffs/nasl2')

    generic_load(soccer_db.ussf2_awards, awards.process_nasl2_awards)
    generic_load(soccer_db.ussf2_awards, awards.process_nasl2p_awards)

    load_excel_standings('nasl2', 'domestic/country/usa/nasl2')





def load_soccernet_league(name, code):
    from soccerdata.scrapers import soccernet
    
    games, goals, lineups = soccernet.scrape_league(code)

    generic_load(soccer_db['%s_games' % name], lambda: games)
    generic_load(soccer_db['%s_goals' % name], lambda: goals)
    generic_load(soccer_db['%s_lineups' % name], lambda: lineups)
    


def load_australia():
    load_games_standard('australia', 'domestic/country/australia')
    generic_load(soccer_db.australia_awards, awards.process_australia_awards)

def load_mexico():
    load_games_standard('mexico', 'international/country/mexico/alltime')
    return
    load_games_standard('mexico', 'international/country/trinidad_tobago')
    load_games_standard('mexico', 'international/country/belize')
    load_games_standard('mexico', 'international/country/bermuda')
    load_games_standard('mexico', 'international/country/panama')
    load_games_standard('mexico', 'international/country/costa_rica')
    load_games_standard('mexico', 'international/country/nicaragua')


    return

    load_new_standings('mexico', 'domestic/country/mexico/1')

    #load_games_standard('mexico', 'domestic/country/mexico/super')
    #load_games_standard('mexico', 'domestic/country/mexico/playoffs')

    load_soccernet_league('mexico', 'mex.1')






def load_concacaf():

    for e in '6789':
        load_games_standard('concacaf', 'domestic/confederation/concacaf/champions_cup/19%s0' % e)

    load_games_standard('concacaf', 'domestic/confederation/concacaf/champions_cup/2000')

    load_games_standard('concacaf', 'domestic/confederation/concacaf/giantscup')
    load_games_standard('concacaf', 'domestic/confederation/concacaf/superliga')
    load_games_standard('concacaf', 'domestic/confederation/concacaf/champions_league')

    generic_load(soccer_db.concacaf_awards, awards.process_concacaf_awards)

    #load_soccernet_league('concacaf', 'concacaf.champions')


def load_ncaa():

    print "Loading NCAA awards.\n"
    load_games_standard('ncaa', 'domestic/country/usa/college')
    generic_load(soccer_db.ncaa_awards, awards.process_ncaa_awards)


def load_fifa():
    from soccerdata.scrapers import fifa
    load_fifa_competition('FIFA U-17 World Cup')

    load_fifa_competition('Olympic Games')

    load_games_standard('fifa', 'international/world/world_cup')

    load_fifa_competition('FIFA Club World Cup')
    load_fifa_competition('FIFA Confederations Cup')
    load_fifa_competition('FIFA U-20 World Cup')


    generic_load(soccer_db.fifa_games, fifa.scrape_all_world_cup_games)
    generic_load(soccer_db.fifa_goals, fifa.scrape_all_world_cup_goals)
    generic_load(soccer_db.fifa_lineups, fifa.scrape_all_world_cup_lineups)

    generic_load(soccer_db.fifa_awards, awards.process_world_cup_awards)



def load_fifa_competition(competition):
    from soccerdata.scrapers import fifa
    games, goals, lineups = fifa.scrape_everything(competition)
    generic_load(soccer_db.fifa_games, lambda: games)
    generic_load(soccer_db.fifa_goals, lambda: goals)
    generic_load(soccer_db.fifa_lineups, lambda: lineups)



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
