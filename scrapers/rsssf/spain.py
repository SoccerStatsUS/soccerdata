from base import RSSSFParser


# Notes:

# Functional through 2000. Not well verified.
# One date problem in 1999.
# Date formatting changes starting in 1998 (down)
# Need to parse differently.
# Not sure if it's worth it. Records stop in 1995/96


class SpainParser(RSSSFParser):
    table_start = "Round 1"
    table_ends = ["Final Table"]

    # Should compile these here.
    RE_CUTOFFS = [
        "Round\s\d{1,2}\s(.*)",
        ]

    SUB_LINES = {
        2011: {
            'Round 37 [May 15]': '[May 15]',
            'Round 38 [May 21]': '[May 21]',
            },

        2010: {
            'Round 37 [May 8]': '[May 8]',
            },


        2009: {
            '[Ma 8]': '[Mar 8]'
            },

        2007: {
            'Round 38 [Jun 17]': '[Jun 17]',
            '[Mar 20]                                          due to crowd trouble]': '[Mar 20]',
            },

        2008: {
            "Betis      1-2 Athletic     [abandoned at 1-2 in 69' due to crowd": 'Betis 1-2 Athletic',
            'Valencia   1-2 Sevilla       trouble; result stood]': 'Valencia 1-2 Sevilla',
            'Round 37 [May 11]': '[May 11]'
            },

        2005: {
            "Madrid       abd Sociedad          [abandoned at 1-1 in 88' after a": 'Madrid abd Sociedad',
            "  [Ronaldo 40; Nihat 72]            bomb alarm]": "[Ronaldo 40; Nihat 72]",
            "Madrid       2-1 Sociedad          [remaining 2' and 4' injury time]": 'Madrid 2-1 Sociedad'
            },

        2004: {
            'Round 38 [May 23]': '[May 23]'
            },

        2002: {
            'Round 37 [May 5]': '[May 5]',
            },

        2001: {
            'Round 37 [Jun 10]': '[Jun 10]',
            },

        1999: {
            '[Peternac 35 (p),59; Oli 88]  outside the European Union; originally 2-1]': '[Peternac 35 (p),59; Oli 88]',
            'Valladolid    awd Betis        [awarded 0-3 as Valladolid used 5 foreigners from': 'Valladolid    awd Betis',
            'First Legs [Jun 27]': '[Jun 27]',
            'Second Legs [Jun 30]': '[Jun 30]',

            # Adding the scorelines to these confused the game parser.
            # Not sure it's really necessary.
            '[Vlaovic 12, Farinos 90 (2-2); Sanchez 41, Karpin 90 (1-2)]': '[Vlaovic 12, Farinos 90; Sanchez 41, Karpin 90]',
            '[Claudio Lopez 90 (1-2); Tamudo 71, Posse 90 (0-2)]': '[Claudio Lopez 90; Tamudo 71, Posse 90]',

            },

        }


def process_year(year):
    if year >= 2010:
        y = str(year)
    else:
        y = str(year)[-2:]

    url = "http://rsssf.com/tabless/span%s.html" % y
    return SpainParser().parse_page(url, year)



if __name__ == "__main__":
    print "\n".join([str(e) for e in process_year(2011)])
