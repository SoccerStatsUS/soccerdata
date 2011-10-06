#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

# A very impressive site with records of all 
# European national team games ever.

# Need to scrape team games, but they have a stupid access scheme.


from soccerdata.utils import scrape_soup, get_contents
from soccerdata.cache import data_cache, set_cache


def scrape_all_games():
    """
    Scrape all scoreboard data from eufootball.
    """
    # Does not scrape detailed data.

    l = []
    for year in range(1872, 2011):
        l.extend(scrape_year(year))
    return l


@set_cache
def scrape_year(year, page=1):
    """
    Scrape all scoreboards for a given year from eufootball.
    """
    # Probably just convert this to scrape_all_urls function.

    if page == 1:
        url = 'http://www.eu-football.info/_year.php?id=%s' % year
    else:
        url = 'http://www.eu-football.info/_year.php?id=%s&page=%s' % (year, page)
    games = scrape_games(url)
    if games:
        games.extend(scrape_year(year, page+1))

    return games
                    


def scrape_games(url):
    """
    Scrape scoreboard game data.
    """
    soup = scrape_soup(url, encoding='iso_8859_1')

    match_table = soup.findAll("table", {"style": "margin-bottom:4"})[5]
    match_rows = match_table.findAll("tr")[2:]
    
    def process_game(tr):
        fields = [get_contents(e) for e in tr.findAll("td")]



        # Every second and third row looks like this:
        # <tr><td>Kuwait</td></tr>
        # <tr><td title="" class="one sprite-149_1"></td><td valign="bottom"><a href="_team.php?id=149"><b>Norway</b></a></td></tr>
        if len(fields) in [1,2]:
            return {}

        # Pages link at the bottom.
        if u'Pages:' in fields:
            return {}

        if len(fields) == 12:
            _, date, city, _, home_team, _, away_team, _, _, score, competition, _ = fields
        elif len(fields) == 13:
            _, date, city, _, _, home_team, hyphen, away_team, _, _, score, competition, _ = fields
        else:
            import pdb; pdb.set_trace()

        # Need to parse date!


        home_score, away_score = [int(e) for e in score.split(":")]

        import pdb; pdb.set_trace()



        return {
            'date': date,
            'season': '',
            'competition': competition,
            'home_team': home_team,
            'away_team': away_team,
            'home_score': home_score,
            'away_score': away_score,
            }
            
    l = []
    for row in match_rows:
        game = process_game(row)
        if game:
            l.append(game)
    return l


if __name__ == "__main__":
    print scrape_all_games()

