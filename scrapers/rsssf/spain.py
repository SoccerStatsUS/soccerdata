
import re
import urllib2
from BeautifulSoup import BeautifulSoup

url = 'http://rsssf.com/tabless/span09.html'


# Generate cross-tables easily.
# Games with results go back to around 98, with apparently some style changes.





def prepare_lines(pre):

    first_division_start = pre.index("Round 1")
    first_division_end = pre[first_division_start:].index("Final Table")

    first_division_table = pre[first_division_start:first_division_end]

    results = process_results(first_division_table)
    return results


def process_results(data):
    # Get all results for a given spanish season.
    # Whao.
    # Need to fix date logic.

    scores = []
    current_date = None

    lines = [e for e in data.split("\n") if e.strip()]
    for line in lines:
        if line.startswith("["):
            current_date = line
        elif re.search("\d-\d", line):
            home_side, away_side = line.split("-")
            home_team, home_score = home_side.split(" ", 1)
            away_score, away_team = away_side.split(" ", 1)
            away_score = int(away_score)
            home_score = int(home_score)
            scores.append({
                    'home_team': home_team.strip(),
                    'home_score': home_score,
                    'away_team': away_team.strip(),
                    'away_score': away_score,
                    'date': current_date
                    })
        else:
            pass
    return scores


def parse_season_page(url):
    html = urllib2.urlopen(url).read()
    pre = html.split("<pre>")[1].split("</pre>")[0]
    return prepare_lines(pre)

def fetch_year(year):
    y = str(year)[-2:]
    url = "http://rsssf.com/tabless/span%s.html" % y
    return parse_season_page(url)
    


if __name__ == "__main__":
    parse_season_page(url)
