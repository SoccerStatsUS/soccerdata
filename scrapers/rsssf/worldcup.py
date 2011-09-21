#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

# Hopefully this will be pretty generic.
# Never mind looks like it's just for this one game.

# Want to process the rows, then process again.

import re

from soccerdata.utils import scrape_url

url = 'http://www.rsssf.com/tables/2010full.html'


def load_2010_scores():
    html = get_data(url)
    lines = preprocess_html(html)
    dates = [parse_date_line(e) for e in lines]
    dates = [e for e in dates if e]
    return dates



def load_2010_goals():
    html = get_data(url)
    lines = preprocess_html(html)
    goals = []
    for e in lines:
        goals.extend(parse_goal_line(e))
    
    return goals

        

def get_data(url):
    
    # Not sure what encoding to use for rsssf.
    html = scrape_url(url, encoding='cp1252')
    pre_text = html.split("<pre>")[1].split("</pre>")[0]
    return pre_text
    


def preprocess_html(html):
    l = []
    for line in html.split("\n"):
        s = line.strip()
        if s:
            l.append(s)
    return l


def parse_date_line(line):
    if re.match("\d{2}/\d{2}/2010", line):
        date, city, stadium, attendance = line.split(",")
        return {
            'date': date,
            'city': city,
            'stadium': stadium,
            'attendance': attendance,
            }
    else:
        return {}

def parse_goal_line(line):


    def parse_goal(s):
        # Need to add an optional type argument for
        # 10 Park Chu-Young 16' OG

        # Probably a good idea just to rewrite this line.
        # URUGUAY             3 (10 Diego Forlán 24' 80' pen, 11 Álvaro Pereira 90+')



        #r = re.compile("\d\s+(?P<name>.*?)\s+(?P<minute>\d+)")
        r = re.compile("\d\s+(?P<name>.*?)\s+(?P<minute>\d+).*(?P<type>\w+)?$")
        d = r.search(s).groupdict()
        d['team'] = team.strip().capitalize()
        return d


    goal_re = re.compile("(?P<team>.*?)\d\s+\((?P<goals>.*?)\)")
    s = goal_re.search(line)
    if s:
        team, goal_string = s.groups()
        goals = goal_string.split(",")
        return [parse_goal(e) for e in goals]
    else:
        return []
        
    
    

