#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime
import json
import re

from soccerdata.utils import scrape_soup, get_contents, scrape_url


# http://a-leaguearchive.tripod.com/2005/results05a.htm

# My stats are USL-1 from 2006-2009, so these scraped data would be perfect.

#
# http://a-leaguearchive.tripod.com/2005/results05a.htm

# Looks like we're missing USL-1 from 2006-2009.



# Woo-hoo! This returns stats json!
# A player bio from somewhere.




def scrape_json_url(url):
    # Preprocess json data.
    # Cause it's not good.
    data = scrape_url(url)
    
    # stats data.
    data = data.replace('players:', '"players":')
    data = data.replace('gk:', '"gk":')

    # Lineups
    data = data.replace("\n", "")
    data = data.replace("\r", "")
    data = re.subn("/\*\w+0*\*/", "", data)[0]

    return data






def parse_scoreboard(url):
    data = scrape_json_url(url)
    data = data.split("=")[1]
    data = data.split(";")[0]

    d = json.loads(data)

    def process_game(game_tuple):
        game_id, game_data = game_tuple

        date_string = game_data['dt']
        date = datetime.datetime.strptime(date_string, '%d-%b-%Y')

        return {
            'game_id': game_id,
            'home_team': game_data['tm1'],
            'away_team': game_data['tm2'],
            'home_score': int(game_data['sc1']),
            'away_score': int(game_data['sc2']),
            'location': game_data['facn'],
            'date': date,
            }

    games = [process_game(e) for e in d.items()]
    return games


def scrape_goals_from_scoreboard(url):
    games = parse_scoreboard(url)

    l = []
    for game in games:
        url = 'http://www.uslsoccer.com/stats/2009/%s.html' % game['game_id']
        goals = process_goals(url)
        l.extend(goals)

    return l


def scrape_lineups_from_scoreboard(url):
    games = parse_scoreboard(url)

    l = []
    for game in games:
        url = 'http://www.uslsoccer.com/stats/2009/%s.html' % game['game_id']
        lineups = process_lineups(url)
        l.extend(lineups)

    return l        


def process_game(url):
    soup = scrape_soup(url, encoding='iso_8859_1', sleep=10)
    tables = soup.findAll("table")

    away_team, home_team = [get_contents(e) for e in tables[7].findAll("a")]
    location, date, time = [get_contents(e).replace("&nbsp;", '').strip() for e in soup.findAll("table")[8].findAll("td")]
    score_text = get_contents(tables[7].find("tr")).replace("&nbsp;", '').split(home_team)[1]
    away_score, home_score = [int(e) for e in score_text.split(":")]

    return {
        'home_team': home_team,
        'away_team': away_team,
        'home_score': home_score,
        'away_score': away_score,
        'date': date,
        'location': location,
        }


def process_goals(url):

    def process_goal(line):
        #non-matching lines
        # MON: David Testo (Joey Gjertsen) 10 (not sure why)


        if not line.strip():
            return {}

        if line.strip() == 'None':
            return {}

        m = re.match("(\w+):\s+(.*?)\s+\((.*?)\)\s+(\d+)", line)
        if m:
            team, goal, assist, minute = m.groups()

        else:
            m = re.match("(\w+):\s+(.*?)\s+(\d+)", line)
            if m:
                team, goal, minute = m.groups()
                assist = None

            else:
                # Probably non-matching.
                print line
                return {}

            

        return {
            'team': team,
            'name': goal,
            'assister': assist,
            'minute': int(minute)
            }

    soup = scrape_soup(url, encoding='iso_8859_1', sleep=10)
    div = soup.find("div", "borderwhite")

    summary = None
    for e in div.contents:
        if "Summary" in get_contents(e):
            summary = unicode(e)

    if summary is None:
        raise

    lines = [e.strip() for e in summary.split("<br />")]

    goals = []
    for line in lines[1:]: # Skip Summary:
        if "Cautions" in line or 'Ejections' in line:
            break
        goals.append(process_goal(line))

    return [e for e in goals if e]


def process_lineups(url):
    soup = scrape_soup(url, encoding='iso_8859_1', sleep=10)
    
    import pdb; pdb.set_trace()

    x = 5
    


# USL-1 urls

# 2009
# http://www.uslsoccer.com/schedules/2009/13380593.html
# http://www.uslsoccer.com/schedules/2009/13380660.js?9228

# 2008
# http://www.uslsoccer.com/schedules/2008/8588667.20086.html

# 2007
# http://www.uslsoccer.com/schedules/2007/6187380.html

# 2006
# http://www.uslsoccer.com/schedules/2006/4068269.html


# 2005
# http://www.uslsoccer.com/schedules/2005/2465825.20058.html

# PDL urls
# All results json:
# 2011
# http://pdl.uslsoccer.com/schedules/2011/33769304.js?2630
# 2010
# http://pdl.uslsoccer.com/schedules/2010/20202833.js?2814
# 2009
# http://www.uslsoccer.com/schedules/2009/13381307.js?0387

# 2008
# http://pdl.uslsoccer.com/scripts/runisa.dll?M2.131326:gp:2049575503.7311:72014+Elements/Display+E+46241++8630281++04/2008+8630213


# Game url:
#http://pdl.uslsoccer.com/stats/2011/2214590.html


# Shit did this already??
def scrape_game_page(url):
    soup = scrape_soup(url, encoding='iso_8859_1')
    div = soup.find("div", {"style": 'border: 1px solid #B0B0B0; background-color: #FFFFFF; padding: 8px;'})    

    text = get_contents(div)
    text = text.replace("&nbsp;", '')
    for e in "Weather", "Attendance", "Summary":
        text = text.replace(e, "")
    text = text.replace("Cautions", ":Cautions:")
    text = text.replace("Referees", ":Referees:")

    data = [e.strip() for e in text.split(":") if e.strip()]

    weather = data[0]
    attendance = data[1]

    goals = []
    for e in data[1:]:
        if e == 'Cautions':
            break
        goals.append(e)


    return {
        'weather': weather,
        'attendance': attendance,
        'goals': goals
        }
    


def scrape_bad(url):
    """
    """
    # uslsoccer.com suggests other urls if you link a bad url.
    soup = scrape_soup(url)
    


    import pdb; pdb.set_trace()

    x = 5

if __name__ == "__main__":
    # bad choice
    #url = 'http://www.uslsoccer.com/stats/2011/2214249.html'
    #scrape_bad(url)
    #json_url = 'http://www.uslsoccer.com/teams/33769235/934451-33769304-stat.js'
    #print scrape_json_url(json_url)

    url2 = 'http://www.uslsoccer.com/schedules/2009/13380660.js?9228'
    #print parse_games(url2)
    print scrape_lineups_from_scoreboard(url2)

    #print scrape_goals_fgame_page('http://www.uslsoccer.com/stats/2005/32094.html')

    #print process_game('http://www.uslsoccer.com/stats/2009/1051806.html')
    #print process_goals('http://www.uslsoccer.com/stats/2009/1051806.html')
