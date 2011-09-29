#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


teams = {
    'Chicago': 'Chicago Fire',
    'Colorado': 'Colorado Rapids',
    'Columbus': 'Columbus Crew',
    'DC United': 'D.C. United',
    'Dallas': 'FC Dallas',
    'Houston': 'Houston Dynamo',
    'Kansas City': 'Kansas City Wizards',
    'Los Angeles': 'Los Angeles Galaxy',
    'New England': 'New England Revolution',
    'New York': 'New York Red Bulls',
    'Philadelphia': 'Philadelphia Union',
    'San Jose': 'San Jose Earthquakes',
    'Seattle': 'Seattle Sounders',
    'Toronto': 'Toronto FC',
    'Metrostars': 'New York Red Bulls',
    'MetroStars': 'New York Red Bulls',
    }


def get_team(name):
    if name in teams:
        return get_team(teams[name])
    return name
    
