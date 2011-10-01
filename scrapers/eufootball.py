#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from soccerdata.utils import scrape_soup, get_contents, get_cache, set_cache, remove_cache

import hashlib

# A very impressive site with records of all european national team games ever.
# I think.

match_url = 'http://www.eu-football.info/_match.php?id=1'
year_url = 'http://www.eu-football.info/_year.php?id=2010'


def scrape_all_games():
    import time
    l = []
    for year in range(1872, 2011):
        l.extend(scrape_year(year))
    return l



def scrape_year(year, page=1):

    key = hashlib.md5(unicode((year, page))).hexdigest()
    #games = get_cache(key)
    games = None
    if games is not None:
        return games
        

    if page == 1:
        url = 'http://www.eu-football.info/_year.php?id=%s' % year
    else:
        url = 'http://www.eu-football.info/_year.php?id=%s&page=%s' % (year, page)
    print "Scraping %s" % url
    games = scrape_games(url)
    if games:
        games.extend(scrape_year(year, page+1))

    set_cache(key, games)
    return games
                    


def scrape_games(url):
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

