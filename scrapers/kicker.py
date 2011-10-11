
# Another source?

# Tremendous german data.
# http://www.kicker.de/

import datetime
import urllib2

from soccerdata.utils import scrape_soup, get_contents
from soccerdata.cache import  data_cache, set_cache


def scrape_all_kicker_seasons():
    l = []
    for e in range(1963, 2009):
        ss = str(e)
        ns = str(e+1)[2:]
        season = "%s-%s" % (ss, ns)
        l.extend(scrape_season_scores(season))
    return l

def scrape_season_scores(season):
    # Consider using their yearly list at -1.
    url_base = 'http://www.kicker.de/news/fussball/bundesliga/spieltag/1-bundesliga/%s/%s/0/spieltag.html'
    l = []
    for e in range(1, 35):
        url = url_base % (season, e)
        try:
            l.extend(scrape_game_scores(url, season))
        except:
            print url
            raise

    return l
            
               

@data_cache
def scrape_game_scores(url, season):
    start_year = int(season.split('-')[0])
    end_year = start_year + 1

    soup = scrape_soup(url)
    
    t = soup.find('table', 'tStat') # may be more than one of these.
    trs = t.findAll("tr")

    def process_row(row):
        formatter = lambda s: s.replace("&nbsp;", ' ')
        tds = tr.findAll('td')
        if len(tds) <= 1:
            return {}
        elif len(tds) == 9:
            day, date_string, home_string, _, away_string, score, link, image, _ = tds
            
        date_string = get_contents(date_string, formatter)

        if not date_string.strip():
            date = None
        else:
            day, month, _ = date_string.split('.')
            if int(month) >= 7:
                year = start_year
            else:
                year = end_year

            try:
                date = datetime.datetime(year, int(month), int(day))
            except:
                import pdb; pdb.set_trace()

        home_team = get_contents(home_string)
        away_team = get_contents(away_string)

        score = get_contents(score, formatter).split("(")[0]

        # Probably incomplete.
        try:
            home_score, away_score = [int(e) for e in score.split(':')]
        except:
            print "bad score %s" % score
            return {}

        # Probably an unplayed game.
        try:
            url = link.find("a")['href']
        except:
            print "no link %s" % link
            return {}

        return {
            'home_team': home_team,
            'away_team': away_team,
            'home_score': home_score,
            'away_score': away_score,
            'date': date,
            'url': url
            }

            
    l = []
    for tr in trs:
            l.append(process_row(tr))
    l = [e for e in l if e]

    date = None
    for e in l:
        if e['date']:
            date = e['date']
        else:
            e['date'] = date

    return l


def scrape_goals(url):
    soup = scrape_soup(url)
    
    import pdb; pdb.set_trace()

    return {}

def scrape_lineups(url):
    # Need to add subs..
    # Use th tags to mark end of goals/lineups
    soup = scrape_soup(url)
    
    lineup_divs = soup.findAll("div", 'schemaaufstellung')
    
    def process_lineup(div):
        l = []
        a_tags = div.findAll("a")
        for e in a_tags:
            l.append((get_contents(e), e['href']))

        return l

    return process_lineup(lineup_divs[0])
            




        


if __name__ == "__main__":
    print scrape_all_seasons()
    #'http://www.kicker.de/news/fussball/bundesliga/spieltag/1-bundesliga/1994-95/34/10909/spielschema_bayer-leverkusen-9_dynamo-dresden-65.html'
    print scrape_lineups('http://www.kicker.de/news/fussball/bundesliga/spieltag/1-bundesliga/1963-64/1/20087/spielschema_1860-muenchen-5_eintracht-braunschweig-41.html')
    #print scrape_season_scores('1963-64')

        
    
