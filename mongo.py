
# Presumably we're going to be sending things into databases from mongo.
# This is how we do it...

# Need to check for duplicates!

import datetime

import pymongo

from scrapers import statto

connection = pymongo.Connection()

db = connection.soccer

def insert_row(collection, row):
    c = db[collection]
    c.insert(row)


def insert_rows(collection, rows):
    c = db[collection]
    for row in rows:
        try:
            c.insert(row)
        except:
            import pdb; pdb.set_trace()

def get_rows(collection):
    c = db[collection]
    return [row for row in c.find().sort('date', pymongo.ASCENDING)]


def delete_rows(collection, rows=None):
    c = db[collection]
    if rows is None:
        rows = c.find()
    c = db[collection]
    for row in rows:
        c.remove(row)


def scrape_statto(date):
    rows = statto.process_date(date)
    insert_rows("statto.games", rows)
    # Statto is scraping all possible games for a given date,
    # e.g. 2011-3-21.
    insert_row("statto.games.dates", {"date": date})

def run_statto():
    dates = [e['date'] for e in get_rows('statto.games.dates')]
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

    delete_rows("rsssf-spain-games")
    for year in years:
        rows = spain.process_year(year)
        insert_rows("rsssf-spain-games", rows)


def scrape_mls(years=None):
    from scrapers.rsssf import usa

    if years is None:
        years = range(1996, 2009)

    delete_rows("rsssf-mls-games")
    for year in years:
        rows = usa.process_year(year)
        insert_rows("rsssf-mls-games", rows)


def scrape_nasl():
    from scrapers import nasl
    scores = nasl.scrape_scores()
    delete_rows("nasl-scores")
    insert_rows("nasl-scores", scores)
        

