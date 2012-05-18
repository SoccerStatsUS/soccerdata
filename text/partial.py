import os
import datetime
import re

stats_path = '/home/chris/www/soccerdata/data/stats/partial_stats.csv'


def process_partial_stats():
    l = []
    f = open(stats_path)
    for line in f:
        fields = line.split("\t")
        try:
            name, team, competition, season, games, goals = fields[:6]
        except:
            import pdb; pdb.set_trace()

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
    print process_partial_stats()
            
        
