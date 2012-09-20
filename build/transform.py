from collections import defaultdict

from soccerdata.mongo import generic_load, soccer_db, insert_rows, insert_row

from settings import SOURCES

# This is for fixing errors in data that we can't address otherwise.
# Currently, remove duplicate players from soccernet game reports
# e.g. http://soccernet.espn.go.com/match?id=259398&cc=5901

# Correct team names for U-20, U-17 World Cup
# e.g. United States -> United States U-17


# Rosters
def generate_prerosters():
    print "Generating all rosters"
    # This is a preliminary roster since player names haven't been normalized and not all stats have been generated.
    generic_load(soccer_db.prerosters, generate_all_time_rosters)


def generate_all_time_rosters():
    team_players = defaultdict(set)
    
    for source in SOURCES:
        for e in soccer_db['%s_stats' % source].find():
            team_players[e['team']].add(e['name'])


    for e in soccer_db['%s_lineups' % source].find():
        team_players[e['team']].add(e['name'])
        

    l = []

    for team, names in sorted(team_players.items()):
        for name in sorted(names):
            l.append({
                    'name': name,
                    'team': team,
                    'start': None,
                    'end': None,
                    })
                   
        
    
    return l
        



def make_player_name_guesser():
    # Need to figure out how to deal with situations like Willie Reid, W. Reid, Reid
    # It's obvious what should happen here. W. Reid gets turned into Willie Reid, then Reid gets turned into Willie Reid
    # But less obvious how to do it.
    
    d = defaultdict(set)
    for e in soccer_db.rosters.find({'end': None, 'start': None}):
        d[e['team']].add(e['name'])

    def get_name(fragment, team):

        candidates = d[team]

        c2 = [e for e in candidates if e.endswith(fragment) and e != fragment]

        if len(c2) == 1:
            #print "Converting %s to % s" % (fragment, c2[0])
            return c2[0]


        elif len(c2) > 1:
            print "Cannot decide between %s for %s" % (str(c2), fragment)
            return fragment

        else:
            return fragment
              

        # This will not work - is always True.
        #if fragment in candidates: 
        #    return fragment

    return get_name





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




def transform_player_names():

    full_name_guesser = make_player_name_guesser()

    for source in SOURCES:
        l = []
        coll = soccer_db["%s_goals" % source]
        print coll
        for e in coll.find():
            if e['date']:
                e['goal'] = full_name_guesser(e['goal'], e['team'])

            l.append(e)
        coll.drop()
        insert_rows(coll, l)


    for source in SOURCES:
        l = []
        coll = soccer_db["%s_lineups" % source]
        print coll
        for e in coll.find():
            if e['date']:
                e['name'] = full_name_guesser(e['name'], e['team'])

            l.append(e)
        coll.drop()
        insert_rows(coll, l)


def transform():
    transform_names_for_competition('fifa', 'FIFA U-17 World Cup', '%s U-17')
    transform_names_for_competition('fifa', 'FIFA U-20 World Cup', '%s U-20')

    print "Transforming names."
    generate_prerosters()
    transform_player_names()

