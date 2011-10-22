from soccerdata.mongo import generic_load, soccer_db, insert_rows, insert_row

from soccerdata.alias import get_team, get_bio

from collections import defaultdict



def first_merge():
    merge_standings()
    merge_bios()
    merge_stats()
    merge_games()
    merge_goals()
    merge_lineups()


def second_merge():
    merge_teams()


def merge_standings():
    soccer_db.standings.drop()
    insert_rows(soccer_db.standings, soccer_db.chris_standings.find())


def merge_teams():
    soccer_db.teams.drop()
    insert_rows(soccer_db.teams, soccer_db.yaml_teams.find())
    insert_rows(soccer_db.teams, soccer_db.wiki_teams.find())



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

    for l in mongo.soccer_db.scaryice_lineups.find():
        key = (l['team'], l['date'])
        v = d[key]
        v.append(l['player'])

    return d



def merge_games():
    """
    Merge games to prevent overlaps, then
    insert into the games db.
    """

    game_dict = {}

    def update_game(d):
        d.pop("_id")
        d['home_team'] = get_team(d['home_team'])
        d['away_team'] = get_team(d['away_team'])
        key = (d['home_team'], d['away_team'], d['date'])
        if key in game_dict:
            orig = game_dict[key]
            for k, v in d.items():
                if not orig.get(k) and v:
                    orig[k] = v
        else:
            game_dict[key] = d

        
    for e in 'mls', 'scaryice', 'usl', 'apsl', : 
        c = '%s_games' % e
        coll = soccer_db[c]
        for e in coll.find():
            update_game(e)
            
    soccer_db.games.drop()
    insert_rows(soccer_db.games, game_dict.values())



def merge_bios():
    """
    Merge stats.
    """

    def update_bio(d):
        name = get_bio(d['name'])
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

    soccer_db.bios.drop()
    insert_rows(soccer_db.bios, bio_dict.values())



def merge_stats():
    """
    Merge stats.
    """


    def update_stat(d):
        d['team'] = get_team(d['team'])
        d['name'] = get_bio(d['name'])
        t = (d['name'], d['team'], d['competition'], d['season'])
        if t in stat_dict:
            orig = stat_dict[t]
            for k, v in d.items():
                if not orig.get(k) and v:
                    orig[k] = v
        else:
            stat_dict[t] = d



    stat_dict = {}
    for e in soccer_db.nasl_stats.find():
        update_stat(e)
    for e in soccer_db.apsl_stats.find():
        update_stat(e)
    for e in soccer_db.mls_stats.find():
        update_stat(e)
    for e in soccer_db.usl_stats.find():
        update_stat(e)

    soccer_db.stats.drop()
    insert_rows(soccer_db.stats, stat_dict.values())




def get_scaryice_goals():
    # Note! scaryice_lineups needs to have been generated alredady for this to work.
    from soccerdata.text import lineups


    lineup_dict = make_scaryice_lineup_dict()
    items = [d for d in soccer_db.scaryice_goals.find()]
    return lineups.correct_goal_names(items, lineup_dict)


def merge_goals():
    """
    Merge stats.
    """


    def update_goal(d):
        d.pop('_id')
        if not d:
            return
        d['team'] = get_team(d['team'])
        d['player'] = get_bio(d['player'])
        # Presumably no player will score twice in the same minute?
        # When this comes untrue, we have a big problem.
        key = (d['player'], d['team'], d['date'], d['minute'])
        if key in goal_dict:
            orig = goal_dict[key]
            for k, v in d.items():
                if not orig.get(k) and v:
                    orig[k] = v
        else:
            goal_dict[key] = d



    goal_dict = {}
    for e in get_scaryice_goals():
        update_goal(e)
    for e in soccer_db.soccernet_goals.find():
        update_goal(e)

    soccer_db.goals.drop()
    insert_rows(soccer_db.goals, goal_dict.values())



def merge_lineups():
    """
    Merge stats.
    """


    def update_lineup(d):
        d.pop('_id')
        if not d:
            return
        d['team'] = get_team(d['team'])
        d['player'] = get_bio(d['player'])

        try:
            key = (d['player'], d['date'])
        except:
            import pdb; pdb.set_trace()
        if key in lineup_dict:
            orig = lineup_dict[key]
            for k, v in d.items():
                if not orig.get(k) and v:
                    orig[k] = v
        else:
            lineup_dict[key] = d



    lineup_dict = {}
    for e in soccer_db.scaryice_lineups.find():
        update_lineup(e)
    for e in soccer_db.soccernet_lineups.find():
        update_lineup(e)

    soccer_db.lineups.drop()
    insert_rows(soccer_db.lineups, lineup_dict.values())




if __name__ == "__main__":
    merge()
