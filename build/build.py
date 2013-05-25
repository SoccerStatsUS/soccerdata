"""
Goal of this package is to completely build all soccer statistics
for the site.

That is to say, import all of them into mongo, and possibly check for consistency.

After that, create canonical lists that can be used for viewing or 
imported into socceroutsider.com for better relationships, etc.
"""

from load import load
from generate import generate, generate2
from check import check
from merge import merge
from normalize import normalize
from denormalize import denormalize
from transform import transform


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



def build():
    """
    Convert unstructured data (text and web) into structure data in a mongo database.
    Load data, normalize it, 
    """

    for func in load, normalize, transform, generate, merge, generate2, denormalize, check:
        print(func.__name__)
        func()
    
    return


    # Do you want to generate before so that you can use / merge those items normally?
    # Or do you want to generate afterwards so that you can filter things easier?
    load()

    # This is where player, team, competition, and place names are normalized.
    # Best to do this as early as possible.
    print("normalize")
    normalize()

    # e.g. United States -> United States U-17
    # Transform names like Carnihan -> Bill Carnihan if possible.
    # Split names like Arsenal (in Argentina D1) -> Arsenal de Sarandi.
    print("transform")
    transform()

    # This is where things like standings and stats are generated.
    # Generating for individual collections
    print("generate")
    generate()

    # Merge everything together.
    print("merge()")
    merge()

    # Generating standings, stats from merged data; generating indexes on db's.
    print("generate2")
    generate2()

    # Convert names like FC Dallas -> Dallas Burn, e.g. 
    print("denormalize")
    denormalize()
    
    # Check data sanity? not heavily used.
    print("check")
    check()


if __name__ == "__main__":
    build()


