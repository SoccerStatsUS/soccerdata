from base import RSSSFParser

# Notes: 

# MLS is "working" through 2003.
# Unsure how well.

# Need to parse out extraneous data on MLS.
# Attendances,
# Shootout results,

# Furthermore, looks like some scores, e.g. 
#   [Butler 68; Diaz Arce (Rammel, Harkes) 23, Rammel (Etcheverry) 35,
#   Rammel (Agoos) 49]
# Are getting parsed as games. In this case, just Rammel (Agoos) 49]

# Also need to remove tables, elements of which are getting interpreted as results.
# e.g. NY/NJ MetroStars           26 13  3 10 38-35  42  Qualified
# And separate parsing of playoffs from parsing of regular season

# Pull out everything in brackets and add it to a notes field.
# Gonna be a problem where brackets aren't closed...


class MLSParser(RSSSFParser):
    table_start = None
    table_ends = [
        'USA Open Cup', 
        'USL - 1ST DIVISION (2nd Division)'
        ]

    # Should compile these here.
    RE_CUTOFFS = [
        "Round\s\d{1,2}\s(.*)",
        ]

    CUTOFFS = [
        'Eastern Final',
        'Western Final',
        'Eastern Conference Final',
        'Western Conference Final',
        'Conference Finals',
        'MLS Cup',
        'Moved Matches',
        'Moved Match',
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


