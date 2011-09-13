from base import RSSSFParser

import re

# Italy seems a little different, but has tremendous records going back quite far.

class ItalyParser(RSSSFParser):

    def get_date(self, line, date, year):
        # Italy looks like this:
        # 3rd round [Sep 22, 1996] 
        # Or like this
        # Bologna 1 - 0 Lazio [Sep 7]
        # Not worrying about the Bologna/Lazio issue yet.

        s = re.search("round\s+[(\w+)\s(\d+),\s(\d+)]", line)
        s2 = re.search("round", line)
        if s2:
            import pdb; pdb.set_trace()
            x = 5

        pass

    

def process_year(year):
    if year >= 2010:
        y = str(year)
    else:
        y = str(year)[-2:]

    url = "http://rsssf.com/tablesi/ital%s.html" % y
    return ItalyParser().parse_page(url, year)
