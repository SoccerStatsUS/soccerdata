#!/usr/bin/env python

# Load country and state data.
# Country names and populations (2000?)
# State and territory names, postal abbreviations, date joining union, and historical populations.

import datetime
import os

PLACES_DIR = "/home/chris/www/soccerdata/data/places"


def load_countries():
    l = []
    p = os.path.join(PLACES_DIR, 'countries')
    for line in open(p):
        if line.strip():
            country, population = line.split(';')
            l.append({
                    'name': country.strip(),
                    'population': int(population)
                    })

    return l
        

def load_states():
    l = []
    p = os.path.join(PLACES_DIR, 'states')
    for line in open(p):
        if line.strip():

            fields = line.split(',')

            if len(fields) == 2:
                name, abbreviation = fields
                d = None

            elif len(fields)== 3:
                name, abbreviation, joined = fields
                month, day, year = [int(e) for e in joined.split('/')]

                d = datetime.datetime(year, month, day)

            else:
                import pdb; pdb.set_trace()
            
            l.append({
                    'name': name.strip(),
                    'abbreviation': abbreviation.strip(),
                    'joined': d,
                    })

    return l


def load_state_populations():
    l = []
    p = os.path.join(PLACES_DIR, 'state_populations_by_year')
    for line in open(p):
        if line.strip():
            abbreviation, year, population = line.split(';')
            l.append({
                    'abbreviation': abbreviation.strip(),
                    'year': int(year),
                    'population': int(population)
                    })

    return l
    


