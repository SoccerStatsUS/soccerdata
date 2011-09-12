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


app = Flask(__name__)
app.config.from_pyfile('settings.cfg')
#cache = Cache(app)


    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/g/<collection>")
def game_page(collection):
    rows = mongo.get_rows(collection)
    rows = mongo.get_rows('statto.games')[:100]
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

