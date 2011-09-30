
from soccerdata.utils import scrape_soup, get_contents

import re


def scrape_live_game(soup):
    score_table = soup.findAll("table")[6]

    home_team = get_contents(score_table.find("td", 'shsTotD shsIFBMastTMName shsHomeTeam'))
    away_team = get_contents(score_table.find("td", 'shsTotD shsIFBMastTMName shsAwayTeam'))

    home_score = int(get_contents(score_table.find('div', 'shsIFBMastHomeScore')))
    away_score = int(get_contents(score_table.find('div', 'shsIFBMastAwayScore')))

    minute_string = get_contents(score_table.find("td", 'shsTotD')).strip()

    if minute_string == 'End of Half':
        minute = 45
    else:
        minute = int(re.search("\((\d+)\'\)", minute_string).groups()[0])


    return {
        'home_team': home_team,
        'away_team': away_team,
        'home_score': home_score,
        'away_score': away_score,
        'minute': minute
        }

def scrape_live_goals(soup):
    goals_table = soup.findAll("table")[7]

    goals = [get_contents(e)for e in goals_table.findAll("tr")]

    # This isn't working.
    def process_goal_line(line):
        name, other = line.split("&nbsp;", 1)
        other = other.replace("&nbsp;", " ")
        minute, score = other.split("'", 1)
        return {
            'name': name,
            'minute': minute,
            }

    return [process_goal_line(e) for e in goals]


def scrape_live_lineups(soup):
    tables = soup.findAll("table")
    home_table = tables[10]
    away_table = tables[12]

    home_players = [get_contents(e) for e in home_table.findAll("a")]
    away_players = [get_contents(e) for e in away_table.findAll("a")]

    return home_players + away_players



if __name__ == "__main__":
    url = 'http://sports.sportsillustrated.cnn.com/mls/boxscore.asp?gamecode=2011092929&season=2011-1'
    soup = scrape_soup(url, refresh=True)
    print scrape_live_game(soup)
    print scrape_live_goals(soup)
    print scrape_live_lineups(soup)


