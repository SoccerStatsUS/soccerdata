#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime
import re

from soccerdata.utils import scrape_soup, get_contents


# Want to scrape next round / previous round urls.
# Actually definitely want to do this. Some rounds aren't even in order.


def scrape_all_games():
    # Looks like we've got some metadata that we're not really handling.
    # Need to investigate.
    l = []
    for year, year_id in season_ids:
        l.extend(scrape_year_games(year))
    return l


season_ids = [
    (2007, 97),
    (2008, 135),
    (2009, 155),
    (2010, 173),
    #(2011, 223),
]



def scrape_aleague_game(url):
    pass

def scrape_aleague_goals(url):
    url = 'http://www.footballaustralia.com.au/aleague/matchcentre/matchstats/Melbourne-Victory-FC-v-Melbourne-Heart-FC-Hyundai-A-League/2601'
    soup = scrape_soup(url)
    import pdb; pdb.set_trace()
    goals = []

    home_stats = soup.findAll("div", {'class': 'hometeamplayerstat'})
    away_stats = soup.findAll("div", {'class': 'awayteamplayerstat'})

    pass

def scrape_aleague_lineups(url):
    url = 'http://www.footballaustralia.com.au/aleague/matchcentre/matchstats/Melbourne-Victory-FC-v-Melbourne-Heart-FC-Hyundai-A-League/2601'
    soup = scrape_soup(url)
    import pdb; pdb.set_trace()
    lineups = []



def get_season_id(year):
    """
    Get the a-league.com id for a given year.
    """
    return dict(season_ids)[year]


def scrape_year_games(year):
    """
    Scrape all game data for a given year in the A-league.
    """
    url = 'http://www.a-league.com.au/default.aspx?s=aleague_fixtures&seasonid=%s&roundid=-2' % get_season_id(year)
    soup = scrape_soup(url)
    table = soup.find("table", "fixturetable")

    def preprocess_row(row):
        if row.get('class') == 'daterow':
            td = row.find("td")
            date = get_contents(td)
            return {
                'type': 'date',
                'date': date 
                }

        elif row.get('class'):
            return {}

        tds = row.findAll("td")
        fields = [get_contents(e) for e in tds]

        if len(fields) == 1:
            print row
            return {}

        home_team, away_team, score, location, report, _ = fields
        home_score, away_score = [int(e) for e in score.split("-")]
        return {
            'type': 'game',
            'home_team': home_team,
            'away_team': away_team,
            'home_score': home_score,
            'away_score': away_score,
            'location': location,
            'competition': "A-League",
            'year': year,
            'season': '%s-%s' % (year, year + 1),
            }

    rows = [preprocess_row(row) for row in table.findAll("tr")]
    rows = [e for e in rows if e]
    
    return RowProcessor().process_rows(rows)


class RowProcessor(object):
    """
    Parse semi-structured, ordered rows.
    """
    def __init__(self):
        self.current_date = None
        self.games = []

        

    def process_row(self, row):

        def process_date(s):
            pieces = s.split(" ")

            # Just split up the pieces because hard to match both
            # Match rescheduled from week 11 Tuesday 11 January 2011
            for e in range(len(pieces)):


                s = " ".join(pieces[e:])
                try:
                    return datetime.datetime.strptime(s, "%A %d %B %Y")
                except ValueError:
                    pass

            # No matches, so throw an error..
            print row
            raise



        if row['type'] == 'date':
            self.current_date = process_date(row['date'])

        if row['type'] == 'game':
            row['date'] = self.current_date
            self.games.append(row)

    def process_rows(self, rows):
        for row in rows:
            self.process_row(row)
        return self.games


def scrape_scoreboard():
    scoreboard_url = 'http://www.a-league.com.au/default.aspx?s=aleague_fixtures&seasonid=173&roundid=505'
    score_url = 'http://www.a-league.com.au/Scoreboard_HAL/0000470194/scoreboard.html'


# This is not really necessary.
def get_season_urls(year):

    def get_next_urls(url):
        soup = scrape_soup(url)
        next = soup.find("a", text="Next Round")

        if next:
            next_url = next.parent['href']
            if next_url.startswith("/"):
                next_url = 'http://www.a-league.com.au' + next_url
            try:
                return url + get_next_urls(next_url)
            except:
                import pdb; pdb.set_trace()
        else:
            return [url]

    url = 'http://www.a-league.com.au/default.aspx?s=aleague_fixtures&seasonid=%s' % get_season_id(year)
    return get_next_urls(url)


if __name__ == '__main__':
    scrape_aleague_lineups('')
