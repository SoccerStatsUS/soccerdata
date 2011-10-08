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


def merge_bios():


    def merge_bio(row):
        # Inactive!
        pass


    soccer_db.bios.drop()
    insert_rows(soccer_db.bios, soccer_db.mls_bios.find())

    # Split off into a separate function.
    # merge bios.
    d = dict([(e['name'], e) for e in soccer_db.bios.find()])
    for row in soccer_db.chris_bios.find():
        name = row['name']
        if name in d:
            merge_bio(row)
        else:
            d[name] = row
            insert_row(soccer_db.bios, row)

def merge_stats():

    def _f(d):
        d['team'] = get_team(d['team'])
        d.pop("_id")
        return d


    soccer_db.stats.drop()
    insert_rows(soccer_db.stats, [_f(d) for d in soccer_db.chris_stats.find()])
    #insert_rows(soccer_db.stats, [_f(d) for d in soccer_db.mls_stats.find()])





def merge_games():

    def _f(d):
        d['home_team'] = get_team(d['home_team'])
        d['away_team'] = get_team(d['away_team'])
        d.pop("_id")
        return d

    soccer_db.games.drop()
    insert_rows(soccer_db.games, [_f(d) for d in soccer_db.scaryice_games.find()])


def merge_goals():

    def _f(d):
        d['team'] = get_team(d['team'])
        d.pop("_id")
        return d

    from soccerdata.text import lineups

    soccer_db.goals.drop()

    lineup_dict = make_scaryice_lineup_dict()
    items = [_f(d) for d in soccer_db.scaryice_goals.find()]
    goals = lineups.correct_goal_names(items, lineup_dict)
    insert_rows(soccer_db.goals, goals)


def merge_lineups():

    def _f(d):
        d['team'] = get_team(d['team'])
        d.pop("_id")
        return d


    soccer_db.lineups.drop()
    insert_rows(soccer_db.lineups, [_f(d) for d in soccer_db.scaryice_lineups.find()])







if __name__ == "__main__":
    merge()
