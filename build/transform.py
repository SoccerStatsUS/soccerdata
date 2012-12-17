from collections import defaultdict

from soccerdata.mongo import generic_load, soccer_db, insert_rows, insert_row
from soccerdata.data.alias import get_team

from settings import SOURCES

# This is for fixing errors in data that we can't address otherwise.
# Currently, remove duplicate players from soccernet game reports
# e.g. http://soccernet.espn.go.com/match?id=259398&cc=5901

# Correct team names for U-20, U-17 World Cup
# e.g. United States -> United States U-17



def transform():
    transform_names_for_competition('fifa', 'FIFA U-17 World Cup', '%s U-17')
    transform_names_for_competition('fifa', 'FIFA U-20 World Cup', '%s U-20')

    print "Transforming names."
    #generate_prerosters()

    # For whatever reason this isn't working at all currently.
    generate_rosters_from_stats('asl')
    generate_rosters_from_stats('apsl')

    generate_rosters_from_stats('nasl')

    # Comment this out if worried about over-assigning full names.
    transform_player_names()
    transform_names_from_rosters()


def generate_rosters_from_stats(source):
    rosters = []
    rdb = soccer_db['%s_rosters' % source]    
    if rdb.count():
        return

    sdb = soccer_db['%s_stats' % source]    
    for e in sdb.find():
        rosters.append({
                'name': e['name'],
                'team': get_team(e['team']),
                'competition': e['competition'],
                'season': e['season'],
                })
        #key = (e['name'], e['team'], e['competition'], e['season'])
        #roster_set.add(key)

    tdb = soccer_db['%s_transform_rosters' % source]

    generic_load(tdb, rosters, delete=True)



             
    


def transform_names_from_rosters():

    for source in SOURCES:
        rdb = soccer_db['%s_transform_rosters' % source]
        if rdb.count():

            rg = make_roster_guesser(rdb)

            l = []
            coll = soccer_db["%s_lineups" % source]
            for e in coll.find():
                e['name'] = rg(e['name'], e['team'], e['competition'], e['season'])
                l.append(e)

            coll.drop()
            insert_rows(coll, l)


            g = []
            coll = soccer_db["%s_goals" % source]
            for e in coll.find():
                e['goal'] = rg(e['goal'], e['team'], e['competition'], e['season'])
                g.append(e)

            coll.drop()
            insert_rows(coll, g)





# Rosters
def generate_prerosters():
    print "Generating all rosters"
    # This is a preliminary roster since player names haven't been normalized and not all stats have been generated.
    # Not really using this - it's too blunt of a tool.
    generic_load(soccer_db.prerosters, generate_all_time_rosters)


def generate_all_time_rosters():
    """
    Generate all-time rosters based on stats and lineups.
    """
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



def get_name_from_fragment(fragment, candidates):
    # Need to figure out how to deal with situations like Willie Reid, W. Reid, Reid
    # It's obvious what should happen here. W. Reid gets turned into Willie Reid, then Reid gets turned into Willie Reid
    # But less obvious how to do it.

    if fragment is None:
        return fragment

    try:
        c2 = [e for e in candidates if e.endswith(fragment) and e != fragment]
    except:
        import pdb; pdb.set_trace()

    if len(c2) == 1:
        #print "Converting %s to % s" % (fragment, c2[0])
        return c2[0]

    elif len(c2) > 1:
        #print "Cannot decide between %s for %s" % (str(c2), fragment)
        return fragment

    else:
        return fragment
        

def make_player_name_guesser():
    
    d = defaultdict(set)
    for e in soccer_db.rosters.find({'end': None, 'start': None}):
        d[e['team']].add(e['name'])

    def getter(name, team):
        candidates = d[team]              
        return get_name_from_fragment(name, candidates)

    return getter



def make_roster_guesser(db):
    d = defaultdict(set)
    for e in db.find():
        key = (e['team'], e['competition'], e['season'])
        d[key].add(e['name'])

    def getter(name, team, competition, season):
        key = (team, competition, season)
        candidates = d[key]
        return get_name_from_fragment(name, candidates)

    return getter

        
def sanitize_lineups():
    """
    Some sort of sanity check. Probably shouldn't be here anyway.
    """

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

        games.append(e)

    coll.drop()
    insert_rows(coll, games)

    goals = []
    coll = soccer_db["%s_goals" % coll_group]
    for e in coll.find():
        if e['competition'] == competition:
            e['team'] = string_format % e['team']

        goals.append(e)

    coll.drop()
    insert_rows(coll, goals)

    lineups = []
    coll = soccer_db["%s_lineups" % coll_group]
    for e in coll.find():
        if e['competition'] == competition:
            e['team'] = string_format % e['team']

        lineups.append(e)

    coll.drop()
    insert_rows(coll, lineups)

    stats = []
    coll = soccer_db['%s_stats' % coll_group]
    for e in coll.find():
        if e['competition'] == competition:
            e['team'] = string_format % e['team']

        stats.append(e)

    coll.drop()
    insert_rows(coll, stats)




def transform_player_names():
    """
    Generate full names from rosters, player stats.
    """

    full_name_guesser = make_player_name_guesser()

    for source in SOURCES:
        l = []
        coll = soccer_db["%s_goals" % source]
        for e in coll.find():
            if e['date']:
                e['goal'] = full_name_guesser(e['goal'], get_team(e['team']))

            l.append(e)
        coll.drop()
        insert_rows(coll, l)


    for source in SOURCES:
        l = []
        coll = soccer_db["%s_lineups" % source]
        for e in coll.find():
            if e['date']:
                e['name'] = full_name_guesser(e['name'], get_team(e['team']))

            l.append(e)
        coll.drop()
        insert_rows(coll, l)



            
            
            
