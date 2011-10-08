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



from load import load
from generate import generate
from check import check
from merge import merge


# Load all possible games into various collections.
# Try to merge all of those into a single games database.
# Load standings from wikipedia.

# Generate standings from games.
# Check generated standings against loaded standings.
# Load wikipedia standings for competitions that don't have them.

# Load goals
# Check goals against games.


def build():
    """
    Rebuild all site data.
    """

    #reset_database()

    # Load all data.
    load()

    # Merge is currently putting games into soccer_db.games
    merge()

    # Generate needs to come after merge.
    generate()


def reset_database():
    from soccerdata import mongo
    mongo.connection.drop_database(mongo.soccer_db)




if __name__ == "__main__":
    build()


