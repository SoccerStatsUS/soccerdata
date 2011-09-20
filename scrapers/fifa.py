#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


import re

from BeautifulSoup import BeautifulSoup

from soccerdata.utils import scrape_url, get_contents

url = "http://www.fifa.com/worldcup/archive/edition=84/results/matches/match=3051/report.html"


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



def scrape_world_cup_game_urls(year):
    d = mapping[year]
    prefix = 'http://www.fifa.com'
    if type(d) == int:
        root_url = '/worldcup/archive/edition=%s/' % d
    else:
        root_url = '/worldcup/archive/%s/' % d
    data = scrape_url(prefix + root_url + "results/index.html")

    match_re = re.compile(root_url + "results/matches/match=\d+/report.html")
    urls = match_re.findall(data)
    return [prefix + e for e in urls]

def scrape_scores_year(year):
    urls = scrape_world_cup_game_urls(year)
    competition = "World Cup %s" % year
    scores = [scrape_world_cup_scores(url, competition) for url in urls]
    return scores

def scrape_goals_year(year):
    urls = scrape_world_cup_game_urls(year)
    goals = []
    for url in urls:
        goals.extend(scrape_world_cup_goals(url))
    return goals

def scrape_world_cup_scores(url, competition):
    data = scrape_url(url)
    data = data.split("<h2>Advertisement</h2>")[0]
    soup = BeautifulSoup(data)
    
    contents = soup.find("div", {"id": "mainContent" })
    
    teams = get_contents(contents.find("div", "bold large teams"))
    home_team, away_team = teams.split("-")
    
    score = get_contents(contents.find("div", "bold large result"))

    game_info = contents.findAll("tbody")[0]
    
    game_tds = game_info.findAll("td", text=True)
    if len(game_tds) == 5:
        match, date, time, location, attendance = game_tds
    elif len(game_tds) == 4:
        date, time, location, attendance = game_tds
    else:
        raise

    return {
        "home_team": home_team,
        "away_team": away_team,
        "score": score,
        "date": date,
        "time": time,
        "location": location,
        "attendance": attendance,
        "competition": competition,
        "url": url,
        }


def scrape_world_cup_refs(url):
    # Ugh.
    data = scrape_url(url)
    soup = BeautifulSoup(data)


# Seems the 2006 world cup report is missing some games for sasa ilic.
goal_replace = {
    u"(SCG) 20',": "Sasa ILIC (SCG) 20',"
    }

def scrape_world_cup_goals(url):
    data = scrape_url(url)
    data = data.split("<h2>Advertisement</h2>")[0]
    soup = BeautifulSoup(data)

    goals_div = soup.find("div", text='Goals scored')
    goals = [get_contents(e) for e in goals_div.parent.parent.findAll("li")]
    goals = [goal_replace.get(e, e) for e in goals]

    goal_re = re.compile("^(?P<name>.*?) \((?P<team>[A-Z]+)\) (?P<minute>\d+)'")
    return [goal_re.search(s.strip()).groupdict() for s in goals]
    
    
def scrape_world_cup_lineups(url):
    data = scrape_url(url)
    data = data.split("<h2>Advertisement</h2>")[0]
    soup = BeautifulSoup(data)

    # Just to get home and away team for now.
    # Pass in a dummy competition.
    game = scrape_world_cup_scores(url, '')

    def filter_lineup(rows):
        number_re = re.compile("\[\d+\]")
        rows = [e for e in rows if e.strip()]
        rows = [e for e in rows if not number_re.search(e)]
        return rows

    home = soup.find("div", "lnupTeam")
    away = soup.find("div", "lnupTeam away")

    home2 = filter_lineup(home.findAll("div", 'playerInfo', text=True))
    away2 = filter_lineup(away.findAll("div", 'playerInfo', text=True))

    import pdb; pdb.set_trace()

    

    return []

    
    

    
    
    
    

    
