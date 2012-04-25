#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


# Errors:
# http://soccernet.espn.go.com/match?id=289678
# http://soccernet.espn.go.com/match?id=262155
# This one is missing match stats...

import datetime
import re

from collections import defaultdict

from soccerdata.alias import get_team, get_name
from soccerdata.utils import scrape_soup, get_contents
from soccerdata.cache import set_cache, data_cache

easy_cache = data_cache


# Need to set up a way of doing this better.


# Soccernet is probably the best of all.
# Triple down on soccernet.

# Need to focus on this socreboard:
# http://soccernet.espn.go.com/scores?date=20110930&league=all&cc=5901&xhr=1

aliases = {
    # CONCACAF Champions League...
    'Motagua': 'CD Motagua',
    'Olimpia (H)': 'Olimpia',
    'San Fco': 'San Francisco',

    'Chicago': 'Chicago Fire',
    'Colorado': 'Colorado Rapids',
    'Columbus': 'Columbus Crew',
    'Houston': 'Houston Dynamo',
    'Impact de Montreal': 'Montreal Impact',
    'Kansas City': 'Sporting Kansas City',
    'Los Angeles': 'Los Angeles Galaxy',
    'New England': 'New England Revolution',
    'Philadelphia': 'Philadelphia Union',
    'Puerto Rico': 'Puerto Rico Islanders',
    'Salt Lake': 'Real Salt Lake',
    'San Jose': 'San Jose Earthquakes',

    'Seattle': 'Seattle Sounders',
    'Toronto': 'Toronto FC',
    'Vancouver': 'Vancouver Whitecaps',
    }

base = 'http://soccernet.espn.go.com'


def code_to_competition(league_code):
    d = {
        'usa.1': 'Major League Soccer',
        'concacaf.champions': 'CONCACAF Champions League',
        }
    {
        'mex.1': 'Mexico',
        'eng.1': 'Premier League',
        'arg.1': 'Argentina',
        'uefa.champions': 'Champions Leageu',
        'uefa.europa': 'Europa League',
        'conmebol.libertadores': 'Copa Libertadores',
        'ger.1': 'Bundesliga',
        'ita.1': 'Serie A',
        'esp.1': 'La Liga',
        }

    return d[league_code]




def get_match_stats_url(url):
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


# Only returning internally used data.

@easy_cache
def scrape_scoreboard_urls(url):
    """
    Returns a list of game urls for a given scoreboard category, e.g. mls.1
    """

    @easy_cache
    def get_previous_url(url):
        """
        Given a scoreboard, scrape the url for the previous scoreboard.
        Returns an ajax url (unformatted)
        """
        soup = scrape_soup(url, encoding='iso_8859_1', sleep=10)
        urls = [a['href'] for a in soup.findAll("ul")[0].findAll("a")]
        full_url = "%s%s&xhr=1" % (base, urls[0])
        return full_url


    new_url = get_previous_url(url)
    urls = [new_url]
    while new_url:
        new_url = get_previous_url(new_url)
        if new_url in urls:
            return urls
        urls.append(new_url)
    return urls



# Just use these to get urls.
# Don't use for actual game results.
@easy_cache
def scrape_league_scoreboard(url):
    """
    Get game result data from a scoreboard page.
    """
    soup = scrape_soup(url, encoding='iso_8859_1', sleep=10)
    
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
            'url': url
            }

    return [process_game(game) for game in gameboxes]




@easy_cache
def scrape_all_league_scores(league_code):
    """
    Scrape all league game data from scoreboards
    """
    # I recommend not doing this. Probably not going to get correct game info from a scoreboard.

    # A league would be, e.g. usa.1
    # The soccernet league code.

    url = 'http://soccernet.espn.go.com/scores?date=20110930&league=%s&cc=5901&xhr=1' % league_code
    urls = scrape_scoreboard_urls(url)

    games = []
    for url in urls:
        try:
            games.extend(scrape_league_scoreboard(url))
        except:
            print url

    return [e for e in games if e]



@easy_cache
def scrape_all_league_games(league_code):
    competition = code_to_competition(league_code)
    games = []
    for score in scrape_all_league_scores(league_code):
        url = get_match_stats_url(score['url'])
        games.append(scrape_live_game(url, competition))
    return games


@easy_cache
def scrape_all_league_goals(league_code):
    competition = code_to_competition(league_code)
    goals = []
    for score in scrape_all_league_scores(league_code):
        url = get_match_stats_url(score['url'])
        goals.extend(scrape_live_goals(url, competition))
    return goals


@easy_cache
def scrape_all_league_lineups(league_code):
    """
    Scrape all lineups ever for a given competition.
    """
    competition = code_to_competition(league_code)
    l = []
    for score in scrape_all_league_scores(league_code):
        url = get_match_stats_url(score['url'])
        l.extend(scrape_live_lineups(url, competition))
    return l




@easy_cache
def scrape_live_game(url, competition):
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
        season, datetime_string, location = data
        referee = None

    elif len(data) == 4:
        season, datetime_string, location, referee = data
        referee = referee.replace("Referee:", '').strip()

    elif len(data) == 5:
        # The second item is another referee (linesman?)
        season, datetime_string, location, referee, _ = data
        referee = referee.replace("Referee:", '').strip()

        
    else:
        import pdb; pdb.set_trace()


    minute, date_string = datetime_string.split(',', 1)
    date = datetime.datetime.strptime(date_string.strip(), "%B %d, %Y")

    home_team = get_team(home_team, pre_dict=aliases)
    away_team = get_team(away_team, pre_dict=aliases)

    return {
        'team1': home_team,
        'team2': away_team,
        'team1_score': home_score,
        'team2_score': away_score,
        'home_team': home_team,
        'competition': competition,
        'season': str(date.year),
        'date': date,
        'location': location,
        'referee': referee,
        'url': url,
        }


@easy_cache
def scrape_live_goals(url, competition):
    """
    Get goal data from a game page.
    """
    
    game_data = scrape_live_game(url, competition)

    soup = scrape_soup(url, encoding='iso_8859_1', sleep=10)
    container = soup.find("div", 'story-container').find("tbody")
    home_goals = [get_contents(e) for e in container.findAll("td", {"style": "text-align:left;"})]
    away_goals = [get_contents(e) for e in container.findAll("td", {"align": 'right'})]

    def process_goal(s, team):

        # Need to check this for own goals?

        goal_type = 'normal'

        s = s.replace("&nbsp;", '').strip()
        if not s:
            return {}

        m = re.match("(.*?)\((\d+)'\)", s)
        if m:
            player, minute = m.groups()

        m = re.match("(.*?)\(og (\d+)'\)", s)
        if m:
            player, minute = m.groups()
            goal_type = 'own goal'

        m = re.match("(.*?)\(pen (\d+)'\)", s)
        if m:
            player, minute = m.groups()
            goal_type = 'own goal'

        m = re.match("(.*?)\(pen miss (\d+)'\)", s)
        if m:
            return {}


        if player == 'player':
            import pdb; pdb.set_trace()

            
        return {
            'goal': get_name(player),
            'minute': minute,
            'team': get_team(team, pre_dict=aliases),
            'type': goal_type,
            'season': unicode(game_data['date'].year),
            'date': game_data['date'],
            'competition': game_data['competition'],
            'assists': [],
            }

    # Not the best way to handle this now that we've switched away from home/away designations.
    goals = []
    for goal in home_goals:
        gd = process_goal(goal, game_data['team1'])
        if gd:
            goals.append(gd)

    for goal in away_goals:
        gd = process_goal(goal, game_data['team2'])
        if gd:
            goals.append(gd)
        
    return goals


@easy_cache
def scrape_live_lineups(url, competition):
    """
    Scrape a lineup from a game url.
    """
    # Not checking for red cards currently.
    soup = scrape_soup(url, encoding='iso_8859_1', sleep=5)

    game_data = scrape_live_game(url, competition)

    tables = soup.findAll("table")
    

    if len(tables) == 11:
        home_lineup, _, home_subs = tables[1:4]
        away_lineup, _, away_subs = tables[6:9]

    elif len(tables) == 12:
        home_lineup, _, home_subs = tables[2:5]
        away_lineup, _, away_subs = tables[7:10]

    else:
        # Bad game listing.
        # Seems all 2006 New York lineups are missing.
        # e.g. http://soccernet.espn.go.com/match?id=207065&cc=5901
        print "Bad soccernet listing: %s" % url
        return []



    def process_substitutions(subs):
        """
        Returns a dict like {"David Beckham": {"off": 45}, "Ryan Giggs": {"on": 45} }
        """

        d = defaultdict(dict)

        for sub in subs.findAll("tr"):
            tds = sub.findAll("td")
            if tds:
                if get_contents(tds[0]) == u'No Substitutions':
                    return {}

                minute = int(get_contents(tds[0]).replace("'", ''))

                l = [get_contents(e) for e in tds[1].findAll("a")]
                if len(l) == 2:
                    on, off = l
                    
                elif len(l) < 2:
                    s = get_contents(tds[1])
                    on, off = [e.strip() for e in s.split('for', 1)]

                else:
                    import pdb; pdb.set_trace()    
                    

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
                    'name': get_name(player),
                    'on': on,
                    'off': off,
                    'team': get_team(team, pre_dict=aliases),
                    'date': game_data['date'],
                    'season': unicode(game_data['date'].year),
                    'competition': game_data['competition'],
                    })

        return lineup

    la = process_lineup(home_lineup, home_subs, game_data['team1'])
    lb = process_lineup(away_lineup, away_subs, game_data['team2'])

    return la + lb

    
    
def scrape_all_dates():
    """
    Scrape the generic scoreboard for all dates.
    """
    # Not fully implemented; 
    # May be a simpler way of scraping all soccernet scores.

    one_day = datetime.timedelta(days=1)
    today = datetime.date.today()
    d = today
    games = []
    while d > datetime.date(2000, 1, 1):
        try:
            d = d - one_day
            url = 'http://soccernet.espn.go.com/scores?date=%s&league=all&cc=5901&xhr=1' % d.strftime("%Y%m%d")
            g = scrape_general_scoreboard(url)
            print g
            games.extend(g)
        except KeyboardInterrupt:
            raise
        except:
            print "Failed %s" % url
    return games



if __name__ == "__main__":

    leagues = [
        'conmebol.libertadores',
        'uefa.champions',
        'usa.1',
        'uefa.europa',
        'eng.1',
        'bra.1',
        'mex.1',
        'arg.1',
        ]

    #print scrape_all_league_games('concacaf.champions')
    print scrape_all_league_games('usa.1')
    #print scrape_all_league_games('uefa.champions')
    #print scrape_all_league_games('usa.1')
    #print scrape_all_league_games('mex.1')
    #print scrape_bio()
