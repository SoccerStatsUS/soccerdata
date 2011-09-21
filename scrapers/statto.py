# Looks promising.

# Ran into a problem at 12-31-2007;
# Statto seems to be doing some liberal banning if
# it suspects you're scraping its site.


from BeautifulSoup import BeautifulSoup

class UnplayedException(Exception):
    pass



def raw_table(url):
    """
    Return the score table for a given url.
    """
    from soccerdata.utils import scrape_url
    data = scrape_url(url, encoding='iso_8859_1')
    start = data.index("<table")
    end = data.index("</table")
    scores_text = data[start:end]
    return scores_text


def rows_generator(text):
    """
    A simple generator to return rows.
    """
    # I guess this is just me being fancy?
    soup = BeautifulSoup(text)
    # We're going to iterate through all the td's in this box.
    for td in soup.findAll("td"):
        yield td


def consume_rows(rows, competition):
    """
    Consumes x rows until it has a game to return, then does it.
    Returns the data and an updated competition value.
    Mutates rows.
    """

    # Maybe would be better to have a two part system?
    # Rows is a generator and so we consume
    # the part we want.

    def check_team(r):
        # Check to see if this is a team.
        if r.get('class') and r['class'] == 'team':
            # Not sure what will happen when we see an unlinked team.
            # Want to make sure to fix this if it's not a link.
            assert r.find('a')
            return r.find('a').contents[0]
        return None

    def check_score(r):
        # Check to see if this is a score.
        if r.get('class') and r['class'] == 'c1 sc':
            text = r.contents[0]
            if text == 'v':
                raise UnplayedException()
            else:
                home, away = [int(e) for e in text.split("-")]

            return home, away
        return None

    def check_competition(r):
        # Check to see if this is a competition name.
        l_class = row.find("span", "l")
        if l_class:
            return l_class.contents[0]
        return None

    payload = {}
    # We assume that a game has been played unless proven wrong.
    played = True
    for row in rows:

        if check_competition(row):
            competition = check_competition(row)

        try:
            score = check_score(row)
            if score:
                payload['home_score'], payload['away_score'] = score
        except UnplayedException:
            payload['home_score'] = payload['away_score'] = ''
            played = False
            
            

        team = check_team(row)
        if team:
            if 'home_team' not in payload:
                payload['home_team'] = team
            else:
                payload['away_team'] = team
                
                # At this point we should have everything.
                for e in 'home_team', 'away_team', 'home_score', 'away_score':
                    try:
                        assert e in payload
                    except:
                        import pdb; pdb.set_trace()
                payload['competition'] = competition
                payload['played'] = played
                return (payload, competition)


def get_scores(url):
    """
    Return a list of scraped scores.
    """
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
        # When we're out of rows, just return our results!
        except TypeError:
            return l


def process_date(dt):
    url = 'http://www.statto.com/football/stats/results/%s' % dt.strftime("%Y-%m-%d")
    return get_scores(url)
    


    
if __name__ == "__main__":
    main()




