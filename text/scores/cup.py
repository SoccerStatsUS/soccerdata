#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

# Process all historical US Open Cup scores pulled from TheCup.us

import datetime
import os


from soccerdata.alias import get_team

open_cup_filename = '/home/chris/www/soccerdata/data/scores/us_open_cup.txt'
american_cup_filename = '/home/chris/www/soccerdata/data/scores/american_cup.txt'

team_map = {
    'New York Freedoms (D3 Pro)': 'New York Freedoms',
    'Atlanta Silverbacks (A-League)': 'Atlanta Silverbacks',
    'Castle Shannon (W. Pa.)': 'Castle Shannon',
    'McCormick Kickers (FL)': 'McCormick Kickers',
    'HRC Kickers (FL)': 'HRC Kickers',

    'Chicago Fire (MLS)': 'Chicago Fire',
    'Colorado Rapids (MLS)': 'Colorado Rapids',
    'Columbus Crew (MLS)': 'Columbus Crew',
    'Dallas Burn (MLS)': 'Dallas Burn',
    'DC United (MLS)': 'DC United',
    'FC Dallas (MLS)': 'FC Dallas',
    'Houston Dynamo (MLS)': 'Houston Dynamo',
    'Kansas City Wizards (MLS)': 'Kansas City Wizards',
    'Miami Fusion (MLS)': 'Miami Fusion',
    'Miami Fusion ((MLS)': 'Miami Fusion',
    'Los Angeles Galaxy (MLS)': 'Los Angeles Galaxy',
    'New England Revolution (MLS)': 'New England Revolution',
    'New York Red Bulls (MLS)': 'New York Red Bulls',
    'Real Salt Lake (MLS)': 'Real Salt Lake',
    'San Jose Clash (MLS)': 'San Jose Clash',
    'San Jose Earthquakes (MLS)': 'San Jose Earthquakes',
    'San Joe Earthquakes (MLS)': 'San Joe Earthquakes',
    'Seattle Sounders (MLS)': 'Seattle Sounders',
    'Seattle Sounders FC (MLS)': 'Seattle Sounders FC',
    'Sporting Kansas City (MLS)': 'Sporting Kansas City',
    'Tampa Bay Mutiny (MLS)': 'Tampa Bay Mutiny',
    'Chivas USA (MLS)': 'Chivas USA',
    'LA Galaxy (MLS)': 'Los Angeles Galaxy',
    'Metrostars (MLS)': 'Metrostars',


    'Atlanta Ruckus (A-League)': 'Atlanta Ruckus',
    'California Jaguars (A-League)': 'California Jaguars',
    'Charleston Battery (A-League)': 'Charleston Batter',
    'Colorado Foxes (A-League)': 'Colorado Foxes',
    'Connecticut Wolves (A-League)': 'Connecticut Wolves',
    'El Paso Patriots (A-League)': 'El Paso Patriots',
    'Hampton Roads Mariners (A-Lg.)': 'Hampton Roads Mariners',
    'Hampton Roads Mariners (A-League)': 'Hampton Roads Mariners',
    'Hershey Wildcats (A-League)': 'Hershey Wildcats',
    'Jacksonville Cyclones (A-League)': 'Jacksonville Cyclones',
    'Milwaukee Rampage (A-League)': 'Milwaukee Rampage',
    'Milwaukee Wave United (A-League)': 'Milwaukee Wave United',
    'Minnesota Thunder (A-League)': 'Minnesota Thunder',
    'Nashville Metros (A-League)': 'Nashville Metros',
    'New Orleans Riverboat Gamblers (A-Lg.)': 'New Orleans Riverboat Gamblers',
    'New York Centaurs (A-League)': 'New York Centaurs',
    'New York Fever (A-League)': 'New York Fever',
    'Orange County Zodiac (A-League)': 'Orange County Zodiac',
    'Orlando Sundogs (A-League)': 'Orlando Sundogs',
    'Pittsburgh Riverhounds (A-League)': 'Pittsburgh Riverhounds',
    'Portland Timbers (A-League)': 'Portland Timbers',
    'Richmond Kickers (A-League)': 'Richmond Kickers',
    'Richhmond Kickers (A-League)': 'Richhmond Kickers',
    'Rochester Raging Rhinos (A-League)': 'Rochester Raging Rhinos',
    'Rochester Raging Rhinos (A-Lg.)': 'Rochester Raging Rhinos',
    'Rochester Raging Rhinos (A-Lg)': 'Rochester Raging Rhinos',
    'San Diego Flash (A-League)': 'San Diego Flash',
    'Seattle Sounders (A-League)': 'Seattle Sounders',
    'Staten Island Vipers (A-League)': 'Staten Island Vipers',
    'Syracuse Salty Dogs (A-League)': 'Syracuse Salty Dogs',
    'Virginia Beach Mariners (A-League)': 'Virginia Beach Mariners',
    'Worcester Wildfire (A-League)': 'Worcester Wildfire',

    'Carolina Dynamo (USISL Select)': 'Carolina Dynamo',
    'El Paso Patriots (USISL Select)': 'El Paso Patriots',

    'San Fern. Valley Golden Eagles (Pro)': 'San Fern. Valley Golden Eagles',
    'Connecticut Wolves (USISL Pro)': 'Connecticut Wolves',
    'Chicago Stingers (USISL Pro)': 'Chicago Stingers',
    'Chico Rooks (USISL Pro)': 'Chico Rooks',
    'Tampa Bay Cyclones (USISL Pro)': 'Tampa Bay Cyclones',
    'El Paso Patriots (USISL Pro)': 'El Paso Patriots',

    'Richmond Kickers (USISL Prem)': 'Richmond Kickers',

    'Atlanta Silverbacks (USL-1)': 'Atlanta Silverbacks',
    'Austin Aztex (USL-1)': 'Austin Aztex',
    'California Victory (USL-1)': 'California Victory',
    'Charleston Battery (USL-1)': 'Charleston Battery',
    'Cleveland City Stars (USL-1)': 'Cleveland City Stars',
    'Miami FC (USL-1)': 'Miami FC',
    'Miami FC Blues (USL-1)': 'Miami FC Blues',
    'Portland Timbers (USL-1)': 'Portland Timbers',
    'Seattle Sounders (USL-1)': 'Seattle Sounders',
    'Richmond Kickers (USL-1)': 'Richmond Kickers',
    'Rochester Rhinos (USL-1)': 'Rochester Rhinos',
    'Rochester Raging Rhinos (USL-1)': 'Rochester Raging Rhinos',
    'Virginia Beach Mariners (USL-1)': 'Virginia Beach Mariners',
    'Carolina RailHawks (USL-1)': 'Carolina RailHawks',

    'Carolina RailHawks (USSF D-2)': 'Carolina Railhawks',
    'Miami FC (USSF D-2)': 'Miami FC',
    'Portland Timbers (USSF D-2)':'Portland Timbers',
    'AC St. Louis (USSF D-2)': 'AC St. Louis',



    'Albuquerque Geckos (D3 Pro)': 'Albuquerque Geckos',
    'Arizona Sahuaros (D3 Pro)': 'Arizona Sahuaros',
    'Austin Lone Stars (D3 Pro)': 'Austin Lone Stars',
    'Cape Cod Crusaders (D3 Pro)': 'Cape Cod Crusaders',
    'Carolina Dynamo (D3 Pro)': 'Carolina Dynamo',
    'Charlotte Eagles (D3 Pro)': 'Charlotte Eagles',
    'Central Jersey Riptide (D3 Pro)': 'Central Jersey Riptide',
    'Chicago Stingers (D3 Pro)': 'Chicago Stingers',
    'Chico Rooks (D3 Pro)': 'Chico Rooks',
    'Delaware Wizards (D3 Pro)': 'Delaware Wizards',
    'Greenville Lions (D3 Pro)': 'Greenville Lions',
    'New Jersey Stallions (D3 Pro)': 'New Jersey Stallions',
    'New York Freedom (D3 Pro)': 'New York Freedom',
    'Northern Virginia Royals (D3 Pro)': 'Northern Virginia Royals',
    'Orlando Nighthawks (D3 Pro)': 'Orlando Nighthawks',
    'Philadelphia Freedom (D3 Pro)': 'Philadelphia Freedom',
    'Reading Rage (D3 Pro)': 'Reading Rage',
    'Rhode Island Stingrays (D3 Pro)': 'Rhode Island Stingrays',
    'Riverside County Elite (D3 Pro)': 'Riverside County Elite',
    'San Francisco Bay Seals (D3 Pro)': 'San Francisco Bay Seals',
    'San Diego Gauchos (D3 Pro)': 'San Diego Gauchos',
    'South Jersey Barons (D3 Pro)': 'South Jersey Barons',
    'Stanislaus United Cruisers (D3 Pro)': 'Stanislaus United Cruisers',
    'Texas Rattlers (D3 Pro)': 'Texas Rattlers',
    'Utah Blitzz (D3 Pro)': 'Utah Blitzz',
    'Western Mass Pioneers (D3 Pro)': 'Western Mass Pioneers',
    'Wilmington Hammerheads (D3 Pro)': 'Wilmington Hammerheads',


    'Carolina Dynamo (PSL)': 'Carolina Dynamo',
    'Charlotte Eagles (PSL)': 'Charlotte Eagles',
    'Long Island Rough Riders (PSL)': 'Long Island Rough Riders',
    'New Hampshire Phantoms (PSL)': 'New Hampshire Phantoms',
    'Reading Rage (PSL)': 'Reading Rage',
    'San Diego Gauchos (PSL)': 'San Diego Gauchos',
    'Utah Blitzz (PSL)': 'Utah Blitzz',
    'Wilmington Hammerheads (PSL)': 'Wilmington Hammerheads',
    'Western Mass Pioneers (PSL)': 'Western Mass Pioneers',

    'Charlotte Eagles (USL-2)': 'Charlotte Eagles',
    'Cincinnati Kings (USL-2)': 'Cincinnati Kings',
    'Cleveland City Stars (USL-2)': 'Cleveland City Stars',
    'Crystal Palace Baltimore (USL-2)': 'Crystal Palace Baltimore',
    'Long Island Rough Riders (USL-2)': 'Long Island Rough Riders',
    'Harrisburg City Islanders (USL-2)': 'Harrisburg City Islanders',
    'New Hampshire Phantoms (USL-2)': 'New Hampshire Phantoms',
    'Pittsburgh Riverhounds (USL-2)': 'Pittsburgh Riverhounds',
    'Real Maryland Monarchs (USL-2)': 'Real Maryland Monarchs',
    'Richmond Kickers (USL-2)': 'Richmond Kickers',
    'Western Mass Pioneers (USL-2)': 'Western Mass Pioneers',
    'Wilmington Hammerheads (USL-2)': 'Wilmington Hammerheads',



    'Charlotte Eagles (USL Pro)': 'Charlotte Eagles',
    'Orlando City SC (USL Pro)': 'Orlando City SC',
    'Pittsburgh Riverhounds (USL Pro)': 'Pittsburgh Riverhounds',
    'Richmond Kickers (USL Pro)': 'Richmond Kickers',
    'Rochester Rhinos (USL Pro)': 'Rochester Rhinos',

    'Central Coast Roadrunners (PDSL)': 'Central Coast Roadrunners',
    'Kansas City Brass (PDSL)': 'Kansas City Brass',
    'Lincoln Brigade (PDSL)': 'Lincoln Brigade',
    'Mid-Michigan Bucks (PDSL)': 'Mid-Michigan Bucks',


    'Boulder Rapids Reserve (PDL)': 'Boulder Rapids Reserve',
    'BYU Cougars (PDL)': 'BYU Cougars',
    'Cape Cod Crusaders (PDL)': 'Cape Cod Crusaders',
    'Carolina Dynamo (PDL)': 'Carolina Dynamo',
    'Cascade Surge (PDL)': 'Cascade Surge',
    'Chesapeake Dragons (PDL)': 'Chesapeake Dragons',
    'Des Moines Menace (PDL)': 'Des Moines Menace',
    'El Paso Patriots (PDL)': 'El Paso Patriots',
    'Fredericksburg Gunners (PDL)': 'Fredericksburg Gunners',
    'Kitsap Pumas (PDL)': 'Kitsap Pumas',
    'Laredo Heat (PDL)': 'Laredo Heat',
    'Mid-Michigan Bucks (PDL)': 'Mid-Michigan Bucks',
    'Michigan Bucks (PDL)': 'Michigan Bucks',
    'Ocean City Barons (PDL)': 'Ocean City Barons',
    'Ventura County Fusion (PDL)': 'Ventura County Fusion',
    'Western Mass Pioneers (PDL)': 'Western Mass Pioneers',

    'Central Florida Kraze (PDL)': 'Central Florida Kraze',
    'Los Angeles Legends (PDL)': 'Los Angeles Legends',
    'Richmond Kickers Future (PDL)': 'Richmond Kickers Future',
    'Sonoma County Sol (PDL)': 'Sonoma County Sol',


    'AAC Eagles (USASA)': 'AAC Eagles',
    'Aegean Hawks FC (USASA)': 'Aegean Hawks FC',
    'Allied SC (USASA)': 'Allied SC',
    'ASC New Stars (USASA)': 'ASC New Stars',
    'Azzurri (USASA)': 'Azzurri',
    'Bavarian SC (USASA)': 'Bavarian SC',
    'Boston Olympiakos (USASA)': 'Boston Olympiakos',
    'Bridgeport Italians (USASA)': 'Bridgeport Italians',
    'Dallas Mustang Legends (USASA)': 'Dallas Mustang Legends',
    'Dallas Mustang Legends (USASA)': 'Dallas Mustang Legends',
    'Dallas Roma FC (USASA)': 'Dallas Roma FC',
    'Legends FC (USASA)': 'Legends FC',
    'Los Lobos (USASA)': 'Los Lobos',
    'Lynch’s FC (USASA)': 'Lynch’s FC',
    'Mexico SC (USASA)': 'Mexico SC',
    'Milford International (USASA)': 'Milford International',
    'NY Pancyprian Freedoms (USASA)': 'NY Pancyprian Freedoms',
    'NY Greek American Atlas (USASA)': 'NY Greek American Atlas',
    'Real Madrid (TX) (USASA)': 'Real Madrid (TX)',
    'Sacramento Knights (USASA)': 'Sacramento Knights',
    'San Jose Oaks (USASA)': 'San Jose Oaks',
    'Sonoma County Sol (USASA)': 'Sonoma County Sol',
    'Spartans SC (USASA)': 'Spartans SC',
    'Uruguay SC (USASA)': 'Uruguay SC',

    'Brooklyn Italians (USASA)': 'Brooklyn Italians',
    'Emigrantes Das Ilhas (USASA)': 'Emigrantes Das Ilhas',

    'United German Hungarians (USASA)': 'United German Hungarians',
    'Reggae Boyz FC (USASA)': 'Reggae Boyz FC',
    'Hollywood United (USASA)': 'Hollywood United',
    'Arizona Sahuaros (USASA)': 'Arizona Sahuaros',
    'Croatian Eagles (USASA)': 'Croatian Eagles',
    'McCormick Kickers (USASA)': 'McCormick Kickers',
    'Regals FC (USASA)': 'Regals FC',
    'Mequon United (USASA)': 'Mequon United',
    'SAC Wisla (USASA)': 'SAC Wisla',
    'Clearwater Galactics (USASA)': 'Clearwater Galactics',
    'RWB Adria (USASA)': 'RWB Adria',
    'Danbury United (USASA)': 'Danbury United',
    'Olympia Stamford (USASA)': 'Olympia Stamford',
    'Baltimore Colts FC (USASA)': 'Baltimore Colts FC',
    'Salinas Valley Samba (USASA)': 'Salinas Valley Samba',
    'Detroit United (USASA)': 'Detroit United',
    'Chaldean Arsenal (USASA)': 'Chaldean Arsenal',
    'Doxa Italia (USASA)': 'Doxa Italia',
    'CASL Elite (USASA)': 'CASL Elite',
    'Chicago Lightning (USASA)': 'Chicago Lightning',
    'Phoenix SC (USASA)': 'Phoenix SC',
    'Atlanta FC (USASA)': 'Atlanta FC',
    'Jerry D’s (USASA)': 'Jerry D’s',
    'DV8 Defenders (USASA)': 'DV8 Defenders',
    'Banat Arsenal (USASA)': 'Banat Arsenal',
    'KC Athletics (USASA)': 'KC Athletics',
    'El Paso Indios USA (USASA)': 'El Paso Indios USA',
    'Iowa Menace (USASA)': 'Iowa Menace',
    'DS United (USASA)': 'DS United',
    '402 (USASA)': '402',
    'Chico Rooks (USASA)': 'Chico Rooks',
    'Mo’s Sport Shop (USASA)': 'Mo’s Sport Shop',
    
    'Fresno Fuego (PDL)': 'Fresno Fuego',
    'Cocoa Expos (PDL)': 'Cocoa Expos',
    'Raleigh CASL Elite (PDL)': 'Raleigh CASL Elite',
    
    'Austin Aztex (USSF D-2)': 'Austin Aztex',
    'Wilmington Hammerheads (USL Pro)': 'Wilmington Hammerheads',
    'Chicago Fire Reserves (PDL)': 'Chicago Fire Reserves',
    'Chicago Fire PDL (PDL)': 'Chicago Fire PDL',
    'Seattle Sounders Select (PDL)': 'Seattle Sounders Select',
    
    'Raftery Painters (St. L)': 'Raftery Painters',
    
    'MacDuff FC (Chicago)': 'MacDuff FC',

    'Sparta SC (Chi.)': 'Sparta (Chicago)',
    'Bricklayers SC (Chi.)': 'Bricklayers SC',
    'Ansonia FC (CT)': 'Ansonia FC',
    'Ansonia FC (Conn.)': 'Ansonia FC',
    '` Miami FC (USSF D-2)': 'Miami FC',
    'Madison Kennels (St. L)': 'Madison Kennels',
    'Memphis Express (PDL)': 'Memphis Express',
    'Real Colorado Foxes (PDL)': 'Real Colorado Foxes',
    'DFW Tornadoes (PDL)': 'DFW Tornadoes',
    'Chicago Fire (PDL)': 'Chicago Fire PDL',
    'Spokane Shadow (PDL)': 'Spokane Shadow',
    'South Jersey Barons (PDL)': 'South Jersey Barons',
    'Chicago Fire Premier (PDL)': 'Chicago Fire Premier',
    'New York Freedoms (PDL)': 'New York Freedoms',
    'San Gabriel Valley Highlanders (PDL)': 'San Gabriel Valley Highlanders',
    'Austin Aztex U23s (PDL)': 'Austin Aztex U23s',
    'Chico Rooks (PDL)': 'Chico Rooks',
    'Central Coast Roadrunners (PDL)': 'Central Coast Roadrunners',
    'Bakersfield Brigade (PDL)': 'Bakersfield Brigade',
    'Bradenton Academics (PDL)': 'Bradenton Academics',
    'Brooklyn Knights (PDL)': 'Brooklyn Knights',
    'Chivas El Paso Patriots (PDL)': 'Chivas El Paso Patriots',
    'Dayton Dutch Lions (PDL)': 'Dayton Dutch Lions',
    'Miami Strike Force (PDL)': 'Miami Strike Force',
    'Mississippi Brilla (PDL)': 'Mississippi Brilla',
    'Ogden Outlaws (PDL)': 'Ogden Outlaws',
    'Orange County Blue Star (PDL)': 'Orange County Blue Star',
    'Reading Rage (PDL)': 'Reading Rage',
    'Reading United (PDL)': 'Reading United',
    'St. Louis Lions (PDL)': 'St. Louis Lions',
    'Texas Spurs (PDL)': 'Texas Spurs',
    'Virginia Beach Submariners (PDL)': 'Virginia Beach Submariners',
    'Yakima Reds (PDL)': 'Yakima Reds (PDL)',
    
    'Long Island Rough Riders (A-League)': 'Long Island Rough Riders',
    'Tennessee Rhythm (A-League)': 'Tennessee Rhythm',
    
    'Charleston Battery (USL-2)': 'Charleston Battery',
    'Los Angeles Blues (USL Pro)': 'Los Angeles Blues',
    'Wilmington Hammerheads (USL Pro)': 'Wilmington Hammerheads',
    'Charleston Battery (USL Pro)': 'Charleston Battery',
    'Charleston Battery (USL-Pro)': 'Charleston Battery',
    
    'Ben Miller FC (Muny)': 'Ben Miller FC',

    'Long Island Rough Riders (PDL)': 'Long Island Rough Riders',
    'FC New York (USL Pro)': 'FC New York',
    'Minnesota Thunder (USL-1)': 'Minnesota Thunder',

    'Hollywood United (NPSL)': 'Hollywood United',
    

    'Cuddy (W. Pa.)': 'Cuddy',
    'Bartunek Slavia (Cle.)': 'Bartunek Slavia',
    
    

    'Dallas Mean Green (North TX)': 'Dallas Mean Green',
    'Dallas Rockets (North TX)': 'Dallas Rockets',
    'Dallas Strikers (North TX)': 'Dallas Strikers',
    'Wichita Falls Fever (North TX)': 'Wichita Falls Fever',
    'Richardson Rockets (North TX)': 'Richardson Rockets',
    'Dallas Inter (North TX)': 'Dallas Inter',

    'Tucson Amigos (PDSL)': 'Tucson Amigos',

    'Galveston Norte America (South TX)': 'Galveston Norte America',
    'Austin Soccadillos (South TX)': 'Austin Soccadillos',

    'Los Angeles Kickers (South CA)': 'Los Angeles Kickers',

    'Real Maryland Monarchs (USL-2)': 'Real Maryland Monarchs',
    'San Gabriel Valley Highlanders (PDSL)': 'San Gabriel Valley Highlanders',
    'Dayton Dutch Lions (USL Pro)': 'Dayton Dutch Lions',
    'Harrisburg City Islanders (USL Pro)': 'Harrisburg City Islanders',


    'Uprising SC (DC/VA)': 'Uprising SC',

    'New Mexico Chiles (NM)': 'New Mexico Chiles',

    'Simpkins Ford (MO)': 'Simpkins Ford',
    'Simpkins Ford (St. L)': 'Simpkins Ford',
    'Minit Rubs (St. L)': 'Minit Rubs',
    'Michelob SC (MO)': 'Michelob SC',
    
    'Bay Area Ambassadors (USASA)': 'Bay Area Ambassadors',


    'Bethlehem Steel (Bal.)': 'Bethlehem Steel',
    'Batchelors Café (Bal.)': 'Batchelors Café',
    

    'St. Gerard (Bal.)': 'St. Gerard',
    'Canton SC (Bal.)': 'Canton SC',
    'Canton FC (Bal.)': 'Canton FC',
    'Canton SC (Balt.)': 'Canton SC',
    'Davis SC (Bal.)': 'Davis SC (Baltimore)',
    'Hasslinger SC (Bal.)': 'Hasslinger SC',
    'Bethlehem Steel (Balt.)': 'Bethlehem Steel',
    'Ruggiero SC (Bal.)': 'Ruggiero SC',


    'Becks German American SC (Buf.)': 'Becks German American SC',
    'Hungarian FC (Buff.)': 'Hungarian FC (Buffalo)',

    'Bricklayers & Masons (Chi.)': 'Bricklayers & Masons',
    'Bricklayers & Masons FC (Chi.)': 'Bricklayers & Masons FC',
    'Bricklayers FC (Chi.)': 'Bricklayers FC',
    'Bricklayers (Chi.)': 'Bricklayers (Chicago)',
    'Canadian Club (Chi.)': 'Canadian Club (Chicago)',
    'Campbell Rovers (Chi.)': 'Campbell Rovers (Chicago)',
    'Carpenters FC (Chi.)': 'Carpenters FC (Chicago)',
    'Chicago Kickers (IL)': 'Chicago Kickers',
    'Hyde Park Blues (Chi.)': 'Hyde Park Blues',
    'Maccabee (Chi.)': 'Maccabee (Chicago)',
    'Maccabee SC (Chi.)': 'Maccabee SC (Chicago)',
    'MacDuff FC (Chi.)': 'MacDuff FC (Chicago)',
    'Norwegian American SC (Chi.)': 'Norwegian American SC (Chicago)',
    'Pullman FC (Chi.)': 'Pullman FC',
    'Olympia FC (Chi.)': 'Olympia FC (Chicago)',
    'Olympia SC (Chi.)': 'Olympia SC (Chicago)',
    'Scottish American FC (Chi.)': 'Scottish American FC (Chicago)',
    'Slovak SC (Chi.)': 'Slovak SC',
    'Sparta (Chi.)': 'Sparta (Chicago)',
    'Sparta FC (Chi.)': 'Sparta FC (Chicago)',
    'Sparta A & BA (Chi.)': 'Sparta (Chicago)',
    'Sparta A & BA': 'Sparta (Chicago)',
    'Sparta Leaders (Chi.)': 'Sparta Leaders (Chicago)',
    'Sparta Leader (Chi.)': 'Sparta Leader (Chicago)',
    'Sparta Ogden Dairy (Chi.)': 'Sparta Ogden Dairy (Chicago)',
    'Swedish American SC (Chi.)': 'Swedish American SC (Chicago)',
    'Thistles FC (Chi.)': 'Thistles FC (Chicago)',
    'Thistle FC (Chi.)': 'Thistle FC (Chicago)',
    'Viking A.A. (Chi.)': 'Viking A.A.',
    'Viking AA (Chi.)': 'Viking AA',
    'Yugoslav American SC (Chi.)': 'Yugoslav American SC (Chicago)',
    'Weiboldt Wonderbolts (Chi.)': 'Weiboldt Wonderbolts',


    'American Hungarian FC (Cle.)': 'American Hungarian FC (Cleveland)',
    'Banat German Sports (Cle.)': 'Banat German Sports (Cleveland)',
    'Bartunek Clothes (Cle.)': 'Bartunek Clothes (Cleveland)',
    'Bricklayers FC (Cle.)': 'Bricklayers FC (Cleveland)',
    'British War Veterans (Cle.)': 'British War Veterans (Cleveland)',
    'Bruell Insurance (Cle.)': 'Bruell Insurance',
    'Bruell Hungarian (Cle.)': 'Bruell Hungarian',
    'Bruell Hungarians (Cle.)': 'Bruell Hungarians',
    'Dalarda SC (Cle.)': 'Dalarda SC',
    'Dalarda (Cle.)': 'Dalarda',
    'Thistle FC (Cle.)': 'Thistle FC (Cleveland)',
    'Thistles FC (Cle.)': 'Thistles FC (Cleveland)',
    'Magyar American FC (Cle.)': 'Magyar American FC (Cleveland)',
    'Rosenblum Slavia (Cle.)': 'Rosenblum Slavia',
    'Schwaben (Chi.)': 'Schwaben (Chicago)',
    'Shamrocks SC (Cle.)': 'Shamrocks SC (Cleveland)',
    'Shamrock SC (Cle.)': 'Shamrock SC (Cleveland)',
    'Cleveland Kickers (North OH)': 'Cleveland Kickers',
    'Mahoning Valley FC (OH)': 'Mahoning Valley FC',
    


    'Danersk FC (CT)': 'Danersk FC',
    'Vasco Da Gama (CT)': 'Vasco Da Gama (Connecticut)',

    'All Scots FC (Det.)': 'All Scots FC (Detroit)',
    'Caledonia FC (Det.)': 'Caledonia FC (Detroit)',
    'Chrysler SC (Det.)': 'Chrysler SC',
    'Packard FC (Det.)': 'Packard FC',
    'Flandria SC (Det.)': 'Flandria SC',
    'Gar Wood SC (Det.)': 'Gar Wood SC',
    'Roses FC (Det.)': 'Roses FC (Detroit)',
    'Thistles SC (Det.)': 'Thistles SC (Detroit)',
    'Wood Hydraulic (Det.)': 'Wood Hydraulic',
    'Holley Carburetor (Det.)': 'Holley Carburetor',
    'United German AA (Det.)': 'United German AA (Detroit)',
    'Pioneer Kickers (Det.)': 'Pioneer Kickers',



    'Gillespie SC (Ill.)': 'Gillespie SC',
    'Schwaben SC (IL)': 'Schwaben SC',
    'Falcons SC (IL)': 'Falcons SC',
    'AAC Eagles (IL)': 'AAC Eagles',
    
    # The same?
    'Harvey FC (Ill.)': 'Harvey FC (Illinois)',
    'Buda A.A. (Harvey, Ill.)': 'Buda A.A. (Illinois)',
    'Buda A.A. (Ill.)': 'Buda A.A. (Illinois)',
    'Lions SC (IL)': 'Lions SC (Illinois)',
    'Chicago Lions (IL)': 'Chicago Lions (Illinois)',
    'Hansa (IL)': 'Hansa (Illinois)',

    'Indianapolis Inferno (IN)': 'Indianapolis Inferno',

    'Louisville Alliance (KY)': 'Louisville Alliance',

    'Kutis SC (MO)': 'Kutis SC',
    'Kutis SC (St. Louis, MO)': 'Kutis SC',
    
    'Scottish American FC (NJ)': 'Scottish American FC (New Jersey)',
    'Bayonne FC (NJ)': 'Bayonne FC (New Jersey)',

    'Maccabee AC (Los Angeles, CA)': 'Maccabee AC',
    
    'Boston Metros (MA)': 'Boston Metros',
    'Fall River SC (MA)': 'Fall River SC',
    'Ponta Delgada (MA)': 'Ponta Delgada',

    'Baltimore Pompei SC (MD)': 'Baltimore Pompei SC',
    'Baltimore Pompei (MD)': 'Baltimore Pompei',

    'Flint IMA (Mich.)': 'Flint IMA',
    'Ukrainian SC (MI)': 'Ukrainian SC (Michigan)',
    'St. Andrews (MI)': 'St. Andrews (Michigan',
    'Detroit Kickers (MI)': 'Detroit Kickers',

    'Deutscher Sport Club (Mil.)': 'Deutscher Sport Club',
    'Schlitz SC (Mil.)': 'Schlitz SC',
    'Wacker FC (Mil.)': 'Wacker FC',
    'Falk Field Club (Mil.)': 'Falk Field Club (Milwaukee)',
    'Schwaben (Mil.)': 'Schwaben (Milwaukee)',
    

    'Brookhattan (NYC)': 'Brookhattan',
    'I.R.T. Celtics (NYC)': 'I.R.T. Celtics',
    'New York Hakoah (East NY)': 'New York Hakoah',
    'Brooklyn Hispano (East NY)': 'Brooklyn Hispano',
    'Brooklyn Italians (East NY)': 'Brooklyn Italians',
    'New York Americans (East NY)': 'New York Americans',
    'NY Pancyprian Freedoms (East NY)': 'NY Pancyprian Freedoms',
    'Galicia SC (NYC)': 'Galicia SC',
    'Tappen Post (NYC)': 'Tappen Post',
    'Kollsman (NYC)': 'Kollsman',
    'Inter-Giuliana (New York, NY)': 'Inter-Giuliana',
    'NY Greek American Atlas (East NY)': 'NY Greek American Atlas',


    'San Francisco AC (North CA)': 'San Francisco AC',
    'CD Mexico (North CA)': 'CD Mexico (North California)',
    'Teutonis SC (North CA)': 'Teutonis SC (North California)',
    'San Francisco Scots (North CA)': 'San Francisco Scots',
    'Greek American AC (North CA)': 'Greek American AC',
    'San Jose Oaks (North CA)': 'San Jose Oaks',

    'Lorain Eagles (Oh.)': 'Lorain Eagles (Ohio)',

    'Centennial FC (Phi.)': 'Centennial FC',
    'Kensington Blue Bells (Phi.)': 'Kensington Blue Bells',
    'German American SC (Phi.)': 'German American SC (Philadelphia)',
    'German SC (Phi.)': 'German SC (Philadelphia)',
    'Fairhill FC (Phi.)': 'Fairhill FC',
    'Fairhill (Phi.)': 'Fairhill',
    'Passon SC (Phi.)': 'Passon SC',
    'Philadelphia Nationals (East PA)': 'Philadelphia Nationals',
    'United German Hungarians (East PA)': 'United German Hungarians',
    'Uhrik Truckers (East PA)': 'Uhrik Truckers',



    'Curry SC (W. Pa.)': 'Curry SC',


    'Curry (Pit.)': 'Curry',
    'Curry Silver Tops (Pit.)': 'Curry Silver Tops (Pittsburg)',
    'Gallatin Sport Club (Pit.)': 'Gallatin Sport Club (Pittsburg)',
    'Jeanette FC (Pit.)': 'Jeanette FC',
    'Pierpoints FC (Pit.)': 'Pierpoints FC',
    'Morgan FC (Pit.)': 'Morgan FC',
    'Morgan (Pit.)': 'Morgan',
    'Morgan Strasser (Pit.)': 'Morgan Strasser',
    'Morgan USCO (Pit.)': 'Morgan USCO',
    'Vestaburg SC (Pit.)': 'Vestaburg SC (Pittsburg)',
    'Curry Vets (W. Pa.)': 'Curry Vets',
    'Curry SC (W. Pa.)': 'Curry SC',
    'Castle Shannon (West PA)': 'Castle Shannon',

    'German AC (Roch.)': 'German AC (Rochester)',

    'Exiles SC (South CA)': 'Exiles SC',
    'McIlvaine Canvasbacks (South CA)': 'McIlvaine Canvasbacks',
    'United Scots (South CA)': 'United Scots (South Californai)',
    'Magyar SC (South CA)': 'Magyar SC (South California)',
    'Orange County SC (South CA)': 'Orange County SC',
    'Los Angeles Kickers-Victoria (South California)': 'Los Angeles Kickers-Victoria',
    
    
    'Armenian SC (South CA)': 'Armenian SC (South California)',
    'Los Angeles Kickers-Victoria (So CA)': 'Los Angeles Kickers-Victoria (South California)',

    'Andersons (St. L)': 'Andersons',
    'Ben Miller SC (St. L)': 'Ben Miller SC',
    'Ben Miller FC (St. L)': 'Ben Miller SC',
    'Ben Miller A.C. (St. L)': 'Ben Miller A.C.',
    'Busch SC (MO)': 'Busch SC',
    'Central Brewewries (St. L)': 'Central Brewewries',
    'Coca Cola (St. L)': 'Coca Cola',
    'Correnti Cleaners (St. L)': 'Correnti Cleaners',
    'Hellrungs FC (St. L)': 'Hellrungs FC',
    'Hellrung SC (St. L)': 'Hellrungs SC',
    'Hellrung Grimm (St. L)': 'Hellrung Grimm',
    'Kavanaugh (St. L)': 'Kavanaugh',
    'Marres (St. L)': 'Marres',
    'Madison Kennel SC (St. L)': 'Madison Kennel SC',
    'Morgan Haulers (St. L)': 'Morgan Haulers',
    'Natural Setups (St. L)': 'Natural Setups',
    'Norwegian American SC (St. L)': 'Norwegian American SC (St. Louis)',
    'Pants Store FC (St. L)': 'Pants Store FC',
    'Royalton Stars (St. L)': 'Royalton Stars',
    'Stix, Baer & Fuller (St. L)': 'Stix, Baer & Fuller',
    'Tablers FC (St. L)': 'Tablers FC',
    'Tablers SC (St. L)': 'Tablers SC',
    'Vesper Buick (St. L)': 'Vesper Buick',
    'Wellston FC (St. L)': 'Wellston FC',
    'White Banner Malt (St. L)': 'White Banner Malt',
    'Scott Gallagher (MO)': 'Scott Gallagher',

    'Hungarian SC (WA)': 'Hungarian SC (Washington)',
    'Mitre Eagles (WA)': 'Mitre Eagles',

    'Kenosha FC (Wis.)': 'Kenosha FC (Wisconsin)',
    'Bavarian SC (WI)': 'Bavarian SC (Wisconsin)',
    'Madison 56ers (WI)': 'Madison 56ers',

    'Glendale (W. Pa.)': 'Glendale',
    'Morgan Strasser (West PA)': 'Morgan Strasser',
    'Morgan Strasser (W. Pa.)': 'Morgan Strasser',
    'Morgan Sport Club (W. Pa.)': 'Morgan Sport Club',
    'Harmarville (W. Pa.)': 'Harmarville',
    'Harmarville Hurricanes (West PA)': 'Harmarville Hurricanes',
    'Beadling (West PA)': 'Beadling',

    'Heidelberg (W. Pa.)': 'Heidelberg',
    'Heidelberg (Pit.)': 'Heidelberg',

    'Gallatin (W. Pa.)': 'Gallatin',
    'Gallatin Sport Club (Pittsburg)': 'Gallatin',
    'Canonsburg (W. Pa.)': 'Canonsburg',
    'Curry (W. Pa.)': 'Curry',
    'Beadling SC (West PA)': 'Beadling SC',

    'Pfaelzer (NYC)': 'Pfaelzer',

    'Kearny Irish (NJ)': 'Kearny Irish',
    'German American SC (Phi.)': 'German American SC',
    'FC Porto (NJ)': 'FC Porto (New Jersey)',

    'Houston Meadows (South TX)': 'Houston Meadows',
    'Ukrainian Nationals (East PA)': 'Ukrainian Nationals',
    'Philadelphia Inter (East PA)': 'Philadelphia Inter',
    'Vereinigung Erzgebirge (East PA)': 'Vereinigung Erzgebirge',
    'S.A. Healey (NY)': 'S.A. Healey',

    'Eintracht SC (NYC)': 'Eintracht SC',
    'Atlanta Datagraphics (GA)': 'Atlanta Datagraphics',

    'Danish American SC (South CA)': 'Danish American SC',
    'Heidelberg SC (West PA)': 'Heidelberg SC',
    'Ludlow Lusitano (MA)': 'Ludlow Lusitano',
    'Cambridge Faialense (MA)': 'Cambridge Faialense',
    'St. Michaels (Mass.)': 'St. Michaels (Massachusetts)',
    'Prague SC (NYC)': 'Prague SC (NYC)',
    

    
    }

def process_open_cup_games():
    return process_games(open_cup_filename)


def process_american_cup_games():
    return process_games(american_cup_filename)


def process_games(fn):
    l = []
    for dx in process_games2(fn):
        d = dx.copy()
        d['home_team'] = d.pop('t1')
        d['home_score'] = d.pop('s1')
        d['away_team'] = d.pop('t2')
        d['away_score'] = d.pop('s2')
        l.append(d)
    return l

def process_games2(fn):
    f = open(fn)
    l = []
    gp = GameProcessor(fn)
    for line in f:
        g = gp.consume_row(line)
        if g:
            l.append(g)
    return l



class GameProcessor(object):
    def __init__(self, path):

        self.filename = os.path.split(path)[1]

        self.season = None

    def get_competition(self):
        d = {
            'us_open_cup.txt': 'Lamar Hunt U.S. Open Cup',
            'american_cup.txt': 'American Cup'
            }

        try:
            return d[self.filename]
        except:
            import pdb; pdb.set_trace()
        pass
        

    def process_score(self, s):
        if "(" in s:
            s, extra = s.split("(")
            extra = extra.replace(")", '').strip()
        else:
            extra = None

        if s == "w/o":
            return None, None

        if s== "?":
            return None, None
        

        if ":" in s:
            s1, s2 = s.split(":")
        else:
            try:
                s1, s2 = s.split("-")
            except:
                import pdb; pdb.set_trace()

        # Coerce to an integer if possible.
        try:
            return int(s1), int(s2)
        except ValueError:
            return s1, s2

        

    def consume_row(self, row):
        row = row.strip()

        if row.startswith("Season:"):
            self.season = int(row.split("Season:")[1].strip())

        elif row.startswith("*"):
            pass

        # A note or a competition/season type
        elif ";" not in row:
            pass

        else:
            fields = [e.strip() for e in row.split(";")]

            if fields[0]:
                if ',' in  fields[0]:
                    dx, hour = fields[0].split(",")
                    hour = int(hour)
                else:
                    dx, hour = fields[0], None

                try:
                    month, day, year = dx.split("/")
                except:
                    import pdb; pdb.set_trace()

                if len(year) == 2:
                    year = "19" + year

                # Skip over data bug.
                if month == '11' and day == '31':
                    return

                if day == "?":
                    d = None
                else:
                    try:
                        d = datetime.datetime(int(year), int(month), int(day))
                    except:
                        import pdb; pdb.set_trace()

            else:
                d = None

            if len(fields) < 4:
                print fields
                return

            t1, score, t2 = fields[1:4]
            s1, s2 = self.process_score(score)
            
            rest = fields[4:]

            stadium = location = attendance = None

            if len(rest) == 0:
                pass

            elif len(rest) == 1:
                location = rest[0]

            elif len(rest) == 2:
                stadium, location = rest

            elif len(rest) == 3:
                stadium, location, attendance = rest

            elif len(rest) == 4:
                stadium, location,referee, attendance = rest

            else:
                import pdb; pdb.set_trace()

            # For now, don't return games without scores. (e.g. W-L)
            if not type(s1) == int:
                return

            t1 = team_map.get(t1, t1)
            t2 = team_map.get(t2, t2)
                
            return {
                    't1': get_team(t1),
                    't2': get_team(t2),
                    's1': s1,
                    's2': s2,
                    'date': d,
                    #'stadium': stadium,
                    #'location': location,
                    'attendance': attendance,
                    'season': self.season,
                    'competition': self.get_competition(),
                    'source': 'TheCup.us',
                    }
                    

if __name__ == "__main__":
    print process_american_cup_games()
