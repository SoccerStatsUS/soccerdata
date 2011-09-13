import bson
import pymongo
import random
import requests

connection = pymongo.Connection()
db = connection.scraper
collection = db.pages

USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.A.B.C Safari/525.13'

def scrape_url(url):
    # Not sure there is any reason to use an md5...

    scrape_db = connection.scraper
    pages_collection = scrape_db.pages

    result = collection.find_one({"url": url })

    if result is None:
        data = requests.get(url, headers=[('User-Agent', USER_AGENT)]).read()
        insert_row(pages_collection, {"url": url, "data": data})
    else:
        data = result['data']
    return data

# Could do something like find_encoding here.
# This is clearly the wrong place to be doing this.
# Need to run these tests when creating the data.
def insert_row(collection, row):
    try:
        bson.BSON.encode(row)
    except bson.errors.InvalidStringData:
        data = row['data'].decode('cp1252').encode('utf8')
        row['data'] = data
    collection.insert(row)



class SelfRegulatingScraper(object):
    def __init__(self, url_list):
        # What if we don't want to use a list?
        self.url_list = url_list
        self.visited_urls = set()

    def scrape_url():
        random.choice(url_list)
