#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

teams = {}


alternate_names = {
    'Toronto Supra Portuguese': 'Toronto Supra',
    "Vancouver 86ers": "Vancouver Whitecaps FC",
    "Golden Bay Earthquakes": "San Jose Earthquakes",
    'NY Pancyprian-Freedoms': 'New York Pancyprian-Freedoms',
    'NY Pancyprian Freedoms': 'New York Pancyprian-Freedoms',
    'Atlanta Datagraphic Magic': 'Atlanta Magic',
    'Atlanta Datagraphic': 'Atlanta Magic',
    'San Jose Clash': 'San Jose Earthquakes',
    'Dallas Burn': 'FC Dallas',
    'Seattle Sounders FC': 'Seattle Sounders',
    'Carolina Railhawks': 'Carolina RailHawks',
    'Phoenix Hearts': 'Arizona Sahuaros',
    'Arizona Cotton': 'Arizona Sahuaros',
    'Arizona Phoenix': 'Arizona Sahuaros',
}
teams.update(alternate_names)

world = {
    
    'Atlante FC': 'Atlante F.C.',
    'Atlante': 'Atlante F.C.',
    'Nacional': 'Club Nacional de Football',
    'Marathon': 'Marathón',
    'Splitdorf FC': 'Splitdorf F.C',
    'Real Espana': 'Real España',

    'Clan Mackenzie FC (Akron)': 'Clan MacKenzie FC (Akron)',
    'Americus AA': 'Americus A.A.',
    'St George FC': 'St. George F.C',

    
    'Wolverhampton': 'Wolverhampton Wanderers F.C.',
    'Schalke 04': 'FC Schalke 04',

    'Asturias': 'Club de Fútbol Asturias',

    'Belgrano': 'Club Atlético Belgrano',




    'Roma': 'A.S. Roma',
    'KS Ruch': 'K.S. Ruch',
    'V.F.B. Stuttgart': 'VfB Stuttgart',
    
    
    'Besiktas': 'Beşiktaş J.K.',
    'Bologna': 'Bologna F.C. 1909',
    'Fenerbahce': 'Fenerbahçe S.K.',
    'Ferencvaros': 'Ferencvárosi TC',
    'Aston Villa': 'Aston Villa F.C.',
    'Bodo/Glimt': 'FK Bodø/Glimt',
    'Napoli': 'S.S.C. Napoli',
    'Newcastle': 'Newcastle United F.C.',
    'Newcastle United': 'Newcastle United F.C.',
    'Nottingham Forest': 'Nottingham Forest F.C.',
    'Norwich City': 'Norwich City F.C.',
    'Orebro': 'Örebro SK',
    'Paris St.-Germain': 'Paris Saint-Germain F.C.',
    'Antwerp': 'Royal Antwerp F.C.',
    'Preston North End': 'Preston North End F.C.',
    'Hearts': 'Hearts of Midlothian F.C.',
    'Hearts of Midlothian': 'Hearts of Midlothian F.C.',
    'Independiente': 'CA Independiente',
    'Manchester City': 'Manchester City F.C.',
    'Mariitimo': 'C.S. Maritimo',
    'Millionarios': 'Millionarios FC',
    'Penarol': 'C.A. Peñarol',
    'Plymouth Argyle': 'Plymouth Argyle F.C.',
    
    
    
    'Sporting Lisbon': 'Sporting Clube de Portugal',
    'Benfica': 'S.L. Benfica',

    'TSC Muenchen 1860': 'TSV 1860 München',
    'Tigres UANL': 'Tigres de la UANL',
    'UANL Tigres': 'Tigres de la UANL',
    'Tecos': 'Estudiantes Tecos',
    'UAG': 'Estudiantes Tecos',
    'UAG Tecos': 'Estudiantes Tecos',
    'Racing (Argentina)': 'Racing Club de Avellaneda',
    'Racing Club (Argentina)': 'Racing Club de Avellaneda',
    'Reggina': 'Reggina Calcio',
    'CD Guadalajara': 'C.D. Guadalajara Chivas',
    'Celtic F.C.': 'Glasgow Celtic F.C.',
    'Celtic FC': 'Glasgow Celtic F.C.',
    

    'Birmingham City': 'Birmingham City F.C.',

    'Huddersfield Town': 'Huddersfield Town F.C.',
    'Rapid Wien': 'Rapid Vienna',
    'Young Boys\' Club': 'BSC Young Boys',
    'Wisla Krakov': 'Wisła Kraków',
    'Bari': 'A.S. Bari',

    'Deportivo Atlas': 'Club Atlas',
    'Atlas': 'Club Atlas',
    'Everton': 'Everton F.C.',
    'Sunderland': 'Sunderland A.F.C.',
    'Sampdoria': 'U.C. Sampdoria',
    'Saarbrucken': '1. FC Saarbrücken',
    'Saarbruecken': '1. FC Saarbrücken',
    

    'Comunicaciones': 'C.S.D. Comunicaciones',
    'Alajuelense': 'L.D. Alajuelense',

    'Leeds United': 'Leeds United A.F.C.',
    'Liverpool': 'Liverpool F.C.',
    'Liverpool FC': 'Liverpool F.C.',
    'Nuernberg': '1. FC Nuremberg',

    'Rangers': 'Rangers F.C.',
    'Rangers FC': 'Rangers F.C.',
    'Rangers F.C.': 'Glasgow Rangers F.C.',
    
    'MacKenzie FC (Akron)': 'Clan Mackenzie FC (Akron)',
    'Clan MacKenzie': 'Clan Mackenzie FC (Akron)',
    

    'Aberdeen': 'Aberdeen F.C.',
    'Inter Milan': 'F.C. Internazionale Milano',
    'Internazionale': 'F.C. Internazionale Milano',

    'Jonkopping': 'Jönköpings Södra IF',
    'Uberlandia (Brazil)': 'Uberlândia Esporte Clube',
    'Bangu': 'Bangu Atlético Clube',
    'Dinamo Kiev': 'FC Dynamo Kyiv',
    'Dynamo Kiev': 'FC Dynamo Kyiv',
    
    'H.S.V. Hannover': 'Hannover 96',
    'America-Cali': 'América de Cali',
    'Barcelona': 'FC Barcelona',
    'Fiorentina': 'AFC Fiorentina',
    'Malmo': 'Malmö FF',
    'A.C. Milan': 'AC Milan',
    'A. C. Milan': 'AC Milan',
    'Tottenham Hotspurs': 'Tottenham Hotspur',
    'Guadalajara': 'CD Guadalajara',
    'Chivas Guadalajara': 'CD Guadalajara',
    'Chivas': 'CD Guadalajara',
    'Chelsea': 'Chelsea FC',
    'Chelsea F.C.': 'Chelsea FC',
    'Santos (Brazil)': 'Santos FC',
    'Santos': 'Santos FC',
    'All Skane': 'All-Skane',
    'Hannover \'96': 'Hannover 96',
    'All Stockholm': 'Stockholm All-Stars',
    'Norrkoping': 'IFK Norrköping',
    'Goteborg Orgryte': 'Örgryte IS',
    'Hammarby': 'Hammarby IF',
    'Ajax': 'AFC Ajax',
    'Ajax Amsterdam': 'AFC Ajax',
    'Slavia Prague': 'SK Slavia Prague',
    

    'A.I.K.': 'AIK Fotboll',
    'G.A.I.S.': 'GAIS',    
    'Saprissa': 'Deportivo Saprissa S.A.D.',

    'Roanoke River Dawgs': 'Roanoke RiverDawgs',
    'Roanoke Riverdawgs': 'Roanoke RiverDawgs',
    
    

}
teams.update(world)

international = {
    'USA': 'United States',
    'South Korea National Team': 'South Korea',
    'Australian National Team': 'Australia',
    'Chinese National Team': 'China',
    'Haiti National Team': 'Haiti',
    'Honduran National Team': 'Honduras',
    'Japan National Team': 'Japan',
    'Japanese National Team': 'Japan',
    'Paraguayan National Team': 'Paraguay',
    'Singapore National Team': 'Singapore',
    'El Salvador National Team': 'El Salvador',
    'China National Team': 'China',
    'Chinese National Team': 'China',
    'Guatemalan National Team': 'Guatemala',
    'Bermuda National Team': 'Bermuda',
    'Colombian National Team': 'Colombian',
    'Indonesia National Team': 'Indonesia',
    'Iran National Team': 'Iran',
    'Malaysia National Team': 'Malaysia',
    'Puerto Rico National Team': 'Puerto Rico',
    'Singapore National Team': 'Singapore',
    'U. S. National Team': 'United States',
    
    

    
    }
teams.update(international)



all_star = {
    'British Columbia Mainland Stars': 'British Columbia Mainland All-Stars',
    'British Columbia Stars': 'British Columbia All-Stars',

    'Calgary XI': 'Calgary All-Stars',
    

    'All Baltimore': 'Baltimore All-Stars',
    'All Chicago': 'Chicago All-Stars',
    'All-Chicago': 'Chicago All-Stars',
    'All-Collegiates': 'College All-Stars',
    'All-Gothenborg': 'Gothenborg All-Stars',
    'All-Indonesia Selection': 'Indonesia All-Stars',
    'All Kents': 'Kent All-Stars',
    'All New York': 'New York All-Stars',
    'All-New York': 'New York All-Stars',
    'All-Philadelphia': 'Philadelphia All-Stars',
    'All Philadelphia': 'Philadelphia All-Stars',
    'All-Stockholm': 'Stockholm All-Stars',
    'All Stockholm': 'Stockholm All-Stars',
    'All Westerns': 'Western All-Stars',
    'All-Skane': 'Skane All-Stars',
    'American Soccer League Stars': 'American Soccer League All-Stars',
    'American League Stars': 'American Soccer League All-Stars',
    'American League XI': 'American Soccer League All-Stars',
    'American League': 'American Soccer League All-Stars',
    'American League All-Stars': 'American Soccer League All-Stars',
    'US Stars': 'U.S. Stars',
    'East L.A. Cobars': 'East L.A. Cobras',


    'C.Y.O. Stars': 'CYO Stars',
    'German American League Stars': 'German-American League All-Stars',
    'German-American League Stars': 'German-American League All-Stars',
    'German-American All-Stars': 'German American All-Stars',



    'Alberta Stars': 'Alberta All-Stars',
    'Chicago Stars': 'Chicago All-Stars',
    'Cleveland Stars': 'Cleveland All-Stars',
    'Connecticut Stars': 'Connecticut All-Stars',
    'CYC Stars': 'CYC All-Stars',
    'CYO Stars': 'CYO All-Stars',
    'Detroit Stars': 'Detroit All-Stars',
    'Eastern USA All-Stars': 'Eastern United States All-Stars',
    'Eastern United States Stars': 'Eastern United States All-Stars',
    'Edmonton Stars': 'Edmonton All-Stars',
    'Fall River XI': 'Fall River All-Stars',
    'Fort William XI': 'Fort William All-Stars',
    'Fall River Stars': 'Fall River All-Stars',
    'Greater Los Angeles Stars': 'Greater Los Angeles All-Stars',
    'Hamilton Stars': 'Hamilton All-Stars',
    'Hartford Stars': 'Hartford All-Stars',
    'Indonesia XI': 'Indonesia All-Stars',
    'Irish Stars': 'Irish All-Stars',
    'Kearny Stars': 'Kearny All-Stars',
    'Los Angeles Stars': 'Los Angeles All-Stars',
    'Detroit All Stars': 'Detroit All-Stars',
    'Mainland Stars': 'Mainland All-Stars',
    'Manitoba Stars': 'Manitoba All-Stars',
    'Milwaukee Stars': 'Milwaukee All-Stars',
    'Montreal Stars': 'Montreal All-Stars',
    'National League Stars': 'National League All-Stars',
    'National Soccer League Stars': 'National League All-Stars',
    'National League Select': 'National League All-Stars',
    'New England Stars': 'New England All-Stars',
    'New Jersey Stars': 'New Jersey All-Stars',
    'New Jersey State Stars': 'New Jersey All-Stars',
    'Ohio Stars': 'Ohio All-Stars',
    'Ohio State Stars': 'Ohio All-Stars',
    'Ontario Stars': 'Ontario All-Stars',
    'Ottawa Stars': 'Ottawa All-Stars',
    'New York Stars': 'New York All-Stars',
    'Philadelphia Stars': 'Philadelphia All-Stars',
    'Rochester Select': 'Rochester All-Stars',
    'Saskatchewan Stars': 'Saskatchewan All-Stars',
    'U. S. Stars': 'U.S. All-Stars',
    'U.S. Stars': 'U.S. All-Stars',
}
teams.update(all_star)


oteams = {
    'Ukrainian SC (East NY)': 'NY Ukrainian SC',

    'White Banner': 'White Banner Malt',
    'White Banner Malt (St. Louis)': 'White Banner Malt',

    # Check these names.
    'Wichita Blue': 'Wichita Blue Angels',

    'Wellston FC (St. Louis)': 'Wellston FC',

    'Chicago Fire S.C.': 'Chicago Fire',

    'Fairhill FC (Philadelphia)': 'Philadelphia Fairhill FC',
    'Fairhill FC': 'Philadelphia Fairhill FC',
    
    'Paterson F.C.': 'Paterson Silk Sox',

    'Avella Polar Stars (W. Pa.)': 'Avella (W. Pa.)',

    'West Hudson FC': 'West Hudson A.A.',
    'West Hudson AC': 'West Hudson A.A.',
    

    'Montclair Standard Falcons': 'Montclair Falcons',
    'Fontana Falcons': 'Montclair Falcons',

    'Buda A.A. (Harvey, Illinois)': 'Harvey Buda A.A.',

    

    'Gray & Davis': 'Grey & Davis', # Not sure about this one.
    'Anderson S.C.': 'Andersons',
    
    

    'Goodyear FC': 'Akron Goodyear FC',
    'Goodyear FC (Akron)': 'Akron Goodyear FC',
    
    


    'Tower Ford': 'Tower Ford Casa Bianca',

    'Gjoa': 'SC Gjoa',
    'Bartunek Slavias': 'Bartunek Slavia',


    'Eintracht S.C.': 'S.C. Eintracht',

    'Chicago Eagles': 'A.A.C. Eagles',

    'New York Hungarian': 'NY Hungaria',
    'New York Hungarians': 'NY Hungaria',


    'Milwaukee Bavarian Blue Ribbon': 'Milwaukee Bavarians',

    'Kodak Park': 'Kodak Park FC',

    'Hoboken F.C.': 'Hoboken FC',

    'Olympic SC (IL)': 'Olympia FC (Chicago)',
    'Olympia SC (Chicago)': 'Olympia FC (Chicago)',

    'Beadling SC (West PA)': 'Beadling SC',
    'Holyoke Falco': 'Holyoke Falcons',
    'Hota SC': 'NY Hota SC',
    'NY Hota-Bavarian SC': 'NY Hota SC',


    
    'Becks German American SC (Buffalo)': 'Buffalo Becks',

    'New York Hispano': 'Brooklyn Hispano',

    'Passon SC': 'Philadelphia Passon',
    'Philadelphia Passon F.C.': 'Philadelphia Passon',
    'Philadelphia Germans': 'Philadelphia German Americans',
    'General Electric': 'General Electric FC',
    'Girondins de Bordeaux': 'FC Girondins de Bordeaux',
    
    'Baltimore Pompeii': 'Baltimore Pompei SC',
    'Guiliana SC (East NY)': 'Giuliana SC',



    'Fall River F.C.': 'Fall River FC',
    'Fall River Football Club': 'Fall River FC',

    'Fall River S.C.': 'Fall River SC',

    'Rochester Celtics': 'Rochester Celtic',

    'Kelly Celtic': 'Rochester Kelly Celtic',
    'Rochester Celtic': 'Rochester Kelly Celtic',
    'Kelly Celtic (Rochester': 'Rochester Kelly Celtic',


    'Slavia F.C.': 'Slavia FC',

    'Bruell F.C.': 'Bruell Insurance',
    
    'Galicia F.C.': 'Galicia FC',
    'D.S.C. Brooklyn': 'DSC Brooklyn',
    'Centro-Hispano': 'Centro Hispano',

    'Newark Ukrainian': 'Newark Ukrainian Sitch',

    'Milwaukee Bavarian': 'Milwaukee Bavarians',
    'Bavarian SC (WI)': 'Milwaukee Bavarians',
    'Simpkins F.C.': 'Simpkins Ford',
    'Simpkins S.C.': 'Simpkins Ford',
    'Schwaben (Chicago)': 'Chicago Schwaben',

    'Chicago Viking AC': 'Chicago Viking A.A.',
    'Viking AC': 'Chicago Viking AC',
    'Chicago Vikings': 'Chicago Viking AC',

    'Hatikvoh': 'Hatikvoh FC',
    'German Hungarian S.C. (NYC)': 'German Hungarian SC',
    'Hungaria SC': 'NY Hungaria',

    'Becks German American S.C. (Buffalo)': 'Becks German American SC (Buffalo)',
}


teams.update(oteams)

asl1 = {

    'Todd Shipyards F.C.': 'Todd Shipyards',

    # Accurate?
    'Philadelphia 1928-1929': 'Philadelphia Field Club',

    'Bridgeport': 'Bridgeport Bears',
    'Brooklyn Hakoah': 'Hakoah All-Stars',

    # Colliding with Jersey City slug.
    'Jersey City ?': 'Jersey City (?x)',


}
teams.update(asl1)


asl2 = {
    'Baltimore Canton': 'Baltimore Americans',
    'Baltimore German': 'Baltimore Americans',
    'Baltimore S.C.': 'Baltimore Americans',
    'Baltimore Rockets': 'Baltimore Pompei',
    'Baltimore St. Gerards': 'Baltimore Flyers',
    'Baltimore Stars': 'Baltimore Bays',
    'Allentown': 'Bethlehem Hungarian',

    'Connecticut Bi-Centennials': 'Connecticut Bicentennials',
    'Hartford Bi-Centennials': 'Connecticut Bicentennials',
    'Atlanta Apollos': 'Atlanta Chiefs',

    'Boston Metros': 'Boston Tigers',
    'Brooklyn Giants': 'Brooklyn Hispano',
    'Connecticut Wildcats': 'Connecticut Yankees',
    'Northeast United': 'Connecticut Yankees',


    # This may not be right. Brooklyn Italians itself seems to have 
    # Gone to lower leagues, played as Palermo and Brokolyn Dodgers.
    'Boca Juniors': 'Brooklyn Italians',
    'Inter-Brooklyn Italians': 'Brooklyn Italians',
    'New York Inter': 'Brooklyn Italians',
    'Inter SC': 'Brooklyn Italians',
    'St. Mary\'s Celtic': 'Brooklyn Celtic',

    'Galicia SC': 'Brookhattan',
    'Brookhattan Galicia': 'Brookhattan',
    'Galicia-Honduras': 'Brookhattan',
    'Cleveland Stars': 'Cleveland Cobras',
    'Georgia Generals': 'Cleveland Cobras',
    'Hartford SC': 'Hartford Kings',
    'Hartford FC': 'Hartford Kings',
    'Gary Tigers': 'Indiana Tigers',
    'Indianapolis Daredevils': 'Rhode Island Oceaneers',
    'New England Oceaneers': 'Rhode Island Oceaneers',
    'Kearny Irish': 'Kearny Celtic',
    'Ludlow S.C.': 'Ludlow Lusitano',
    'Miami Americans': 'New Jersey Americans',
    'Newark Falcons': 'Elizabeth Falcons',
    'Falcons SC': 'Elizabeth Falcons',
    'Falcons-Warsaw': 'Elizabeth Falcons',
    'New Brunswick Hungarian Americans': 'New Brunswick Hungarians',
    'New Jersey Shaefer Brewers': 'New Jersey Brewers',
    'New York Greeks': 'New York Apollo',
    'New York United': 'New York Apollo',
    'Paterson Caledonian': 'Paterson F.C.',
    'Newark Germans': 'Paterson F.C.',
    'Philadelphia Passon': 'Philadelphia Nationals',
    'Sacramento Spirits': 'Sacramento Gold',
    'Syracuse Scorpions': 'Syracuse Suns',
    'Virginia Capitol Cavaliers': 'Washington Cavaliers',
    'Fall River Astros': 'Boston Astros',
    
}
teams.update(asl2)

# Going to organize this alphabetically?

misc = {

    # Need to make sure America is not a regional US team.
    'America': 'América',



    'Club Espana': 'Club España',

    'St. Mary’s Celtic': 'St. Mary\'s Celtic',
    'St. Michael’s': 'St. Michael\'s',

    'Everett BigFoot': 'Seattle BigFoot',
    'Everett Bigfoot': 'Seattle BigFoot',
    'Elizabeth SC': 'Elizabeth S.C.',

    'Federal Ship': 'Federal Ship FC',
    'Federal Shipyard': 'Federal Ship FC',
    'Federal Shipbuilding': 'Federal Ship FC',
    'Federal Shipyards': 'Federal Ship FC',

    'Kearny Erie': 'Erie AA',

    'Scottish Americans': 'Kearny Scots',
    'Scottish-Americans': 'Kearny Scots',
    'Kearny Scottish-Americans': 'Kearny Scots',
    'Kearny Scottish Americans': 'Kearny Scots',
    'Scottish American FC (NJ)': 'Kearny Scots',
    'Scottish American FC': 'Kearny Scots',




    'Becks German American SC (Buf.)': 'Becks German American S.C. (Buf.)',

    'Montclair': 'Fontana Falcons',
    'NY/NJ Stallions': 'New Jersey Stallions',
    'Newark SC': 'Newark S.C.',
    'New York Hungaria': 'NY Hungaria',
    'New York National Giants': 'New York Giants',
    'New York Nationals': 'New York Giants',


    'Gjoa SC': 'SC Gjoa',
    'Gjoa FC': 'SC Gjoa',
    'Hellrung & Grimm': 'Hellrung FC',


    'Clan Macdonald': 'Clan MacDonald',
    'Clark A.A': 'Clark A.A.',

    'IRT Rangers': 'I.R.T. Rangers',

    


    'Puritan Y.M.L': 'Puritan Y.M.L.',
    'Hakoah FC': 'Hakoah F.C.',

    'German American SC': 'German American S.C.',
    'German-American AC': 'German American AC',

    'German-Hungarian SC': 'German Hungarian SC',
    'German-Hungarians': 'German Hungarian SC',
    'German Hungarians': 'German Hungarian SC',

    'St. Michaels': 'St. Michael\'s',
    'St. Michael’s': 'St. Michael\'s',

    'Brookhattan-Galicia': 'Brookhattan Galicia',
    'IRT Strollers': 'I.R.T. Strollers',
    'Pawtucket FC': 'Pawtucket F.C.',
    'SC Eintracht':'S.C. Eintracht',
    'Edmonton FC': 'Edmonton F.C.',


    'Harrison SC': 'Harrison S.C.',
    'Harrison Soccer Club': 'Harrison S.C.',
    'Harrison Field Club': 'Harrison S.C.',
    'Harrison S.C.': 'Erie A.A.',
    'Erie AA': 'Erie A.A.',
    
    
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

    'Chicago Sparta Falstaff': 'Chicago Sparta ABA',
    'Sparta (Chicago)': 'Chicago Sparta ABA',
    'Sparta': 'Chicago Sparta ABA',
    'Sparta FC': 'Chicago Sparta ABA',
    'Sparta F.C.': 'Chicago Sparta ABA',
    'Sparta ABA': 'Chicago Sparta ABA',
    'Sparta Leader': 'Chicago Sparta ABA',
    'Sparta Garden City': 'Chicago Sparta ABA',
    'Sparta Union': 'Chicago Sparta ABA',
    'Chicago Sparta Falstaff': 'Chicago Sparta ABA',
    'Sparta Ogden Dairy': 'Chicago Sparta ABA',

    'Mid-Michigan Bucks': 'Michigan Bucks',

    'Los Angeles Kickers-Victoria (South California)': 'Los Angeles Kickers',
    
    'D. C. United': 'D.C. United',


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

    'St. Louis Scullin Steel': 'Scullin Steel',
    'Scullin St.': 'Scullin Steel',

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

    'Slovak AA': 'Chicago Slovak SC',
    'Slovak SC': 'Chicago Slovak SC',
    

    'Richhmond Kickers': 'Richmond Kickers',


    'San Fern. Valley Golden Eagles': 'San Fernando Valley Golden Eagles',
    'Valley Golden Eagles': 'San Fernando Valley Golden Eagles',
    'SFV Golden Eagles': 'San Fernando Valley Golden Eagles',

    'CD Mexico (North California)': 'El Farolito Soccer Club',
    'AAC Eagles': 'A.A.C. Eagles',

    'Syracus Suns': 'Syracuse Suns',
    


    'Harmarville': 'Harmarville Hurricanes',

    'Kutis SC': 'St. Louis Kutis',
    'Kutis': 'St. Louis Kutis',
    

    'Ukrainian Nationals': 'Philadelphia Ukrainians',
    'Hungaria SC (East NY)': 'New York Hungaria',



    'Maccabee AC': 'Maccabi Los Angeles',

    'Club Espana (DC/VA)': 'Club Espana',

    'Busch SC': 'Busch SC (MO)',

    'HRC Kickers': 'St. Petersburg Kickers',
    'McCormick Kickers': 'St. Petersburg Kickers',

    'Greek American SC (East NY)': 'NY Greek American Atlas',
    'Greek American Atlas': 'NY Greek American Atlas',
    'NY Greek-American Atlas': 'NY Greek American Atlas',
    'NY Greek-Americans Hellenic SC': 'NY Greek American Atlas',
    'Greek American AA': 'NY Greek American Atlas',
    'Greek-American A.C.': 'NY Greek American Atlas',
    'Greek American AC': 'NY Greek American Atlas',

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
    'Philadelphia German-Americans': 'Philadelphia German Americans',
    'Philadelphia German-American': 'Philadelphia German Americans',
    'Philadelphia German American': 'Philadelphia German Americans',
    'Philadelphia Americans': 'Philadelphia German Americans',
    'Uhrik Truckers': 'Philadelphia German Americans',

    # Not sure of these.
    'Hungaria': 'New York Hungaria', 

    

    'Central Jersey Rpitide': 'Central Jersey Riptide',

    'Slavia Bartunek': 'Bartunek Slavia',
    'Rosenblum Slavia': 'Bartunek Slavia',
    'Cleveland Slavia': 'Bartunek Slavia',
    'Bartunek Clothes (Cleveland)': 'Bartunek Slavia',
    

    'LA Blues': 'Los Angeles Blues',
    'Antigua Barricudas FC': 'Antigua Barracuda',
    'Dayton Dutch Lions FC': 'Dayton Dutch Lions',

    'Brooklyn Dodgers S.C.': 'Brooklyn Italians',
    'Brooklyn Dodgers SC': 'Brooklyn Italians',

    'San Francisco C.D. Mexico' : 'El Farolito Soccer Club',
    'Philadelphia Uhrik Truckers': 'Uhrik Truckers',




}

teams.update(misc)


mls_teams = {

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


# Should remove these.

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


def get_team(name, competition=None, pre_dict={}):
    # Remove pre_dict, competition from get_team

    name = pre_dict.get(name, name)
        
    if competition is not None and (name, competition) in teams:
        name = teams[(name, competition)]
        return get_team(name, competition)

    if name in teams:
        return get_team(teams[name])


    return name
    
