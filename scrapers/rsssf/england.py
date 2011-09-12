#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


# Hopefully the same as spain.py

from base import RSSSFParser


# Early english results could probably be scraped from statto.

# England starts in 2010.


# Championship formatting is like italy's.
# Gonna handle it later.

class EnglandParser(RSSSFParser):

    UNIVERSAL_REPLACE = [
        ('\x96', '-'), # Should probably be in base.py
        ]

    CUT_OFFS = [
        "Round 38",
        "Quarterfinals",
        "Semifinals",
        "First Leg",
        "First leg",
        "Second Leg",
        "First Round",
        "Second Round",
        "Round 2",
        ]
    

    SUB_LINES = {
        2009: {
            'Round 19 [Dec 26]': '[Dec 26]',
            "North-West [Sep 2]": '[Sep 2]',

            },
        }




def process_year(year):
    if year >= 2010:
        y = str(year)
    else:
        y = str(year)[-2:]

    url = 'http://rsssf.com/tablese/eng%s.html' % y
    return EnglandParser().parse_page(url, year)


