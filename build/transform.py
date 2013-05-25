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

    # Transform team names for a given competition based on the applied formatting string.
    # e.g. United States -> United States U-17.
    transform_team_names_for_competition('fifa', 'FIFA U-17 World Cup', '%s U-17')
    transform_team_names_for_competition('concacaf_i', 'CONCACAF U-17 Championship', '%s U-17')


    transform_team_names_for_competition('fifa', 'FIFA U-20 World Cup', '%s U-20')

    transform_team_names_for_competition('concacaf_i', 'CONCACAF U-20 Championship', '%s U-20')

    transform_team_names_for_competition('concacaf_i', 'CONCACAF Men\'s Olympic Qualifying Tournament', '%s Olympic')

    # Lots of complicated player name transformations that really don't work.


    print("Transforming names.")
    # Comment this out if worried about over-assigning full names.
    #generate_prerosters()
    #transform_player_names() 


    # For whatever reason this isn't working at all currently.
    generate_rosters_from_stats('asl')
    generate_rosters_from_stats('apsl')
    generate_rosters_from_stats('nasl')


    # This is really what you should be using.
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

    tdb = soccer_db['%s_gen_rosters' % source]

    generic_load(tdb, rosters, delete=True)





def get_name_from_fragment(fragment, candidates):
    # Need to figure out how to deal with situations like Willie Reid, W. Reid, W.Reid, Reid
    # It's obvious what should happen here. W. Reid gets turned into Willie Reid, then Reid gets turned into Willie Reid
    # But less obvious how to do it.

    if fragment is None:
        return fragment


    cx = [e for e in candidates if e.endswith(fragment) and e != fragment]

    if len(cx) == 1:
        #print("Converting %s to % s" % (fragment, c2[0]))
        return cx[0]

    elif len(cx) > 1:
        #print("Cannot decide between %s for %s" % (str(c2), fragment))
        return fragment

    else:
        # We've failed to find a match. This may be because we have a situation like W. Reid.
        if fragment.count('.') != 1:
            return fragment

        else:
            f1, f2 = fragment.split('.')
            
            # Presumably there should be more than one match. This is why you would include a first initial at all.
            cx = [e for e in candidates if e.endswith(f2) and e != f2]

            # This is the only case where we want produce a match.
            # right?
            matches = []
            for cd in cx:
                if cd.startswith(f1):
                    matches.append(cd)

            if len(matches) == 1:
                return matches[0]

            # This should never happen.
            elif len(matches) > 1:
                print(fragment, matches)

    return fragment
            

        
        



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


             
    


def transform_names_from_rosters():
    """
    """
    # transform_rosters are rosters that have been generated from stats.

    for source in SOURCES:
        #printsource


        # Try to use independently defined rosters.
        # If that doesn't work, use rosters generated from stats
        rdb = soccer_db['%s_rosters' % source]

        if rdb.count() == 0:
            rdb = soccer_db['%s_gen_rosters' % source]



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



def transform_team_names_for_competition(coll_group, competition, string_format):
    """
    For a given and collection, competition, transform team names based on the give formatting string.
    """

    games = []
    coll = soccer_db["%s_games" % coll_group]
    for e in coll.find():
        if e['competition'] == competition:
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






# NOT IN USE.
# Generate prerosters stuff seems to have been eclipsed by generate_rosters_from_stats.

# Rosters
def generate_prerosters():
    print("Generating all rosters")
    # This is a preliminary roster since player names haven't been normalized and not all stats have been generated.
    # Not using this - it's too blunt of a tool.
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






def make_player_name_guesser():
    # Uses all-time rosters to guess player names for teams.
    # All-time rosters are generated by the generate all-time rosters function?
    
    d = defaultdict(set)
    for e in soccer_db.rosters.find({'end': None, 'start': None}):
        d[e['team']].add(e['name'])

    def getter(name, team):
        candidates = d[team]              
        return get_name_from_fragment(name, candidates)

    return getter




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



# This isn't used.
def transform_name(s, string_format):
    return string_format % s
            
