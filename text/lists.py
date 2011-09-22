#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

# File for loading all lists.

from soccerdata.data.lists import africa, argentina, asia, australia

# Should create standardized processors for easy data entry.
# Then should dump those files into yaml.


def load_member(l, award):
    # The simplest of all.
    return [{'name': name, 'award': award} for name in l]

def load_list(l, award):
    r = []
    for number, name in l:
        r.append({
                'number': number, 
                'name': name,
                'award': award,
                })
    return r

def load_set(s, award):
    r = []
    for name in s:
        r.append({
                'name': name,
                'award': award,
                })
    return r

def load_fifa_100():
    from soccerdata.data.lists import fifa
    return load_set(fifa.fifa_100, "Fifa 100")



def load_top_three(lst):
    l = []
    for t in lst:
        year = t[0]
        winners = t[1:]
        for i, e in enumerate(winners):
            if i > 2:
                place = 3
            else:
                place = i

            l.append({
                'year': year,
                'name': e,
                'place': place
                })
    return l

        
        

def load_simple(l, award):
    """Format:     (1991, 'Raymond Goethals'),"""
    def process_line(line):
        year, name = line
        return {
            'year': year,
            'name': name,
            'award': award,
            }

    return [process_line(line) for line in l]


def load_top_three_tuples(lst):
    l = []
    for t in lst:
        year = t[0]
        winners = t[1:]
        for i, e in enumerate(winners):
            name, votes = e
            if i > 2:
                place = 3
            else:
                place = i

            l.append({
                'year': year,
                'name': name,
                'place': place,
                'votes': votes,
                })
    return l


# year, names
def load_argentina_footballer():
    def format_award(name):
        return {
            'year': year,
            'name': name,
            'award': 'Footballer of the Year Argentina',
            }

    l = []
    for year, t in argentina.footballer:
        for name in t:
            l.append(format_award(name))
    return l


    


def load_africa_young():
    return load_simple(africa.young_player, "Africa Young Player")

def load_africa_coach():
    return load_simple(africa.coach, "Coach")

def load_africa_team():
    return load_simple(africa.team, "Team")

# Need to do asia footballer...
def load_asia_young():
    return load_simple(asia.young_player, "Asia Young Player")

# Australia

def load_australia_mvp():
    return load_simple(australia.johnny_warren_medal, "Johnny Warren Medal")

def load_australia_finals_mvp():
    return load_simple(australia.joe_marston_medal)
def load_australia_finals():
    return load_simple(australia.nab_young_fooballer)
def load_australia_goalkeeper():
    return load_simple(australia.goalkeeper_of_the_year)
def load_australia_manager():
    return load_simple(australia.manager_of_the_year)





                           

def load_caf():
    return load_top_three(africa.caf_award)
                           

def load_french_african():
    return load_top_three_tuples(africa.french_african)

        
if __name__ == "__main__":
    print load_caf()
    print load_africa_young()
    print load_africa_coach()
    print load_africa_team()
    print load_asia_young()
    print load_argentina_footballer()

