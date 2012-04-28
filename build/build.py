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
    from soccerdata.alias import get_team, get_name
    from settings import SOURCES
    from soccerdata.mongo import generic_load, soccer_db, insert_rows, insert_row

    # Team names in games.
    for s in SOURCES:
        coll = soccer_db["%s_games" %s]
        l = []
        for e in coll.find():
            e['team1'] = get_team(e['team1'])
            e['team2'] = get_team(e['team2'])
            if e['home_team']:
                e['home_team'] = get_team(e['home_team'])

            l.append(e)

        coll.drop()
        print len(l)
        insert_rows(coll, l)


    for s in SOURCES:
        coll = soccer_db["%s_goals" %s]
        l = []
        for e in coll.find():
            e['team'] = get_team(e['team'])
            try:
                e['goal'] = get_name(e['goal'])
            except:
                import pdb; pdb.set_trace()
            e['assists'] = [get_name(n) for n in e['assists']]

            l.append(e)

        coll.drop()
        print len(l)
        insert_rows(coll, l)


    for s in SOURCES:
        coll = soccer_db["%s_stats" %s]
        l = []
        for e in coll.find():
            e['team'] = get_team(e['team'])
            e['name'] = get_name(e['name'])

            l.append(e)

        coll.drop()
        print len(l)
        insert_rows(coll, l)



    for s in SOURCES:
        coll = soccer_db["%s_lineups" %s]
        l = []
        for e in coll.find():
            e['team'] = get_team(e['team'])
            e['name'] = get_name(e['name'])

            l.append(e)

        coll.drop()
        print len(l)
        insert_rows(coll, l)



    for s in SOURCES:
        coll = soccer_db["%s_standings" %s]
        l = []
        for e in coll.find():
            # NB - weird naming.
            e['name'] = get_team(e['name'])

            l.append(e)

        coll.drop()
        print len(l)
        insert_rows(coll, l)



    for s in SOURCES:
        coll = soccer_db["%s_drafts" %s]
        l = []
        for e in coll.find():
            # NB - weird naming.
            e['team'] = get_team(e['team'])
            e['text'] = get_name(e['text'])

            l.append(e)

        coll.drop()
        print len(l)



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
    print "NORMALIZING"
    normalize()

    # This is where things like standings and stats (not much else) can be generated.
    # Should be relatively simple.
    generate()


    # Merge everything together.
    first_merge()

    # Second pass
    second_merge()

    from soccerdata import mongo


    check()




if __name__ == "__main__":
    build()


