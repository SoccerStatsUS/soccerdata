import datetime
import StringIO
from os.path import join, split
from collections import defaultdict

from flask import Flask, render_template, redirect, url_for, request, jsonify, Response, flash, send_file

from flask.templating import TemplateNotFound

#from flaskext.cache import Cache

import pymongo
import mongo

soccer_db = mongo.soccer_db

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

STAT_TABLES = 'games', 'goals', 'stats', 'lineups', 'standings', 'bios', 'teams'




# Issues to work on.
# - show problem rows
# - searchable
# - filters
# - pages


    
@app.route("/")
def index():
    return redirect(url_for('dashboard'))

@app.route("/dashboard")
def dashboard():
    """
    A dashboard for showing the status of the project
    """

    def process_scraper(scraper):
        table_names = ['%s_%s' % (scraper, table) for table in STAT_TABLES]
        return [(table_name, soccer_db[table_name].count()) for table_name in table_names]

    ctx = {
        'main': [(table_name, soccer_db[table_name].count()) for table_name in STAT_TABLES],
        'yaml_data': process_scraper('yaml'),
        'mlssoccer_data': process_scraper('mls'),
        'soccernet_data': process_scraper('soccernet'),
        'cnnsi_data': process_scraper('cnnsi'),
        'uslsoccer_data': process_scraper('uslsoccer'),
        'scaryice_data': process_scraper('scaryice'),
        'chris_data': process_scraper('chris'),
        'fbleague_data': process_scraper('fbleague'),
        'fifa_data': process_scraper('fifa'),
        'mediotiempo_data': process_scraper('mediotiempo'),
        'wiki_data': process_scraper('wiki'),
        'eufootball_data': process_scraper('eufootball'),
        }

    return render_template("dashboard.html", **ctx)    


def dashboard_detail(coll_list):
    """
    Pass in a list of collections 
    corresponding to games, goals, stats, lineups, standings, bios.
    """



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




@app.route('/d')
def data():
    """
    Gives back a listing of the elements in the collection.
    """
    collection_name = request.args['c']
    collection = soccer_db[collection_name]

    if collection.count():
        keys = collection.find()[0].keys()
        keys.remove("_id")
    else:
        keys = []

    ctx = {
        'keys': keys,
        'data':  collection.find()
        }

    return render_template("data.html", **ctx)



'''












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


@app.route("/<url>")
def flatpage(url):
    if url.endswith("/"):
        url = url[:-1]
    
    template = url + ".html"                 
    try:
        return render_template(template)
    except TemplateNotFound:
        return render_template("404.html")




'''

if __name__ == "__main__":
    app.run(port=29111)
