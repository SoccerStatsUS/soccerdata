from base import RSSSFParser


class AustraliaParser(RSSSFParser):
    CUTOFFS = [
        "Midweek Match",
        'Minor Semifinal',
        'Preliminary Final',
        'Grand Final',
        ]

    RE_CUTOFFS = [
        "Round\s\d{1,2}\s(.*)",
        ]

    SUB_LINES = {
        2010: {
            'Grand Final [Mar 20, Etihad Stadium, Melbourne]': '[Mar 20]',
            },

        }


def process_year(year):
    if year >= 2010:
        y = str(year)
    else:
        y = str(year)[-2:]

    url = "http://rsssf.com/tablesa/aus%s.html" % y
    return AustraliaParser().parse_page(url, year)


