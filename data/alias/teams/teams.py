#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from soccerdata.mongo import soccer_db

from international import international
from college import college
from allstar import allstar
from mls import mls_abbreviations
from usl import usl_abbreviations
from usa import usa

teams = {}


# Map country codes to names.
country_code_dict = dict([(e['code'], e['name']) for e in soccer_db.countries.find()])

def convert_country_code(code):
    if code in country_code_dict:
        return country_code_dict[code]

    return code



# Handle name loops before processing everything.
def check_for_team_loops():
    errors = False
    for e in teams.keys():
        try:
            get_team(e)
        except:
            print(e)
            errors = True

    if errors:
        raise



def get_team(name, competition=None):

    if name is None:
        import pdb; pdb.set_trace()

    name = convert_country_code(name).strip()

    # This should be split out into a separate function. Currently only used in leach, usl abbreviations.
    if competition is not None and (name, competition) in teams:
        name = teams[(name, competition)]
        return get_team(name, competition)

    if name in teams:
        return get_team(teams[name])


    return name




teams.update(world)
teams.update(usa)
teams.update(college)
teams.update(international)
teams.update(allstar)
teams.update(mls_abbreviations)
teams.update(usl_abbreviations)