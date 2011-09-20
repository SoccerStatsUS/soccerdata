import datetime
import StringIO
from os.path import join, split
from collections import defaultdict

from flask import Flask, render_template, redirect, url_for, request, jsonify, Response, flash, send_file

from flask.templating import TemplateNotFound

#from flaskext.cache import Cache


#from forms import BlogEditForm
#from models import Blog, Status, Rental
#from models import engine

import mongo

import pymongo

connection = pymongo.Connection()
soccer_db = connection.soccer



app = Flask(__name__)
app.config.from_pyfile('settings.cfg')
#cache = Cache(app)


    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/g/games")
def game_page():
    rows = mongo.get_rows('statto.games')[:100]
    return render_template("game.html", rows=rows)

@app.route("/g/spain")
def spain_page():
    rows = mongo.get_rows('rsssf-spain-games')
    return render_template("game.html", rows=rows)

@app.route("/g/nasl")
def nasl():
    rows = mongo.get_rows(soccer_db.nasl_scores)
    return render_template("game.html", rows=rows)    

@app.route("/g/mls-rsssf")
def mls_rsssf():
    rows = mongo.get_rows('rsssf-mls-games')
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

