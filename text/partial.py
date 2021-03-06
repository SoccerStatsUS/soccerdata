import os
import datetime
import re


from soccerdata.settings import ROOT_DIR

def process_asl2_partial():
    return process_partial_stats(os.path.join(ROOT_DIR, 'asl2-data/stats/asl2'))

def process_apsl_partial():
    return process_partial_stats(os.path.join(ROOT_DIR, 'soccerdata/data/stats/partial/apsl'))

def process_csl_partial():
    return process_partial_stats(os.path.join(ROOT_DIR, 'soccerdata/data/stats/partial/csl'))


def process_partial_stats(p):
    l = []
    f = open(p)
    for line in f:
        fields = line.split("\t")
        try:
            name, team, competition, season, games, goals = fields[:6]
        except:
            import pdb; pdb.set_trace()

        if line.startswith("*"):
            continue

        assists = None
        if len(fields) == 7:
            s = fields[6].strip()
            if s:
                try:
                    assists = int(s)
                except:
                    pass

        if games.strip():
            games = int(games)
        else:
            games = None

        if goals.strip():
            goals = int(goals)
        else:
            goals = None

        l.append({
                'name': name,
                'team': team,
                'competition': competition,
                'season': season,
                'games': games,
                'goals': goals,
                'assists': assists,
                'position': '',
                })

    return l

        

        
if __name__ == "__main__":
    print(process_partial_stats())
            
        
