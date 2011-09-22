#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup
import datetime
from decimal import Decimal
import re
import sys
import urllib2

# Try to kill this guy.
from soccerdata.utils import scrape_url, scrape_soup, get_contents


import pymongo

connection = pymongo.Connection()

# Need a better name.
numbers_db = connection.numbers_db


# Search space seems to be sparse so it's probably better to crawl pages looking for links.


def never_stop():
    import time
    import random
    print scrape_player_id(93, "mls")
    while True:
        process_player()
        sleep_time = 60
        print "sleeping for %s seconds" % sleep_time
        time.sleep(sleep_time)

def process_player():
    """
    Logic to slowly scrape a site.
    """
    import time
    import random
    for e in range(5):
        numbers = set(range(1, 200))
        coll = numbers_db.cnnsi_player
        scraped_numbers = set([e['number'] for e in coll.find()])
        unscraped = numbers - scraped_numbers
        next = random.choice(list(unscraped))
        print 'scraping %s' % next
        print scrape_player_id(next, 'mls')
        time.sleep(1)
    
    
def scrape_player_id(player_id, league):
    return scrape_player('http://sports.sportsillustrated.cnn.com/%s/players.asp?player=%s' % (league, player_id))

def scrape_player(url):
    soup = scrape_soup(url)

    bio_masts = soup.findAll("table", {"class": 'shsSportMastHead'})
    if bio_masts:
        bio_mast = bio_masts[0]
    else:
        return {}

    clean_cell = lambda t: unicode(t.replace("&nbsp;", '').replace(":", '').strip())
    
    bio_items = [clean_cell(e) for e in bio_mast.findAll("td", text=True)]

    name = get_contents(bio_mast.find("strong", 'shsPlayerName'))
    if name.endswith("-"):
        name = name[:-1]
    name = clean_cell(name)

    if name == '{PLAYERNAME}':
        return {}

    d = dict(zip(bio_items, bio_items[1:]))

    birthdate = d.get('Birth Date') or d.get('Birthdate') or ''
    if birthdate:
        birthdate = datetime.datetime.strptime(birthdate, '%d/%m/%Y')        
    

    return {
        'url': url,
        'name': name,
        'team': d['Team'],
        'height': d['Height'],
        'birthdate': birthdate,
        'position': d['Position'],
        'weight': d['Weight'],
        'birthplace': d['Birthplace'],
        }

    
    
    





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

    def get_scoreboard_page(self, date, competition):
        """
        Load the scoreboard page 
        """
        url = self.make_url(competition, date)
        html = scrape_url(url)
        return BeautifulSoup(html)


    def process_date(self, date, competition):
        """
        Get the scores from a date.
        """

        soup = self.get_scoreboard_page(date, competition)
        matches = [e.parent for e in soup.findAll("tr", "shsMatchDayRow")]
        box_scores = soup.findAll("tr", "shsOfficialBox")

        def process_score(match, box_score):
            try:
                scores = match.find("td", "shsTotD shsSBScoreTD").contents[0]
            # Need a reason for this exception.
            # And obviously cut this out eventually.
            except:
                import pdb; pdb.set_trace()
            home_score, away_score = scores.split("-")
            home_team = match.find("td", "shsNamD shsHomeTeam").find("a").contents[0]
            away_team = match.find("td", "shsNumD shsAwayTeam").find("a").contents[0]

            url = box_score.previousSibling.find("a")['href']

            return {
                "home_team": home_team,
                "away_team": away_team,
                "home_score": home_score,
                "away_score": away_score,
                "date": date,
                "competition": competition,
                'url': url,
                }

            
        if date >= datetime.date.today():
            return []
        else:
            return [process_score(m, b) for (m, b) in zip(matches, box_scores)]





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


    
            

            

    


if __name__ == "__main__":
    never_stop()
