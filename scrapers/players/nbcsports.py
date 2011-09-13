#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import datetime
from decimal import Decimal
import re
import sys

from abstract import AbstractPlayerScraper


class NBCSportsPlayerScraper(AbstractPlayerScraper):
    FILE_PREFIX = 'nbcsports'
    PLAYER_URL = 'http://scores.nbcsports.msnbc.com/epl/players.asp?player=%s'

    def scrape_player(self, soup):
        bio_masts = soup.findAll("table", {"class": 'shsSportMastHead'})
        if bio_masts:
            bio_mast = bio_masts[0]
        else:
            return {}

        tds = bio_mast.findAll("td", text=True)

        clean_cell = lambda t: unicode(t.replace("&nbsp;", '').replace(":", '').strip())
        cleaned_tds = [clean_cell(e) for e in tds]
        d = dict(zip(cleaned_tds[:-1], cleaned_tds[1:]))

    
        name = unicode(bio_mast.findAll("strong", {"class": 'shsPlayerName'})[0].contents[0])
        if name.endswith("-"):
            name = name[:-1]
            name = clean_cell(name)

        bio = {'name': name}

        if d['Birthdate']:
            bd = d['Birthdate']
            birthdate = datetime.datetime.strptime(bd, '%d/%m/%Y')
            bio['birthdate'] = birthdate

        if d['Birthplace']:
            bio['birthplace'] = d['Birthplace']

        if d['Height']:
            h = d['Height']
            if h.endswith("."): h = h[:-1]
            if h.endswith("m"): h = h[:-1]
            bio['height'] = int(100 * Decimal(h))

        return bio



    def scrape_stats(self, soup):

        keys = ['Year', 'Team', 'MP', 'Min', 'G', 
                'Ast', 'PS', 'SHTS', 'SOG', 
                'YC', 'RC', 'FC', 'FS', 'CR', 'Off']        
        
        tr = soup.findAll("tr", {"class": "shsTableTtlRow"})
        if not tr:
            return

        filter_empty = lambda l: [e.strip() for e in l if e.strip()]
        stat_trs = soup.find('h2', text='Player Stats').parent.nextSibling.findAll("tr")
        header = filter_empty(stat_trs[0].findAll('td', text=True))
        
        stats = []
        for tr in stat_trs[1:-1]:
            s = filter_empty(tr.findAll('td', text=True))
            d = dict(zip(header, s))
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
        
                             
        
    

    

