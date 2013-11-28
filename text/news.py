import datetime
import os
import re

from soccerdata.settings import ROOT_DIR

NEWS_FILE = os.path.join(ROOT_DIR, 'soccerdata/data/news')

def load():
    l = []
    for line in open(NEWS_FILE):
        if line.strip():
            line = line.strip()
            name, url = line.split(',')
            l.append({
                    'name': name,
                    'url': url,
                    })
    return l
            

if __name__ == "__main__":
    print(load())
