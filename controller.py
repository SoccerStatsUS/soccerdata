import datetime
import StringIO
from os.path import join, split
from collections import defaultdict

from flask import Flask, render_template, redirect, url_for, request, jsonify, Response, flash, send_file

from flask.templating import TemplateNotFound

#from flaskext.cache import Cache

from collections import defaultdict

import pymongo
import mongo

soccer_db = mongo.soccer_db



app = Flask(__name__)
app.config.from_pyfile('settings.cfg')
#cache = Cache(app)


    
@app.route("/")
def index():
    return render_template("index.html")

# What do we really want from these pages?

# Probably need to dump all rows into a single db.

# !!! Rows with problems!!

# Listing of all rows.
# Searchable
# filters
# pages




# The years we're trying to cover.
YEARS = list(reversed(range(1996,2012)))

# The competitions we're trying to cover.
DOMESTIC_COMPETITIONS = [
    #'NASL',
    'MLS',
    'La Liga',
    'Bundesliga',
    'Russian Premier League',
    'Portuguese Liga',
    'Serie A',
    'Eredivisie',
    'Ligue 1',
    'Premier League',
    'Mexico',
    'A-League',
    'Champions League',
    ]

INTERNATIONAL_COMPETITIONS = [
    'World Cup',
    'European Championship',
    'Copa America',
    'Gold Cup',
    'Asian Cup',
    'African Cup of Nations',
    ]




@app.route('/d')
def data():
    coll = request.args['c']
    ctx = {
        'data':  soccer_db[coll].find(),
        }
    return render_template("data.html", **ctx)




def get_competitions(coll):
    competitions = set()
    for e in coll.find():
        competitions.add(e['competition'])
    return sorted(competitions)



def get_years_generic(coll):
    
    years = set(YEARS) # Unnecessary

    result = {}
    for name in DOMESTIC_COMPETITIONS:
        s = set()
        r = coll.find({'competition': name})
        for e in r:
            year = e['year']
            if year in years:
                s.add(year)

        result[name] = list(s)
        
    # This part is not necessary.
    t = sorted([(k, sorted(v)) for (k, v) in result.items()])
    return t



def get_goal_years():
    return get_years_generic(soccer_db.goals)

def get_game_years():
    return get_years_generic(soccer_db.games)

#def get_standing_years():
#    return get_years_generic(soccer_db.standings)


def get_stat_years():
    return get_years_generic(soccer_db.stats)

def get_lineup_years():
    return get_years_generic(soccer_db.lineups)

def get_bios():
    return soccer_db.find().sort([("birthdate", pymongo.ASCENDING), ('minute', pymongo.ASCENDING)])

@app.route("/dashboard/stats")
def stats_dashboard():
    years = range(1996, 2011)
    mls_games = soccer_db.stats.find({'competition': 'MLS' })
    teams = sorted(set([e['team'] for e in mls_games]))

    def get_team_years(team):

        team_years = sorted(set([e['year'] for e in soccer_db.stats.find({'competition': 'MLS', 'team': team})]))
        return [(year in team_years and year) for year in years]

    team_years = [(team, get_team_years(team)) for team in teams]

    ctx = {
        'team_years': team_years,
        'years': years,
        }
            

    return render_template("stats_dashboard.html", **ctx)

@app.route('/dashboard/scraper')
def scraper_dashboard():
    scrapers = ['mls', 'soccernet', 'cnnsi', 'scaryice', 'fbleague', 'fifa', 'mediotiempo', 'wiki']
    tables = ['games', 'goals', 'stats', 'lineups', 'standings', 'bios']

    def process_scraper(scraper):
        table_names = ['%s_%s' % (scraper, table) for table in tables]
        return [soccer_db[table_name].count() for table_name in table_names]

    ctx = {
        'mls_data': process_scraper('mls'),
        'soccernet_data': process_scraper('soccernet'),
        'cnnsi_data': process_scraper('cnnsi'),
        'scaryice_data': process_scraper('scaryice'),
        'fbleague_data': process_scraper('fbleague'),
        'fifa_data': process_scraper('fifa'),
        'mediotiempo_data': process_scraper('mediotiempo'),
        'wiki_data': process_scraper('wiki'),
        }

    return render_template("scraper_dashboard.html", **ctx)



@app.route('/dashboard/<competition>')
def competition_dashboard(competition):

    seasons = [str(e) for e in range(1996, 2011)]

    def get_year_list(coll, seasons):
        season_count = defaultdict(int)
        for item in coll.find({'competition': competition}):
            season = item['season']
            season_count[season] += 1
        return [(season, season_count.get(season, 0)) for season in seasons]
            
            
    game_seasons = get_year_list(soccer_db.games, seasons)
    goal_seasons = get_year_list(soccer_db.goals, seasons)
    stat_seasons = get_year_list(soccer_db.gstats, seasons)
    lineup_seasons = get_year_list(soccer_db.lineups, seasons)
    standing_seasons = get_year_list(soccer_db.standings, seasons)

    ctx = {
        'game_seasons': game_seasons,
        'goal_seasons': goal_seasons,
        'stat_seasons': stat_seasons,
        'lineup_seasons': lineup_seasons,
        'standing_seasons': standing_seasons,
        'seasons': seasons,
        'competition': competition,
        }

    
    return render_template("mls_dashboard.html", **ctx)



@app.route("/dashboard")
def dashboard():

    #competition_and_seasons = "MLS" + get_seasons(soccer_db.games.find({"competition": "MLS"}))
    


    ctx = {
        #'competition_and_seasons': competition_and_seasons,
        #'results_list': results_list,
        'years': YEARS,
        'game_years': get_game_years(),
        #'standing_years': get_standing_years(),
        'goal_years': get_goal_years(),
        'stat_years': get_stat_years(),
        'lineup_years': get_lineup_years(),
        }
    
    return render_template("dashboard.html", **ctx)


@app.route("/stats/<season>")
def season_stats(season):

    stats = soccer_db.stats.find({"season": season}).sort("name", pymongo.ASCENDING)
    ctx = {
        'stats': stats,
        'season': season
        }
    return render_template("stats.html", **ctx)




@app.route("/stats")
def stats():
    d = dict([(k, v) for (k, v) in request.args.items()])
    stats = soccer_db.stats.find(d).sort("name", pymongo.ASCENDING)
    return render_template("stats.html", stats=stats, request=d)

@app.route("/standings")
def standings():
    d = dict([(k, v) for (k, v) in request.args.items()])
    standings = soccer_db.standings.find(d).sort([("competition", pymongo.ASCENDING), ("season", pymongo.ASCENDING), ("name", pymongo.ASCENDING)])
    return render_template("standings.html", standings=standings)


@app.route("/games")
def games():
    d = dict([(k, v) for (k, v) in request.args.items()])
    games = soccer_db.games.find(d).sort("date", pymongo.ASCENDING)
    return render_template("games.html", games=games)


@app.route("/goals")
def goals():
    d = dict([(k, v) for (k, v) in request.args.items()])
    goals = soccer_db.goals.find(d).sort("date", pymongo.ASCENDING)
    return render_template("goals.html", goals=goals)


    



@app.route("/g/nasl")
def nasl():
    rows = mongo.get_rows(soccer_db.nasl_scores)
    return render_template("game.html", rows=rows)    

@app.route("/g/mls")
def mls():
    rows = mongo.get_rows(soccer_db.mlssoccer_mls_games)
    return render_template("game.html", rows=rows)    


@app.route("/g/australia")
def australia():
    rows = mongo.get_rows(soccer_db.mlssoccer_mls_games)
    return render_template("game.html", rows=rows)    


@app.route("/<url>")
def flatpage(url):
    if url.endswith("/"):
        url = url[:-1]
    
    template = url + ".html"                 
    try:
        return render_template(template)
    except TemplateNotFound:
        return render_template("404.html")


if __name__ == "__main__":
    app.run(port=29111)

