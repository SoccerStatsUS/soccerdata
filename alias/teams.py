#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

teams = {}

mls_teams = {
    'NY Red Bulls': 'New York Red Bulls',
    'Salt Lake': 'Real Salt Lake',
    'Portland': 'Portland Timbers',
    
    'Chicago': 'Chicago Fire',
    'Colorado': 'Colorado Rapids',
    'Columbus': 'Columbus Crew',
    'DC United': 'D.C. United',
    'Dallas': 'FC Dallas',
    'Houston': 'Houston Dynamo',
    'Kansas City': 'Kansas City Wizards',
    'Los Angeles': 'Los Angeles Galaxy',
    'Miami': 'Miami Fusion',
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
    'SEA': 'Seattle Sounders',
    'TB': 'Tampa Bay Mutiny',
    'MIA': 'Miami Fusion',
    'MET': 'New York Red Bulls',
    }
teams.update(mls_teams)

usl_teams = {
    'NOGM': 'New Orleans Riverboat Gamblers',
    'ATLS': 'Atlanta Silverbacks',
    'CALJ': 'California Jaguars',
    'CARD': 'Carolina Dynamo',
    'CHAB': 'Charleston Battery',
    'COLF': 'Colorado Foxes',
    'CONW': 'Connecticut Wolves',
    'ELPP': 'El Paso Patriots',
    'HERW': 'Hershey Wildcats',
    'JAXC': 'Jacksonville Cyclones',
    'LIRR': 'Long Island Rough Riders',
    'MILW': 'Milwaukee Rampage',
    'MINN': 'Minnesota Thunder',
    'MONT': 'Montreal Impact',
    'NASM': 'Nashville Metros',
    'NOST': 'New Orleans Riverboat Gamblers',
    'ORCZ': 'Orange County Zodiac',
    'ORLS': 'Orlando Sundogs',
    'RICK': 'Richmond Kickers',
    'ROCH': 'Rochester Rhinos',
    'SEAS': 'Seattle Sounders',
    'TORL': 'Toronto Lynx',
    'VANW': 'Vancouver Whitecaps FC',
    'WORW': 'Worcester Wildfire',
    'AQGK': 'Albuquerque Geckos',
    'ATLS': 'Atlanta Silverbacks',
    'RCEX': 'Raleigh Express',
    'CINR': 'Cincinnati Riverhawks',
    'SDFL': 'San Diego Flash',
    'STIV': 'Staten Island Vipers',
    'USPS': 'US Project 40',
    'VABM': 'Virginia Beach Mariners',
    'BSBD': 'Boston Bulldogs',
    'INDB': 'Indiana Blast',
    'LHVS': 'Lehigh Valley Steam',
    'MARM': 'Maryland Mania',
    'PITT': 'Pittsburgh Riverhounds',
    'SFBS': 'San Francisco Bay Seals',
    'TENR': 'Tennessee Rhythm',
    'TSAC': 'Team Sacramento',
    'PORT': 'Portland Timbers',
    'CHAE': 'Charlotte Eagles',
    'CLGS': 'Calgary Storm',
    'SYSD': 'Syracuse Salty Dogs',
    'TCAL': 'Team Calgary',
    'CALM': 'Calgary Mustangs',
    'EDFC': 'Edmonton F.C.',
    'PRIS': 'Puerto Rico Islanders',
    'MIAB': 'Miami Breakers',
    'BALB': 'Baltimore Blast',
    'ALBA': 'Albany Alleycats',
    }
teams.update(usl_teams)


# Need to watch out for duplicates names here.
# Need to scrape standings and use that first.
# Dummy.


pdl_teams = {
    'Cape Cod': 'Cape Cod Crusaders',
    'Cocoa': 'Cocoa Expos',
    'El Paso': 'El Paso Patriots',
    ('Kansas City', 'PDL'): 'Kansas City Brass',
    ('Richmond', 'PDL'): 'Richmond Kickers Future',
    'Boulder': 'Boulder Rapids Reserve',
    'Ocean City': 'Ocean City Barons',
    ('Austin', 'PDL'): 'Austin Lightning',
    ('Raleigh', 'PDL'): 'Raleigh CASL Elite',
    'Thunder Bay': 'Thunder Bay Chill',
    'Ottawa': 'Ottawa Fury',
    'Springfield': 'Springfield Storm',
    'Colorado Springs': 'Colorado Springs Blizzard',
    'Sioux Falls': 'Sioux Falls Spitfire',
    'Augusta': 'Augusta Fireball',
    'West Virginia': 'West Virginia Chaos',
    'Williamsburg': 'Williamsburg Legacy',
    'Albany': 'Albany Admirals',
    ('Albany', 'PDL', 2003): 'Albany Blackwatch Highlanders',
    'Vermont': 'Vermont Voltage',
    'Reading': 'Reading Rage',
    'Rhode Island': 'Rhode Island Stingrays',
    'Brooklyn': 'Brooklyn Knights',
    'Westchester': 'Westchester Flames',
    'Laredo': 'Laredo Heat',
    'BYU': 'BYU Cougars',
    'Southern California': 'Southern California Seahorses',
    'Orange County': 'Orange County Blue Star',
    'Bakersfield': 'Bakersfield Brigade',
    'San Diego': 'San Diego Gauchos',
    'Spokane': 'Spokane Shadow',
    'Cascade': 'Cascade Surge',
    'Yakima': 'Yakima Reds',
    'Abbotsford': 'Abbotsford Rangers',
    'Bradenton': 'Bradenton Academics',
    'Palm Beach': 'Palm Beach Pumas',
    'Kalamazoo': 'Kalamazoo Kingdom',
    'West Michigan': 'West Michigan Edge',
    ('Houston', 'PDL'): 'Houston Toros',
    'Texas': 'Texas Spurs',
    'Louisiana': 'Louisiana Outlaws',
    'Memphis': 'Memphis Express',
    'New Orleans': 'New Orleans Riverboat Gamblers',
    'Nashville': 'Nashville Metros',
    'Worcester': 'Worcester Kings',
    'Jersey Shore': 'Jersey Shore Boca',
    'Jersey': 'Jersey Falcons',
    'Chesapeake': 'Chesapeake Dragons',
    ('St. Louis', 'PDL', 2003): 'St. Louis Strikers',
    'Wisconsin': 'Wisconsin Rebels',
    ('Chicago', 'PDL'): 'Chicago Fire Reserves',
    'Des Moines': 'Des Moines Menace',
    'Toledo': 'Toledo Slayers',
    'Fort Wayne': 'Fort Wayne Fever',
    
    }
teams.update(pdl_teams)

misc_teams = {
    "Vancouver 86ers": "Vancouver Whitecaps FC",
    "Golden Bay Earthquakes": "San Jose Earthquakes",
    'NY Pancyprian-Freedoms': 'New York Pancyprian-Freedoms',
    'NY Pancyprian Freedoms': 'New York Pancyprian-Freedoms',
    'Atlanta Datagraphic Magic': 'Atlanta Magic',
    'San Jose Clash': 'San Jose Earthquakes',
    'Dallas Burn': 'FC Dallas',
    'Seattle Sounders FC': 'Seattle Sounders',
    'Carolina Railhawks': 'Carolina RailHawks',
    'Phoenix Hearts': 'Arizona Sahuaros',
    'Arizona Cotton': 'Arizona Sahuaros',
    'Arizona Phoenix': 'Arizona Sahuaros',
    }

teams.update(misc_teams)

def get_team(name, league=None):
    if league and (name, league) in teams:
        name = teams[(name, league)]
        return get_team(name, league)

    if name in teams:
        return get_team(teams[name])
    return name
    
