
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
    return [row for row in collection.find()]


def generic_load(coll, func):
    """
    Call with something like
    
    generic_load(soccer_db.fbleague_scores, fbleague.scrape_all_seasons)
    """
    coll.drop()
    insert_rows(coll, func())



# Statto data
# Statto can only be scraped up to 2008, 1, 1 (or maybe earlier?)



# RSSSF Data

# Move all of these into rsssf modules.

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
