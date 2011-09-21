import mongo


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


def build():
    """
    Rebuild all site data.
    """
    # Cities
    # Countries
    # Confederations
    # Leagues
    # Competitions
    # Stadiums

    reset_database()
    load()
    generate()
    check()

def load():
    # load
    load_people()
    load_games()
    load_goals()
    load_lineups()
    load_salaries()
    load_drafts()
    load_lists()
    load_stats()

def generate():
    # Generate
    generate_stats()
    generate_transfers()

def check():
    # Verify
    check_goals()
    check_people()
    check_games()
    check_lineups()
    check_stats()


def reset_database():
    """
    Clean up the database.
    """
    pass



# People

def load_people():
    """
    Loads my MLS and USL bios.
    """

    mongo.load_mls_bios()

    # cnnsi bios.
    # wikipedia bios?
    # Might make more sense to load bios after lineups so we have 
    # a pool to load from.


def check_people():
    # Not sure what kind of consistency checking is necessary here.
    pass


# Games

def load_games():
    # below are skipped for testing.
    """
    # General
    mongo.scrape_all_statto()

    # International
    mongo.scrape_world_cup_scores()
    """


    # USA
    mongo.scrape_mls_mlssoccer()
    mongo.scrape_nasl()

    mongo.load_scaryice_mls_scores()

    # Next up.
    mongo.scrape_england_cnnsi()

    # Non-functional.
    return
    mongo.scrape_mls_rsssf()

    # Europe
    mongo.scrape_spain_rsssf()

    # Asia
    mongo.scrape_australia_rsssf()


def check_games():
    pass


# Goals

def load_goals():
    pass
    # International
    # Works.
    #mongo.scrape_world_cup_goals()


def check_goals():
    pass
    

# Lineups 

def load_lineups():
    pass

def check_lineups():
    pass

# Salaries

def load_salaries():
    print "Loading mls salaries."
    mongo.load_mls_salaries()



# Drafts

def load_drafts():
    print "Loading mls drafts."
    mongo.load_mls_drafts()

def load_lists():
    print "Loading lists"
    pass


# Stats

def load_stats():
    pass

def generate_stats():
    pass


def check_stats():
    pass


if __name__ == "__main__":
    build()


