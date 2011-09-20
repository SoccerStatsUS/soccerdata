
# Presumably we're going to be sending things into databases from mongo.
# This is how we do it...

# Need to check for duplicates!


import datetime
import pymongo

from soccerdata.scrapers import statto


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


def scrape_statto(date):
    rows = statto.process_date(date)
    insert_rows(soccer_db.statto_games, rows)
    # Statto is scraping all possible games for a given date,
    # e.g. 2011-3-21.
    insert_row(soccer_db.statto_games_dates, {"date": date})

def run_statto():
    dates = [e['date'] for e in get_rows(soccer_bd.statto.games.dates)]
    if dates:
        next_date = min(dates) - datetime.timedelta(days=1)
    else:
        next_date = datetime.datetime.today() - datetime.timedelta(days=1)
    print next_date
    scrape_statto(next_date)


def scrape_spain(years=None):
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


def scrape_mls_mlssoccer(years=None):
    from scrapers import mls

    if years is None:
        years = range(1996, 2011)

    delete_rows(soccer_db.mlssoccer_mls_games)
    for year in years:
        rows = mls.scrape_scores(year)
        insert_rows(soccer_db.mlssoccer_mls_games, rows)


def scrape_australia(years=None):
    from scrapers.rsssf import australia

    if years is None:
        years = range(2006, 2012)

    delete_rows(soccer_db.rsssf_australia_games)
    for year in years:
        rows = australia.process_year(year)
        insert_rows(soccer_db.rsssf_australia_games, rows)



def scrape_nasl():
    from scrapers import nasl
    scores = nasl.scrape_scores()
    delete_rows(soccer_db.nasl_scores)
    insert_rows(soccer_db.nasl_scores, scores)
        

