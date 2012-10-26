#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from soccerdata.mongo import soccer_db

teams = {}


def get_team(name, competition=None):
    # Remove pre_dict, competition from get_team
    #print name

    name = convert_country_code(name)

    if name is None:
        import pdb; pdb.set_trace()

    name = name.strip()

    # This should be split out into a separate function. Currently only used in leach.
    # 
    if competition is not None and (name, competition) in teams:
        name = teams[(name, competition)]
        return get_team(name, competition)

    if name in teams:
        return get_team(teams[name])


    return name


country_code_dict = dict([(e['code'], e['name']) for e in soccer_db.countries.find()])

def convert_country_code(code):
    if code in country_code_dict:
        return country_code_dict[code]

    return code

    


leach = {

    'Columbia College': 'Columbia University',
    'Princeton College': 'Princeton University',
    'Rutgers College': 'Rutgers University',
    'Yale College': 'Yale University',
    'City College New York': 'City College of New York',
    'Tufts College': 'Tufts University',
    'Brooklyn Poly Institute': 'Brooklyn Poly',
    'Penn (Gettysburg) College': 'Gettysburg College',
    'Cornell College': 'Cornell University',
    'Richmond College': 'University of Richmond',
    'State University of Iowa': 'Iowa State University',
    'Washington & Lee': 'Washington & Lee University',
    'Minnesota College': 'University of Minnesota',
    'Critchley AA': 'Critchley\'s',
    'Critchley': 'Critchley\'s',
    

#Brooklyn Italians
'CD Guadalajara -- Mexico': 'CD Guadalajara',
#San Jose Oaks
'Monterrey - Mexico': 'Mexico',
#CD Mexico
#New York Centaurs
#Ireland U-23
'Necaxa -- Mexico': 'Necaxa',

'Tusberg Landshut - Germany': 'Tusberg Landshut',
'Shimizu S-Pulse - Japan': 'Shimizu S-Pulse',
'Norresundby Boldklub - Denmark': 'Norresundby Boldklub',
'Gamba Osaka - Japan': 'Gamba Osaka',
'Vissel Kobe - Japan': 'Vissel Kobe',
'Fiorentina - Italy': 'Fiorentina',
'Bayer Leverkusen - Germany': 'Bayer Leverkusen',
'Feyenoord - Netherlands': 'Feyenoord',

'Sporting Lisbon XI - Portugal': 'Sporting Lisbon XI',
'UNAM - Mexico': 'UNAM',
'Wisla Krakow - Poland': 'Wisla Krakow',
'CD Aguila - El Salvador': 'CD Aguila',
'Necaxa - Mexico': 'Necaxa',
'Luis Angel Firpo - El Salvador': 'Luis Angel Firpo',
'Cruz Azul - Mexico': 'Cruz Azul',
'Deportivo Cali - Colombia': 'Deportivo Cali',
'Sichuan Quanxing - China': 'Sichuan Quanxing',
'Beijing Guoan - China': 'Beijing Guoan',
'SSK Vitkovice - Czech': 'SSK Vitkovice',
'Arezzo - Italy': 'Arezzo',
'Serie  C U-21 - Italy': 'Serie C U-21',
'Genoa - Italy': 'Genoa',
'Viborg - Denmark': 'Viborg',
'Atlas - Mexico': 'Atlas',
'Atlas Academicos - Mexico': 'Atlas Academicos',
'CD Guadalajara Chivas - Mexico': 'CD Guadalajara',
'Venezia - Italy': 'Venezia',
'Tecos - Mexico': 'Tecos',
'Grampus Eight - Japan': 'Grampus Eight',
'FinnPa - Finland': 'FinnPa',
'Reggiana - Italy': 'Reggiana',
'Instant Dict - Japan': 'Double Flower FA',
'Club Sol - Mexico': 'Club Sol',
'UAG - Mexico': 'Tecos',
'Alianza - El Salvador': 'Alianza',
'FAS - El Salvador': 'FAS',
'Bermuda NT': 'Bermuda',
'Aston Villa - England': 'Aston Villa',
'Colombia NT': 'Colombia',
'Leeds United - England': 'Leeds United',
'Sampdoria - Italy': 'Sampdoria',
'SV Transvaal -- Suriname': 'SV Transvaal',
'Alianza Lima - Peru': 'Alianza Lima',
'San Lorenzo - Argentina': 'San Lorenzo',
'CSD Comunicaciones-- Guatemala': 'CSD Comunicaciones',
'Galatasaray - Turkey': 'Galatasaray',
'Cruz Azul -- Mexico': 'Cruz Azul',
'Palmeiras - Brazil': 'Palmeiras',
'Santos -- Mexico': 'Santos Laguna',
'United Petrotrin -- T & T': 'United Petrotrin',
'Luis Angel Firpo-- El Salvador': 'Luis Angel Firpo',
'Veracruz - Mexico': 'Veracruz',
'Atlante - Mexico': 'Atlante',
'Buenaventura - Colombia': 'Buenaventura',
'America de Cali - Colombia': 'America de Cali',
'Guatemala NT': 'Guatemala',
'Comunicaciones - Guatemala': 'CSD Comunicaciones',
'IFK Gothenburg - Sweden': 'IFK Gothenburg',
'Tapatio - Mexico': 'Tapatio',
'Univ. de Guadalajara - Mexico': 'Universidad de Guadalajara',
'Ikast - Denmark': 'Ikast',
'Coban - Guatemala': 'Coban',
'Suchitepequez - Guatemala': 'Suchitepequez',
'Dallas Burn/FC Dallas 96': 'FC Dallas',
'Bachilleres - Mexico': 'Bachilleres',
'AC Milan - Italy': 'AC Milan',
'Leicester City - England': 'Leicester City',
'Benfica - Portugal': 'Benfica',
'Leon -- Mexico': 'Leon',
'Morelia - Mexico': 'Morelia',
'Joe Public -- T & T': 'Joe Public',
'Toluca -- Mexico': 'Toluca',
'Vasco da Gama -- Brazil': 'Vasco da Gama',
'Toluca - Mexico': 'Toluca',
'Manchester United - England': 'Manchester United',
'Sheffield Wednesday - England': 'Sheffield Wednesday',
'Sunderland - England': 'Sunderland',
'Everton - England': 'Everton',
'Sheffield United - England': 'Sheffield United',
'Oro - Mexico': 'Oro',
'IBV - Iceland': 'IBV',
'Aguila - El Salvador': 'Aguila',
'Lyngby - Denmark': 'Lyngby',
'Jaguares - Mexico': 'Jaguares',
'Stade Laussane - Switzerland': 'Stade Laussane',
'Modena - Italy': 'Modena',
'AD Limonense - Costa Rica': 'AD Limonense',
'Tijuana Chivas - Mexico': 'Tijuana Chivas',
'Herediano - Costa Rica': 'Herediano',
'Gallos de Jalisco - Mexico': 'Gallos de Jalisco',
'Puntarenas - Costa Rica': 'Puntarenas',
'Limon - Costa Rica': 'Limon',
'Jalisco - Mexico': 'Jalisco',
'Colima Jaguares - Mexico': 'Colima Jaguares',
'Santa Clara - Portugal': 'Santa Clara',
'Legia-Daewoo Warsaw - Poland': 'Legia-Daewoo Warsaw',
'Derby County - England': 'Derby County',
'Ajax - Netherlands': 'Ajax',
'Haiti NT': 'Haiti',
'Puerto Rico NT': 'Puerto Rico',
'Olimpia -- Honduras': 'Olimpia',
'Alajuela -- Costa Rica': 'Alajuelense',
'Hamburg SV - Germany': 'Hamburg SV',
'Millonarios - Colombia': 'Millonarios',
'Newcastle United - England': 'Newcastle United',
'FC Salzburg - Austria': 'FC Salzburg',
'Puebla - Mexico': 'Puebla',
'Nacional de Tijuana - Mexico': 'Nacional de Tijuana',
'Real Espana-- Honduras': 'Real Espana',
'LD Alajuelense-- Costa Rica': 'LD Alajuelense',
'Celtic Glasgow - Scotland': 'Glasgow Celtic',
'Glasgow Rangers - Scotland': 'Glasgow Rangers',
'Pachuca-- Mexico': 'Pachuca',
'CD Olympia-- Honduras': 'CD Olimpia',
'Santa Teresita FC -Costa Rica': 'Santa Teresita FC',
'Deportivo Belen - Costa Rica': 'Belen',
'Fylkir - Iceland': 'Fylkir',
'San Lorenzo - Costa Rica': 'San Lorenzo Costa Rica',
'Soacha FC - Colombia': 'Soacha FC',
'CD Saprissa-- Costa Rica': 'Saprissa',
'Arnett Gardens-- Jamaica': 'Arnett Gardens',
'Fulham - England': 'Fulham',
'Bayern Munich - Germany': 'Bayern Munich',
'Sporting Cristal -- Peru': 'Sporting Cristal',
'Club America -- Mexico': 'Club America',
'Italchacao -- Venezuela': 'Italchacao',
'Barcelona -- Ecuador': 'Barcelona Sporting Club',
'Millionarios -- Colombia': 'Millonarios',
'Chivas -- Mexico': 'Chivas',
'Oscar\'s FC - Brazil': 'Oscar\'s FC',
'Magallanes - Chile': 'Magallanes',
'Colo Colo - Chile': 'Colo Colo',
'Universidad de Chile - Chile': 'Club Universidad de Chile',
'Universidad Catolica - Chile': 'CD Universidad Católica',
'San Felipe - Chile': 'Unión San Felipe',
'W. Connection -- Jamaica': 'W Connection',
'W. Connection FC - Trinidad': 'W Connection',
'CSD Municipal -- Guatemala': 'Municipal',
'FC Nurnberg - Germany': 'FC Nurnberg',
'Boca Juniors - Argentina': 'Boca Juniors',
'Club Tigres - Mexico': 'Tigres',
'Morelia -- Mexico': 'Morelia',
'Olympia - Honduras': 'CD Olimpia',
'Santos Laguna - Mexico': 'Santos Laguna',
'Rosenborg Trondheim -- Norway': 'Rosenborg Trondheim',
'Lyn Oslo -- Norway': 'Lyn Oslo',
'Rubin Kazan -- Russia': 'Rubin Kazan',
'Torpedo Moscow -- Russia': 'Torpedo Moscow',
'Odd Grenland -- Norway': 'Odd Grenland',
'Viking Stavangar -- Norway': 'Viking FK',
'Santos - Mexico': 'Santos Laguna',
'Motagua -- Honduras': 'Motagua',
'Deportivo Arabe Unido --Panama': 'Arabe Unido',
'Palestino - Chile': 'Palestino',
'Tottenham Hotspur - England': 'Tottenham Hotspur',
'Nacional -- Uruguay': 'Nacional',
'1860 Munchen -- Germany': '1860 Munchen',
'PSV Eindhoven -- Netherlands': 'PSV Eindhoven',
'Gif Sundsvall -- Sweden': 'Gif Sundsvall',
'Dynamo Kiev -- Ukraine': 'Dynamo Kiev',
'Bodo/Glimt -- Norway': 'Bodo/Glimt',
'Stabaek -- Norway': 'Stabaek',
'San Juan Jabloteh -- T & T': 'San Juan Jabloteh',
'Harbour View FC -- Jamaica': 'Harbour View FC',
'Deportivo Saprissa -Costa Rica': 'Deportivo Saprissa',
'UNAM -- Mexico': 'UNAM',
'Puerto Rico Islanders - USL': 'Puerto Rico Islanders',
'Hoppers FC - Antigua': 'Hoppers FC',
'Puntarenas FC - Costa Rica': 'Puntarenas FC',
'HitachiCentre SAP FC - Antigua': 'Hitachi Centre SAP FC',
'Inter Moengotapoe - Surinam': 'Inter Moengotapoe',
'SV Leo Victor - Surinam': 'SV Leo Victor',
'Sydney FC - Australia': 'Sydney FC',

    'Toronto Ulster': 'Toronto Ulster United',
    'Ulster United': 'Toronto Ulster United',

    'Rochester Raging Rhinos': 'Rochester Rhinos',
    'San Fernando Quakes': 'San Fernando Valley Quakes',
    'Atlanta Silverbacks U-23\'s': 'Atlanta Silverbacks U23\'s',
    'Sioux Falls SpitFire': 'Sioux Falls Spitfire',
    'Albany Black Watch Highlanders': 'Albany Blackwatch Highlanders',
    'Ft. Wayne Fever': 'Fort Wayne Fever',
    'Augusta Fireball United': 'Augusta Fireball',
    'Austin Lighting': 'Autin Lightning',
    'Autin Lightning': 'Austin Lightning',

    'Isidro Metapan': 'Isidro Metapán',
    'Xelaju': 'Xelajú MC',
    'Chorrillo': 'Chorrillo F.C.',
    'Olimpia': 'CD Olimpia',
    'Municipal': 'CSD Municipal',
    'San Francisco': 'San Francisco FC',
    'Motagua': 'CD Motagua',
    'Brujas': 'Brujas FC',

    'New Bedford F.C.': 'New Bedford Whalers',
    'Real Maryland Monarchs FC': 'Real Maryland Monarchs',

    'Al Ahly': 'Al Ahly SC',
    'Al Ahly Sporting Club': 'Al Ahly SC',

    'West Brom Albion': 'West Bromwich Albion',
    'West Ham': 'West Ham United',

    'DC United Reserves': 'D.C. United Reserves',

    'Kansas City Wizards Reserves': 'Sporting Kansas City Reserves',
    'MetroStars Reserves': 'New York Red Bulls Reserves',

    'Garland Genesis': 'DFW Tornados',
    'Addison Arrows': 'DFW Tornados',
    'North Texas United': 'DFW Tornados',
    'Fort Worth Kickers': 'DFW Tornados',
    'Dallas Kickers': 'DFW Tornados',
    'Dallas Americans': 'DFW Tornados',
    'Dallas-Fort Worth Toros': 'DFW Tornados',
    'Texas Toros': 'DFW Tornados',
    'Texas Rattlers': 'DFW Tornados',
    'Texas Spurs': 'DFW Tornados',

    'McKeesport National Tube': 'McKeesport FC',

    'New York FC': 'New York Field Club',
    'Brooklyn F.C.': 'Brooklyn Field Club',
    'Fore River FC': 'Fore River Rovers',
    'Akron FC': 'Akron Goodyear FC',
    'Correnti Cleaners (St. Louis)': 'Simpkins Ford',
    'DeAndreis': 'DeAndreis Council',
    'De Andreis SC (St. Louis)': 'DeAndreis Council',

    'Raleigh Capital Express': 'Raleigh Flyers',
    'Vancouver North Shore United': 'Vancouver North Shore',
    'Vereinigung Erzgebirge (East PA)': 'Vereinigung Erzgebirge',
    'Philadelphia Hibernians': 'Philadelphia Hibernian',
    'Platense (Honduras)': 'Platense F.C.',
    'Platense': 'Platense F.C.',

    'Miami FC': 'Fort Lauderdale Strikers',
    'San Jose Hawks': 'San Francisco Bay Blackhawks',
    'J & J Dobson AA': 'J & J Dobson FC',
    'Jeanette FC (Pittsburgh)': 'Jeanette FC',
    'Johnston City AFC (Illinois)': 'Johnston City AFC',
    'Johnston City': 'Johnston City AFC',
    'Kearny Celtics': 'Kearny Celtic',
    'New Orleans Gamblers': 'New Orleans Riverboat Gamblers',
    'Merrimac Valley': 'Merrimac Valley FC',
    'Minerva-Pfuelzer': 'Minerva-Pfaelzer SC',
    'Minit Rubs (St. Louis)': 'Minit-Rubs',
    'Minnesota Stars': 'Minnesota Stars FC',
    'NSC Minnesota Stars': 'Minnesota Stars FC',
    'New York Freedom': 'New York Freedoms',
    'Newark Portugeuse': 'Newark Portuguese',
    'Newark Portuguese (NJ)': 'Newark Portuguese',
    'New York Hota': 'NY Hota SC',
    'Olímpia (H)': 'CD Olimpia',
    'Orlando City': 'Orlando City SC',
    'Team Calgary': 'Calgary Storm',

    


    


    'New Orleans Storm': 'New Orleans Riverboat Gamblers',
    'Raleigh Express': 'Raleigh Capital Express',
    'US Pro 40': 'US Project 40',
    'Hampton Rds Mariners': 'Hampton Roads Mariners',
    'SFB Seals': 'San Francisco Bay Seals',
    'Atlanta Ruckus': 'Atlanta Silverbacks',
    'Miami FC Blues': 'Miami FC',
    'FC Dallas 96': 'FC Dallas',
    'FC Tampa Bay': 'Tampa Bay Rowdies',
    'CD Chivas USA': 'Chivas USA',
    'Philadephia Union': 'Philadelphia Union',
    'Portland Timbers U23': 'Portland Timbers U23\'s',
    'Ft. Lauderdale Strikers': 'Fort Lauderdale Strikers',
    'Hamilton FC Rage': 'Hamilton Rage',
    'Chivas El Paso Patriots': 'El Paso Patriots',
    'Rio Grande Valley Grandes FC': 'Rio Grande Valley Grandes',
    'Antigua Barracuda': 'Antigua Barracuda FC',
    'Team Sacramento': 'Sacramento Geckos',
    'Albuquerque Geckos': 'Sacramento Geckos',
    'Dallas Toros': 'Dallas-Fort Worth Toros',
    'DFW Toros': 'Dallas-Fort Worth Toros',
    'Victoria Riptide': 'Victoria Riptides',
    'North Virginia Royals': 'Northern Virginia Royals',
    'Las Vegas Quicksilvers': 'Las Vegas Quicksilver',
    'Chicago Horizons': 'Chicago Horizon',
    'Bay Area Seals': 'San Francisco Bay Seals',
    'San Francisco Seals': 'San Francisco Bay Seals',
    'Cosmos': 'New York Cosmos',
    'Supra de Montreal': 'Montreal Supra',
    'Hapoel Tel Aviv': 'Hapoel Tel Aviv F.C.',
    'Coventry City': 'Coventry City FC',
    'AC Lanerossi-Vicenza': 'Vicenza Calcio',
    'Bangu AC': 'Bangu Atlético Clube',
    'Varzim': 'Varzim S.C.',
    'Varzim (Portugal)': 'Varzim S.C.',
    'Apollon': 'Apollon Limassol',
    'Heart of Midlothian': 'Heart of Midlothian F.C.',
    'Hearts of Midlothian F.C.': 'Heart of Midlothian F.C.',
    'Merchant Ship B': 'Philadelphia Merchant Ship B',
    'Merchant Ship A': 'Philadelphia Merchant Ship',
    'Merchants Ship': 'Philadelphia Merchant Ship',
    'Merchant Ship': 'Philadelphia Merchant Ship',
    'Raleigh Elite': 'Raleigh CASL Elite',
    'Real Estelí': 'Real Estelí F.C.',
    'RWB Adria (IL)': 'RWB Adria',
    'Acros': 'Acros Crystal',
    'Aegean Hawks': 'Aegean Hawks FC',
    'Alley Boys': 'Alley Boys FC',
    'Austin Aztex U23s': 'Austin Aztex U23',
    'Avella (W. Pa.)': 'Avella Polar Star',
    'Avella Polar Star (W. Pa.)': 'Avella Polar Star',
    'Bayonne Centerville': 'Centreville AC',
    'Calgary Storm Prospects': 'Calgary Storm Select',
    'Brooklyn Hispanos': 'Brooklyn Hispano',
    'CASL Elite': 'Raleigh CASL Elite',
    'Celtics of New Jersey': 'Celtics FC (New Jersey)',
    'Charlton Athletic': 'Charlton Athletic F.C.',
    'Chicago Croatian': 'Chicago Croatian SC',
    'Chicago Fire Premier': 'Chicago Fire Reserves',
    'Clan MacDonald': 'Clan MacDonald FC',
    'Clan MacDuff': 'Clan MacDuff FC',
    'Crompton': 'Crompton FC',
    'Cruz Azul (Mexico)': 'Cruz Azul',
    'DFW Tornadoes': 'DFW Tornados',
    'Djurgardens IF': 'Djurgårdens IF',
    'Esmond Cortez': 'Esmond Cortex',
    'Fore River SC': 'Fore River FC',
    'Fore River': 'Fore River FC',
    'Germantown BC': 'Germantown Boys Club',
    'Germantown Boys': 'Germantown Boys Club',
    'Giuliana': 'Giuliana SC',
    'New York Greek-Americans': 'NY Greek American Atlas',
    'Greek-Americans': 'NY Greek American Atlas',
    'NY Greek American SC': 'NY Greek American Atlas',
    'New York Greek-American': 'NY Greek American Atlas',
    'Greek American AC (North CA)': 'San Francisco Greek American AC',
    'San Francisco Greek Americans': 'San Francisco Greek American AC',
    

    'Hapoel Petah Tikvah': 'Hapoel Petah Tikva F.C.',
    'Hapoel Petah Tikva': 'Hapoel Petah Tikva F.C.',
    'Hapoel Haifa': 'Hapoel Haifa F.C.',
    

}

teams.update(leach)

alternate_names = {
    'Clark A.A.': 'Kearney Clarks ONT',
    'East Newark Clark AA': 'Kearney Clarks ONT',

    'Fall River County Street Rovers': 'Fall River Rovers',

    'Hampton Roads Mariners': 'Virginia Beach Mariners',

    'Thornton British Hosiers': 'Thornton Rovers',
    'Thornton British Hosieries': 'Thornton Rovers',


    'St. Louis Irish Americans': 'St. Louis Irish Americans AC',
    'North Grafton Association': 'North Grafton Association Foot Ball',
    'New York Irish-Americans': 'New York Irish Americans',
    'New Rochelle Association': 'New Rochelle Foot Ball Association',
    'Manville AC': 'Manville Athletics',
    'Lonsdale Athletics': 'Lonsdale Athletes',
    'Brooklyn Cricket Association': 'Brooklyn Cricket Athletic Club',
    'Ansonias Association': 'Ansonia Association',
    'Braidwood Association': 'Braidwoods Association',
    'Brooklyn Logs': 'Brooklyn Longfellows',
    'Clark O.N.T.': 'Kearney Clarks ONT',
    'Kearny Clarks ONT': 'Kearney Clarks ONT',
    'Kearny Rovers': 'Kearney Rovers',
    'Kearny Rangers': 'Kearney Rangers',
    'Lonsdales Association': 'Lonsdale Association',
    'Missouri Amateur AC': 'Missouri Amateur AA',

    'Domestic': 'Newark Domestics',
    'Newark Domestics Baseball AC': 'Newark Domestics',
    'Clark ONT': 'Kearney Clarks ONT',

    'Trenton Association': 'Trentons Association',
    'Tiffany Rovers': 'Newark Tiffany Rovers',

    'Toronto Supra Portuguese': 'Toronto Supra',
    'Vancouver 86ers': 'Vancouver Whitecaps',
    'Golden Bay Earthquakes': 'San Jose Earthquakes',
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


colleges = {
    'SFU': 'Simon Fraser University',
    'Chico State': 'Chico State University',
    'Duke': 'Duke University',
}
teams.update(colleges)

mexican = {
    'St. Patricks': 'St. Patrick\'s',
    'St. George FC': 'St. George F.C.',
    'C.D. Aguila': 'C.D. Águila',
    'C.D. Atletico Marte': 'C.D. Atlético Marte',
    'Espana': 'España',
    'U.S. All-stars': 'U.S. All-Stars', #find
    'Splitdorf F.C': 'Splitdorf F.C.', #find
    'World All-stars': 'World All-Stars', #find
    'San Sebastian': 'San Sebastián',
    

    'Scots Americans': 'Kearny Scots',

    'Indios': 'Indios de Ciudad Juárez',

    'México Country Club': 'México Cricket Club',

    'Oro': 'C.D. Oro',
    'CD Oro': 'C.D. Oro',
    'CD Toluca': 'Toluca',

    'Club Celaya': 'Celaya FC',

    'Athletico Morelia': 'Monarcas Morelia',
    'Athlético Morelia': 'Monarcas Morelia',
    'Atlético Morelia': 'Monarcas Morelia',

    # Unicode problems?
    #u'Athl\xe9tico Morelia': 'Monarcas Morelia',
    #u'Atl\xe9tico Morelia': 'Monarcas Morelia',

    'Morelia': 'Monarcas Morelia',
    'CA Monarcas Morelia': 'Monarcas Morelia',

    'Atletico Espanol': 'Atlético Español',
    'Atletico Potosino': 'Atlético Potosino',
    


    'América': 'Club América',
    'Club America': 'Club América',
    'CF América': 'Club América',

    #u'Am\xe9rica': 'Club América',

    'León': 'Club León',
    'Leon': 'Club León',

    #u'Club Le\xf3n': 'Club León',


    'Club Deportivo Veracruz': 'Veracruz',

    'Pachuca': 'C.F. Pachuca',
    'Pachuca CF': 'C.F. Pachuca',
    'Pachuca AC': 'C.F. Pachuca',

    'C.D. Irapuato': 'CD Irapuato',
    'Irapuato': 'CD Irapuato',
    'Deportivo Irapuato': 'CD Irapuato',

    'Laguna F.C.': 'Santos Laguna',
    'Laguna FC': 'Santos Laguna',

    'Club Necaxa': 'Necaxa',
    

    'UAT': 'Correcaminos UAT',
    'U.A.T.': 'Correcaminos UAT',


    'Unam Pumas': 'UNAM',
    'Pumas': 'UNAM',
    'Pumas UNAM': 'UNAM',
    'UNAM Pumas': 'UNAM',
    'U.N.A.M.': 'UNAM',

    'Tigres': 'UANL',
    'U.A.N.L': 'UANL',
    'U.A.N.L.': 'UANL',
    'Tigres UANL': 'UANL',
    'UANL Tigres': 'UANL',
    'Tigres de la UANL': 'UANL',
    


    


    'Monterrey': 'C.F. Monterrey',
    'C.F. Monterrey': 'CF Monterrey',

    'Tampico-Madero': 'Tampico Madero',

    'Puebla F.C.': 'Puebla',
    'Puebla FC': 'Puebla',
    'Puebla AC': 'Puebla',
    
    'San Luis': 'San Luis FC',
    'San Luis F.C.': 'San Luis FC',

    'U.A. de G.': 'Tecos',
    'Estudiantes Tecos': 'Tecos',
    'UAG': 'Tecos',
    'U.A.G.': 'Tecos',
    'UAG Tecos': 'Tecos',

    'C.D. Guadalajara Chivas': 'CD Guadalajara',
    'Guadalajara': 'CD Guadalajara',
    'Chivas Guadalajara': 'CD Guadalajara',
    'C.D. Guadalajara': 'CD Guadalajara',
    'Chivas': 'CD Guadalajara',

    'Univ. de Guadalajara': 'Universidad de Guadalajara',
    'Univ Guadalajara': 'Universidad de Guadalajara',
    'Universidad Guadalajara': 'Universidad de Guadalajara',
    'U de G': 'Universidad de Guadalajara',
    'U Guadalajara': 'Universidad de Guadalajara',

    'Club Deportivo Marte': 'Marte',
    'Marte FC': 'Marte',

    'Deportivo Atlas': 'Atlas',
    'Club Atlas': 'Atlas',

    'CA Atlas': 'Atlas',
    'F.C. Atlas': 'Atlas',

}
teams.update(mexican)


concacaf = {
    'C.D. FAS': 'CD FAS',
    'C.D. Fas': 'CD FAS',
    'CD Fas': 'CD FAS',
}

teams.update(concacaf)

us = {
    'Scullin Steels': 'Scullin Steel',    
    'Solidarite Scolair': 'Solidarite Scolaire',
    'Sacachisapas': 'Sacachispas Fútbol Club', 

    'Sacachispas': 'Sacachispas Fútbol Club',
    'Real Estelí': 'Real Estelí F.C.',
    'Inter Monegotapoe': 'Inter Moengotapoe',
    'Brooklyn Celtic': 'Brooklyn Celtics',
    'New Bedford Celtic': 'New Bedford Celtics',
    'West Philadelphia': 'West Philadelphia FC',
    'Chicago Maccabi': 'Maccabee SC (Chicago)', #verify 11/22/1936 game vs. Tel Aviv Maccabi was Maccabee SC
    'Thistle FC (Chicago)': 'Thistles FC (Chicago)',
    'Stix Baer & Fuller': 'Stix, Baer and Fuller F.C.',
    'Hellrungs': 'Stix, Baer and Fuller F.C.',
    'Hellrung FC': 'Stix, Baer and Fuller F.C.',
    'Howard and Bullough': 'Howard & Bullough',

    'Central Breweries': 'Stix, Baer and Fuller F.C.',
    'St. Louis Carondolet': 'St. Louis Carondolets',
    'St. Louis Raiders': 'St. Louis Kutis',
    'St. Louis Zenthoefer Furs': 'St. Louis Kutis',
    'Zenthoefer Furs': 'St. Louis Kutis',
    'Dallas Mulhausers': 'Dallas Mulhauser',
    'Angeles': 'Ángeles',

}

teams.update(us)

world = {

    'Celtic': 'Glasgow Celtic',

    'A.O. Krete': 'AO Krete',
    'Pembroke-Hamilton Club': 'Pembroke Hamilton Club',
    'Vasco Da Gama': 'Vasco da Gama',

    'Bunker Hill F.C.': 'Bunker Hill FC',
    'Isidro-Metapan': 'Isidro Metapán',
    'Torreón F.C.': 'Torreón FC',
    'SIU-Edwardsville': 'SIU Edwardsville',

    'W Connection FC': 'W Connection',

    'Sport Guyanais': 'ASL Sport Guyanais',

    'Barcelona (Ecuador)': 'Barcelona Sporting Club',
    'Aurora': 'Aurora F.C.',
    'Uniao de Santarem': 'União de Santarém',

    'Bayern Munchen': 'FC Bayern Munich',
    'Bayern Munich': 'FC Bayern Munich',

    'Alianza FC': 'Alianza',
    'America (Nicaragua)': 'América Managua',
    'Juventud Olimpica': 'Juventud Olímpica',
    'Olympique (Ft-de-France)': 'Olympique du Marin',
    'Robin Hood': 'S.V. Robinhood',
    'SV Robin Hood': 'S.V. Robinhood',
    'SV Robinhood': 'S.V. Robinhood',
    'Tauro': 'Tauro FC',



    'Victory Boys': 'SV Victory Boys',
    'Violette': 'Violette AC',
    'FAS': 'C.D. FAS',
    'Deportivo FAS': 'C.D. FAS',

    'Esteli': 'Real Estelí F.C.',
    'Real Esteli': 'Real Estelí F.C.',
    'Real Estelí': 'Real Estelí F.C.',
    'RCA': 'Racing Club Aruba',
    'Racing Club (Haiti)': 'Racing Club Haitien',
    

    'Juventus (Saint-Martin)':  'Juventus de Saint-Martin',
    'Juventus de Saint-Anne': 'ASG Juventus de Sainte-Anne',
    'Etoile de Monre-a-l\'Eau': 'Etoile de Morne-à-l\'Eau',
    'Hankok Verdes': 'Club Verdes',
    'Joe Public': 'Joe Public F.C.',
    'Joe Public FC': 'Joe Public F.C.',

    'Feijenoord': 'Feyenoord',

    'Norrkoeping': 'IFK Norrköping',
    'Glenavon': 'Glenavon F.C.',
    'Nice': 'OGC Nice',
    'Kilmarnock': 'Kilmarnock F.C.',
    'Karlsruhe': 'Karlsruher SC',
    'Monaco': 'AS Monaco FC',
    'Espanyol': 'RCD Espanyol',
    'Mantova': 'Mantova F.C.',
    'Reutlingen': 'SSV Reutlingen 05',
    
    

    'Burnley': 'Burnley F.C.',
    'Burnley FC': 'Burnley F.C.',

    
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
    'Academica de Coimbra': 'Académica de Coimbra',
    'Galcasa': 'CSD Galcasa',
    'Marinhense': 'A.C. Marinhense',

    'Glasgow Celtic F.C.': 'Glasgow Celtic',
    'Glasgow Rangers F.C.': 'Glasgow Rangers',
    'Grasshoppers': 'Grasshoppers Zurich',
    'Hamburg SV': 'Hamburger SV',
    




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
    'Millionarios': 'Millonarios FC',
    'Millonarios': 'Millonarios FC',
    'Penarol': 'C.A. Peñarol',
    'Plymouth Argyle': 'Plymouth Argyle F.C.',
    
    
    
    'Sporting Lisbon': 'Sporting Clube de Portugal',
    'Benfica': 'S.L. Benfica',

    'TSC Muenchen 1860': 'TSV 1860 München',


    'Racing (Argentina)': 'Racing Club de Avellaneda',
    'Racing Club (Argentina)': 'Racing Club de Avellaneda',
    'Reggina': 'Reggina Calcio',

    'Celtic F.C.': 'Glasgow Celtic F.C.',
    'Celtic FC': 'Glasgow Celtic F.C.',
    

    'Birmingham City': 'Birmingham City F.C.',

    'Huddersfield Town': 'Huddersfield Town F.C.',
    'Rapid Wien': 'Rapid Vienna',
    'Young Boys\' Club': 'BSC Young Boys',
    'Wisla Krakov': 'Wisła Kraków',
    'Bari': 'A.S. Bari',

    'Everton': 'Everton F.C.',
    'Sunderland': 'Sunderland A.F.C.',
    'Sampdoria': 'U.C. Sampdoria',
    'Saarbrucken': '1. FC Saarbrücken',
    'Saarbruecken': '1. FC Saarbrücken',
    

    'Comunicaciones': 'C.S.D. Comunicaciones',
    'Comunciaciones': 'C.S.D. Comunicaciones',
    'Communicaciones': 'C.S.D. Comunicaciones',
    'Alajuelense': 'L.D. Alajuelense',
    'Herediano': 'C.S. Herediano',
    

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
    'Internazionale': 'Inter Milan',
    'F.C. Internazionale Milano': 'Inter Milan',

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
    'Saprissa': 'Deportivo Saprissa',
    'Deportivo Saprissa S.A.D.': 'Deportivo Saprissa',
    'Etoile de Morne-a-l\'Eau': 'Etoile de Morne-à-l\'Eau',
    'L.D. Alajuelense': 'LD Alajuelense',
    'RC Riviere-Pilote': 'RC Rivière-Pilote',
    'Transvaal': 'SV Transvaal',

    'Undeba': 'UNDEBA',
    'Union Dep. Banda\'bou': 'UNDEBA',

    'Roanoke River Dawgs': 'Roanoke RiverDawgs',
    'Roanoke Riverdawgs': 'Roanoke RiverDawgs',
    'Leslie Verdes': 'Club Verdes',
    'Voorwaarts': 'SV Voorwaarts',
    'Aguila': 'C.D. Águila',
    
    

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
    'Colombian National Team': 'Colombia',
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
    #'Cleveland Stars': 'Cleveland All-Stars',
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

    'Manhattan Beer': 'Chicago Manhattan Beer',
    'Tower Ford Casa Bianca': 'Casa Bianca',

    'Ukrainian SC (East NY)': 'NY Ukrainian SC',

    'White Banner': 'White Banner Malt',
    'White Banner Malt (St. Louis)': 'White Banner Malt',

    # Check these names.
    'Wichita Blue': 'Wichita Blue Angels',

    'Wellston FC (St. Louis)': 'Wellston FC',

    'Chicago Fire S.C.': 'Chicago Fire',

    'Fairhill FC (Philadelphia)': 'Philadelphia Fairhill FC',
    'Fairhill FC': 'Philadelphia Fairhill FC',
    
    
    'Paterson Silk Sox': 'Paterson F.C.',
    'Trenton Highlanders': 'Paterson F.C.',
    'Paterson Caledonian': 'Paterson F.C.',
    'Newark Germans': 'Paterson F.C.',

    'Paterson Caledonian Thistles': 'Paterson Thistles',


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



    'Hungaria': 'New York Hungaria',     
    'NY Hungaria': 'New York Hungaria',
    'New York Hungarian': 'New York Hungaria',
    'New York Hungarians': 'New York Hungaria',
    'Hungaria SC (East NY)': 'New York Hungaria',
    'Hungaria SC': 'New York Hungaria',





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

    'Bruell F.C.': 'Cleveland Bruell Insurance',
    'Bruell Insurance': 'Cleveland Bruell Insurance',
    'Cleveland Bruells': 'Cleveland Bruell Insurance',
    
    'Galicia F.C.': 'New York Galicia',
    'Galicia FC': 'New York Galicia',
    'NY Galicia': 'New York Galicia',
    'Galicia SC': 'Brookhattan',
    'Galicia-Honduras': 'Brookhattan',
    'D.S.C. Brooklyn': 'DSC Brooklyn',
    'Centro-Hispano': 'Centro Hispano',

    'Newark Ukrainian': 'Newark Ukrainian Sitch',

    'Milwaukee Bavarian': 'Milwaukee Bavarian SC',
    'Milwaukee Bavarian Blue Ribbon': 'Milwaukee Bavarian SC',
    'Bavarian SC (WI)': 'Milwaukee Bavarians SC',
    'Milwaukee Bavarians': 'Milwaukee Bavarian SC',
    'Bavarian SC': 'Milwaukee Bavarian SC',

    'Simpkins F.C.': 'Simpkins Ford',
    'Simpkins S.C.': 'Simpkins Ford',
    'Schwaben (Chicago)': 'Chicago Schwaben',

    'Chicago Viking AC': 'Chicago Viking A.A.',
    'Viking AC': 'Chicago Viking AC',
    'Chicago Vikings': 'Chicago Viking AC',

    'Hatikvoh': 'Hatikvoh FC',
    'German Hungarian S.C. (NYC)': 'German Hungarian SC',


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
    'Hartford Bicentennials': 'Connecticut Bicentennials',
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


    'Brookhattan-Galicia': 'Brookhattan',
    'Brookhattan Galicia': 'Brookhattan',

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


    'New York National Giants': 'New York Giants',

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
    'Chicago Sparta Fallstaff': 'Chicago Sparta ABA',
    'Chicago Sparta': 'Chicago Sparta ABA',
    'Sparta (Chicago)': 'Chicago Sparta ABA',
    'Sparta': 'Chicago Sparta ABA',
    'Sparta FC': 'Chicago Sparta ABA',
    'Sparta F.C.': 'Chicago Sparta ABA',
    'Sparta ABA': 'Chicago Sparta ABA',
    'Sparta Leader': 'Chicago Sparta ABA',
    'Sparta Garden City': 'Chicago Sparta ABA',
    'Sparta Union': 'Chicago Sparta ABA',

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
    'Chicago Eagles': 'A.A.C. Eagles',

    'Syracus Suns': 'Syracuse Suns',
    
    'Harmarville': 'Harmarville Hurricanes',

    'Kutis SC': 'St. Louis Kutis',
    'Kutis': 'St. Louis Kutis',
    'St. Louis Kutis SC': 'St. Louis Kutis',

    'Tempête': 'Tempête Football Club',
    'Tempete': 'Tempête Football Club',

    'Trintoc': 'United Petrotrin',
    'Trintoc FC': 'United Petrotrin',

    'Ukrainian Nationals': 'Philadelphia Ukrainians',



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
    'Vancouver Whitecaps FC': 'Vancouver Whitecaps',

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
    'MOBR': 'Mobile Revelers',
    'NASM': 'Nashville Metros',
    'NOST': 'New Orleans Riverboat Gamblers',
    'ORCZ': 'Orange County Zodiac',
    'ORLS': 'Orlando Sundogs',
    'RICK': 'Richmond Kickers',
    'ROCH': 'Rochester Rhinos',
    'SEAS': 'Seattle Sounders',
    'TORL': 'Toronto Lynx',
    'VANW': 'Vancouver Whitecaps',
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


# Need to pull this out of here and put it into pdl stat processing.
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



