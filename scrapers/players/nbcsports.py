#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import datetime
from decimal import Decimal
import re
import sys

from abstract import AbstractPlayerScraper

# Are this and cnnsi IDENTICAL???
class NBCSportsPlayerScraper(AbstractPlayerScraper):
    """
    Scrape player data from nbcsports.com.
    """


    FILE_PREFIX = 'nbcsports'
    PLAYER_URL = 'http://scores.nbcsports.msnbc.com/epl/players.asp?player=%s'

    # Actually scrape_player_page?
    def scrape_player(self, soup):
        """
        Returns a dict with a player's name, birthdate, birthplace, and height.
        """

        # Should this just be soup.find?
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
        d = dict(zip(bio_items[:-1], bio_items[1:]))

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
            'height': height
            }

    def scrape_stats(self, soup):

        # possible stats
        keys = [
            'Year', 
            'Team', 
            'MP', 
            'Min', 
            'G', 
            'Ast', 
            'PS', 
            'SHTS', 
            'SOG', 
            'YC', 
            'RC', 
            'FC', 
            'FS', 
            'CR', 
            'Off',
            ]        
        
        tr = soup.findAll("tr", {"class": "shsTableTtlRow"})
        if not tr:
            return []

        filter_empty = lambda l: [e.strip() for e in l if e.strip()]
        stat_trs = soup.find('h2', text='Player Stats').parent.nextSibling.findAll("tr")
        header = filter_empty(stat_trs[0].findAll('td', text=True))
        
        stats = []
        for tr in stat_trs[1:-1]: # Why these?
            s = filter_empty(tr.findAll('td', text=True))
            d = dict(zip(header, s))
            
            # Probably a better way to do this.
            nd = {}
            for k in keys:
                nd[k] = d[k]
            stats.append(nd)
            
        return stats



            
if __name__ == "__main__":
    s = NBCSportsPlayerScraper()
    if len(sys.argv) > 1:
        s.search_profiles(int(sys.argv[1]))
    else:
        s.search_profiles()
        
                             
        
    

    

