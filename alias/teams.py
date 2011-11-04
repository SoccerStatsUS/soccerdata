#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

teams = {}

mls_teams = {
    'Brooklyn Dodgers S.C.': 'Brooklyn Italians',
    'San Francisco C.D. Mexico' : 'El Farolito Soccer Club',
    'Philadelphia Uhrik Truckers': 'Uhrik Truckers',


    'Connecticut Bi-Centennials': 'Connecticut Bicentennials',
    'Hartford Bi-Centennials': 'Connecticut Bicentennials',
    'Atlanta Apollos': 'Atlanta Chiefs',


    'C.D. Chivas USA': 'Chivas USA',
    'Kansas City Wiz': 'Kansas City Wizards',
    'Kansas City Wizards': 'Sporting Kansas City',
    'LA Galaxy': 'Los Angeles Galaxy',
    'NE Revolution': 'New England Revolution',
    'Metrostars': 'New York Red Bulls',
    'MetroStars': 'New York Red Bulls',
    'New York/New Jersey MetroStars': 'New York Red Bulls',
    'NY Red Bulls': 'New York Red Bulls',
    'SJ Earthquakes': 'San Jose Earthquakes',
    'Sounders FC': 'Seattle Sounders',
    'Sporting KC': 'Sporting Kansas City',
    'Toronto F.C.': 'Toronto FC',
    'Vancouver Whitecaps': 'Vancouver Whitecaps FC',

    'Red Bull New York': 'New York Red Bulls',
    'F.C. Dallas': 'FC Dallas',
    'Houston 1836': 'Houston Dynamo',

    'Chicago': 'Chicago Fire',
    'Colorado': 'Colorado Rapids',
    'Columbus': 'Columbus Crew',
    'DC United': 'D.C. United',
    'Dallas': 'FC Dallas',
    'Houston': 'Houston Dynamo',
    'Kansas City': 'Kansas City Wizards',
    'Tampa Bay': 'Tampa Bay Mutiny',
    'Toronto': 'Toronto FC',
    'Miami': 'Miami Fusion',
    'New England': 'New England Revolution',
    'New York': 'New York Red Bulls',
    'Philadelphia': 'Philadelphia Union',
    'San Jose': 'San Jose Earthquakes',
    'Seattle': 'Seattle Sounders',
    'Portland': 'Portland Timbers',
    'Los Angeles': 'Los Angeles Galaxy',
    'Salt Lake': 'Real Salt Lake',    

    'LA': 'Los Angeles Galaxy',
    'KC': 'Sporting Kansas City',
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

world_cup_teams = {
    'ALG': 'Algeria',
    'ANG': 'Angola',
    'ARG': 'Argentina',
    'AUS': 'Australia',
    'AUT': 'Austria',
    'BEL': 'Belgium',
    'BOL': 'Bolivia',
    'BRA': 'Brazil',
    'BUL': 'Bulgaria',
    'China PR': 'China',
    'CHI': 'Chile',
    'CIV': 'Ivory Coast',
    'CMR': 'Cameroon',
    'COL': 'Colombia',
    'CRC': 'Costa Rica',
    'CRO': 'Croatia',
    'CUB': 'Cuba',
    'CZE': 'Czech Republic',
    'DEN': 'Denmark',
    'ECU': 'Ecuador',
    'ENG': 'England',
    'EGY': 'Egypt',
    'ESP': 'Spain',
    'FRA': 'France',
    'FRG': 'West Germany',
    'German DR': 'East Germany',
    'Germany FR': 'West Germany',
    'GDR': 'East Germany',
    'GER': 'Germany',
    'GHA': 'Ghana',
    'HAI': 'Haiti',
    'HON': 'Honduras',
    'HUN': 'Hungary',
    'Ivory Coast': 'Côte d\'Ivoire',
    'IRL': 'Ireland',
    'IRN': 'Iran',
    'IRQ': 'Iraq',
    'ISR': 'Israel',
    'ITA': 'Italy',
    'JAM': 'Jamaica',
    'JPN': 'Japan',
    'Korea Republic': 'South Korea',
    'KOR': 'South Korea',
    'KSA': 'Saudi Arabia',
    'KUW': 'Kuwait',
    'MAR': 'Morocco',
    'MEX': 'Mexico',
    'NED': 'Netherlands',
    'NIR': 'Northern Ireland',
    'NGA': 'Nigeria',
    'NOR': 'Norway',
    'PAR': 'Paraguay',
    'PER': 'Peru',
    'POL': 'Poland',
    'POR': 'Portugal',
    'PRK': 'North Korea',
    'ROU': 'Romania',
    'Republic of Ireland': 'Ireland',
    'RSA': 'South Africa',
    'RUS': 'Russia',
    'SCG': 'Serbia and Montenegro',
    'SCO': 'Scotland',
    'SEN': 'Senegal',
    'SLV': 'Slovenia',
    'SUI': 'Switzerland',
    'SVN': 'Slovenia',
    'SWE': 'Sweden',
    'TCH': 'Czechoslovakia',
    'TOG': 'Togo',
    'TRI': 'Trinidad & Tobago',
    'TUN': 'Tunisia',
    'TUR': 'Turkey',
    'UAE': 'United Arab Emirates',
    'UKR': 'Ukraine',
    'URS': 'Soviet Union',
    'URU': 'Uruguay',
    'USA': 'United States',
    'WAL': 'Wales',
    'YUG': 'Yugoslavia',
    }

for k, v in world_cup_teams.items():
    t = (k, "FIFA World Cup")
    teams[t] = v


def get_team(name, competition=None):
    if competition is not None and (name, competition) in teams:
        name = teams[(name, competition)]
        return get_team(name, competition)

    if name in teams:
        return get_team(teams[name])

    return name
    
