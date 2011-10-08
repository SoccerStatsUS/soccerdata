from soccerdata.mongo import generic_load, soccer_db, insert_rows, insert_row

from soccerdata.alias import get_team

from collections import defaultdict



def merge():
    merge_teams()
    merge_bios()
    merge_stats()
    merge_games()
    merge_goals()
    merge_lineups()




def merge_teams():
    soccer_db.teams.drop()
    insert_rows(soccer_db.teams, soccer_db.yaml_teams.find())



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
        v.append(l['name'])

    return d



def merge_games():

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


    for e in soccer_db.scaryice_games.find():
        update_game(e)
    for e in soccer_db.soccernet_games.find():
        update_game(e)

    soccer_db.games.drop()
    insert_rows(soccer_db.games, game_dict.values())



def merge_bios():
    """
    Merge stats.
    """

    def update_bio(d):
        name = d['name']
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
        t = (d['name'], d['team'], d['competition'], d['season'])
        if t in stat_dict:
            orig = stat_dict[t]
            for k, v in d.items():
                if not orig.get(k) and v:
                    orig[k] = v
        else:
            stat_dict[t] = d



    stat_dict = {}
    for e in soccer_db.mls_stats.find():
        update_stat(e)
    for e in soccer_db.chris_stats.find():
        update_stat(e)

    soccer_db.stats.drop()
    insert_rows(soccer_db.stats, stat_dict.values())




def get_scaryice_goals():
    # Note! scaryice_lineups needs to have been generated alredady for this to work.
    from soccerdata.text import lineups

    def _f(d):
        d['team'] = get_team(d['team'])
        return d

    lineup_dict = make_scaryice_lineup_dict()
    items = [_f(d) for d in soccer_db.scaryice_goals.find()]
    return lineups.correct_goal_names(items, lineup_dict)


def merge_goals():
    """
    Merge stats.
    """


    def update_goal(d):
        d.pop('_id')
        if not d:
            return
        try:
            d['team'] = get_team(d['team'])
        except:
            import pdb; pdb.set_trace()
        try:
            key = (d['player'], d['team'], d['date'], d['minute'])
        except:
            import pdb; pdb.set_trace()
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

    def _f(d):
        d['team'] = get_team(d['team'])
        d.pop("_id")
        return d


    soccer_db.lineups.drop()
    insert_rows(soccer_db.lineups, [_f(d) for d in soccer_db.scaryice_lineups.find()])







if __name__ == "__main__":
    merge()
