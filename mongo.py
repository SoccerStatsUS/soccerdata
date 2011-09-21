
# Presumably we're going to be sending things into databases from mongo.
# This is how we do it...

# Need to check for duplicates!


import datetime
import pymongo

connection = pymongo.Connection()
soccer_db = connection.soccer

def insert_row(collection, row):
    collection.insert(row)

def insert_rows(collection, rows):
    for row in rows:
        insert_row(collection, row)
    
def get_rows(collection):
    return [row for row in collection.find().sort('date', pymongo.ASCENDING)]


def delete_rows(collection, rows=None):
    if rows is None:
        rows = collection.find()
    for row in rows:
        collection.remove(row)


# Statto data
# Statto can only be scraped up to 2008, 1, 1 (or maybe earlier?)

def scrape_statto(date):
    """
    Scrape a single statto game. 
    """
    from soccerdata.scrapers import statto
    rows = statto.process_date(date)
    insert_rows(soccer_db.statto_games, rows)
    # Statto is scraping all possible games for a given date,
    # e.g. 2011-3-21.
    insert_row(soccer_db.statto_games_dates, {"date": date})


def scrape_all_statto():
    """
    Download all statto schedules.
    """
    date = datetime.datetime(2008, 1, 1)
    # Will run including today.
    while date < datetime.datetime.now():
        scrape_statto(date)
        date += datetime.timedelta(days=1)


# RSSSF Data

def scrape_spain_rsssf(years=None):
    from scrapers.rsssf import spain

    if years is None:
        years = range(2000, 2012)

    delete_rows(soccer_db.rsssf_spain_games)
    for year in years:
        rows = spain.process_year(year)
        insert_rows(soccer_db.rsssf_spain_games, rows)


def scrape_mls_rsssf(years=None):
    from scrapers.rsssf import usa

    if years is None:
        years = range(1996, 2009)

    delete_rows(soccer_db.rsssf_mls_games)
    for year in years:
        rows = usa.process_year(year)
        insert_rows(soccer_db.rsssf_mls_games, rows)

def scrape_australia_rsssf(years=None):
    from scrapers.rsssf import australia

    if years is None:
        years = range(2006, 2012)

    delete_rows(soccer_db.rsssf_australia_games)
    for year in years:
        rows = australia.process_year(year)
        insert_rows(soccer_db.rsssf_australia_games, rows)


# MLSsoccer data

def scrape_mls_mlssoccer(years=None):
    from scrapers import mls

    if years is None:
        years = range(1996, 2011)

    delete_rows(soccer_db.mlssoccer_mls_games)
    for year in years:
        rows = mls.scrape_scores(year)
        insert_rows(soccer_db.mlssoccer_mls_games, rows)


# Nasl data

def scrape_nasl():
    from scrapers import nasl
    scores = nasl.scrape_scores()
    delete_rows(soccer_db.nasl_scores)
    insert_rows(soccer_db.nasl_scores, scores)

# CNNSI data

def scrape_england_cnnsi():
    pass

# World Cup data

# Does not include 2010 World Cup.

def scrape_world_cup_scores():
    from scrapers import fifa
    coll = soccer_db.fifa_world_cup_games
    scores = fifa.scrape_all_world_cup_games()
    delete_rows(coll)
    insert_rows(coll, scores)



def scrape_world_cup_goals():
    from scrapers import fifa
    coll = soccer_db.fifa_world_cup_goals
    goals = fifa.scrape_all_world_cup_goals()
    delete_rows(coll)
    insert_rows(coll, goals)


# Bio data.

def load_mls_bios():
    print "loading bios"
    from text import bios
    coll = soccer_db.chris_bios
    bios = bios.load_bios()
    delete_rows(coll)
    insert_rows(coll, bios)


def load_mls_salaries():
    print "loading salaries"
    from text import salaries
    coll = soccer_db.mls_salaries
    salaries = salaries.load_salaries()
    delete_rows(coll)
    insert_rows(coll, salaries)


def load_mls_drafts():
    from text import drafts
    coll = soccer_db.mls_drafts
    drafts = drafts.load_drafts()
    delete_rows(coll)
    insert_rows(coll, drafts)

def load_scaryice_mls_scores():
    from text import lineups
    coll = soccer_db.scaryice_scores
    scores = lineups.load_all_scores()
    delete_rows(coll)
    insert_rows(coll, scores)

def load_fbleague_scores():
    from scrapers import fbleague
    coll = soccer_db.fbleague_scores
    scores = fbleague.scrape_all_seasons()
    delete_rows(coll)
    insert_rows(coll, scores)

