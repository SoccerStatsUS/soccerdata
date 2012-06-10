from soccerdata.mongo import generic_load, soccer_db, insert_rows, insert_row

from soccerdata.data.alias import get_team, get_name

from soccerdata.settings import SOURCES

from collections import defaultdict

import random


# Merge should be used for avoiding duplicate elements.


def first_merge():
    merge_standings()
    merge_awards()
    merge_stats()
    merge_games()

    merge_goals()
    merge_lineups()



def second_merge():
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
        d.pop("_id")
        
        # normalize things.
        d['team'] = get_team(d['team'])
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
        d['name'] = get_name(d['name'])
        d['team'] = get_team(d['team'])

        # Technically, the same player could score two goals in the
        # same minute. If this ever comes up, I'll have to reconsider
        # this issue.

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



def merge_games():
    """
    Merge games to prevent overlaps, then
    insert into the games db.
    """

    game_dict = {}

    def update_game(d):
        d.pop("_id")
        
        # normalize things.
        d['team1'] = get_team(d['team1'])
        d['team2'] = get_team(d['team2'])

        if d['home_team']:
            d['home_team'] = get_team(d['home_team'])

        teams = tuple(sorted([d['team1'], d['team2']]))

        key = (teams, d['date'])

        # If there is already a game, update empty fields.
        if key in game_dict:
            orig = game_dict[key]
            for k, v in d.items():
                if not orig.get(k) and v:
                    orig[k] = v
        # Otherwise, add the game.
        else:
            game_dict[key] = d

        
    for e in SOURCES:
        c = '%s_games' % e
        coll = soccer_db[c]
        for e in coll.find():
            update_game(e)
            
    soccer_db.games.drop()
    insert_rows(soccer_db.games, game_dict.values())





def merge_bios():
    """
    Merge bios
    """
    # Am not using this for now. Eventually it might be useful in bio separation?
    # All bios currently generated together.


    def update_bio(d):
        name = get_name(d['name'].strip())
        d['name'] = name
        
        if name in bio_dict:
            orig = bio_dict[name]
            for k, v in d.items():
                if not orig.get(k) and v:
                    orig[k] = v
        else:
            bio_dict[name] = d

    bio_dict = {}
    for e in soccer_db.mls_bios.find():
        update_bio(e)
    for e in soccer_db.chris_bios.find():
        update_bio(e)

    for e in soccer_db.asl_bios.find():
        update_bio(e)

    soccer_db.bios.drop()
    insert_rows(soccer_db.bios, bio_dict.values())


def merge_stats():
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


    for coll in SOURCES:
        k = '%s_stats' % coll
        for e in soccer_db[k].find():
            update_stat(e)

    soccer_db.stats.drop()
    insert_rows(soccer_db.stats, stat_dict.values())




def get_scaryice_goals():
    # Note! scaryice_lineups needs to have been generated alredady for this to work.
    # This is not the right way to do anything.
    from soccerdata.text import lineups


    lineup_dict = make_scaryice_lineup_dict()
    items = [d for d in soccer_db.mls_goals.find()]
    return lineups.correct_goal_names(items, lineup_dict)



if __name__ == "__main__":
    merge()
