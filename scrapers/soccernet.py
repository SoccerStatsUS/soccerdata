#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime
import re

from collections import defaultdict

from soccerdata.utils import scrape_soup, get_contents, get_cache, set_cache

# Soccernet is probably the best of all. 
# Triple down on soccernet.

# Need to focus on this socreboard:
# http://soccernet.espn.go.com/scores?date=20110930&league=all&cc=5901&xhr=1

base = 'http://soccernet.espn.go.com'

def get_match_url(url):
    """
    Get the match url of a different link to a game.
    """
    # This is the match stats url which has subs, goals, etc.
    # Also want to get the player stats url.

    m = re.search('id=(\d+)[&$]', url)
    if m:
        url = '%s/match?id=%s' % (base, m.groups()[0])
        return url

    m = re.search("/_/id/(\d+)$", url)
    if m:
        url = '%s/match?id=%s' % (base, m.groups()[0])
        return url

    else:
        import pdb; pdb.set_trace()
        raise


def scrape_all_league_games(league_code):
    """
    Scrape all league game data.
    Scrape the scoreboards, then scrape individual games.
    """
    # A league would be, e.g. usa.1
    # The soccernet league code.

    url = 'http://soccernet.espn.go.com/scores?date=20110930&league=%s&cc=5901&xhr=1' % league_code
    urls = scrape_all_scoreboards(url)

    games = []
    for url in urls:
        soup = scrape_soup(url, encoding='iso_8859_1', sleep=10)
        try:
            games.extend(scrape_scoreboard(soup))
        except:
            print url


    games =  [e for e in games if e]

    real_games = []
    for game in games:
        url = get_match_url(game['url'])
        real_games.append(scrape_live_game(url))
        try:
            scrape_live_goals(url)
        except:
            import pdb; pdb.set_trace()

        try:
            scrape_live_lineups(url)
        except:
            import pdb; pdb.set_trace()
        

    x = 5
    return real_games


def scrape_all_dates():
    """
    Scrape the generic scoreboard for all dates.
    """
    one_day = datetime.timedelta(days=1)
    today = datetime.date.today()
    d = today
    games = []
    while d > datetime.date(2000, 1, 1):
        try:
            d = d - one_day
            url = 'http://soccernet.espn.go.com/scores?date=%s&league=all&cc=5901&xhr=1' % d.strftime("%Y%m%d")
            soup = scrape_soup(url, encoding='iso_8859_1', sleep=10)
            g = scrape_scoreboard(soup)
            print g
            games.extend(g)
        except KeyboardInterrupt:
            raise
        except:
            print "Failed %s" % url
    return games





def scrape_all_scoreboards(url):
    """
    Returns a list of game urls for a given scoreboard category, e.g. mls.1
    """
    soup = scrape_soup(url, encoding='iso_8859_1', sleep=10)
    new_url = scrape_scoreboard_url_from_scoreboard(soup)
    urls = [new_url ]
    while new_url:
        soup = scrape_soup(new_url, encoding='iso_8859_1', sleep=10)
        new_url = scrape_scoreboard_url_from_scoreboard(soup)
        if new_url in urls:
            return urls
        urls.append(new_url)
    return urls


def scrape_scoreboard_url_from_scoreboard(soup):
    """
    Given a scoreboard, scrape the url for the previous scoreboard.
    Returns an ajax url (unformatted)
    """

    urls = [a['href'] for a in soup.findAll("ul")[0].findAll("a")]
    full_url = "%s%s&xhr=1" % (base, urls[0])
    return full_url



def scrape_scoreboard(soup):
    """
    Get game result data from a scoreboard page.
    """
    
    gameboxes = soup.findAll("div", 'gamebox')
    
    def process_game(game):
        data = [get_contents(e) for e in game.findAll("a")] 
        home_team, score, away_team = data[:3]

        urls = [e['href'] for e in game.findAll("a")]
        url = base + urls[1]


        score = score.replace("&nbsp;", ' ')

        # Game postponed
        if score == "P - P":
            return {}

        if score == 'v':
            return {}

        try:
            home_score, away_score = [int(e) for e in  score.replace("&nbsp;", '').split("-")]
        except:
            print data
            return {}

        return {
            'home_team': home_team,
            'away_team': away_team,
            'home_score': home_score,
            'away_score': away_score,
            'url': url,
            }

    return [process_game(game) for game in gameboxes]


def scrape_live_game(url):
    """
    Get game data from a game page.
    """

    soup = scrape_soup(url, encoding='iso_8859_1', sleep=10)

    
    home_team, away_team = [get_contents(e) for e in soup.findAll("div", "team-info")]
    game_data = soup.find("div", "game-time-location")

    score = get_contents(soup.find("p", "matchup-score"))
    home_score, away_score = [int(e) for e in score.replace("&nbsp;", " ").split("-")]


    data = [get_contents(e) for e in game_data]

    if len(data) == 3:
        competition, datetime_string, location = data
        referee = None

    if len(data) == 4:
        competition, datetime_string, location, referee = data
        referee = referee.replace("Referee:", '').strip()

    minute, date_string = datetime_string.split(',', 1)

    date = datetime.datetime.strptime(date_string.strip(), "%B %d, %Y")


    return {
        'home_team': home_team,
        'away_team': away_team,
        'home_score': home_score,
        'away_score': away_score,
        'competition': competition,
        'date': date,
        'location': location,
        'referee': referee
        }


def scrape_live_goals(url):
    """
    Get goal data from a game page.
    """
    
    game_data = scrape_live_game(url)

    soup = scrape_soup(url, encoding='iso_8859_1', sleep=10)
    container = soup.find("div", 'story-container').find("tbody")
    home_goals = [get_contents(e) for e in container.findAll("td", {"style": "text-align:left;"})]
    away_goals = [get_contents(e) for e in container.findAll("td", {"align": 'right'})]

    def process_goal(s, team):

        # Need to check this for own goals?

        own_goal = penalty = False

        s = s.replace("&nbsp;", '').strip()
        if not s:
            return {}

        m = re.match("(.*?)\((\d+)'\)", s)
        if m:
            player, minute = m.groups()

        m = re.match("(.*?)\(og (\d+)'\)", s)
        if m:
            player, minute = m.groups()
            own_goal = True

        m = re.match("(.*?)\(pen (\d+)'\)", s)
        if m:
            player, minute = m.groups()
            own_goal = True

        m = re.match("(.*?)\(pen miss (\d+)'\)", s)
        if m:
            return {}



        return {
            'player': player,
            'minute': minute,
            'team': team,
            'own_goal': own_goal,
            'penalty': penalty,
            }

    goals = []
    for goal in home_goals:
        gd = process_goal(goal, game_data['home_team'])
        goals.append(gd)

    for goal in away_goals:
        gd = process_goal(goal, game_data['away_team'])
        goals.append(gd)
        
    return goals


def scrape_live_lineups(url):
    soup = scrape_soup(url, encoding='iso_8859_1', sleep=10)

    game_data = scrape_live_game(url)

    tables = soup.findAll("table")

    home_lineup, _, home_subs = tables[2:5]
    away_lineup, _, away_subs = tables[7:10]

    def process_substitutions(subs):

        d = defaultdict(dict)

        for sub in subs.findAll("tr"):
            tds = sub.findAll("td")
            if tds:
                minute = int(get_contents(tds[0]).replace("'", ''))
                on, off = [get_contents(e) for e in tds[1].findAll("a")]
                d[off]['off'] = d[on]['on'] = minute

        return d
            
            


    def process_lineup(lineup, subs, team):
        players = [get_contents(e) for e in lineup.findAll("a")]
        sub_dict = process_substitutions(subs)


        lineup = []

        for player in players:

            if player in sub_dict:
                sub_data = sub_dict[player]
                on = sub_data.get('on', 0)
                off = sub_data.get('off', 90)
            else:
                on = 0
                off = 90

            lineup.append({
                    'player': player,
                    'on': on,
                    'off': off,
                    'team': team
                    })

        return lineup

    l1 = process_lineup(home_lineup, home_subs, game_data['home_team'])
    l2 = process_lineup(away_lineup, away_subs, game_data['away_team'])

    return l1 + l2

    
    
        



if __name__ == "__main__":

    leagues = [
        'uefa.champions',
        'uefa.europa',
        'conmebol.libertadores',
        'usa.1',
        'eng.1',
        'bra.1',
        'mex.1',
        'arg.1',
        ]


    print scrape_all_league_games('usa.1')
    
