#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime
import re

from BeautifulSoup import BeautifulSoup

from soccerdata.utils import scrape_url, get_contents
from soccerdata.cache import data_cache, set_cache

# Map years to fifa id's.
mapping = {
    1930: 1,
    1934: 3,
    1938: 5,
    1950: 7,
    1954: 9,
    1958: 15,
    1962: 21,
    1966: 26,
    1970: 32,
    1974: 39,
    1978: 50,
    1982: 59,
    1986: 68,
    1990: 76,
    1994: 84,
    1998: 1013,
    2002: 4395,
    2006: "germany2006",
    }

        

def scrape_all_world_cup_games():
    """
    Scrape game data for all world cups.
    """

    def scrape_scores_year(year):
        urls = scrape_world_cup_game_urls(year)
        scores = [scrape_world_cup_game(url) for url in urls]
        return scores

    l = []
    for year in sorted(mapping.keys()):
        l.extend(scrape_scores_year(year))
    return l

def scrape_all_world_cup_goals():
    """
    Scrape goal data for all world cups.
    """
    def scrape_goals_year(year):
        urls = scrape_world_cup_game_urls(year)
        goals = []
        for url in urls:
            goals.extend(scrape_world_cup_goals(url))
        return goals

    l = []
    for year in sorted(mapping.keys()):
        l.extend(scrape_goals_year(year))
    return l


def scrape_all_world_cup_lineups():
    """
    Scrape goal data for all world cups.
    """
    def scrape_lineups_year(year):
        urls = scrape_world_cup_game_urls(year)
        goals = []
        for url in urls:
            goals.extend(scrape_world_cup_lineups(url))
        return goals

    l = []
    for year in sorted(mapping.keys()):
        l.extend(scrape_lineups_year(year))
    return l

def scrape_world_cup_game_urls(year):
    """
    Get the game urls for a given year.
    """

    d = mapping[year]
    prefix = 'http://www.fifa.com'
    if type(d) == int:
        root_url = '/worldcup/archive/edition=%s/' % d
    else:
        root_url = '/worldcup/archive/%s/' % d
    data = scrape_url(prefix + root_url + "results/index.html")

    # Find urls in the page.
    match_re = re.compile(root_url + "results/matches/match=\d+/report.html")
    urls = match_re.findall(data)
    return [prefix + e for e in urls]


@data_cache
def scrape_world_cup_game(url):
    """
    Returns a dict with world cup data.
    """
    # Consider adding referee data.

    data = scrape_url(url)
    data = data.split("<h2>Advertisement</h2>")[0]
    soup = BeautifulSoup(data)
    
    contents = soup.find("div", {"id": "mainContent" })
    
    teams = get_contents(contents.find("div", "bold large teams"))
    home_team, away_team = teams.split("-")
    
    score_string = get_contents(contents.find("div", "bold large result"))

    if 'a.e.t.' in score_string:
        score_string = score_string.split('a.e.t')[0]

    home_score, away_score = [int(e) for e in score_string.split("(")[0].split(":")]

    game_info = contents.findAll("tbody")[0]
    
    game_tds = game_info.findAll("td", text=True)

    if len(game_tds) == 5:
        match, date_string, time, location, attendance = game_tds
    elif len(game_tds) == 4:
        date_string, time, location, attendance = game_tds
    else:
        raise

    date = datetime.datetime.strptime(date_string.strip(), "%d %B %Y")

    return {
        "home_team": unicode(home_team),
        "away_team": unicode(away_team),
        'home_score': home_score,
        'away_score': away_score,
        'competition': "World Cup",
        'season': date.year,
        "date": date,
        "location": unicode(location),
        "attendance": unicode(attendance),
        "url": url,
        }




@data_cache
def scrape_world_cup_goals(url):
    """
    Returns a list of dicts in standard goal form.
    """

    # Seems the 2006 world cup report is missing some games for sasa ilic.
    goal_replace = {
        u"(SCG) 20',": "Sasa ILIC (SCG) 20',"
        }


    data = scrape_url(url)
    data = data.split("<h2>Advertisement</h2>")[0]
    soup = BeautifulSoup(data)

    goals_div = soup.find("div", text='Goals scored')
    goals = [get_contents(e) for e in goals_div.parent.parent.findAll("li")]
    goals = [goal_replace.get(e, e) for e in goals]

    goal_re = re.compile("^(?P<name>.*?) \((?P<team>[A-Z]+)\) (?P<minute>\d+)'")

    game_data = scrape_world_cup_game(url)

    l = []

    for s in goals:
        name, team, minute = goal_re.search(s.strip()).groups()
        l.append({
                'season': game_data['season'],
                'competition': game_data['competition'],
                'player': name.strip().title(),
                'team': team,
                'date': game_data['date'],
                'minute': minute
                })

    return l
    

@set_cache
def scrape_world_cup_lineups(url):
    """
    Scrape lineups for a game.
    """
    # Not quite finished.

    data = scrape_url(url)
    data = data.split("<h2>Advertisement</h2>")[0]
    soup = BeautifulSoup(data)

    game_data = scrape_world_cup_game(url)

    def process_lineup(rows, team):
        process_name = lambda s: s.strip().replace("(C)", '').replace("(GK)", '').title()

        l = []
        starters = rows[:11]
        subs = rows[11:]

        # Doesn't handle multiple subs yet.
        for starter in starters:
            starter = get_contents(starter)
            
            m = re.search("(.*?)\(-(\d+)'\)", starter)

            if m:
                name, off = m.groups()
            else:
                name = starter
                off = 'end'

            l.append({
                    'player': process_name(name),
                    'on': 0,
                    'off': off,
                    'team': team,
                    'competition': game_data['competition'],
                    'season': game_data['season'],
                    'date': game_data['date'],
                    })

        for sub in subs:
            sub = get_contents(sub)
            m = re.search("(.*?)\(\+(\d+)'\)", sub)
            if m:
                name, on = m.groups()
            else:
                name = sub
                off = 'end' # fix this.

            if m:
                l.append({
                        'player': process_name(name),
                        'on': on,
                        'off': off,
                        'team': team,
                        'competition': game_data['competition'],
                        'season': game_data['season'],
                        'date': game_data['date'],
                        })

        return l
            
        number_re = re.compile("\[\d+\]")
        rows = [e for e in rows if e.strip()]
        rows = [e for e in rows if not number_re.search(e)]
        return rows

    home = soup.find("div", "lnupTeam").findAll("span")
    away = soup.find("div", "lnupTeam away").findAll("span")
    
    home_lineup = process_lineup(home, game_data['home_team'])
    away_lineup = process_lineup(away, game_data['away_team'])

    return home_lineup + away_lineup


if __name__ == "__main__":
    scrape_all_world_cup_games()

    
    

    
    
    
    

    
