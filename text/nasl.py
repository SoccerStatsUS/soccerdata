

import os

from soccerdata.cache import data_cache

DIR = '/home/chris/www/soccerdata/data/stats'

if not os.path.exists(DIR):
    DIR = "/Users/chrisedgemon/www/soccerdata/data/stats"


filename = os.path.join(DIR, 'nasl.txt')

def process_stats():
    f = open(filename)
    lst = []
    for line in f:

        fields = line.split("  ") # 2 spaces
        fields = [e.strip() for e in fields if e.strip()]
        name, team, goals, assists, shots, yc, rc, minutes = fields
        name = name.split(")")[1].strip()
        lst.append({
                'competition': "North American Soccer League (2011-)",
                'season': '2011',
                'name': name,
                'team': team,
                'goals': int(goals),
                'assists': int(assists),
                'shots': int(shots),
                'yellow_cards': int(yc),
                'red_cards': int(rc),
                'minutes': int(minutes)
                })
                
    return lst



if __name__ == "__main__":
    print process_stats()
