

from soccerdata.utils import scrape_soup, get_contents

import re

# Soccernet is probably the best of all. 
# Triple down on soccernet.


def scrape_scores(soup):
    
    gameboxes = soup.findAll("div", 'gamebox')
    
    def process_game(game):
        data = [get_contents(e) for e in game.findAll("a")]
        home_team, score, away_team = data[:3]

        home_score, away_score = [int(e) for e in  score.replace("&nbsp;", '').split("-")]

        return {
            'home_team': home_team,
            'away_team': away_team,
            'home_score': home_score,
            'away_score': away_score,
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
    print scrape_scores(soup)

