
# Presumably we're going to be sending things into databases from mongo.
# This is how we do it...

import pymongo

connection = pymongo.Connection()

db = connection.soccer

def insert_rows(collection, rows):
    c = db[collection]
    for row in rows:
        c.insert(row)

def get_rows(collection):
    c = db[collection]
    return [row for row in c.find()]


    
