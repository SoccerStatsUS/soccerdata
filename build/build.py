"""
Goal of this package is to completely build all soccer statistics
for the site.

That is to say, import all of them into mongo, and possibly check for consistency.

After that, create canonical lists that can be used for viewing or 
imported into socceroutsider.com for better relationships, etc.
"""

from load import first_load, second_load
from generate import generate
from check import check
from merge import first_merge, second_merge


# Load all possible games into various collections.
# Try to merge all of those into a single games database.

# Generate standings from games.
# Check generated standings against loaded standings.
# Load wikipedia standings for competitions that don't have them.

# Load goals
# Check goals against games.



def reset_database():
    # Not used.
    from soccerdata import mongo
    mongo.connection.drop_database(mongo.soccer_db)


def normalize():
    pass



def build():
    """
    Rebuild all site data.
    """

    # Do you want to generate before so that you can use / merge those items normally?

    # Or do you want to generate afterwards so that you can filter things easier?

    # There should only be one load.
    first_load()

    # This is where player, team, competition, and place names are normalized.
    # Best to do this as early as possible.
    normalize()

    # This is where things like standings and stats (not much else) can be generated.
    # Should be relatively simple.
    generate()


    # Merge everything together.
    first_merge()

    # Second pass
    second_merge()




    check()




if __name__ == "__main__":
    build()


