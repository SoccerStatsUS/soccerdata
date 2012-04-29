#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

teams = {}

# Going to organize this alphabetically?
mls_teams = {

    'New York National Giants': 'New York Giants',
    'New York Nationals': 'New York Giants',

    'Todd Shipyards F.C.': 'Todd Shipyards',
    'Bridgeport': 'Bridgeport Bears',
    'Brooklyn Hakoah': 'Hakoah All-Stars',

    # Accurate?
    'Philadelphia 1928-1929': 'Philadelphia Field Club',

    # Need to make sure America is not a regional US team.
    'America': 'América',

    # Colliding with Jersey City slug.
    'Jersey City ?': 'Jersey City (?x)',

    'Club Espana': 'Club España',
    'St. Mary’s Celtic':'St. Mary\'s Celtic',
    'St. Michael’s': 'St. Michael\'s',

    'Federal Ship': 'Federal Shipyards',
    'Federal Ship FC': 'Federal Shipyards',
    'Federal Shipbuilding': 'Federal Shipyards',

    'Philadelphia German-Americans': 'Philadelphia German Americans',
    'Everett BigFoot': 'Seattle BigFoot',
    'Everett Bigfoot': 'Seattle BigFoot',
    'Elizabeth SC': 'Elizabeth S.C.',
    'Newark SC': 'Newark S.C.',
    'Becks German American SC (Buf.)': 'Becks German American S.C. (Buf.)',
    
    'New York Hungaria': 'NY Hungaria',

    'Gjoa SC': 'SC Gjoa',
    'Gjoa FC': 'SC Gjoa',

    'Hellrung & Grimm': 'Hellrung FC',


    'Montclair': 'Fontana Falcons',
    'NY/NJ Stallions': 'New Jersey Stallions',

    'Clark A.A': 'Clark A.A.',
    'IRT Rangers': 'I.R.T. Rangers',
    'Kearny Scottish Americans': 'Kearny Scottish-Americans',
    'St. Mary’s Celtic': 'St. Mary\'s Celtic',
    'Clan Macdonald': 'Clan MacDonald',
    'Puritan Y.M.L': 'Puritan Y.M.L.',
    'Hakoah FC': 'Hakoah F.C.',

    'German American SC': 'German American S.C.',
    'German-American AC': 'German American AC',

    'German-Hungarian SC': 'German Hungarian SC',
    'German-Hungarians': 'German Hungarians',

    'St. Michaels': 'St. Michael\'s',
    'St. Michael’s': 'St. Michael\'s',

    'Brookhattan-Galicia': 'Brookhattan Galicia',
    'IRT Strollers': 'I.R.T. Strollers',
    'Pawtucket FC': 'Pawtucket F.C.',
    'SC Eintracht':'S.C. Eintracht',
    'Edmonton FC': 'Edmonton F.C.',
    'Harrison SC': 'Harrison S.C.',
    'San Francisco AC': 'San Francisco A.C.',
    
  

    'Central Valley Hydra': 'CCV Hydra',
    'Dallas/Ft. Worth Toros': 'Dallas-Fort Worth Toros',
    
    'Robbins Dry Dock': 'Robins Dry Dock',
    'Harrison Erie S.C.': 'Erie AA',
    'Brooklyn Morse Dry Dock': 'Morse Dry Dock',

    'Hakoah All Stars': 'Hakoah All-Stars',

    'Dallas Inter': 'Dallas Mean Green',
    'Bridgeport City AF.C': 'Bridgeport City AFC',
    'apollon': 'Apollon',
    'American AA': 'American A.A.',
    'varzim': 'Varzim',
    'New york Field Club': 'New York Field Club',

    'Heidelberg SC': 'Heidelberg S.C.',
    'Heidelberg Losegos': 'Heidelberg S.C.',

    'German Hungarian SC (NYC)': 'German Hungarian S.C. (NYC)',
    'Eintracht SC': 'Eintracht S.C.',
    'Buda AA': 'Buda A.A.',
    'Scots-Americans': 'Scots Americans',
    'Puritan YML': 'Puritan Y.M.L',
    'Norwegian American SC': 'Norwegian American S.C.',
    'Madison SC': 'Madison S.C.',
    'Lynn Gas & electric': 'Lynn Gas & Electric',
    'lanerossi': 'Lanerossi',
    'Irish-Americans': 'Irish Americans',
    'hertha': 'Hertha BSC',
    'Hertha': 'Hertha BSC',
    'Centennial FC': 'Centennial F.C.',
    'hapoel': 'Hapoel',
    'Brooklyn-Italians': 'Brooklyn Italians',
    
    
    'Disston FC': 'Disston A.A.',
    'Prospect H.': 'Prospect Hill FC',
    'Prospect Hill': 'Prospect Hill FC',
    'Prospect Hill FC (MA)': 'Prospect Hill FC',


    'FC Portland': 'Portland Timbers',
    'Portland F.C.': 'Portland Timbers',

    'Hellrung Grimm': 'Hellrung & Grimm',
    'Baltimore SC': 'Baltimore S.C.',

    'Hollywood Inn': 'Yonkers Hollywood Inn',
    'Jersey AC': 'Jersey A.C.',
    'Newark FC': 'Newark F.C.',
    'Brooklyn FC': 'Brooklyn F.C.',
    'East Newark Clark AA': 'East Newark Clark A.A.',
    'New Bedford FC': 'New Bedford F.C.',
    'YMCTAS': 'YMCA Total Abstinence Society FC',
    

    'Tacony Disston A.A.': 'Disston A.A.',
    'Philadelphia Disston': 'Disston A.A.',
    'Tacony FC': 'Disston A.A.',


    'New York Brookhattan': 'Brookhattan',

    'Packard FC': 'Detroit Packard FC',

    'San Joe Earthquakes': 'San Jose Earthquakes',
    'Clark ONT': 'Clark O.N.T.',
    'Alma': 'Newark Almas',
    'Paterson FC': 'Paterson F.C.',

    'Fall River Olympic': 'Fall River Olympics',

    'Brooklyn Robins Dry Dock': 'Robins Dry Dock',
    'West Hudson AA': 'West Hudson A.A.',
    'Disston AA': 'Disston A.A.',

    'DC United': 'D.C. United',
    'Abbot W.': 'Abbot Worsted',
    'Scullin St.': 'St. Louis Scullin Steel',
    'Yonkers Th.': 'Yonkers Thistle',
    'Holley C.': 'Holley Carburetor F.C.',

    'Whittall': 'Whittall Carpet Mills F.C.',
    'Centennial': 'Centennial F.C.',
    'Cleveland B.': 'Cleveland Bruell Insurance',
    'Lucy Recs': 'Lusitania Recreation',
    'Hispano': 'Brooklyn Hispano',
    'J&P Coats': 'J & P Coats',
    'NY Giants': 'New York Giants',
    'Fleischer': 'Fleisher Yarn',
    'Fleischer Yarn': 'Fleisher Yarn',

    'Ben Miller FC': 'Ben Millers',
    'Ben Miller SC': 'Ben Millers',
    'Ben Miller A.C.': 'Ben Millers',
    
    'Bethlehewm Steel': 'Bethlehem Steel',

    'Chicago Bricklayers & Masons': 'Chicago Bricklayers',
    'Bricklayers': 'Chicago Bricklayers',
    'Chicago Bricklayers FC': 'Chicago Bricklayers',
    'Chicago Bricklayers SC': 'Chicago Bricklayers',
    'Bricklayers & Masons': 'Chicago Bricklayers',
    'Bricklayers & Masons FC': 'Chicago Bricklayers',
    'Bricklayers': 'Chicago Bricklayers',
    'Bricklayers (Chicago)': 'Chicago Bricklayers',
    'Bricklayers SC': 'Chicago Bricklayers',
    'Bricklayers FC': 'Chicago Bricklayers',
    
    'MacKenzie SC (Niagra Falls)': 'MacKenzie FC (Niagara Falls)',

    'Mahoning Valley FC': 'Mahoning Valley',

    # Cuddy is not Curry.
    'Cuddy': 'Cuddy AC',

    'Curry': 'Curry FC',
    'Curry FC': 'Curry Silver Tops',
    'Curry Vets': 'Curry FC',
    'Curry SC': 'Curry FC',
    'Curry S.C.': 'Curry FC',
    'Castle Shannon FC': 'Castle Shannon',

    'Bruell Hungarian': 'Bruell Hungarians',
    'Bruell Hungarians': 'Bruell Insurance',

    'Sparta (Chicago)': 'Chicago Sparta',
    'Sparta': 'Chicago Sparta',
    'Sparta FC': 'Chicago Sparta',
    'Sparta ABA': 'Chicago Sparta',
    'Sparta Leader': 'Chicago Sparta',
    'Sparta Garden City': 'Chicago Sparta',
    'Sparta Union': 'Chicago Sparta',
    'Chicago Sparta Falstaff': 'Chicago Sparta',
    'Sparta Ogden Dairy': 'Chicago Sparta',
    


    'Mid-Michigan Bucks': 'Michigan Bucks',

    'Los Angeles Kickers-Victoria (South California)': 'Los Angeles Kickers',
    
    

    'St. Louis Scullin Steel': 'Scullin Steel',
    'Stix, Baer & Fuller': 'Stix, Baer and Fuller F.C.',
    'Stix, Baer and Fuller': 'Stix, Baer and Fuller F.C.',
    'St. Louis Central Breweries F.C.': 'Central Breweries',
    'St. Louis Simpkins-Ford': 'Simpkins Ford',

    # Pretty sure this is correct.
    'Coca Cola (St. L)': 'Kavanaugh',
    'Coca Cola': 'Kavanaugh',

    'Tablers': 'Tablers FC',

    'Innisfall FC': 'Innisfails FC',
    'Innisfalls FC': 'Innisfails FC',
    'Innisfails': 'Innisfails FC',
    'Scullin Steel': 'Scullin Steels',
    'Vesper Buick': 'Vesper Buicks',
    'Wellston\'s': 'Wellston FC',
    'Hellrungs SC': 'Hellrungs',
    'Hellrungs FC': 'Hellrungs',
    
    'Brooklyn St. Mary\'s Celtic': 'St. Mary\'s Celtic',

    'Pawtucket Rngers': 'Pawtucket Rangers',

    'Raftery’s': 'Raftery Painters',

    'Chicago Viking': 'Chicago Viking A.A.',
    'Viking AA': 'Chicago Viking A.A.',
    'Viking A.A.': 'Chicago Viking A.A.',

    'Richhmond Kickers': 'Richmond Kickers',


    'San Fern. Valley Golden Eagles': 'San Fernando Valley Golden Eagles',
    'Valley Golden Eagles': 'San Fernando Valley Golden Eagles',
    'SFV Golden Eagles': 'San Fernando Valley Golden Eagles',

    'CD Mexico (North California)': 'El Farolito Soccer Club',
    'AAC Eagles': 'A.A.C. Eagles',
    'Greek American AC': 'Greek American A.C.',
    'Syracus Suns': 'Syracuse Suns',
    


    'Harmarville': 'Harmarville Hurricanes',

    'Kutis SC': 'St. Louis Kutis',
    'Kutis': 'St. Louis Kutis',
    

    'Ukrainian Nationals': 'Philadelphia Ukrainians',
    'Hungaria SC (East NY)': 'New York Hungaria',

    'Greek American SC (East NY)': 'Greek American AA',

    'Maccabee AC': 'Maccabi Los Angeles',

    'Club Espana (DC/VA)': 'Club Espana',

    'Busch SC': 'Busch SC (MO)',

    'HRC Kickers': 'St. Petersburg Kickers',
    'McCormick Kickers': 'St. Petersburg Kickers',

    'NY Greek American Atlas': 'Greek-American A.C.',

    'Marres': 'Marre\'s',
    'Marre': 'Marre\'s',
    'MacDuffs': 'MacDuff FC',
    'MacDuffs FC': 'MacDuff FC',

    'Morgan FC': 'Morgan Strasser',
    'Morgan SC': 'Morgan Strasser',
    'Morgan Haulers': 'Morgan Strasser',
    'Morgan Sport Club': 'Morgan Strasser',
    'Morgan': 'Morgan Strasser',
    
    'Gallatin F.C.': 'Pittsburgh Gallatin SC',
    'Gallatin Sport Club': 'Pittsburgh Gallatin SC',
    'Gallatin': 'Pittsburgh Gallatin SC',
    'Gallatin-Dunlevy': 'Pittsburgh Gallatin SC',
    'Gallatin FC': 'Pittsburgh Gallatin SC',
    'Gallatin SC': 'Pittsburgh Gallatin SC',
    'Gallatin Sport Clun': 'Pittsburgh Gallatin SC',
    
    'Falk Field Club (Mil.)': 'Falk Field Club',
    
    
    'Yugoslav Americnan SC': 'Yugoslav American SC',
    
    'Whitall Carpet Mill': 'Whittal F.C.',
    'Whittall Carpet Mill': 'Whittal F.C.',
    'Whittall Carpet Mills': 'Whittal F.C.',
    'Whittal Carpet Mill': 'Whittal F.C.',
    
    'White Auto FC': 'White Motor FC',
    'White Motors': 'White Motor FC',
    'White Auto': 'White Motor FC',
    'White Automobile': 'White Motor FC',
    'White Motor': 'White Motor FC',
    'White Motors FC': 'White Motor FC',
    
    'West End Polish FC': 'West End Polish Club',
    
    'True Blues FC': 'Paterson True Blues',
    
    'Abbott Worsted': 'Abbot Worsted',
    
    'Anderson SC': 'Anderson S.C.',
    
    'Babcock & Wilcaox': 'Babcock & Wilcox',
    'Babcock & Wilson': 'Babcock & Wilcox',
    'Babcock and Wilcox': 'Babcock & Wilcox',
    'Bayonne Babcock & Wilcox': 'Babcock & Wilcox',
    
    'Baltimore Pompei': 'Baltimore Pompei SC',
    'Beadling': 'Beadling SC',
    'Beadling FC': 'Beadling SC',
    'Beadlign FC': 'Beadling SC',
    


    
    'Passon FC': 'Philadelphia Passon',




    # Uh...might not be a good name to use Uhrik Truckers.
    'Philadelphia German-American': 'Uhrik Truckers',
    'Philadelphia German American': 'Uhrik Truckers',
    'Philadelphia Americans': 'Uhrik Truckers',

    # Not sure of these.
    'Hungaria': 'New York Hungaria', 
    'NY Greek-Americans Hellenic SC': 'Greek American AA',
    

    'Central Jersey Rpitide': 'Central Jersey Riptide',

    'Slavia Bartunek': 'Bartunek Slavia',
    'Rosenblum Slavia': 'Bartunek Slavia',
    'Cleveland Slavia': 'Bartunek Slavia',
    'Bartunek Clothes (Cle.)': 'Bartunek Slavia',
    

    'LA Blues': 'Los Angeles Blues',
    'Antigua Barricudas FC': 'Antigua Barracuda',
    'Dayton Dutch Lions FC': 'Dayton Dutch Lions',

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
    'NZL': 'New Zealand',
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


def get_team(name, competition=None, pre_dict={}):
    name = pre_dict.get(name, name)
        
    if competition is not None and (name, competition) in teams:
        name = teams[(name, competition)]
        return get_team(name, competition)

    if name in teams:
        return get_team(teams[name])


    return name
    
