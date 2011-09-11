import datetime
import re
import urllib2

from BeautifulSoup import BeautifulSoup

#from soccer.teams.models import Team


result_re = re.compile("^(.*?)(\d+)-(\d+)(.*)$")
schedule_re = re.compile("^.*?(\s+\d+){4,}.*$")

month_string = "|".join(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
date_re = re.compile("\[(%s) \d+\]" % month_string)

def find_date_prefixes(line):
    """
    Basically find problem areas for matching dates,
    e.g. Semi-final [Nov 13]
    """
    a = bool(check_date(line))
    b = bool(date_re.search(line))
    return a == b
    

    




def check_schedule(line):
    m = schedule_re.search(line)
    if m:
        return line
    

def check_result(line):
    # Not the easiest regular expression to check.
    # Need a giant list of teams to check against each side, or something else...
    m = result_re.search(line)
    if m:
        home_team, home_score, away_score, away_team = m.groups()
        home_team = home_team.strip()
        away_team = away_team.strip()
        home_score = int(home_score)
        away_score = int(away_score)


        if home_team == '' or away_team == '':
            return None
        else:
            return home_team, away_team, home_score, away_score

def check_date(line):
    prefixes = [
        'First Leg',
        'First Legs', 
        'Second Leg',
        'Second Legs', 
        'Second Round',
        'Quarterfinals',
        'Semifinals',
        'Final',
        'Qualifying Match',
        'Western Final', 
        'Eastern Final', 
        'MLS Cup',
                ]

    rounds = ["Round %s" % e for e in range(33)]

    obstacles = prefixes + rounds

    # Try replacing the string with each possible obstacle.
    # Some may match, but not convert to a date.
    # e.g. 'Second Leg' matches Second Legs [Mar 30],
    # but won't work.  
    # So try all of them until you get a match
    # or return None if nothing matches.
    for e in obstacles:
        if line.startswith(e):
            nl = line.replace(e, '', 1).strip()
            try:
                return datetime.datetime.strptime(nl, "[%b %d]")
            except ValueError:
                pass
    return None
        
def rsssf_lines(url):
    text = urllib2.urlopen(url).read()
    text = text.replace("\r", "")
    lines = text.split("\n")
    return [e.strip() for e in lines]
    #soup = BeautifulSoup(text).findAll("pre")
    #contents = str(soup[0].contents[0])


def find_problems(url):
    lines = rsssf_lines(url)
    for line in lines:
        if not find_date_prefixes(line):
            print line
                    

def scrape_results(url):
    """ Rather tricky turning all of this into structured data."""


    lines = rsssf_lines(url)
    results = []
    game_date = None

    for line in lines:
        if line:
            s = check_schedule(line)
            d = check_date(line)
            r = check_result(line)
            
            if s:
                pass #print line
            elif d:
                game_date = d
            elif r:
                t = (game_date, r)
                results.append(t)
            else:
                print line

    return results
                
