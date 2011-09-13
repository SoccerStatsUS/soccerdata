from base import RSSSFParser


# Results going back quite far

class Parser(RSSSFParser):
    CUTOFFS = [
        ]

    RE_CUTOFFS = [
        "Round\s\d{1,2}\s(.*)",
        ]

    SUB_LINES = {
        2010: {
            },
        }


def process_year(year):
    if year >= 2010:
        y = str(year)
    else:
        y = str(year)[-2:]

    url = 'http://rsssf.com/tablesa/arg%s.html' % y
    return Parser().parse_page(url, year)

