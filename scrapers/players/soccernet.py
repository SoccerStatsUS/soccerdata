#!/usr/bin/env python

import datetime
from decimal import Decimal
import re
import sys

import urllib2
from BeautifulSoup import BeautifulSoup


from abstract import AbstractPlayerScraper

class SoccernetPlayerScraper(AbstractPlayerScraper):

    # Scraper should only return dicts. No knowledge of what happens after.
    # Scrapers should also apply minimum logic. Mostly keep text values.
    # Try to parse dates? Probably not.
    PLAYER_URL = 'http://soccernet.espn.go.com/player/_/id/%s'
    GAME_URL = 'http://soccernet.espn.go.com/match?id=%s'
    

    def scrape_player(self, soup):
        """
        Returns a dict with a player's name, birthdate, birthplace, and height.
        """


        # Don't need to explicitly say class?
        bio_div = soup.findAll("div", {"class": "profile"})[0]
        bio_li = bio_div.findAll("li")

        name = unicode(bio_div.findAll("h1")[0].contents[0])

        d = {
            'name': name,
            }


        for li in bio_li:
            text = li.contents[0]
        
            # This is pretty ugly.
            # Also seems to overlap the upcoming hasattr.
            try:
                text.startswith("")
            except TypeError:
                continue

            birthplace = birthdate = height
            
            if hasattr(text, 'startswith'):
                if text.startswith("Birth Place"):
                    birthplace = unicode(text.replace("Birth Place:", '').strip())
        
                if text.startswith("Birth Date"):
                    text = text.replace("Birth Date:", '').strip()
                    birthdate = datetime.datetime.strptime(text, '%b %d, %Y')
            
                # Should probably not be parsing things here.
                # Just use the scraper to find data and identify it.
                # e.g. consistently name height, birthplace, birthdate, name, source, etc.
                # Then process them individually afterwards.
                if text.startswith('Height'):
                    text = text.replace("Height:", '').strip()
                    r1 = re.compile("(?P<meters>\d\.\d+)m")
                    r2 = re.compile('.*?\((?P<meters>\d\.\d+)m\)')
                    for regex in (r1, r2):
                        if regex.search(text):
                            meters_s = regex.search(text).groups()[0]
                            meters = Decimal(meters_s)
                            # Height in centimeters.
                            height = int(100 * meters)


        return d

    def id_from_player_href(self, url):
        """
        Extract the player id from a url.
        """
        return re.compile('http://soccernet.espn.go.com/player/_/id/(\d+)/?').search(url).groups()[0]


    def process_goal_record(self, td):
        """
        Process a td goal line.
        """
        # This would probably be better served in the postprocessor.
        # Maybe not. It's the scraper's job to convert from html to structured text.

        child = td.first()
        if not child:
            return {}

        player_href = child['href']
        # Would probably be a good idea to create a giant one of these.
        # Function where you give it a href it returns a player id, or player bio, or whatever.
        player_id = self.id_from_player_href(player_href)
        player_name = child.contents[0]

        # Scored for the home or away team?
        if td.get('style'):
            home = True
        elif td.get('align'):
            home = False
        else:
            # Raise what?
            raise

        # What is td.contents[1]?
        own_goal = 'og' in td.contents[1]
        minute = int(re.search('(\d+)', td.contents[1]).groups()[0])

        return {
            'name': player_name, 
            'id': player_id, 
            'home': home,
            'own_goal': own_goal,
            'minute': minute,
            }

    def process_sub_record(self, tr, home):
        """
        Process a substitution record.
        What minute, who came in, who came out, and whether or not it was the home or the visitor
        """
        # home is unnecessary.
        # Don't need both name and id?

        anchors = tr.findAll("a")
        if not anchors:
            return {}
        
        id_in, id_out = [self.id_from_player_href(e['href']) for e in anchors]
        name_in, name_out = [e.contents[0] for e in anchors]
        minute_s = tr.findAll('td')[0].contents[0]

        minute = int(minute_s.replace('\'', ''))

        return {
            'minute': minute,
            'in': (id_in, name_in),
            'out': (id_out, name_out),
            'home': home,
            }

    def process_red_card(self, tr, home):
        """
        Returns a dict with the name, id, and minute of the red card event.
        """
        
        anchors = tr.findAll('a')
        if not anchors:
            return {}
        
        a = anchors[0]
        sub_id = self.id_from_player_href(a['href'])
        sub_name = a.contents[0]

        # Try to figure out the minute.
        minute_s = tr.contents[0].contents[0]
        minute = int(minute_s.replace('\'', ''))
        
        return {
            'name': sub_name,
            'id': sub_id,
            'minute': minute,
            }


    def scrape_game(self, id):
        """
        Returns a dict with relevant information about the result of a game.
        """
        # I think I want to get rid of this.
        # I want to destructure the data so that goals, lineups, and events are not
        # contained within the game or even explictily linked to it. That data can
        # be determined later when the parsed data is put into a relational db.

        # Move these sections into helper methods, then eliminate scrape game.

        soup = self.open_game_page(id)
        summary = soup.findAll("div", {'class': 'summary-tabs-container'})

        if not summary:
            return {}

        # Get game info
        game_info = soup.find("div", {"class": 'game-time-location'})
        comp, d, location = [e.contents[0] for e in game_info.findAll('p')]
        
        dt = datetime.datetime.strptime(d, '%H:%M GMT, %B %d, %Y')
        
        # Get the name of the competition (e.g. Premier League)
        competition = soup.findAll("a", {"class": 'section-title'})[0]
        competition_name = competition.contents[0]
        competition_href = competition['href']

        # Get the score of the game
        score_s = soup.findAll("p", {'class': 'matchup-score'})[0].contents[0].strip()
        home_score, away_score = [int(e) for e in score_s.split('-')]

        # Get the individual gal records.
        team_url_parser = re.compile('^http://soccernet.espn.go.com/team/_/team/(\d+)')
        anchor_hrefs = [e['href'] for e in summary[0].findAll("a", {'class': 'team-link'})]
        team_ids = [team_url_parser.search(e).groups()[0] for e in anchor_hrefs]
        scoring_summary = soup.findAll(text="Scoring Summary")[0].parent.parent.parent
        scoring_tds = scoring_summary.findAll('td')
        goals = filter(bool, [self.process_goal_record(e) for e in scoring_tds])

        # Make sure the goal records are equivalent to the score.
        assert len([e for e in goals if e['home']]) == home_score
        assert len([e for e in goals if not e['home']]) == away_score

        # Get lineups
        format_lineup = lambda l: [(self.id_from_player_href(e['href']), e.contents[0]) for e in l]
        lineups = [format_lineup(e.findAll('a')) for e in soup.findAll("div", {'class': 'matchBody'})]

        # Get substitutions
        substitution_text = soup.findAll(text=re.compile('\w*Substitutions\w*'))
        substitution_divs = [e.parent.parent.parent.parent for e in substitution_text]
        get_subs = lambda div, home: [self.process_sub_record(tr, home) for tr in div.findAll("tr")]
        substitutions = get_subs(substitution_divs[0], True)
        substitutions.extend(get_subs(substitution_divs[1], False))
        substitutions = [e for e in substitutions if e]

        # Get Red Cards
        red_card_text = soup.findAll(text=re.compile('\w*Red Cards\w*'))[1:]
        red_card_divs = [e.parent.parent.parent.parent for e in red_card_text]
        get_red_cards = lambda div, home: [self.process_red_card(tr, home) for tr in div.findAll('tr')]
        red_cards = get_red_cards(red_card_divs[0], True)
        red_cards.extend(get_red_cards(red_card_divs[1], False))
        red_cards = [e for e in red_cards if e]

        return {
            'datetime': dt,
            'location': location,
            'competition': competition,
            'team_ids': team_ids,
            'goals': goals,
            'lineups': lineups,
            'substitutions': substitutions,
            'red_cards': red_cards,
            }
    




# This currently isn't working...
def process_game_stats(url):
    text = urllib2.urlopen(url)
    soup = BeautifulSoup(text)
    div = soup.find("div", {"id": "statsDiv"})
    
    odds = soup.findAll("tr", {"class": "oddrow"})
    evens = soup.findAll("tr", {"class": "evenrow"})
    
    stats = []
    for e in odds + evens:
        stats.append([get_contents(x) for x in e.findAll("td")])

    return stats


            
if __name__ == "__main__":
    sp = SoccernetPlayerScraper()
    if len(sys.argv) > 1:
        sp.search_profiles(int(sys.argv[1]))
    else:
        sp.search_profiles()
