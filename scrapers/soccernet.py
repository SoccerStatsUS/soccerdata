

from soccerdata.utils import scrape_soup, get_contents

import re

# Soccernet is probably the best of all. 
# Triple down on soccernet.

base = 'http://soccernet.espn.go.com'

def create_match_url(url):

    
    m = re.search('id=(\d+)[&$]', url)
    if m:
        url = '%s/match?id=%s' % (base, m.groups()[0])
        return url

    else:
        raise


def scrape_games_from_scoreboard(soup):
    
    games = []
    goals = []
    lineups = []

    for game in scrape_scoreboard(soup):
        url = game['url']
        full_url = create_match_url(url)
        print url
        soup = scrape_soup(full_url, encoding='iso_8859_1', sleep=8)
        games.append(scrape_live_game(soup))
        goals.append(scrape_live_goals(soup))
        #lineups.append(scrape_live_lineups(soup))

    return (games, goals, lineups)



def scrape_scoreboards_from_scoreboard(soup):
    urls = [a['href'] for a in soup.findAll("ul")[0].findAll("a")]
    previous_url = urls[0]
    if previous_url:
        full_url = "%s%s&xhr=1" % (base, previous_url)
        soup = scrape_soup(full_url, encoding='iso_8859_1', sleep=10)
        return [full_url] + scrape_scoreboards_from_scoreboard(soup)
    return [full_url]





# Scrape game pages.

def scrape_scoreboard(soup):
    
    gameboxes = soup.findAll("div", 'gamebox')
    
    def process_game(game):
        data = [get_contents(e) for e in game.findAll("a")]
        home_team, score, away_team = data[:3]

        home_score, away_score = [int(e) for e in  score.replace("&nbsp;", '').split("-")]

        urls = [e['href'] for e in game.findAll("a")]
        game_url = urls[-1]
        
        return {
            'home_team': home_team,
            'away_team': away_team,
            'home_score': home_score,
            'away_score': away_score,
            'url': game_url,
            }

    return [process_game(game) for game in gameboxes]


def scrape_live_game(soup):
    
    home_team, away_team = [get_contents(e) for e in soup.findAll("div", "team-info")]

    score = get_contents(soup.find("p", "matchup-score"))
    home_score, away_score = [int(e) for e in score.replace("&nbsp;", " ").split("-")]

    game_data = soup.find("div", "game-time-location")
    competition, date, location, referee = [get_contents(e) for e in game_data]

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


def scrape_live_goals(soup):
    container = soup.find("div", 'story-container').find("tbody")
    home_goals = [get_contents(e) for e in container.findAll("td", {"style": "text-align:left;"})]
    away_goals = [get_contents(e) for e in container.findAll("td", {"align": 'right'})]
    return home_goals + away_goals


def scrape_live_lineups(soup):
    home_starters = soup.findAll("table")[2]
    home_subs = soup.findAll("table")[3]
    away_starters = soup.findAll("table")[2]
    away_subs = soup.findAll("table")[2]

    import pdb; pdb.set_trace()

    pass


if __name__ == "__main__":
    url = 'http://soccernet.espn.go.com/match?id=314360&cc=5901'
    soup = scrape_soup(url, refresh=True, encoding='iso_8859_1')
    #print scrape_live_game(soup)
    #print scrape_live_goals(soup)
    #print scrape_live_lineups(soup)

    url = 'http://soccernet.espn.go.com/scores/_/league/uefa.europa/uefa-europa-league?cc=5901'
    soup = scrape_soup(url, refresh=True, encoding='iso_8859_1')
    #print scrape_games_from_scoreboard(soup)

    #url = 'http://soccernet.espn.go.com/scores?date=20110915&league=uefa.europa&cc=5901&xhr=1'
    url = 'http://soccernet.espn.go.com/scores?date=20110920&league=conmebol.libertadores&cc=5901&xhr=1'
    url = 'http://soccernet.espn.go.com/scores?date=20111002&league=usa.1&cc=5901&xhr=1'
    soup = scrape_soup(url, encoding='iso_8859_1')
    print scrape_scoreboards_from_scoreboard(soup)
