#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

# Looks to have old premiership scores.

# A lot of nice stuff.
# 

# Starts in 1888.

# http://www.fanbase.com/Arsenal-FC-1926-27/schedule


# Failing
# http://www.fanbase.com/Charlton-Athletic-2009-10/schedule
# http://www.fanbase.com/Luton-Town-2009-10/schedule
# http://www.fanbase.com/Milton-Keynes-Dons-2009-10/schedule
# downloading http://www.fanbase.com/Plymouth-Argyle-2009-10/schedule
# ownloading http://www.fanbase.com/Oldham-Athletic-AFC-2009-10/schedule
# downloading http://www.fanbase.com/Milton-Keynes-Dons-2009-10/schedule


from soccerdata.utils import scrape_soup, get_contents

import re
import time

def scrape_everything():

    def test_team(n):
        for e in ("Be", "FC-Inter", "FC-Porto", "Havant", "Olympique", "Toulouse", "Olympiakos"):
            if n.startswith(e):
                return False
        return True

    def helper(team, year):
        time.sleep(5)
        try:
            scrape_team_year(team, year)
        except Exception, e:
            print e
            print team
            print year
            print

    url1 = 'http://www.fanbase.com/Liverpool-FC-2007-08/schedule'
    url2 = 'http://www.fanbase.com/Arsenal-FC-1989-90/schedule'
    url3 = 'http://www.fanbase.com/Queens-Park-Rangers-FC-2010-11/schedule'

    teams = sorted(set(scrape_teams(url1) + scrape_teams(url2)))
    teams = [e for e in teams if test_team(e)]
    
    for team in teams:
        for year in range(1990, 2010):
            helper(team, year)

def scrape_teams(url):
    soup = scrape_soup(url)
    table = soup.find("table", "schedule full_table")
    trs = table.findAll("tr")[1:]
    
    def find_team_slug(row):
        team_url = row.findAll("td")[3].find("a")['href']
        team_slug = re.search("/(?P<slug>.*?)-\d+", team_url).groups()[0]
        return team_slug
    
    return [find_team_slug(tr) for tr in trs]
        


# Using only for EPL scores.
def scrape_team_year(team, year):

    # Probably the wrong place for this logic.
    if year == 2009:
        slug = team.replace("-FC", "")
    else:
        slug = team
    
    next_year = str(year + 1)[2:]
    season = "%s-%s" % (year, next_year)
    url = 'http://www.fanbase.com/%s-%s/schedule' % (slug, season)
    return scrape_scores(url, team, year)

def scrape_scores(url, team, year):
    soup = scrape_soup(url)
    table = soup.find("table", "schedule full_table")
    trs = table.findAll("tr")[1:]

    def process_row(row):
        tds = row.findAll("td")
        fields = [get_contents(e) for e in tds]
        date, _, homeaway, opponent, result, score = fields
        competition = row.find("img")['alt']

        if score.strip() == '-':
            return {}

        team_score, opponent_score = [int(e) for e in score.split("-")]
        if homeaway == 'vs':
            home_team, away_team = team, opponent
            home_score, away_score = team_score, opponent_score
        elif homeaway == 'at':
            home_team, away_team = opponent, team
            home_score, away_score = opponent_score, team_score

        return {
            'date': date,
            'year': year,
            'competition': competition,
            'home_team': home_team,
            'away_team': away_team,
            'home_score': home_score,
            'away_score': away_score,
            }

    return [process_row(row) for row in trs]


if __name__ == "__main__":
    scrape_team_year("Arsenal-FC", 2005)
    
