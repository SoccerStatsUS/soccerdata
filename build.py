import mongo


def build():
    """
    """
    reset_database()

    # Cities
    # Countries
    # Confederations
    # Leagues
    # Competitions
    # Stadiums
    # Teams

    # People
    load_people()
    check_people()

    # Games
    load_games()
    check_games()

    # Goals
    load_goals()
    check_goals()

    # Lineups
    load_lineups()
    check_lineups()

    # Salaries
    load_salaries()

    # Drafts
    load_drafts()

    # Stats
    generate_stats()
    check_stats()





def reset_database():
    """
    Clean up the database.
    """
    pass



def check_games():
    pass


def load_people():
    mongo.load_mls_bios()


def check_people():
    pass


def load_games():
    # General
    mongo.scrape_all_statto()

    # International
    mongo.scrape_world_cup_scores()

    # USA
    mongo.scrape_mls_rsssf()
    mongo.scrape_mls_mlssoccer()
    mongo.scrape_nasl()

    # Europe
    mongo.scrape_spain_rsssf()
    mongo.scrape_england_cnnsi()
    
    # Asia
    mongo.scrape_australia_rsssf()




def load_goals():
    
    # International
    mongo.scrape_world_cup_goals()


def check_goals():
    pass
    

def load_lineups():
    pass

def check_lineups():
    pass


def load_drafts():
    pass

def load_salaries():
    pass


def generate_stats():
    pass


def check_stats():
    pass


