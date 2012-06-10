

from soccerdata.mongo import generic_load, soccer_db, insert_rows, insert_row

# This is for fixing errors in data that we can't address otherwise.
# Currently, remove duplicate players from soccernet game reports
# e.g. http://soccernet.espn.go.com/match?id=259398&cc=5901

# Correct team names for U-20, U-17 World Cup
# e.g. United States -> United States U-17



def sanitize_lineups():
    from settings import SOURCES

    l = []

    for s in SOURCES:
        game_set = set()

        coll = soccer_db["%s_standings" %s]

        for e in coll.find():
            t = (e['name'], e['team'], e['date'])
            if t in game_set:
                pass
            else:
                game_set.add(t)
                l.append(e)


def transform_name(s, string_format):
    return string_format % s
            


def transform_names_for_competition(coll_group, competition, string_format):


    games = []
    coll = soccer_db["%s_games" % coll_group]
    for e in coll.find():
        if e['competition'] == competition:
            print "Transforming"

            e['team1'] = string_format % e['team1']
            e['team2'] = string_format % e['team2']

            print e


        games.append(e)

    coll.drop()
    insert_rows(coll, games)



            
    goals = []

    coll = soccer_db["%s_goals" % coll_group]
    for e in coll.find():
        if e['competition'] == competition:
            e['team'] = string_format % e['team']

        goals.append(e)

    insert_rows(coll, goals)

    lineups = []
    coll = soccer_db["%s_lineups" % coll_group]
    for e in coll.find():
        if e['competition'] == competition:
            e['team'] = string_format % e['team']

        lineups.append(e)

    insert_rows(coll, lineups)

    stats = []
    coll = soccer_db['%s_stats' % coll_group]
    for e in coll.find():
        if e['competition'] == competition:
            e['team'] = string_format % e['team']

        stats.append(e)

    insert_rows(coll, stats)


def transform():
    transform_names_for_competition('fifa', 'FIFA U-17 World Cup', '%s U-17')
    transform_names_for_competition('fifa', 'FIFA U-20 World Cup', '%s U-20')

