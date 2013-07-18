from soccerdata.mongo import generic_load, soccer_db

from soccerdata.data.alias.people import check_for_name_loops
from soccerdata.data.alias.teams import check_for_team_loops
from soccerdata.text import awards, bios, drafts, lineups, ltrack, partial, rosters, salaries, standings, stats
from soccerdata.text.cmp import apsl, asl, copaamerica, nasl
#from soccerdata import scrapers
#from soccerdata.scrapers import mls

def clear_all():
    """
    Clear all relevant mongo tables.
    """
    from soccerdata.settings import STAT_TABLES, SOURCES, SINGLE_SOURCES
    for e in STAT_TABLES:
        soccer_db['%s' % e].drop()

    for s in SOURCES:
        for e in STAT_TABLES: 
            soccer_db['%s_%s' % (s, e)].drop()

    for e in SINGLE_SOURCES:
        soccer_db[e].drop()


def load_games_standard(coll, fn, games_only=False):
    """
    Load standard data from a standard games file.
    """
    from soccerdata.text import games

    print(fn)
    games, goals, fouls, lineups, rosters = games.process_games_file(fn)

    generic_load(soccer_db['%s_games' % coll], lambda: games, delete=False)

    if not games_only:
        generic_load(soccer_db['%s_lineups' % coll], lambda: lineups, delete=False)
        generic_load(soccer_db['%s_fouls' % coll], lambda: fouls, delete=False)
        generic_load(soccer_db['%s_goals' % coll], lambda: goals, delete=False)
        generic_load(soccer_db['%s_rosters' % coll], lambda: rosters, delete=False)


def load_standings_standard(coll, filename, delimiter=';'):
    """
    Load standard standings.
    """
    generic_load(soccer_db['%s_standings' % coll], lambda: standings.process_standings_file(filename, delimiter))


def load():
    """
    Load everything.
    
    # House-cleaning
    Make sure that aliases don't have any cycles.
    Clear mongo database.

    # load background data
    - sources
    - competitions
    - places
    - teams
    - name maps (team,date->name)
    - stadium maps (team,date->stadium)
    - competition maps (competition,date->stadium)
    -? organizations

    # load personal info
    - biographical data
    - salaries
    - job information
    - drafts
    -? stats

    # load game data
    - currently loading games, standings, stats mixed.
    """

    check_for_name_loops()
    check_for_team_loops()
    clear_all()

    load_sources()
    load_places()

    load_competitions()
    load_seasons()


    load_teams()

    load_name_maps()
    load_stadium_maps()
    load_competition_maps()

    #load_games(); return

    load_bios()
    load_salaries()
    load_positions()
    load_drafts()

    load_games()

    #load_news()
    #load_analysis()


def load_drafts():
    generic_load(soccer_db.drafts, drafts.load_drafts)
    generic_load(soccer_db.picks, drafts.load_picks)

def load_games():
    return
    load_world_international()
    load_concacaf()

    load_mls() 

    load_usmnt()
    load_uncaf()
    return

    load_asl()  
    load_nasl() 
    load_usa_cups()
    load_world()
    load_concacaf_international()
    load_conmebol()
    load_uncaf_international()


    load_women()
    load_china()
    load_australia()    
    load_korea()
    load_japan()
    load_oceania()

    load_mexico()



    load_chile()


    load_colombia()
    load_ecuador()

    load_conmebol_international()

    load_peru()
    load_uruguay()
    load_bolivia()

    load_mixed_confederation()

    load_usl()




    load_early_friendlies()
    load_modern_friendlies()
    load_brazil()
    load_argentina()
    load_cfu()

    load_ltrack()
    load_pdl()

    load_asl2()           
    load_apsl()
    load_nafbl()

    load_city()
    load_ny()
    load_canada()



    load_oceania_international()
    load_ncaa()
    load_indoor()

    #load_brazil_international()
    # scrapers
    #load_fifa()
    #load_mediotiempo()



def load_excel_standings(coll, fn):
    """
    Load standard excel-formatted standings.
    """
    generic_load(soccer_db['%s_standings' % coll], lambda: standings.process_excel_standings(fn))


def load_new_standings(coll, fn, delimiter=';'):
    """
    Load semicolon-style standings
    """
    generic_load(soccer_db['%s_standings' % coll], lambda: standings.process_standings_file(fn, delimiter))

            
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
    print("Loading ASL Bios")
    print(soccer_db.bios.count())
    generic_load(soccer_db.asl_bios, bios.process_asl_bios)

    #print("Loading MLSsoccer.com player bios.")
    #generic_load(soccer_db.mls_bios, mls.scrape_all_bios_mlssoccer)
    #print(soccer_db.bios.count())

    print("Loading chris's compiled bios.")

    generic_load(soccer_db.fifa_bios, bios.process_world_cup_bios)
    generic_load(soccer_db.nasl_bios, bios.process_misl_bios)
    generic_load(soccer_db.nasl_bios, bios.process_nasl_bios)
    generic_load(soccer_db.usa_bios, bios.process_usa_bios)
    generic_load(soccer_db.mls_bios, bios.process_mls_bios)
    generic_load(soccer_db.mls_reserve_bios, bios.process_mls_reserve_bios)
    generic_load(soccer_db.asl_bios, bios.process_asl_bios2)
    generic_load(soccer_db.asl2_bios, bios.process_asl2_bios)
    generic_load(soccer_db.us_d2_bios, bios.process_ussf2_bios)
    generic_load(soccer_db.us_d2_bios, bios.process_nasl2_bios)
    generic_load(soccer_db.us_d2bios, bios.process_apsl_bios)

    generic_load(soccer_db.us_d2_bios, bios.process_usl1_bios)
    generic_load(soccer_db.us_d3_bios, bios.process_usl2_bios)
    generic_load(soccer_db.us_d4_bios, bios.load_all_bios) # d4?



def load_places():
    from text import places
    generic_load(soccer_db.countries, places.load_countries)
    generic_load(soccer_db.states, places.load_states)
    generic_load(soccer_db.state_populations, places.load_state_populations)
    generic_load(soccer_db.stadiums, places.load_stadiums)



def load_usmnt():
    from soccerdata.text import awards

    for e in [1880, 1910, 1980, 1990, 2000, 2010]:
        load_games_standard('usa', 'international/country/usa/%s' % e)

    load_games_standard('usa', 'international/country/usa/world_cup')
    load_games_standard('usa', 'international/country/usa/us_cup')
    generic_load(soccer_db.usa_awards, awards.load_hall_of_fame)


def load_usa_cups():

    generic_load(soccer_db.us_cups_awards, awards.process_american_cup_awards)
    generic_load(soccer_db.us_cups_awards, awards.process_us_open_cup_awards, delete=False)
    generic_load(soccer_db.us_cups_awards, awards.process_lewis_cup_awards, delete=False)

    load_games_standard('us_cups', 'domestic/country/usa/cups/afa')
    load_games_standard('us_cups', 'domestic/country/usa/cups/afa2')
    load_games_standard('us_cups', 'domestic/country/usa/cups/lewis')
    load_games_standard('us_cups', 'domestic/country/usa/cups/duffy')
    load_games_standard('us_cups', 'domestic/country/usa/cups/aafa')

    for e in range(191, 202):
        load_games_standard('us_cups', 'domestic/country/usa/cups/open/%s0' % e)#, games_only=True)


def load_canada():
    load_excel_standings('canada', 'domestic/country/canada/csl')
    # Incomplete formatting: load_excel_standings('canada', 'domestic/country/canada/cnsl')
    load_games_standard('canada', 'domestic/country/canada/cups/championship')
    load_games_standard('canada', 'domestic/country/canada/cups/early')

    load_games_standard('canada', 'domestic/country/canada/friendly/1')
    load_games_standard('canada', 'domestic/country/canada/friendly/friendly2')
    load_games_standard('canada', 'domestic/country/canada/friendly/toronto')
    load_games_standard('canada', 'domestic/country/canada/friendly/vancouver')

    generic_load(soccer_db.canada_stats, partial.process_csl_partial)

    generic_load(soccer_db.canada_awards, awards.process_csl_awards)
    generic_load(soccer_db.canada_awards, awards.process_canada_awards)


def load_uncaf():

    generic_load(soccer_db.uncaf_awards, awards.process_uncaf_awards)

    load_games_standard('uncaf', 'domestic/confederation/concacaf/uncaf/fraternidad')
    load_games_standard('uncaf', 'domestic/confederation/concacaf/uncaf/torneograndes')
    load_games_standard('uncaf', 'domestic/confederation/concacaf/uncaf/interclube')

    # Guatemala
    load_standings_standard('uncaf', 'domestic/country/guatemala3')
    #generic_load(soccer_db.uncaf_awards, awards.process_guatemala_awards)

    # Whoops! deleted these?
    #load_games_standard('uncaf', 'domestic/country/guatemala/guatemala')

    for e in range(1996, 2010):
        load_games_standard('uncaf', 'domestic/country/guatemala/league/%s' % e)

    # El Salvador
    #generic_load(soccer_db.panama_awards, awards.process_elsalvador_awards)
    load_standings_standard('uncaf', 'domestic/country/elsalvador2')
    for e in range(1999, 2013):
        load_games_standard('uncaf', 'domestic/country/el_salvador/%s' % e)

    load_games_standard('uncaf', 'domestic/country/el_salvador/torneo')


    # Honduras
    load_standings_standard('uncaf', 'domestic/country/honduras')
    generic_load(soccer_db.uncaf_awards, awards.process_honduras_awards)
    for e in range(2000, 2012):
        load_games_standard('uncaf', 'domestic/country/honduras/%s' % e)

    # Costa Rica
    #generic_load(soccer_db.uncaf_awards, awards.process_costa_rica_awards)
    load_standings_standard('uncaf', 'domestic/country/costarica2')
    load_standings_standard('uncaf', 'domestic/country/costarica3')
    for e in range(2003, 2012):
        load_games_standard('uncaf', 'domestic/country/costa_rica/league/%s' % e)

    # Panama
    #generic_load(soccer_db.panama_awards, awards.process_panama_awards)
    load_standings_standard('uncaf', 'domestic/country/panama')
    for e in range(2000, 2013):
        load_games_standard('uncaf', 'domestic/country/panama/%s' % e)

    # Nicaragua
    load_standings_standard('uncaf', 'domestic/country/nicaragua')
    #generic_load(soccer_db.panama_awards, awards.process_nicaragua_awards)


    # Belize
    #load_standings_standard('uncaf', 'domestic/country/belize')



def load_uruguay():
    load_standings_standard('uruguay', 'domestic/country/uruguay')
    generic_load(soccer_db.uruguay_awards, awards.process_uruguay_awards)
    load_games_standard('uruguay', 'domestic/country/uruguay/prelibertadores')
    for year in range(1932, 1960):
        load_games_standard('uruguay', 'domestic/country/uruguay/%s' % year)

    for year in range(1994, 1995):
        load_games_standard('uruguay', 'domestic/country/uruguay/%s' % year)

def load_colombia():
    #load_standings_standard('colombia', 'domestic/country/colombia2')
    for e in range(2002, 2011):
        load_games_standard('colombia', 'domestic/country/colombia/%s' % e)

def load_ecuador():
    #load_standings_standard('colombia', 'domestic/country/ecuador')
    for e in range(2006, 2011):
        load_games_standard('colombia', 'domestic/country/ecuador/%s' % e)

def load_bolivia():
    #load_standings_standard('colombia', 'domestic/country/bolivia')
    for e in range(2011, 2012):
        load_games_standard('colombia', 'domestic/country/bolivia/%s' % e)

def load_peru():
    #load_standings_standard('colombia', 'domestic/country/bolivia')
    for e in range(2011, 2011):
        load_games_standard('colombia', 'domestic/country/peru/%s' % e)

def load_chile():
    load_standings_standard('chile', 'domestic/country/chile')
    generic_load(soccer_db.chile_awards, awards.process_chile_awards)

    for year in range(1933, 1968):
        load_games_standard('chile', 'domestic/country/chile/%s' % year)

    for year in range(1971, 1979):
        load_games_standard('chile', 'domestic/country/chile/%s' % year)


def load_argentina():
    generic_load(soccer_db.argentina_awards, awards.process_argentina_awards)
    load_games_standard('argentina', 'domestic/country/argentina/leagues/1891')
    load_games_standard('argentina', 'domestic/country/argentina/leagues/1893')
    load_games_standard('argentina', 'domestic/country/argentina/leagues/1896')

    for year in range(1899, 1911):
        load_games_standard('argentina', 'domestic/country/argentina/leagues/%s' % year)

    for year in range(1932, 1965):
        load_games_standard('argentina', 'domestic/country/argentina/leagues/%s' % year)

    for year in range(1976, 1976):
        load_games_standard('argentina', 'domestic/country/argentina/leagues/%s' % year)

    for year in range(2009, 2011):
        load_games_standard('argentina', 'domestic/country/argentina/leagues/%s' % year)



def load_brazil():
    for e in range(2005, 2013):
        load_games_standard('brazil', 'domestic/country/brazil/brasileiro/%s' % e)


    for year in range(1920, 1966):
        load_games_standard('brazil', 'domestic/country/brazil/paulista/%s' % year)


def load_brazil_international():
    load_games_standard('brazil', 'international/country/brazil/1914')
    load_games_standard('brazil', 'international/country/brazil/1923')


def load_women():

    generic_load(soccer_db.women_awards, awards.process_women_awards)

    load_games_standard('women', 'domestic/country/usa/leagues/women/wusa')
    load_games_standard('women', 'domestic/country/usa/leagues/women/nwsl')
    load_games_standard('women', 'domestic/country/usa/leagues/women/wps')
    load_games_standard('women', 'domestic/country/usa/leagues/women/wpsl_elite')

    #for e in range(2007, 2013):
    #    load_games_standard('women', 'domestic/country/usa/leagues/women/wpsl/%s' % e)


def load_mls():

    load_excel_standings('mls', 'domestic/country/usa/mls')
    load_games_standard('mls', 'domestic/country/usa/playoffs/mls')

    print("Loading MLS reserves data.")
    for e in [2005, 2006, 2007, 2008, 2011, 2012, 2013]:
        load_games_standard('mls', 'domestic/country/usa/leagues/reserve/mls/%s' % e)

    print("Loading mls bio stats.")
    # Not loading 1996-2011 stats?
    generic_load(soccer_db.mls_stats, stats.process_mls_2012_stats)
    load_mls_lineup_db()

    print("Loading MLS awards.")
    generic_load(soccer_db.mls_awards, awards.process_mls_awards)

    for e in ['1996.2010', '2011', '2012', '2013']:
        load_games_standard('mls', 'domestic/country/usa/leagues/d1/mls/%s' % e)

    # Not loading playoff data?



    """
    from scrapers.mls2 import scrape_competition

    # MLS League 2012
    url = 'http://www.mlssoccer.com/schedule?month=all&year=2012&club=all&competition_type=46&broadcast_type=all&op=Search&form_id=mls_schedule_form'
    games, goals, lineups = scrape_competition(url, 'Major League Soccer')

    # Need to fix some stuff here, obvs.
    generic_load(soccer_db['mls2_games'], lambda: games)
    generic_load(soccer_db['mls2_goals'], lambda: goals)
    generic_load(soccer_db['mls2_lineups'], lambda: lineups)

    # MLS Playoffs 2012
    url = 'http://www.mlssoccer.com/schedule?month=all&year=2012&club=all&competition_type=45&broadcast_type=all&op=Search&form_id=mls_schedule_form'
    games, goals, lineups = scrape_competition(url, 'MLS Cup Playoffs')

    # We're getting null values for some lineups here. Not sure why.

    generic_load(soccer_db['mls2_games'], lambda: games)
    generic_load(soccer_db['mls2_goals'], lambda: goals)
    generic_load(soccer_db['mls2_lineups'], lambda: lineups)

    # MLS Cup 2012
    url = 'http://www.mlssoccer.com/schedule?month=all&year=2012&club=all&competition_type=44&broadcast_type=all&op=Search&form_id=mls_schedule_form'
    games, goals, lineups = scrape_competition(url, 'MLS Cup Playoffs')

    generic_load(soccer_db['mls2_games'], lambda: games)
    generic_load(soccer_db['mls2_goals'], lambda: goals)
    generic_load(soccer_db['mls2_lineups'], lambda: lineups)
    """



def load_nafbl():
    # Also loading ALPF and SNESL
    generic_load(soccer_db.asl_awards, awards.process_nafbl_awards, delete=False)
    generic_load(soccer_db.asl_awards, awards.process_snesl_awards, delete=False)

    load_excel_standings('nafbl', 'domestic/country/usa/early')

    load_games_standard('nafbl', 'domestic/country/usa/leagues/d1/alpf')

    load_games_standard('nafbl', 'domestic/country/usa/leagues/regional/nafbl1')
    load_games_standard('nafbl', 'domestic/country/usa/leagues/regional/nafbl2')
    load_games_standard('nafbl', 'domestic/country/usa/leagues/regional/snesl')
    load_games_standard('nafbl', 'domestic/country/usa/leagues/regional/nasfl')
    load_games_standard('nafbl', 'domestic/country/usa/leagues/misc/isl') # ISL 1925?



def load_city():
    #load_games_standard('city', 'city')
    load_excel_standings('city', 'domestic/city/slsl')
    load_excel_standings('city', 'domestic/city/cosmo')
    #generic_load(soccer_db.city_awards, awards.process_chicago_awards, delete=False)


def load_ny():
    load_games_standard('state', 'domestic/country/usa/leagues/metropolitan')
    load_games_standard('state', 'domestic/country/usa/friendly/1900_ny')
    generic_load(soccer_db.state_awards, awards.process_ny_awards, delete=False)


def load_early_friendlies():

    for e in range(1865, 1891, 5):
        load_games_standard('us_friendly', 'domestic/country/usa/friendly/%s' % e)

    for e in range(1900, 1951, 10):
        load_games_standard('us_friendly', 'domestic/country/usa/friendly/%s' % e)


def load_modern_friendlies():
    load_games_standard('us_friendly', 'domestic/country/usa/friendly/carolina')
    load_games_standard('us_friendly', 'domestic/country/usa/friendly/dynamo')
    load_games_standard('us_friendly', 'international/country/usa/bicentennial')
    load_games_standard('us_friendly', 'domestic/country/usa/friendly/mls_all_star')
    load_games_standard('us_friendly', 'domestic/country/usa/friendly/1960')
    load_games_standard('us_friendly', 'domestic/country/usa/friendly/1967')
    load_games_standard('us_friendly', 'domestic/country/usa/friendly/1970')
    load_games_standard('us_friendly', 'domestic/country/usa/friendly/1980')
    load_games_standard('us_friendly', 'domestic/country/usa/friendly/tours/1970')
    load_games_standard('us_friendly', 'domestic/country/usa/friendly/tours/1980')
    load_games_standard('us_friendly', 'domestic/country/usa/friendly/1990')
    load_games_standard('us_friendly', 'domestic/country/usa/friendly/2000')
    load_games_standard('us_friendly', 'domestic/country/usa/friendly/2010')

def load_competitions():
    from soccerdata.text import competitions
    print("Loading competitions.")
    generic_load(soccer_db.competitions, competitions.load_competitions)


def load_seasons():
    from soccerdata.text import seasons
    print("Loading seasons.")
    generic_load(soccer_db.seasons, seasons.load_seasons)



def load_teams():
    from soccerdata.text import teams
    print("Loading teams.")
    generic_load(soccer_db.teams, teams.load)


def load_salaries():
    soccer_db.salaries.drop()
    generic_load(soccer_db.salaries, salaries.load_salaries)


def load_positions():
    from soccerdata.text.positions import process_positions
    print("Loading positions.")
    generic_load(soccer_db.positions, process_positions)


def load_analysis():
    from soccerdata.text import ratings
    print("Loading ratings.")
    generic_load(soccer_db.analysis_ratings, ratings.get_ratings)
    

def load_copa_america():

    coll = 'conmebol_i'
    games, goals, fouls, lineups = copaamerica.process_copa_files()

    generic_load(soccer_db['%s_games' % coll], lambda: games, delete=False)
    generic_load(soccer_db['%s_lineups' % coll], lambda: lineups, delete=False)
    generic_load(soccer_db['%s_fouls' % coll], lambda: fouls, delete=False)
    generic_load(soccer_db['%s_goals' % coll], lambda: goals, delete=False)

    generic_load(soccer_db.conmebol_i_rosters, lambda: rosters.process_rosters('international/copa_america'))
    load_games_standard('conmebol_i', 'international/confederation/conmebol/copa_america/stadia')



    
def load_asl():
    load_excel_standings('asl', 'domestic/country/usa/asl')
    generic_load(soccer_db.asl_awards, awards.process_asl_awards, delete=False)
    generic_load(soccer_db.asl_awards, awards.process_esl_awards, delete=False)

    # Colin Jose data
    generic_load(soccer_db.asl_goals, asl.process_asl_goals)
    generic_load(soccer_db.asl_stats, asl.process_stats)
    generic_load(soccer_db.asl_games, asl.process_asl_games)

    load_games_standard('asl', 'domestic/country/usa/leagues/d1/asl')
    load_games_standard('asl', 'domestic/country/usa/leagues/d2/esl')


def load_asl2():
    generic_load(soccer_db.asl2_awards, awards.process_asl2_awards, delete=False)
    generic_load(soccer_db.asl2_stats, partial.process_asl2_partial)
    load_excel_standings('asl2', 'domestic/country/usa/asl2')
    load_games_standard('asl2', 'domestic/country/usa/leagues/d2/asl2')


def load_nasl():
    """
    Load stats from the old nasl and misl.
    """

    print("Loading NASL data.")
    load_excel_standings('nasl', 'domestic/country/usa/nasl')
    load_excel_standings('nasl', 'domestic/country/usa/nasl0')
    generic_load(soccer_db.nasl_awards, awards.process_nasl_awards)
    generic_load(soccer_db.nasl_awards, awards.process_usa_awards)
    generic_load(soccer_db.nasl_awards, awards.process_npsl_awards)

    generic_load(soccer_db.nasl_rosters, lambda: rosters.process_rosters2('nasl'))

    load_games_standard('nasl', 'domestic/country/usa/playoffs/nasl')

    generic_load(soccer_db.nasl_games, nasl.process_npsl_games)
    generic_load(soccer_db.nasl_goals, nasl.process_npsl_goals)
    load_games_standard('nasl', 'domestic/country/usa/leagues/d2/usa')

    generic_load(soccer_db.nasl_stats, stats.process_nasl_stats)

    # Need to work some integrity issues on games.
    generic_load(soccer_db.nasl_games, nasl.process_nasl_games)
    generic_load(soccer_db.nasl_goals, nasl.process_nasl_goals)
    generic_load(soccer_db.nasl_lineups, nasl.process_nasl_lineups)


def load_apsl():
    """
    Load stats and games from the APSL and WSA.
    """
    from soccerdata.text import awards

    print("loading apsl stats")
    generic_load(soccer_db.us_d2_stats, apsl.process_apsl_stats)

    print("loading apsl partial stats")
    generic_load(soccer_db.us_d2_stats, partial.process_apsl_partial)

    generic_load(soccer_db.us_d2_awards, awards.process_apsl_awards)

    load_excel_standings('us_d2', 'domestic/country/usa/apsl')
    load_excel_standings('us_d2', 'domestic/country/usa/wsa')
    load_excel_standings('us_d2', 'domestic/country/usa/lssa')
    
    #print("loading apsl scores")
    #generic_load(soccer_db.us_d2_games, apsl.process_apsl_scores)
    #load_games_standard('us_d2', 'domestic/country/usa/leagues/wsa3')

    load_games_standard('us_d2', 'domestic/country/usa/leagues/d2/apsl')
    load_games_standard('us_d2', 'domestic/country/usa/leagues/d3/wsa4')

    load_games_standard('us_d2', 'domestic/country/usa/playoffs/apsl')
    load_games_standard('us_d2', 'domestic/country/usa/playoffs/wsa')
    load_games_standard('us_d2', 'domestic/country/usa/cups/apsl_professional')


def load_indoor():
    """
    Load stats and games from the MISL, standings from MISL, APSL and WSA.
    """
    load_excel_standings('misl', 'indoor/all')
    load_excel_standings('misl', 'indoor/misl')
    print("Loading MISL stats.")
    generic_load(soccer_db.misl_stats, stats.process_misl_stats)


def load_ltrack():
    generic_load(soccer_db.ltrack_goals, ltrack.process_goals)
    generic_load(soccer_db.ltrack_games, ltrack.process_games)
    generic_load(soccer_db.ltrack_lineups, ltrack.process_lineups)


def load_mls_lineup_db():
    # Load scaryice lineup data.

    # MLS lineup data 1996-2010
    print("Loading scaryice score data.")
    generic_load(soccer_db.mls_games, lineups.load_all_games_scaryice)

    print("Loading scaryice goal data.")
    generic_load(soccer_db.mls_goals, lineups.load_all_goals_scaryice)
    
    print( "Loading scaryice lineup data.")
    generic_load(soccer_db.mls_lineups, lineups.load_all_lineups_scaryice)


def load_pdl():
    from soccerdata.text.cmp import pdl
    load_excel_standings('us_d4', 'domestic/country/usa/usl/pdl')
    generic_load(soccer_db.us_d4_awards, awards.process_pdl_awards)
    generic_load(soccer_db.us_d4_stats, stats.process_pdl_stats)
    generic_load(soccer_db.us_d4_games, pdl.load_pdl_games)


def load_usl():
    """
    Load usl stats and nasl stats.
    """

    # Division 2
    generic_load(soccer_db.us_d2_awards, awards.process_usl_awards) #split 2 and 3
    generic_load(soccer_db.us_d2_awards, awards.process_ussf2_awards)
    generic_load(soccer_db.us_d2_awards, awards.process_nasl2_awards)

    generic_load(soccer_db.us_d2_stats, stats.process_usl1_stats)
    generic_load(soccer_db.us_d2_stats, stats.process_usl2_stats)
    generic_load(soccer_db.us_d2_stats, nasl.process_stats)

    load_excel_standings('us_d2', 'domestic/country/usa/usl/usl0')
    load_excel_standings('us_d2', 'domestic/country/usa/usl/12') # split
    load_excel_standings('us_d2', 'domestic/country/usa/ussf2')
    load_excel_standings('us_d2', 'domestic/country/usa/nasl2')

    load_games_standard('us_d2', 'domestic/country/usa/leagues/d2/usl1')
    load_games_standard('us_d2', 'domestic/country/usa/leagues/d2/ussfd2')
    load_games_standard('us_d2', 'domestic/country/usa/leagues/d2/nasl/2011')
    load_games_standard('us_d2', 'domestic/country/usa/leagues/d2/nasl/2012')
    load_games_standard('us_d2', 'domestic/country/usa/leagues/d2/nasl/2013')

    load_games_standard('us_d2', 'domestic/country/usa/playoffs/usl1')
    load_games_standard('us_d2', 'domestic/country/usa/playoffs/nasl2')

    # Division 3
    load_excel_standings('us_d3', 'domestic/country/usa/usl/pro') # 2 or 3?
    load_excel_standings('us_d3', 'domestic/country/usa/usl/premier')
    load_excel_standings('us_d3', 'domestic/country/usa/usl/usl_pro')
    load_excel_standings('us_d3', 'domestic/country/usa/usl/usisl')
    load_excel_standings('us_d3', 'domestic/country/usa/usl/select') # 2 or 3?

    for e in range(2003, 2014):
        load_games_standard('us_d3', 'domestic/country/usa/leagues/d3/%s' % e)
    load_games_standard('us_d3', 'domestic/country/usa/playoffs/usl2')



def load_china():
    load_games_standard('china', 'domestic/country/china/leaguea')
    load_standings_standard('china', 'domestic/country/china')
    generic_load(soccer_db.china_awards, awards.process_china_awards)


def load_japan():
    load_standings_standard('japan', 'domestic/country/japan')


def load_korea():
    load_standings_standard('korea', 'domestic/country/korea')


def load_australia():
    load_standings_standard('australia', 'domestic/country/australia')
    load_games_standard('australia', 'domestic/country/australia/league/australia')
    load_games_standard('australia', 'domestic/country/australia/playoffs')
    generic_load(soccer_db.australia_awards, awards.process_australia_awards)


def load_mediotiempo():
    from scrapers import mediotiempo2
    generic_load(soccer_db.mediotiempo_games, lambda: mediotiempo2.scrape_games(range(6700, 9000)))

def load_mexico():

    generic_load(soccer_db.mexico_awards, awards.process_mexico_awards)

    load_new_standings('mexico', 'domestic/country/mexico/1', ';')
    load_new_standings('mexico', 'domestic/country/mexico/short', ';')
    load_new_standings('mexico', 'domestic/country/mexico/primera_fuerza')

    for e in range(1970, 2020, 10):
        load_games_standard('mexico', 'domestic/country/mexico/playoffs/%s' % e)

    for e in range(1970, 2012):
        load_games_standard('mexico', 'domestic/country/mexico/league/%s' % e)


    load_games_standard('mexico', 'domestic/country/mexico/interliga')
    load_games_standard('mexico', 'domestic/country/mexico/pre_libertadores')

    load_games_standard('mexico', 'domestic/country/mexico/super')

    # league
    load_games_standard('mexico', 'domestic/country/mexico/league/1943')
    load_games_standard('mexico', 'domestic/country/mexico/league/1963')
    load_games_standard('mexico', 'domestic/country/mexico/league/1964')
    load_games_standard('mexico', 'domestic/country/mexico/league/1967')
    load_games_standard('mexico', 'domestic/country/mexico/league/1970mexico')


    # Cups




    # Friendlies.
    load_games_standard('mexico', 'domestic/country/mexico/friendly/adolfo_lopez_mateos')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/agosto')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/chiapas')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/corona')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/gol')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/mesoamericana')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/leon')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/mexico_city')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/mexico_city2')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/milenio')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/monterrey')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/nike')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/pentagonal2')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/puebla')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/quadrangular')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/queretaro')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/real_madrid')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/tijuana')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/toluca')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/torreon')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/tour')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/universidades')
    load_games_standard('mexico', 'domestic/country/mexico/friendly/veracruz')



def load_oceania():
    load_games_standard('oceania', 'domestic/confederation/ofc/wantok')


def load_oceania_international():
    load_games_standard('oceania_i', 'international/confederation/ofc/wcq')
    #load_games_standard('oceania_i', 'international/confederation/ofc/wcq')
    load_games_standard('oceania_i', 'international/confederation/ofc/melanesia')
    load_games_standard('oceania_i', 'international/confederation/ofc/polynesia')
    load_games_standard('oceania_i', 'international/confederation/ofc/nations')

def load_mixed_confederation():

    load_games_standard('world', 'domestic/confederation/mixed/panpacific')
    load_games_standard('world', 'domestic/confederation/mixed/interamerican')
    load_games_standard('world', 'domestic/confederation/mixed/suruga')

    for e in [1960, 1970, 1980, 1990, 2000]:
        load_games_standard('world', 'domestic/confederation/mixed/intercontinental/%s' % e)


def load_conmebol():

    generic_load(soccer_db.conmebol_awards, awards.process_conmebol_awards)

    load_games_standard('conmebol', 'domestic/confederation/conmebol/aldao')
    load_games_standard('conmebol', 'domestic/confederation/conmebol/copa_ibarguren')

    load_games_standard('conmebol', 'domestic/confederation/conmebol/copa_tie')
    load_games_standard('conmebol', 'domestic/confederation/conmebol/masters')

    load_games_standard('conmebol', 'domestic/confederation/conmebol/recopa_sudamericana')
    load_games_standard('conmebol', 'domestic/confederation/conmebol/sacc')


    load_games_standard('conmebol', 'domestic/confederation/conmebol/merconorte')
    load_games_standard('conmebol', 'domestic/confederation/conmebol/mercosur')
    load_games_standard('conmebol', 'domestic/confederation/conmebol/mercosul')



    for e in range(1992, 2000):
        load_games_standard('conmebol', 'domestic/confederation/conmebol/conmebol/%s' % e)

    for e in range(2002, 2013):
        load_games_standard('conmebol', 'domestic/confederation/conmebol/sudamericana/%s' % e)


    for e in range(1960, 1993):
        load_games_standard('conmebol', 'domestic/confederation/conmebol/libertadores/%s' % e)

    for e in range(1994, 2014):
        load_games_standard('conmebol', 'domestic/confederation/conmebol/libertadores/%s' % e)


def load_conmebol_international():
    generic_load(soccer_db.conmebol_i_awards, awards.process_conmebol_international_awards)

    for year in range(1958, 2015, 4):
        load_games_standard('conmebol_i', 'international/confederation/conmebol/wcq/%s' % year)

    load_copa_america()
    load_games_standard('canada', 'international/country/argentina')
    load_games_standard('conmebol_i', 'international/country/bolivia')
    #load_games_standard('conmebol_i', 'international/country/brazil')
    load_games_standard('conmebol_i', 'international/country/chile')
    load_games_standard('conmebol_i', 'international/country/colombia')
    load_games_standard('conmebol_i', 'international/country/ecuador')
    load_games_standard('conmebol_i', 'international/country/paraguay')
    load_games_standard('conmebol_i', 'international/country/peru')
    load_games_standard('conmebol_i', 'international/country/uruguay'),
    load_games_standard('conmebol_i', 'international/country/venezuela')

    load_games_standard('conmebol_i', 'international/confederation/conmebol/early_south_america')
    load_games_standard('conmebol_i', 'international/confederation/conmebol/copa_premio_honor')
    load_games_standard('conmebol_i', 'international/confederation/conmebol/copa_del_atlantico')
    load_games_standard('conmebol_i', 'international/confederation/conmebol/copa_newton')
    load_games_standard('conmebol_i', 'international/confederation/conmebol/copa_lipton')
    load_games_standard('conmebol_i', 'international/confederation/conmebol/copa_mayo')


def load_cfu():
    generic_load(soccer_db.cfu_awards, awards.process_cfu_awards)

    load_standings_standard('cfu', 'domestic/country/bermuda')
    load_standings_standard('cfu', 'domestic/country/trinidad')
    load_standings_standard('cfu', 'domestic/country/curacao')
    load_standings_standard('cfu', 'domestic/country/martinique')
    load_standings_standard('cfu', 'domestic/country/jamaica')
    load_games_standard('cfu', 'domestic/confederation/concacaf/cfu/1990')
    load_games_standard('cfu', 'domestic/confederation/concacaf/cfu/2000')
    load_games_standard('cfu', 'domestic/confederation/concacaf/cfu/2010')


def load_uncaf_international():
    #generic_load(soccer_db.uncaf_awards, awards.process_uncaf_international_awards)

    load_games_standard('uncaf', 'international/confederation/concacaf/uncaf')

    load_games_standard('concacaf_i', 'international/country/belize')
    load_games_standard('concacaf_i', 'international/country/costa_rica')
    load_games_standard('concacaf_i', 'international/country/el_salvador')
    load_games_standard('concacaf_i', 'international/country/guatemala')
    load_games_standard('concacaf_i', 'international/country/honduras')
    load_games_standard('concacaf_i', 'international/country/nicaragua')
    load_games_standard('concacaf_i', 'international/country/panama')


def load_world_international():
    generic_load(soccer_db.world_i_rosters, lambda: rosters.process_rosters('international/olympics'))
    generic_load(soccer_db.world_i_rosters, lambda: rosters.process_rosters2('confederations'))

    confed = [1992, 1995, 1997, 1999, 2001, 2003, 2005, 2009, 2013]

    for e in confed:
        load_games_standard('world_i', 'international/world/confederations/%s' % e)

    generic_load(soccer_db.world_i_awards, awards.process_world_cup_awards)
    generic_load(soccer_db.world_i_awards, awards.process_olympics_awards)

    for e in [1930, 1934] + list(range(1950, 2014, 4)):
        load_games_standard('world_i', 'international/world/world_cup/%s' % e)

    #load_games_standard('world_i', 'international/world/u20')
    #load_games_standard('world_i', 'international/world/u17')

    load_games_standard('world_i', 'international/world/artemio_franchi')
    load_games_standard('world_i', 'international/world/interallied')
    load_games_standard('world_i', 'international/world/mundialito')

    olympics = [1900, 1904, 1908, 1912, 1920, 1924, 1928, 1936, 
                1948, 1952, 1956, 1960, 1964, 1968, 1972, 2008, 2012]

    for e in olympics:
        load_games_standard('world_i', 'international/world/olympics/%s' % e)



def load_world():

    generic_load(soccer_db.world_awards, awards.process_world_awards)

    load_games_standard('world', 'domestic/world/club_world_cup/2000')
    load_games_standard('world', 'domestic/world/club_world_cup/2001')
    for e in range(2005, 2013):
        load_games_standard('world', 'domestic/world/club_world_cup/%s' % e)

    # International friendly club tournaments.
    # Also existed in Brazil / Argentina / Colombia?

    generic_load(soccer_db.world_awards, awards.process_isl_awards)

    generic_load(soccer_db.world_rosters, lambda: rosters.process_rosters2('club_world_cup'))
    generic_load(soccer_db.world_rosters, lambda: rosters.process_rosters2('isl'))
    generic_load(soccer_db.world_rosters, lambda: rosters.process_rosters2('copita'))

    load_excel_standings('world', 'domestic/country/usa/isl')
    load_games_standard('world', 'domestic/country/usa/leagues/isl2')

    load_games_standard('world', 'domestic/country/mexico/friendly/palmares')

    load_games_standard('world', 'domestic/world/parmalat')
    load_games_standard('world', 'domestic/world/copa_rio')
    load_games_standard('world', 'domestic/confederation/conmebol/pequena')
    load_games_standard('world', 'international/misc/fifa_world_stars_games')


def load_caribbean_international():
    generic_load(soccer_db.concacaf_i_awards, awards.process_caribbean_awards)

    load_games_standard('uncaf', 'international/confederation/concacaf/caribbean/cfu')
    load_games_standard('uncaf', 'international/confederation/concacaf/caribbean/1980')
    load_games_standard('uncaf', 'international/confederation/concacaf/caribbean/1990')
    load_games_standard('uncaf', 'international/confederation/concacaf/caribbean/2001')

    load_games_standard('concacaf_i', 'international/country/anguilla')
    load_games_standard('concacaf_i', 'international/country/antigua')
    load_games_standard('concacaf_i', 'international/country/aruba')
    load_games_standard('concacaf_i', 'international/country/bahamas')
    load_games_standard('concacaf_i', 'international/country/barbados')
    load_games_standard('concacaf_i', 'international/country/bermuda')    
    load_games_standard('concacaf_i', 'international/country/bvi')
    load_games_standard('concacaf_i', 'international/country/cayman')
    load_games_standard('concacaf_i', 'international/country/cuba')
    load_games_standard('concacaf_i', 'international/country/dominica')
    load_games_standard('concacaf_i', 'international/country/dr')
    load_games_standard('concacaf_i', 'international/country/french_guyana')
    load_games_standard('concacaf_i', 'international/country/grenada')
    load_games_standard('concacaf_i', 'international/country/guadeloupe')
    load_games_standard('concacaf_i', 'international/country/guyana')
    load_games_standard('concacaf_i', 'international/country/haiti')
    load_games_standard('concacaf_i', 'international/country/jamaica')
    load_games_standard('concacaf_i', 'international/country/martinique')
    load_games_standard('concacaf_i', 'international/country/montserrat')
    load_games_standard('concacaf_i', 'international/country/puerto_rico')
    load_games_standard('concacaf_i', 'international/country/nevis')
    load_games_standard('concacaf_i', 'international/country/st_lucia')
    load_games_standard('concacaf_i', 'international/country/saint_martin')
    load_games_standard('concacaf_i', 'international/country/st_vincent')
    load_games_standard('concacaf_i', 'international/country/sint_maarten')
    load_games_standard('concacaf_i', 'international/country/suriname')
    load_games_standard('concacaf_i', 'international/country/trinidad_tobago')
    load_games_standard('concacaf_i', 'international/country/turks_caicos')
    load_games_standard('concacaf_i', 'international/country/usvi')

    #load_games_standard('concacaf_i', 'international/country/saint_croix')
    #load_games_standard('concacaf_i', 'international/country/saint_thomas')    
    #load_games_standard('concacaf_i', 'international/country/tortola')
    #load_games_standard('concacaf_i', 'international/country/virgin_gorda')


def load_panamerican():

    generic_load(soccer_db.concacaf_i_awards, awards.process_panamerican_awards)

    for e in [1951, 1955, 1959, 1963, 1967, 1971, 1975, 1979, 1983, 1987, 
              1991, 1995, 1999, 2003, 2007]:
        load_games_standard('concacaf_i', 'international/world/panamerican/%s' % e)



def load_concacaf_international():

    for year in range(1994, 2015, 4):
        load_games_standard('concacaf_i', 'international/confederation/concacaf/wcq/%s' % year)

    for year in [2009, 2011, 2013]:
        load_games_standard('concacaf_i', 'international/confederation/concacaf/u20/%s' % year)

    for year in range(2000, 2014, 4):
        load_games_standard('concacaf_i', 'international/confederation/concacaf/olympic/%s' % year)

    for year in [2009, 2011, 2013]:
        load_games_standard('concacaf_i', 'international/confederation/concacaf/u17/%s' % year)
    # Add u-17 qualifying.

    generic_load(soccer_db.concacaf_i_awards, awards.process_concacaf_international_awards)

    load_uncaf_international()
    load_caribbean_international()

    load_games_standard('concacaf_i', 'international/confederation/concacaf/gold')

    load_games_standard('concacaf_i', 'international/confederation/concacaf/championship')
    load_games_standard('concacaf_i', 'international/confederation/concacaf/cccf')
    load_games_standard('concacaf_i', 'international/confederation/concacaf/cacg')

    load_games_standard('concacaf_i', 'international/confederation/concacaf/martinez')
    load_games_standard('concacaf_i', 'international/confederation/concacaf/independence')
    load_games_standard('concacaf_i', 'international/confederation/concacaf/friendly')

    load_games_standard('concacaf_i', 'international/confederation/concacaf/world_cup_qualifying')

    load_games_standard('canada', 'international/country/canada/1900')
    load_games_standard('canada', 'international/country/canada/2000')
    load_games_standard('mexico', 'international/country/mexico/alltime')

    load_panamerican()


def load_concacaf():

    load_games_standard('concacaf', 'domestic/confederation/concacaf/giantscup')
    load_games_standard('concacaf', 'domestic/confederation/concacaf/recopa')
    load_games_standard('concacaf', 'domestic/confederation/concacaf/superliga')
    for e in range(2008, 2014):
        load_games_standard('concacaf', 'domestic/confederation/concacaf/champions/league/%s' % e)
    generic_load(soccer_db.concacaf_awards, awards.process_concacaf_awards)

    load_games_standard('concacaf', 'domestic/confederation/concacaf/champions/2000')
    
    # Unicode problem on 1960 Champions Cup data.
    for e in '6789':
        try:
            load_games_standard('concacaf', 'domestic/confederation/concacaf/champions/19%s0' % e)
        except:
            import pdb; pdb.set_trace()



def load_ncaa():
    print("Loading NCAA awards.")
    load_games_standard('ncaa', 'domestic/country/usa/college')
    generic_load(soccer_db.ncaa_awards, awards.process_ncaa_awards)


def load_fifa():
    from soccerdata.scrapers import fifa

    generic_load(soccer_db.fifa_games, fifa.scrape_all_world_cup_games)
    generic_load(soccer_db.fifa_goals, fifa.scrape_all_world_cup_goals)
    generic_load(soccer_db.fifa_lineups, fifa.scrape_all_world_cup_lineups)

    load_fifa_competition('FIFA U-17 World Cup')
    load_fifa_competition('Olympic Games')
    load_fifa_competition('FIFA Club World Cup')
    load_fifa_competition('FIFA Confederations Cup')
    load_fifa_competition('FIFA U-20 World Cup')



def load_fifa_competition(competition):
    from soccerdata.scrapers import fifa
    games, goals, lineups = fifa.scrape_everything(competition)
    generic_load(soccer_db.fifa_games, lambda: games)
    generic_load(soccer_db.fifa_goals, lambda: goals)
    generic_load(soccer_db.fifa_lineups, lambda: lineups)



if __name__ == "__main__":
    load()
