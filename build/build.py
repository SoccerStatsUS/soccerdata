
"""
Goal of this package is to completely build all soccer statistics
for the site.

That is to say, import all of them into mongo, and possibly check for consistency.

After that, create canonical lists that can be used for viewing or 
imported into socceroutsider.com for better relationships, etc.


Things that have successfully been built.

people:
 - MLS/USL bios

games:
 - statto
 - fifa world cup

goals:
 - fifa world cup

salaries:
 - mls salaries
"""

from soccerdata import mongo

from load import load
from generate import generate
from check import check
from merge import merge


def build():
    """
    Rebuild all site data.
    """
    reset_database()
    load()
    generate()
    check()
    merge()


def reset_database():
    """
    Drop the old database.
    """
    print "Dropping database."
    mongo.connection.drop_database(mongo.soccer_db)




if __name__ == "__main__":
    build()


