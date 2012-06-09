#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime
import re

from BeautifulSoup import BeautifulSoup

from soccerdata.utils import scrape_url, get_contents
from soccerdata.cache import data_cache, set_cache

# For scraping all FIFA tournaments!
# There are a lot of them!



# Map years to fifa id's.
world_cup_mapping = {
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





OLD_STYLE_COMPETITIONS = {
    'FIFA Confederations Cup': (101, [4297, 4301, 3424, 4356, 4515, 6489, 8503]),
    'FIFA Club World Cup': (107, [3692, 4735, 248388]),
    'FIFA U-20 World Cup': (104, [191057, 191081, 191109, 191120, 191144, 191161, 191209, 191232, 191252, 191263, 191276, 191313, 4295, 6537, 9102]),
    'FIFA U-17 World Cup': (102, [191425, 191448, 191533, 191544, 191563, 191591, 191606, 3611, 4695, 6946, 9095]),
    }

NEW_STYLE_COMPETITIONS = [
    ('FIFA Club World Cup', 'clubworldcup', ['japan2007', 'japan2008', 'uae2009', 'uae2010']),
]





def scrape_everything(competition):
    tournament_id, edition_ids = OLD_STYLE_COMPETITIONS[competition]
    games = scrape_tournament_games(competition, tournament_id, edition_ids)
    goals = scrape_tournament_goals(competition, tournament_id, edition_ids)
    lineups = scrape_tournament_lineups(competition, tournament_id, edition_ids)
    return (games, goals, lineups)



def scrape_fifa_scoreboard(tournament_id, edition_id):
    """
    Get the game urls for a given year.
    """

    prefix = 'http://www.fifa.com'
    root_url = '/tournaments/archive/tournament=%s/edition=%s/' % (tournament_id, edition_id)
    data = scrape_url(prefix + root_url + "results/index.html")

    # Find urls in the page.
    match_re = re.compile(root_url + "matches/match=\d+/report.html")
    urls = match_re.findall(data)
    return [prefix + e for e in urls]


def scrape_tournament_games(competition_name, tournament_id, edition_ids):
    """
    Scrape game data for all tournaments listed.
    """

    l = []
    for edition_id in edition_ids:
        urls = scrape_fifa_scoreboard(tournament_id, edition_id)
        games = [scrape_fifa_game(url, competition_name) for url in urls]
        l.extend(games)
    return l



def scrape_tournament_goals(competition_name, tournament_id, edition_ids):
    """
    Scrape goal data for all world cups.
    """

    l = []
    for edition_id in edition_ids:
        urls = scrape_fifa_scoreboard(tournament_id, edition_id)
        goals = []
        for url in urls:
            l.extend(scrape_fifa_goals(url, competition_name))
    return l




def scrape_tournament_lineups(competition_name, tournament_id, edition_ids):
    """
    Scrape goal data for all world cups.
    """

    l = []
    for edition_id in edition_ids:
        urls = scrape_fifa_scoreboard(tournament_id, edition_id)
        for url in urls:
            l.extend(scrape_fifa_lineups(url, competition_name))
    return l





# World Cup url formatting is different.
# This can probably be merged with the above functions.

def scrape_world_cup_scoreboard(year):
    """
    Get the game urls for a given year.
    """
    # Replace this with the results logic somehow...

    d = world_cup_mapping[year]
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


        
def scrape_all_world_cup_games():
    """
    Scrape game data for all world cups.
    """

    def scrape_scores_year(year):
        urls = scrape_world_cup_scoreboard(year)
        scores = [scrape_fifa_game(url, 'FIFA World Cup') for url in urls]
        return scores

    l = []
    for year in sorted(world_cup_mapping.keys()):
        l.extend(scrape_scores_year(year))
    return l


def scrape_all_world_cup_goals():
    """
    Scrape goal data for all world cups.
    """
    def scrape_goals_year(year):
        urls = scrape_world_cup_scoreboard(year)
        goals = []
        for url in urls:
            goals.extend(scrape_fifa_goals(url, 'FIFA World Cup'))
        return goals

    l = []
    for year in sorted(world_cup_mapping.keys()):
        l.extend(scrape_goals_year(year))
    return l


def scrape_all_world_cup_lineups():
    """
    Scrape goal data for all world cups.
    """
    def scrape_lineups_year(year):
        urls = scrape_world_cup_scoreboard(year)
        lineups = []
        for url in urls:
            lineups.extend(scrape_fifa_lineups(url, 'FIFA World Cup'))
        return lineups

    l = []
    for year in sorted(world_cup_mapping.keys()):
        l.extend(scrape_lineups_year(year))
    return l



# Generic scraping methods for games, goals, and lineups.


# Seriously do this as soon as possible.
def scrape_fifa_roster(url):
    # Need to figure out what other attributes this needs.
    # e.g. http://www.fifa.com/tournaments/archive/tournament=104/edition=6537/teams/team=1889391.html
    pass
    


@data_cache
def scrape_fifa_game(url, competition):
    """
    Returns a dict with standard game data
    """
    # Need to add referee data.

    data = scrape_url(url)
    data = data.split("<h2>Advertisement</h2>")[0]
    soup = BeautifulSoup(data)
    
    contents = soup.find("div", {"id": "mainContent" })
    
    teams = get_contents(contents.find("div", "bold large teams"))
    home_team, away_team = [e.strip() for e in teams.split("-")]
    score_string = get_contents(contents.find("div", "bold large result"))

    if 'a.e.t.' in score_string:
        score_string = score_string.split('a.e.t')[0]

    home_score, away_score = [int(e) for e in score_string.split("(")[0].split(":")]

    # Implement this if header order is more unpredictable.
    #game_head = contents.findAll("thead")
    #head_teas = game_head.findAll("td", text=True

    game_info = contents.findAll("tbody")[0]
    
    game_tds = game_info.findAll("td", text=True)

    if len(game_tds) == 5:
        match, date_string, time, location, attendance = game_tds

        # In the FIFA Club World Championship 2000 (and likely others, time and location are swapped.
        # Account for this.
        # Could also map tame_tds to game_ths
        if ':' in location:
            time, location = location, time



    elif len(game_tds) == 4:
        date_string, time, location, attendance = game_tds
    else:
        raise

    # Standardize city and stadium fields
    try:
        city, stadium = [e.strip() for e in location.rsplit("/", 1)]
    except:
        import pdb; pdb.set_trace()

    # Avoid duplication of city name?
    if stadium.endswith(city):
        nlocation = stadium
    else:
        nlocation = "%s, %s" % (stadium, city)

    date = datetime.datetime.strptime(date_string.strip(), "%d %B %Y")

    return {
        "team1": unicode(home_team),
        "team2": unicode(away_team),
        'home_team': unicode(home_team),
        'team1_score': home_score,
        'team2_score': away_score,
        'competition': competition,
        'season': unicode(date.year),
        "date": date,
        "location": unicode(nlocation),
        "attendance": unicode(attendance),
        "sources": [url],
        }




@set_cache
def scrape_fifa_goals(url, competition):
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

    goal_re = re.compile("^(?P<name>.*?) \((?P<team>[A-Z]+)\) (?P<minute>\d+)'?")

    game_data = scrape_fifa_game(url, competition)

    l = []

    for s in goals:
        try:
            name, team, minute = goal_re.search(s.strip()).groups()
        except:
            import pdb; pdb.set_trace()
        team = team.strip()
        l.append({
                'team': team,
                'competition': competition,
                'season': game_data['season'],
                'date': game_data['date'],
                'goal': name.strip().title(),


                'minute': int(minute),
                'assists': [],
                'source': url
                })

    return l
    

@set_cache
def scrape_fifa_lineups(url, competition):
    """
    Scrape lineups for a game.
    """
    # Not quite finished.

    data = scrape_url(url)
    data = data.split("<h2>Advertisement</h2>")[0]
    soup = BeautifulSoup(data)

    game_data = scrape_fifa_game(url, competition)

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
                off = 90

            l.append({
                    'name': process_name(name),
                    'on': 0,
                    'off': int(off),
                    'team': team, 
                    'competition': competition,
                    'season': game_data['season'],
                    'date': game_data['date'],
                    'source': url
                    })

        for sub in subs:

            sub = get_contents(sub)

            # Clean up these mysterious dudes.
            # Diego LOPEZ (+69')(-69')
            #m = re.search("(.*?)\(\+(\d+)'\)(\-(\d+)'\)", sub)
            m = False
            if m:
                print "Confusing appearances %s" % sub
                name, _, _ = m.groups()

            m = re.search("(.*?)\(\+(\d+)'\)", sub)
            if m:
                name, on = m.groups()
                off = 90
            else:
                m = re.search("(.*?)\(\-(\d+)'\)", sub)
                if m:
                    name, off = m.groups()
                    on = 90
                else:
                    name = sub
                    on = off = 0

            if m:
                l.append({
                        'name': process_name(name),
                        'on': int(on),
                        'off': off,
                        'team': team, 
                        'competition': competition,
                        'season': game_data['season'],
                        'date': game_data['date'],
                        'source': url
                        })

        return l
            
        number_re = re.compile("\[\d+\]")
        rows = [e for e in rows if e.strip()]
        rows = [e for e in rows if not number_re.search(e)]
        return rows

    home = soup.find("div", "lnupTeam").findAll("span")
    away = soup.find("div", "lnupTeam away").findAll("span")
    
    home_lineup = process_lineup(home, game_data['team1'])
    away_lineup = process_lineup(away, game_data['team2'])

    return home_lineup + away_lineup


if __name__ == "__main__":
    scrape_everything('Confederations Cup')

    
    

    
    
    
    

    
