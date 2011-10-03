#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


# Owns soccerway.
# Lots and lots of stats.

# Has NASL Scores AND stats?!?
# USL scores through 2003.

# Use this for A-League scores, Mexico scores, CL scores...
# England goals.

# Maybe start out with tournaments, since they're smaller and less likely to get you banned?

# Need to fix the year.




# Need to figure out how to use the previous button.

#Some consecutive previous urls
# 


# http://concacaf.globalsportsmedia.com/ajax.php?sport=soccer&language_id=us&block_id=page_competition_1_block_competition_matches_summary_2&block_name=block_competition_matches_summary&callback_params=%7B%22page%22%3A%200%2C%20%22round_id%22%3A%206722%2C%20%22outgroup%22%3A%20false%7D&action=changePage&params=%7B%22page%22%3A%20-1%7D
# http://concacaf.globalsportsmedia.com/ajax.php?sport=soccer&language_id=us&block_id=page_competition_1_block_competition_matches_summary_2&block_name=block_competition_matches_summary&callback_params=%7B%22page%22%3A%20-2%2C%20%22round_id%22%3A%206722%2C%20%22outgroup%22%3A%20false%7D&action=changePage&params=%7B%22page%22%3A%20-3%7D

# Deconstructed
# Seems like either from callback_params or params

"""
callback_params=%7B%22page%22%3A%20-2%2C%20%22round_id%22%3A%206722%2C%20%22outgroup%22%3A%20false%7D

callback_params=%7B%22page%22%3A%200%2C%20%22round_id%22%3A%206722%2C%20%22outgroup%22%3A%20false%7D

params=%7B%22page%22%3A%20-3%7D'
params=%7B%22page%22%3A%20-1%7D

"""

# There's one big problem with this data.
# League data is split up into pages, and
# the paging through those is really awkward.


from soccerdata.utils import scrape_soup, get_contents


def scrape_all_games():
    """
    """
    # Not sure what this is supposed to be doing.
    urls = get_urls()
    games = []
    for url in urls[1:]:
        games.extend(scrape_games(url))
    return games


def get_urls(url, searched=None):
    """
    Get all urls linked from a page via the select dropdowns.
    """
    

    if url == 'http://concacaf.globalsportsmedia.com0':
        import pdb; pdb.set_trace()

    if searched is None:
        searched = set([url])

    soup = scrape_soup(url, sleep=10)
    options = soup.findAll("option")
    relative_urls = [e['value'] for e in options if e['value'].startswith("/")]
    urls = ['http://concacaf.globalsportsmedia.com%s' % u for u in relative_urls]

    for url in urls:
        if url not in searched:
            searched.add(url)
            urls.extend(get_urls(url, searched))
        
    return sorted(list(set(urls)))
    


def scrape_games(url):
    """
    Scrape games from a scoreboard.
    """

    soup = scrape_soup(url)
    tables = soup.findAll("table", "matches  ")


    def process_row(row):
        tds = row.findAll("td")
        if not tds:
            return {}

        fields = [get_contents(e) for e in tds]

        # Aggregate score.
        if fields[0] == u'Aggr.':
            return {}


        # 2010-11
        _, home_team, score, away_team, _, _ = fields

        # Need to record what happened here!
        if "Pen" in score:
            score, penalties = score.split("Pen")

        # Game was cancelled.
        if score == "CANC":
            return {}

        # Get this info later.
        if "AET" in score:
            score = score.replace("AET", "")


        home_score, away_score = [int(e) for e in score.split('-')]

        return {
            'home_team': home_team,
            'away_team': away_team,
            'home_score': home_score,
            'away_score': away_score,
            'competition': 'CONCACAF Champions League',
            }
    scores = []
    for table in tables:
        for tr in table.findAll("tr"):
            try:
                game = process_row(tr)
            except:
                import pdb; pdb.set_trace()
                game = None
            if game:
                scores.append(game)


    return scores


if __name__ == "__main__":
    # Don't want to scrape this year.
    scrape_all_games()
