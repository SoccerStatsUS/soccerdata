import datetime
import re
import urllib2
from BeautifulSoup import BeautifulSoup


months = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12,
    }


def preprocess_line(line, year):

    years = {
        2009: {
            '[Ma 8]': '[Mar 8]'
            },
        }
    if year in years and line in years[year]:
        return years[year][line]
    else:
        return line
    

# Generate cross-tables easily.
# Games with results go back to around 98, with apparently some style changes.]

def parse_season_page(url, year):
    html = urllib2.urlopen(url).read()
    pre = html.split("<pre>")[1].split("</pre>")[0]

    # Prepare the lines
    first_division_start = pre.index("Round 1")
    first_division_end = pre[first_division_start:].index("Final Table")

    first_division_table = pre[first_division_start:first_division_end]
    lines = [e for e in first_division_table.split("\n") if e.strip()]

    scores = []

    date = None
    for line in lines:
        line = line.strip()
        pline = preprocess_line(line, year)
        date = get_date(pline, date, year)
        result = process_line(pline, date)
        if result:
            scores.append(result)
    return scores

def get_date(line, date, year):
    if line.startswith("["):
        line = line.strip().replace("[", "").replace("]", "")
        try:
            month, day = line.split(" ")
        except:
            import pdb; pdb.set_trace()
        try:
            month_number = months[month]
        except KeyError:
            import pdb; pdb.set_trace()
        try:
            return datetime.datetime(year, month_number, int(day))
        except:
            import pdb; pdb.set_trace()
    else:
        return date


def process_line(line,  date):
    if re.search("\d-\d", line):
        home_side, away_side = line.split("-")
        home_team, home_score = home_side.split(" ", 1)
        away_score, away_team = away_side.split(" ", 1)
        away_score = int(away_score)
        home_score = int(home_score)
        return {
            'home_team': home_team.strip(),
            'away_team': away_team.strip(),
            'home_score': home_score,
            'away_score': away_score,
            'date': date,
            }
    else: 
        return None


