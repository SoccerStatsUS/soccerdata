from soccerdata.mongo import generic_load, soccer_db, insert_rows, insert_row

from soccerdata.data.alias import get_team, get_name

from soccerdata.settings import SOURCES

from collections import defaultdict

import random


# Merge should be used for avoiding duplicate elements.


def first_merge():
    merge_standings()
    merge_awards()
    merge_all_stats()
    merge_all_games()

    merge_goals()
    merge_lineups()

    merge_bios()

    merge_teams()
        


def standard_merge(coll):
    from settings import SOURCES

    soccer_db[coll].drop()
    for e in SOURCES:
        insert_rows(soccer_db[coll], soccer_db['%s_%s' % (e, coll)].find())


def merge_teams():
    soccer_db.teams.drop()
    insert_rows(soccer_db.teams, soccer_db.chris_teams.find())
    insert_rows(soccer_db.teams, soccer_db.wiki_teams.find())



def merge_standings():
    standard_merge('standings')


def merge_awards():
    standard_merge('awards')

    return
    soccer_db.awards.drop()
    insert_rows(soccer_db.awards, soccer_db.asl_awards.find())
    insert_rows(soccer_db.awards, soccer_db.nasl_awards.find())
    insert_rows(soccer_db.awards, soccer_db.apsl_awards.find())
    insert_rows(soccer_db.awards, soccer_db.mls_awards.find())
    insert_rows(soccer_db.awards, soccer_db.ncaa_awards.find())
    insert_rows(soccer_db.awards, soccer_db.usl_awards.find())
    insert_rows(soccer_db.awards, soccer_db.asl_awards.find())
    insert_rows(soccer_db.awards, soccer_db.usa_awards.find())

    






    
# Where to have this stuff?
# Needs to be run.
# Maybe add lineup_dict as an argument to correct_goal_names
def make_scaryice_lineup_dict():
    """
    Returns a dict with key/value pairs like this:
    ("FC Dallas", datetime.datetime(2011,8,1)): ["Kevin Hartman", "Jair Benitez"...
    """
    from soccerdata import mongo

    d = defaultdict(list)

    for l in mongo.soccer_db.mls_lineups.find():
        key = (l['team'], l['date'])
        v = d[key]
        v.append(l['player'])

    return d


def merge_goals():

    dd = {}

    def update_goal(d):
        if '_id' in d:
            d.pop("_id")
        
        # normalize things.
        d['team'] = get_team(d['team'])

        if d['goal']:
            d['goal'] = get_name(d['goal'].strip())

        d['assists'] = [get_name(e.strip()) for e in d['assists']]

        # Technically, the same player could score two goals in the
        # same minute. If this ever comes up, I'll have to reconsider
        # this issue.
        if d['minute']:
            key = (d['date'], d['goal'], d['minute'])
        else: 
            # For the case where a player has scored multiple goals, but we don't have a minute for any of them.
            key = (d['date'], d['goal'], random.random())

        if key in dd: 
            orig = dd[key]
            for k, v in d.items():
                if not orig.get(k) and v:
                    orig[k] = v

        # Otherwise, add the game.
        else:
            dd[key] = d

        
    for e in SOURCES:
        c = '%s_goals' % e
        coll = soccer_db[c]
        for e in coll.find():
            update_goal(e)
            
    soccer_db.goals.drop()
    insert_rows(soccer_db.goals, dd.values())

def merge_lineups():

    dd = {}

    def update_lineup(d):
        d.pop("_id")
        
        # normalize things.
        # Do this elsewhere?
        d['name'] = get_name(d['name'])
        d['team'] = get_team(d['team'])

        key = (d['name'], d['date'], d['team'])

        if key in dd: 
            orig = dd[key]
            for k, v in d.items():
                if not orig.get(k) and v:
                    orig[k] = v

        # Otherwise, add the game.
        else:
            dd[key] = d

        
    for e in SOURCES:
        c = '%s_lineups' % e
        coll = soccer_db[c]
        for e in coll.find():
            update_lineup(e)
            
    soccer_db.lineups.drop()
    insert_rows(soccer_db.lineups, dd.values())



def merge_all_games():            
    games_coll_names = ['%s_games' % coll for coll in SOURCES]
    games_lists = [soccer_db[k].find() for k in games_coll_names]

    games = merge_games(games_lists)
    soccer_db.games.drop()
    insert_rows(soccer_db.games, games)


def merge_games(games_lists):
    """
    Merge games to prevent overlaps, then
    insert into the games db.
    """

    def update_game(d):

        if '_id' in d:
            d.pop("_id")
        
        # normalize things.
        d['team1'] = get_team(d['team1'])
        d['team2'] = get_team(d['team2'])

        if d.get('home_team'):
            d['home_team'] = get_team(d['home_team'])

        teams = tuple(sorted([d['team1'], d['team2']]))

        key = (teams, d['date'], d['season'])


        # Add the game if we don't have a match.
        if key not in game_dict:
            game_dict[key] = d


        # If there is already a game, update empty fields.
        else:
            orig = game_dict[key]

            # Overreaction to a bug that was seriously mangling scores when multiple games records were present.
            # (Was replacing scores of 0 with the larger score for both games.)
            t1, t2, t1s, t2s, t1r, t2r = [d.pop(e) for e in ('team1', 'team2', 'team1_score', 'team2_score', 'team1_result', 'team2_result')]
            if t1 == orig['team1'] and t2 == orig['team2']:
                pass
            elif t1 == orig['team2'] and t2 == orig['team1'] and d['date'] is not None: # make allowances for multiple unknown dates...
                t1, t1s, t1r, t2, t2s, t2r = t2, t2s, t2r, t1, t1s, t1r
                try:
                    assert t1s == orig['team1_score']
                    assert t2s == orig['team2_score']
                    assert t1r == orig['team1_result']
                    assert t1r == orig['team1_result']
                except:
                    import pdb; pdb.set_trace()
            else:
                if d['date'] is not None:
                    print "Game information mismatch."
                    print orig
                    print d
                
            for k, v in d.items():
                if not orig.get(k) and v:
                    orig[k] = v

            orig['sources'] = orig.get('sources', []) + d.get('sources', [])

    game_dict = {}

    for games_list in games_lists:
        for e in games_list:
            update_game(e)

    return game_dict.values()

            



def merge_bios():
    """
    Merge bios
    """

    bio_dict = {}


    def update_bio(d):
        # This will produce some bad data, eg: 
        # { 'name': 'John Smith', 'birthdate': datetime.datetime(1900, 1, 1) }
        # merged with  
        # { 'name': 'John Smith', 'birthdate': datetime.datetime(1980, 6, 15), 
        # 'birthplace': 'Atlanta, Georgia' } 
        # will become 
        # { 'name': 'John Smith', 'birthdate': datetime.datetime(1900, 1, 1), 
        # birthplace': 'Atlannta, Georgia' }
        
        name = get_name(d['name'].strip())
        d['name'] = name
        
        if name in bio_dict:
            orig = bio_dict[name]
            for k, v in d.items():
                if not orig.get(k) and v:
                    orig[k] = v
        else:
            bio_dict[name] = d

      
    for e in SOURCES:
        c = '%s_bios' % e
        coll = soccer_db[c]
        for e in coll.find():
            update_bio(e)

    soccer_db.bios.drop()
    insert_rows(soccer_db.bios, bio_dict.values())



def merge_all_stats():            
    stats_coll_names = ['%s_stats' % coll for coll in SOURCES]
    stats_lists = [soccer_db[k].find() for k in stats_coll_names]

    stats = merge_stats(stats_lists)
    soccer_db.stats.drop()
    insert_rows(soccer_db.stats, stats)

    
def merge_stats(stats_lists):
    """
    Merge stats.
    """


    def update_stat(d):
        if 'team' not in d:
            import pdb; pdb.set_trace()
        d['team'] = get_team(d['team'].strip())
        d['name'] = get_name(d['name'].strip())
        t = (d['name'], d['team'], d['competition'], d['season'])
        if t in stat_dict:
            orig = stat_dict[t]
            for k, v in d.items():
                if not orig.get(k) and v:
                    orig[k] = v
        else:
            stat_dict[t] = d



    stat_dict = {}

    for stats_list in stats_lists:
        for e in stats_list:
            update_stat(e)

    return stat_dict.values()





def get_scaryice_goals():
    # Note! scaryice_lineups needs to have been generated alredady for this to work.
    # This is not the right way to do anything.
    from soccerdata.text import lineups


    lineup_dict = make_scaryice_lineup_dict()
    items = [d for d in soccer_db.mls_goals.find()]
    return lineups.correct_goal_names(items, lineup_dict)



if __name__ == "__main__":
    merge()
