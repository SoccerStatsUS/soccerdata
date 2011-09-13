#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import datetime
from decimal import Decimal
import re
import sys

from abstract import AbstractPlayerScraper

feet2cm = lambda feet, inches: int(round(2.54 * ((12 * feet) + inches)))


num = 46612

class SoccerbasePlayerScraper(AbstractPlayerScraper):
    FILE_PREFIX = 'soccerbase'
    PLAYER_URL = 'http://www.soccerbase.com/players_details.sd?playerid=%s'

    def preprocess_bio_html(self, html):
        return html.replace("scri'+'pt", '').replace("&nbsp;", '')


    def scrape_player(self, soup):
        bio_table = soup.findAll("table")[1]

        if not bio_table:
            return

        format_list = lambda l: [e.strip() for e in l if e != '\n']
        tds = format_list(bio_table.findAll("td", text=True))


        zipped = dict(zip(tds[:-1], tds[1:]))

        bio = {}
        if "Real name" in zipped:
            bio['name'] = zipped['Real name']
        else:
            # Return if there is not a name.
            return {}

        if zipped['Height']:
            hs = zipped['Height']
            try:
                feet, inches = [int(e) for e in hs.split('.')]
            except:
                import pdb; pdb.set_trace()
            bio['height'] = feet2cm(feet, inches)

        if zipped['Date of birth']:
            dob = zipped['Date of birth']
            try:
                bio['birthdate'] = datetime.datetime.strptime(dob, '%d-%m-%Y')
            except ValueError:
                self.LOGGER.error("birthdate failed on %s" % id)

        if zipped['Place of birth']:
            bio['birthplace'] = zipped['Place of birth']

        if zipped['Nationality']:
            bio['nationality'] = zipped['Nationality']

        return bio
    
            
if __name__ == "__main__":
    sp = SoccerbasePlayerScraper()
    if len(sys.argv) > 1:
        sp.search_profiles(int(sys.argv[1]))
    else:
        sp.search_profiles()
