from base import RSSSFParser

# Italy seems a little different, but has tremendous records going back quite far.

class ItalyParser(RSSSFParser):
    table_start = None
    table_end = None
    

def process_year(year):
    if year >= 2010:
        y = str(year)
    else:
        y = str(year)[-2:]

    url = "http://rsssf.com/tablesi/ital%s.html" % y
    return SpainParser().parse_page(url, year)
