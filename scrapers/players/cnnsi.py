#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
import datetime
from decimal import Decimal
import re
import sys
import urllib2

from abstract import AbstractPlayerScraper, get_contents

# Not used.
GAME_URL = "http://sports.sportsillustrated.cnn.com/mls/boxscore.asp?gamecode=2010082103&show=pstats&ref="


class CNNSIScoreboardScraper(object):
    """
    Scrape scores form the cnnsi scoreboard.
    """

    def __init__(self):
        pass

    def make_url(self, competition, date):
        """
        Generate a cnnsi scoreboard url for a given competition and date.
        """
        base = "http://sports.sportsillustrated.cnn.com/%s/scoreboard_daily.asp?gameday=%s"
        url_map = {
            "USA": 'mls',
            "Germany": 'bund',
            "England": 'epl',
            "Italy": 'seri',
            "Holland": 'holl',
            "Scotland": 'scot',
            "Mexico": 'fmf',
            "Spain": 'liga',
            }
           
        return base % (url_map[competition], self.format_date(date))

    def format_date(self, date):
        """
        Format the date for the scoreboard url.
        """
        return date.strftime("%Y%m%d")

    def get_date_page(self, date, competition):
        """
        """
        url = self.make_url(competition, date)
        html = urllib2.urlopen(url).read()
        return BeautifulSoup(html)


    def process_date(self, date, competition):
        soup = self.get_date_page(date, competition)
        matches = [e.parent for e in soup.findAll("tr", "shsMatchDayRow")]
        box_scores = soup.findAll("tr", "shsOfficialBox")
        results = []
        for match, box_score in zip(matches, box_scores):
            # Need to handle bad dates anyway...
            if date < datetime.date.today():
                try:
                    scores = match.find("td", "shsTotD shsSBScoreTD").contents[0]
                except:
                    import pdb; pdb.set_trace()
                home_score, away_score = [int(e) for e in scores.strip().split("-")]
                home = match.find("td", "shsNamD shsHomeTeam").find("a").contents[0]
                away = match.find("td", "shsNumD shsAwayTeam").find("a").contents[0]

                url = box_score.previousSibling.find("a")['href']

                d = {
                    "home": home,
                    "away": away,
                    "home_score": home_score,
                    "away_score": away_score,
                    "date": date,
                    "competition": competition,
                    'url': url,
                    }
                results.append(d)

        return results


    
def create_games(date, competition, create=True):
    from soccer.lineups.models import Game, Team
    css = CNNSIScoreboardScraper()
    results = css.process_date(date, competition)
    for result in results:

        import pdb; pdb.set_trace()

        try:
            home_team = Team.objects.get_team(result['home'])
        except:
            #import pdb; pdb.set_trace()
            print result['home']

        try:
            away_team = Team.objects.get_team(result['away'])
        except:
            #import pdb; pdb.set_trace()
            print result['away']

        if create:
            Game.objects.create(
                date=date,
                home_team=home_team,
                away_team=away_team,
                home_score=result['home_score'],
                away_score=result['away_score'],
                competition=result['competition'],
                )
            


def xdaterange(start, end):
    # Does not include end.
    d = start
    while d < end:
        yield d
        d += datetime.timedelta(days=1)


def create_span(start, end, competition, create=True):
    while start < end:
        create_games(start, competition, create)
        start += datetime.timedelta(days=1)


def do_year(year, competition):
    start = datetime.date(year, 1, 1)
    end = datetime.date(year + 1, 1, 1)
    create_span(start, end, competition)


def until_now(competition, create):
    start = datetime.date(2011,8,1)
    end = datetime.date.today() - datetime.timedelta(days=1)
    create_span(start, end, competition, create)

def until_now_all(create=True):
    start = datetime.date(2011,8,1)
    end = datetime.date.today() - datetime.timedelta(days=1)
    for date in xdaterange(start, end):
        try:
            create_all(date, create)
        except:
            print date
    

def create_all(date, create=True):
    leagues = [
        "Germany",
        "England",
        "Italy",
        "Holland",
        "Scotland",
        "Mexico",
        "Spain",
        ]
    for league in leagues:
        create_games(date, league, create)
        



class CNNSIEventScraper(object):
    """
    Scrape events from a url...
    """

    def __init__(self):
        pass

    def get_events(self, url):
        """
        Create a list to fetch the events.
        """
        soup = Soup(urllib2.urlopen(url).read())
        events_div = soup.find("div", "shsEventsContainer")
        events = events_div.findAll("tr",  {'class': ["shsRow1Row", 'shsRow0Row']})

        # Turn this into a helper function.
        l = []
        for event in events:
            r = [get_contents(e) for e in event]
            minute = int(r[1].replace("'", ''))
            description = r[3]
            if "\r\n" in description:
                event, actor = [e.strip() for e in description.split("\r\n") ]
            else:
                event = description.strip()
                actor = ''
            l.append((minute, event, actor))

        return l


    def main(self):
        return self.parse('http://sports.sportsillustrated.cnn.com/epl/boxscore.asp?gamecode=2011091010021&show=events&ref=')


# This is not being used?
def scrape_player_stats(url='http://sports.sportsillustrated.cnn.com/mls/boxscore.asp?gamecode=2011091006&show=pstats&ref='):
    """
    Scrape player stats.
    """
    soup = BeautifulSoup(urllib2.urlopen(url).read())
    # Missing one team's stats.
    player_stats = soup.find('div', {'id': "shsIFBBoxPlayerStats1"})
    rows = player_stats.findAll("tr", {"class": ['shsRow0Row', 'shsRow1Row']})
    
    def process_row(row):
        l = [get_contents(e) for e in row]
        l = [e for e in l if e] # Clean out empty lines.
        number, name, minutes, goals, yellows, reds, allowed, saves = l
        return {
            'number': number,
            'name': name,
            'minutes': minutes,
            'goals': goals,
            'yellows': yellows,
            'reds': reds,
            'allowed': allowed,
            'saves': saves,
            }

    stats =  [process_row(row) for row in rows]

    goals_table = soup.find("table", 'shsGoalScorers')
    goal_anchors = [e.find("a") for e in goals_table.findAll("td", "shsTotD")]
    goal_anchors = [e for e in goal_anchors if e]
    goals = [(e['href'], e.nextSibling.strip()) for e in goal_anchors]

    return {
        'stats': stats,
        'goals': goals,
        }


def get_events(url):
    return CNNSIEventScraper().get_events(url)


class CNNSIPlayerScraper(AbstractPlayerScraper):

    # Should not be a FILE_PREFIX!
    # Dump players into a mongo database.
    # Tag with their source url.

    FILE_PREFIX = 'cnnsi'

    PLAYER_URL = 'http://sports.sportsillustrated.cnn.com/mls/players.asp?player=%s'

    # Actually scrape_player_page?
    def scrape_player(self, soup):
        """
        Returns a dict with a player's name, birthdate, birthplace, and height.
        """

        # If a bio mast doesn't exist, return an empty dict.
        bio_masts = soup.findAll("table", {"class": 'shsSportMastHead'})
        if bio_masts:
            bio_mast = bio_masts[0]
        else:
            return {}

        # Coerce to unicode so it doesn't use a ton of memory.
        # also clean up the text a bit.
        # Why removing the colon?
        clean_cell = lambda t: unicode(t.replace("&nbsp;", '').replace(":", '').strip())

        # NB text = True is a very useful.
        bio_items = [clean_cell(e) for e in bio_mast.findAll("td", text=True)]

        # Layer the list of td's into a dict.
        d = dict(zip(cleaned_tds[:-1], cleaned_tds[1:]))

        birthdate = birthplace = height = None

        name = unicode(bio_mast.findAll("strong", {"class": 'shsPlayerName'})[0].contents[0])
        if name.endswith("-"):
            name = name[:-1]
            name = clean_cell(name)

        if d['Birthdate']:
            bd = d['Birthdate']
            birthdate = datetime.datetime.strptime(bd, '%d/%m/%Y')


        if d['Birthplace']:
            birthplace = d['Birthplace']

        if d['Height']:
            h = d['Height']
            if h.endswith("."): 
                h = h[:-1]
            if h.endswith("m"): 
                h = h[:-1]
            height = int(100 * Decimal(h))

        return {
            'name': name,
            'birthdate': birthdate,
            'birthplace': birthplace,
            'height': height,
            }

    def scrape_stats(self, id):
        # FIXME: This is BROKEN

        # Getting too many stats 
        # Should maybe use a list of keys like nbcsports.

        soup = self.open_bio(id)

        # should be .find?
        tr = soup.findAll("tr", {"class": "shsTableTtlRow"})
        if not tr:
            return []

        header = self.strip_list(tr[0].findAll("td", text=True))

        stats = []
        # These are the classes that contain stat data?
        for tr_class in ['shsRow0Row', 'shsRow1Row']:
            trs = soup.findAll("tr", {"class": tr_class})
            for tr in trs:
                # Whoops this operation isn't working at all!
                numbers = filter_empty(tr.findAll("td", text=True))

                stat = zip(header, numbers)
                stats.append(stat)

        import pdb; pdb.set_trace()
        return stats
                
            

            
if __name__ == "__main__":
    s = CNNSIPlayerScraper()
    if len(sys.argv) > 1:
        s.search_profiles(int(sys.argv[1]))
    else:
        s.search_profiles()
        
                             
        
    

    


