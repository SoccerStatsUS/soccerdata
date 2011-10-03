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
    'Tampa Bay': 'Tampa Bay Mutiny',
    'Toronto': 'Toronto FC',
    'Metrostars': 'New York Red Bulls',
    'MetroStars': 'New York Red Bulls',
    'LA': 'Los Angeles Galaxy',
    'KC': 'Sporting Kansas City',
    'Kansas City Wizards': 'Sporting Kansas City',
    'SJ': 'San Jose Earthquakes',
    'CLB': 'Columbus Crew',
    'NY': 'New York Red Bulls',
    'TOR': 'Toronto FC',
    'RSL': 'Real Salt Lake',
    'DAL': 'FC Dallas',
    'HOU': 'Houston Dynamo',
    'CHI':'Chicago Fire',
    'CHV': 'Chivas USA',
    'COL': 'Colorado Rapids',
    'NE': 'New England Revolution',
    'DC': 'D.C. United',
    'PHI': 'Philadelphia Union',
    'Sea': 'Seattle Sounders',
    'TB': 'Tampa Bay Mutiny',
    'MIA': 'Miami Fusion',
    'MET': 'New York Red Bulls',
    
    
    }


def get_team(name):
    if name in teams:
        return get_team(teams[name])
    return name
    
