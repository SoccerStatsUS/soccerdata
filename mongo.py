
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
        c.insert(row)

def get_rows(collection):
    c = db[collection]
    return [row for row in c.find()]


def delete_rows(collection, rows):
    if rows is None:
        rows = c.find()
    c = db[collection]
    for row in rows:
        c.remove(row)


def scrape_statto(date):
    rows = statto.process_date(date)
    insert_rows("statto.games", rows)
    insert_row("statto.games.dates", {"date": date})

def run_statto():
    dates = [e['date'] for e in get_rows('statto.games.dates')]
    if dates:
        next_date = min(dates) - datetime.timedelta(days=1)
    else:
        next_date = datetime.datetime.today() - datetime.timedelta(days=1)
    print next_date
    scrape_statto(next_date)
