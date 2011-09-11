# Looks promising.

import urllib2
from BeautifulSoup import BeautifulSoup

url = 'http://www.statto.com/football/stats/results/2011-09-10'


class StattoParser(object):

    def __init__(self):
        
        # Used while processing rows to
        # keep track of the current competition
        # whose results are being examined.
        self.competition = None
        self.current = {}


    def process_row(self, row):
        # This span indicates a league, like
        # <td colspan="4"><span class="l">English Premier League</span>

        l_class = row.find("span", "l")
        if l_class:
            self.competition = l_class.contents[0]

        payload = {}
        team = check_team(row)
        if team:
            if 'home_team' in payload:
                self.current['away_team'] = team
            else:
                self.current['home_team'] = team


def raw_table(url):
    data = urllib2.urlopen(url).read()
    start = data.index("<table")
    end = data.index("</table")
    scores_text = data[start:end]
    return scores_text



def rows_generator(text):
    soup = BeautifulSoup(text)
    # We're going to iterate through all the td's in this box.
    for td in soup.findAll("td"):
        yield td


def consume_rows(rows, competition):
    # Rows is a generator and so we consume
    # the part we want.

    def check_team(r):
        if r.get('class') and r['class'] == 'team':
            # Not sure what will happen when we see an unlinked team.
            # Want to make sure to fix this if it's not a link.
            assert r.find('a')
            return r.find('a').contents[0]
        return None

    def check_score(r):
        if r.get('class') and r['class'] == 'c1 sc':
            text = r.contents[0]
            home, away = [int(e) for e in text.split("-")]
            return home, away
        return None

    def check_competition(r):
        l_class = row.find("span", "l")
        if l_class:
            return l_class.contents[0]
        return None


    payload = {}
    for row in rows:

        if check_competition(row):
            competition = check_competition(row)

        if check_score(row):
            payload['home_score'], payload['away_score'] = check_score(row)

        team = check_team(row)
        if team:
            if 'home_team' not in payload:
                payload['home_team'] = team
            else:
                payload['away_team'] = team
                
                # At this point we should have everything.
                for e in 'home_team', 'away_team', 'competition', 'home_score', 'away_score':
                    assert e in payload
                    payload['competition'] = competition
                    return (payload, competition)


def get_scores(url):
    table = raw_table(url)
    rows = rows_generator(table)
    l = []
    competition = None
    while True:
        try:
            (row, c) = consume_rows(rows, competition)
            competition = c
            l.append(row)
        # This is what is thrown when we run out of rows.
        except TypeError:
            return l

    
def main():
    return get_scores(url)

if __name__ == "__main__":
    main()




