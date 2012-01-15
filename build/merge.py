from soccerdata.mongo import generic_load, soccer_db, insert_rows, insert_row

from soccerdata.alias import get_team, get_name

from soccerdata.settings import SOURCES

from collections import defaultdict


def first_merge():
    merge_standings()
    merge_drafts()
    merge_awards()
    merge_positions()
    merge_bios()
    merge_stats()
    merge_games()
    merge_goals()
    merge_lineups()



def second_merge():
    merge_teams()


def merge_teams():
    soccer_db.teams.drop()
    insert_rows(soccer_db.teams, soccer_db.chris_teams.find())
    insert_rows(soccer_db.teams, soccer_db.wiki_teams.find())



def merge_standings():
    soccer_db.standings.drop()
    insert_rows(soccer_db.standings, soccer_db.chris_standings.find())
    insert_rows(soccer_db.standings, soccer_db.mls_reserve_standings.find())
    insert_rows(soccer_db.standings, soccer_db.open_cup_standings.find())
    insert_rows(soccer_db.standings, soccer_db.concacaf_standings.find())


def merge_drafts():
    soccer_db.drafts.drop()
    insert_rows(soccer_db.drafts, soccer_db.chris_drafts.find())
    insert_rows(soccer_db.drafts, soccer_db.usa_drafts.find())


def merge_awards():
    soccer_db.awards.drop()
    insert_rows(soccer_db.awards, soccer_db.asl_awards.find())
    insert_rows(soccer_db.awards, soccer_db.nasl_awards.find())
    insert_rows(soccer_db.awards, soccer_db.apsl_awards.find())
    insert_rows(soccer_db.awards, soccer_db.mls_awards.find())
    insert_rows(soccer_db.awards, soccer_db.ncaa_awards.find())
    insert_rows(soccer_db.awards, soccer_db.usl_awards.find())
    insert_rows(soccer_db.awards, soccer_db.asl_awards.find())

    

def merge_positions():
    soccer_db.positions.drop()
    insert_rows(soccer_db.positions, soccer_db.chris_positions.find())




def merge_lineups():
    soccer_db.lineups.drop()
    insert_rows(soccer_db.lineups, soccer_db.mls_reserve_lineups.find())
    insert_rows(soccer_db.lineups, soccer_db.mls_lineups.find())
    insert_rows(soccer_db.lineups, soccer_db.fifa_lineups.find())
    insert_rows(soccer_db.lineups, soccer_db.usa_lineups.find())




def merge_goals():
    soccer_db.goals.drop()
    insert_rows(soccer_db.goals, soccer_db.mls_reserve_goals.find())
    insert_rows(soccer_db.goals, soccer_db.mls_goals.find())
    insert_rows(soccer_db.goals, soccer_db.fifa_goals.find())
    insert_rows(soccer_db.goals, soccer_db.usa_goals.find())
    
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

    def update_bio(d):
        name = get_name(d['name'])
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
        if 'team' not in d:
            import pdb; pdb.set_trace()
        d['team'] = get_team(d['team'])
        d['name'] = get_name(d['name'])
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
    from soccerdata.text import lineups


    lineup_dict = make_scaryice_lineup_dict()
    items = [d for d in soccer_db.mls_goals.find()]
    return lineups.correct_goal_names(items, lineup_dict)



if __name__ == "__main__":
    merge()
