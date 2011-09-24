import datetime
import StringIO
from os.path import join, split
from collections import defaultdict

from flask import Flask, render_template, redirect, url_for, request, jsonify, Response, flash, send_file

from flask.templating import TemplateNotFound

#from flaskext.cache import Cache

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
    'NASL',
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

def get_stat_years():
    return get_years_generic(soccer_db.stats)

def get_lineup_years():
    return get_years_generic(soccer_db.lineups)





@app.route("/dashboard")
def dashboard():

    ctx = {
        'years': YEARS,
        'game_years': get_game_years(),
        'goal_years': get_goal_years(),
        'lineup_years': get_lineup_years(),
        }
    
    return render_template("dashboard.html", **ctx)


@app.route("/games")
def games():
    pass

@app.route("/goals")
def goals():
    pass

@app.route("/lineups")
def lineups():
    pass



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

