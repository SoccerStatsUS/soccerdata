# Process Reserve league games, lineup, and goal data; pulled from MLSoccer.com

import datetime
import os
import re

from soccerdata.alias import get_team, get_name

SCORES_PATH = '/home/chris/www/soccerdata/data/scores/reserve.txt'
GOALS_PATH = '/home/chris/www/soccerdata/data/goals/reserve.txt'
MISCONDUCT_PATH = '/home/chris/www/soccerdata/data/misconduct/reserve.txt'
LINEUPS_PATH = '/home/chris/www/soccerdata/data/lineups/reserve.txt'

city_map = {
    'Chicago': 'Chicago Fire',
    'Colorado': 'Colorado Rapids',
    'Columbus': 'Columbus Crew',
    'Dallas': 'FC Dallas',
    'Houston': 'Houston Dynamo',
    'Kansas City': 'Kansas City Wizards',
    'Tampa Bay': 'Tampa Bay Mutiny',
    'Toronto': 'Toronto FC',
    'Miami': 'Miami Fusion',
    'New England': 'New England Revolution',
    'New York': 'New York Red Bulls',
    'Philadelphia': 'Philadelphia Union',
    'San Jose': 'San Jose Earthquakes',
    'Seattle': 'Seattle Sounders',
    'Portland': 'Portland Timbers',
    'Los Angeles': 'Los Angeles Galaxy',
    'Salt Lake': 'Real Salt Lake',    
    'San Joe Earthquakes': 'San Jose Earthquakes',
}

def preprocess(s):
    return s.strip().replace('\xc2', '').replace('\xa0', '')


def process_scores():
    """
    Get reserve game scores.
    """


    f = open(SCORES_PATH)
    l = []
    for row in f:
        row = preprocess(row)

        fields = row.split('\t')
        if len(fields) < 3:
            print fields
        if fields[2] in ('PPD', 'PPD.', ''):
            continue


        if len(fields) == 7:
            date_string, home_team, score, away_team, time, location, url = fields
        else:
            date_string, home_team, score, away_team, time, location = fields

        source = url or ''

        home_team = get_team(home_team, pre_dict=city_map)
        away_team = get_team(away_team, pre_dict=city_map)


        home_score, away_score = [int(e) for e in score.split('-')]
        date_string = '2011 %s' % date_string
        date = datetime.datetime.strptime (date_string, "%Y %d-%b")
        l.append({
                'competition': 'Major League Soccer Reserve League',
                'season': '2011',
                'date': date,
                'location': location,
                'home_team': "%s Reserves" % home_team,
                'away_team': "%s Reserves" % away_team,
                'home_score': home_score,
                'away_score': away_score,
                #'source': url,
                'source': 'http://www.mlssoccer.com/2011-reserve-league',
                })
    return l


def process_goals():
    """
    Get reserve goals.
    """
    f = open(GOALS_PATH)
    l = []
    date = None
    for row in f:
        row = row.strip()
        m = re.match("(\d+)/(\d+)/(\d+)", row)
        if m:
            month, day, year = [int(e) for e in m.groups()]
            date = datetime.datetime(year, month, day)
        else:
            fields = row.strip().split(';')
            minute = fields[-1].split('+')[0]
            try:
                minute = int(minute)
            except:
                print row; continue
            team = get_team(fields[0], pre_dict=city_map)
            other = fields[1:-1]
            goal_type = 'normal'
            if len(other) == 1:
                assists = []
            elif len(other) == 2 and other[1].strip() in('penalty kick', 'own goal'):
                goal_type = other[1].strip()
                assists = []
            else:
                assists = other[1:]

            l.append({
                'competition': 'Major League Soccer Reserve League',
                'season': '2011',
                'date': date,
                'minute': minute,
                'team': "%s Reserves" % team,
                'goal': get_name(other[0].strip()),
                'type': goal_type,
                'assists': [get_name(e.strip()) for e in assists],
                'source': 'http://www.mlssoccer.com/2011-reserve-league',
                })
                
                    
    return l


def process_lineups():
    """
    Get all linup data for MLS reserve league.
    """
    f = open(LINEUPS_PATH)
    lineups = []
    date = None

        
    for row in f:
        row = row.strip()
        if not row:
            continue
            
        m = re.match("(\d+)/(\d+)/(\d+)", row)
        if m:
            month, day, year = [int(e) for e in m.groups()]
            date = datetime.datetime(year, month, day)
        else:    
            fields = row.split(';')
            team = fields[0]
            players = fields[1:]
            for s in players:
                l = process_lineup_string(s, date, team)
                lineups.extend(l)

    for e in lineups:
        e['source'] = 'http://www.mlssoccer.com/2011-reserve-league'

    return lineups




def process_lineup_string(s, date, team):
    """
    Process a lineup item (potentially multiple lineup objects)
    """
    l = [e.strip() for e in s.replace(")", '').split("(")]
    team = "%s Reserves" % get_team(team, pre_dict=city_map)
    start = 0
    lineups = []
    for e in l:
        m = re.match("(.*?)(\d+)", e)
        if not m:
            if not e.strip():
                import pdb; pdb.set_trace()
            
            lineups.append({
                    'name': get_name(e.strip()),
                    'on': 0,
                    'date': date,
                    'team': team,
                    })
        else:
            name = m.groups()[0].strip()
            if not name:
                import pdb; pdb.set_trace()
            on = int(m.groups()[1])
            lineups.append({
                    'name': get_name(name),
                    'on': on,
                    'date': date,
                    'team': team
                    })

    for i, lineup in enumerate(lineups):
        if i == len(lineups) - 1:
            lineup['off'] = 90
        else:
            lineup['off'] = lineups[i+1]['on']

        lineup.update({
                'competition': 'Major League Soccer Reserve League',
                'season': '2011',
                })

    return lineups
        
        
        

            

        



if __name__ == "__main__":
    print process_scores()
    #print process_goals()
    #print process_lineups()


