from base import RSSSFParser

# Notes: 

# MLS is "working" through 2003.
# Unsure how well.

class MLSParser(RSSSFParser):
    table_start = None
    table_ends = [
        'USA Open Cup', 
        'USL - 1ST DIVISION (2nd Division)'
        ]

    CUTOFFS = [
        'Eastern Final',
        'Western Final',
        'Eastern Conference Final',
        'Western Conference Final',
        'Conference Finals',
        'MLS Cup',
        ]

    SUB_LINES = {

        2010: {
            'Final [Nov 21, MBO Field, Toronto]': '[Nov 21]',
            },
        2009: {

            },

        2008: {

            },

        2007: {

            },

        2006: {
            },

        2005: {
            },

        2004: {},
        2003: {
            },
        2002: {

            },




        }


def process_year(year):
    if year >= 2010:
        y = str(year)
    else:
        y = str(year)[-2:]

    url = "http://rsssf.com/tablesu/usa%s.html" % y
    return MLSParser().parse_page(url, year)


