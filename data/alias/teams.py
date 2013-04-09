#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from soccerdata.mongo import soccer_db

teams = {}




# Handle name loops before processing everything.
def check_for_team_loops():
    errors = False
    for e in teams.keys():
        try:
            get_team(e)
        except:
            print e
            errors = True

    if errors:
        raise



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

# Need to add slugs for Cote d'Ivoire.    

slugs = {
    'cote-divoire-ivory-coast': 'Côte d\'Ivoire',
}


world = {
    'Western Samoa': 'Samoa',
    'Virginia Tech University': 'Virginia Tech',
    'Dorados Sinaloa': 'Dorados de Sinaloa',
    'Ferencvaros': 'Ferencváros',
    'Uda Dukla': 'Dukla Prague',
    'Ujpest': 'Újpest FC',
    'Újpesti Dózsa': 'Újpest FC',
    'Espoli': 'ESPOLI',
    'Guaraní': 'Club Guaraní',
    'Deportivo Italia': 'Deportivo Petare', # add alias.
    'Exiles SC (South CA)': 'Exiles SC',
    'Real Madrid (TX)': 'Real Madrid AC',
    'Dallas Mustangs Legends': 'Legends FC',
    'Lynch\'s FC': 'Lynch\'s Irish Pub',
    'DS United': 'Lynch\'s Irish Pub',
    'Atlanta FC': 'Atlanta Silverbacks Reserves',
    'Croatian Eagles': 'Milwaukee Croatian Eagles', # Make sure there are no other Croatian Eagles.
    'Newcastle United Jets': 'Newcastle Jets',
    'North Queensland Fury': 'Northern Fury',
    'AS Monaco': 'AS Monaco FC',
    'Ferencvaros': 'Ferencváros',
    'Bon Sucesso': 'Bonsucesso',
    'Fluminense FC': 'Fluminense',
    'UDA Dukla Praha': 'Dukla Prague',
    'CA River Plate': 'River Plate',
    'Atlante CF': 'Atlante',
    'Club Atlante': 'Atlante',
    'Racing Avellaneda': 'Racing Club (Argentina)',
    'Racing Club (Avellaneda)': 'Racing Club (Argentina)',
    'Real Madrid CF': 'Real Madrid',
    'Pepeganga': 'Pepeganga Margarita',
    'Santa Fe': 'CD Santa Fe',
    'Tuluá': 'Cortuluá',
    'San José (Bolivia)': 'CD San José',
    'Libertad': 'Club Libertad',
    'Monagas': 'Monagas SC',
    'Atletico Goianiense': 'Atlético Goianiense',
    'Iquique': 'Deportes Iquique',
    'Union Comercio': 'Unión Comercio',
    'CD Universitario San Francisco Xavier': 'Club Universitario',
    'Gremio Prudente': 'Grêmio Barueri',
    'EC Goias': 'Goiás EC',
    'Union Atletico Maracaibo': 'UA Maracaibo',
    'Coritiba': 'Coritiba FC',
    'Alianza Atletico': 'Alianza Atlético',
    'Gimnasia y Esgrima (LP)': 'Gimnasia y Esgrima',
    'Danubio FC': 'Danubio F.C.',

    'Atletico Wanderers': 'Montevideo Wanderers', # name map.
    'Talleres': 'Talleres de Córdoba',
    'El Nacional (Ecuador)': 'CD El Nacional',
    'Nacional (Ecuador)': 'CD El Nacional',
    'Municipal (Peru)': 'Deportivo Municipal',
    'Universitario (Bolivia)': 'Club Universitario',
    'Atletico-PR': 'Atlético Paranaense',
    'Universidad Cesar Vallejo': 'Universidad César Vallejo',
    'Zamora': 'Zamora FC',
    'Universidad Los Andes': 'Universidad de Los Andes',
    'Atlético Junior': 'Junior de Barranquilla',
    'Deportivo Canarias': 'Deportiva Canarias',
    'Santo Andre': 'Santo André',
    'América (Cali)': 'America de Cali',
    'América Cali': 'America de Cali',
    'Atletico-MG': 'Atlético Mineiro',
    'Deportivo Concepción': 'Deportes Concepción',
    'Colón': 'CA Colón',
    'Bucaramanga': 'Atlético Bucaramanga',
    'Atletico Bucaramanga': 'Atlético Bucaramanga',
    'Cienciano (Cuzco)': 'Cienciano',
    'CD Lara': 'Deportivo Lara',
    'Atletico Huila': 'Atlético Huila',
    'Boyaca Chico FC': 'Boyacá Chicó',
    'Deportivo Anzoategui': 'Deportivo Anzoátegui',
    'Rangers (Chile)': 'C.S.D. Rangers',
    'Always Ready': 'Club Always Ready',
    #'Nuevo de Octubre': '12 de Octubre',
    'St. Louis Mules': 'St. Louis Frogs',
    'Brooklyn Hispanos': 'Brooklyn Hispano',
    'Morse Dry Dock': 'Brooklyn Morse Dry Dock',
    'St. Francis Solanus College': 'Quincy University',
    'Galt FBC': 'Galt F.C.',
    'Randolph Macon College': 'Randolph-Macon College',
    'Stevens Tech': 'Stevens Institute of Technology',
    'Western Reserve University': 'Case Western Reserve University',
    'Washington & Lee University': 'Washington and Lee University',
    'Washburn College': 'Washburn University',
    'Fall River County St Rovers': 'Fall River County Street Rovers',
    'Tijuana Chivas': 'Chivas Tijuana',
    'Lyngby': 'Lyngby BK',
    'Norresundby Boldklub': 'Nørresundby Boldklub',
    'British Guiana': 'Guyana',
    'FYR Macedonia': 'Macedonia',
    'Zaire': 'Congo DR',
    'DR Congo': 'Congo DR',
    'Burma': 'Myanmar',
    'Pegasus AFC': 'Pegasus A.F.C.',
    'Crystal Palace': 'Crystal Palace F.C.',
    'Crystal Palace FC': 'Crystal Palace F.C.',
    'Bromsgrove Rovers FC': 'Bromsgrove Rovers F.C.',
    'Barking FC': 'Barking F.C.',
    'Peterborough United FC': 'Peterborough United F.C.',
    'Newmarket Town FC': 'Newmarket Town F.C.',
    'Ely City FC': 'Ely City F.C.',
    'King\'s Lynn FC': 'King\'s Lynn F.C.',
    'Wisbech Town FC': 'Wisbech Town F.C.',
    'Republic of Ireland': 'Ireland',
    'China PR': 'China',
    'Holland': 'Netherlands',
    'West Germany': 'Germany',
    'Olimpia Asuncion': 'Club Olimpia',
    'Olímpia (Paraguay)': 'Club Olimpia',
    'Cruzeiro EC': 'Cruzeiro',
    'Audax CS Italiano': 'Audax Italiano',
    'Parmalat FC': 'Videoton FC', #team map',
    'AC Parma': 'Parma F.C.',
    'EC Palmeiras': 'Palmeiras',
    'Crvena zvezda Beograd': 'Red Star Belgrade',
    'Atletico Nacional Medellin': 'Atletico Nacional',
    'Milan AC': 'AC Milan',
    'Steaua Bucuresti': 'FC Steaua București',
    'FC Saarbrücken': '1. FC Saarbrücken',
    'Grasshopper': 'Grasshoppers',
    'Gremio FBPA': 'Grêmio',
    'SV River Plate': 'SV River Plate Aruba',
    'Juventus (Nicaragua)': 'Juventus Managua',
    'Pembroke-Hamilton Zebras': 'PHC Zebras',
    'Reveil Sportif': 'Réveil-Sportif',
    'Solidarite Scolaire': 'Solidarité Scolaire',
    'Seba United': 'Montego Bay United', # name map.
    'Santiagueno': 'C.D. Santiagueño',
    'Border Bandits (South TX)': 'Border Bandits',
    'Banat Arsenal': 'Phoenix Banat Storm', #name map
    'Phoenix Pride': 'Phonenix Inferno', #name map
    'Lubbock Tornado': 'Lubbock Lazers', #name map
    'Indiana Kick': 'New York Kick', # name amp.
    'Chicago Vultures': 'Chicago Shoccers', # name map
    'Orlando City FC': 'Orlando City SC',
    'La Victoria (Belize)': 'Nizhee Corozal',
    'Eurokickers': 'A.F.C. Euro Kickers',
    'Boulder Nova': 'Colorado Rapids U-23',
    'LA Blues 23': 'OC Blues Strikers FC',
    'Minnesota Stars FC': 'Minnesota United FC',
    'CFC Azul': 'Connecticut FC Azul',
    'University of Nebraska at Omaha': 'University of Nebraska Omaha',
    'Phoenix FC Wolves': 'Phoenix FC',
    'Pennsylvania Freedom': 'Philadelphia Freedom', # name map
    'Oklahoma City Stampede': 'Oklahoma City Slickers', # name map
    'San Francisco All-Blacks United': 'San Francisco Seals', # name map
    'San Francisco All Blacks': 'San Francisco Seals', # name map
    'San Fernando Valley Golden Eagles': 'Los Angeles Heroes', # name map
    'San Fernando Valley Heroes': 'Los Angeles Heroes', # name map
    'Lubbock Lasers': 'Lubbock Lazers',

    'Hampton Roads Hurricane': 'Virginia Beach Mariners',
    'Los Angeles Salsa U-23\'s': 'Los Angeles Cobras',
    'East Los Angeles Cobras': 'Los Angeles Cobras',
    'East L.A. Cobras': 'East Los Angeles Cobras',
    'East L.A. Cobars': 'East L.A. Cobras',
    'San Antonio Generals': 'San Antonio Pumas',
    'San Antonio Heat': 'San Antonio Pumas',
    'Permian Basin Shootin\' Stars': 'Permian Basin Shooting Stars',
    'Los Angeles Fireballs': 'Tucson Fireballs',# team map
    'Tampa Bay Cyclones': 'Jacksonville Cyclones',# team map
    'Gwinnett County Steamers': 'Atlanta Express',# team map
    'Greensboro Dynamo': 'Carolina Dynamo',# team map
    'Chicago Stingers': 'Chicago Sockers',# team map
    'Richardson Rockets': 'Dallas Rockets',# team map
    'Eastern Shore Sharks': 'Baltimore Bays',# team map
    'Columbus Xoggz': 'Ohio Xoggz', # team map
    'Columbia Heat': 'Columbia Spirit', # team map
    'Vermont Wanderers': 'Vermont Voltage', # team map
    'Tyler Lightning': 'Texas Lightning', # team map
    'Dallas Lightning': 'Texas Lightning', # team map
    'South Florida Sun': 'Fort Lauderdale Sun', # team map
    'Charlotte Gold': 'Carolina Lightnin', # team map
    'Carolina Lightnin': 'Carolina Lightnin\'',
    'Atlanta Lightning': 'Atlanta Quicksilver',  # team map
    'Georgia Steamers': 'Atlanta Quicksilver', # team map
    'Atlanta Lasers': 'Atlanta Magic', # team map
    'Arkansas A\'s': 'Arkansas Diamonds', # team map
    'Ann Arbor Elites': 'Michigan Madness',# team map
    'Albuquerque Geckos': 'Sacramento Geckos', # team map
    'Albuquerque Gunners': 'New Mexico Chiles',
    'Albuquerque Outlaws': 'New Mexico Chiles',
    'New Mexico Roadrunners': 'New Mexico Chiles',

    'Bolívar': 'Club Bolívar',
    'Marítimo (Venezuela)': 'Club Sport Marítimo de Venezuela',
    'Minervén': 'AC Minervén FC',
    'Texas Dutch Lions': 'Houston Dutch Lions',# name map
    'Seattle Wolves': 'Washington Crossfire',# name map

    'Portland Timbers U23\'s': 'Portland Timbers U23s',
    'Orlando City U23': 'Orlando City U-23',
    'Colorado Springs Stampede': 'Colorado Springs Ascent',#name map
    'New Hampshire Phantoms': 'Seacoast United Phantoms',#name map
    'Augusta Fireball': 'Augusta FireBall',
    'Daytona Tigers': 'Orlando Nighthawks',#name map
    'Lancaster Rattlers': 'FC Santa Clarita', #name map
    'Lafayette Lightning': 'Austin Lightning',#name map
    'Hamilton Rage': 'K-W United FC',#name map
    'Grand Rapids Explosion': 'West Michigan Edge',#name map
    'West Michigan Explosion': 'West Michigan Edge',#name map
    'Abbotsford Mariners': 'Fraser Valley Mariners', #name map
    'Fox River Rebels': 'Wisconsin Rebels', #name map
    'Colorado Comets': 'Denver Cougars', #name map
    'Dayton Gems': 'Dayton Gemini', # name map
    'RGV Grandes FC': 'Rio Grande Valley Grandes',
    'FC Jax Destroyers': 'FC JAX Destroyers',
    'Jax Destroyers': 'FC JAX Destroyers',
    'New Jersey Rangers FC': 'New Jersey Rangers',
    'Victoria Highlanders FC': 'Victoria Highlanders',
    'North Sound SeaWolves FC': 'North Sound SeaWolves',
    'Palmetto FC Bantams': 'SC United Bantams',
    'Ocean City FC': 'Ocean City Nor\'easters',# name map.
    'Chattanooga Railroaders': 'Chattanooga Express', # name map
    'Capital District Shockers': 'Albany Alleycats',# name map.
    'Central Florida Lionhearts': 'Central Florida Kraze', # name map.
    'Miami Freedom': 'Miami Sharks',
    'Valenciennes': 'Valenciennes FC',
    'Zaglebie Sosnowiec': 'Zagłębie Sosnowiec',
    'Guimaraes': 'Vitória de Guimarães',
    'Vitoria Guimaraes': 'Vitória de Guimarães',
    '1 Schwechater SC': 'SV Schwechat',
    'Schwechater': 'SV Schwechat',
    'Groningen': 'FC Groningen',
    'Zenit Leningrad': 'FC Zenit Saint Petersburg',
    'Borussia Moenchengladbach': 'Borussia Mönchengladbach',
    'Inter-Bratislava': 'FK Inter Bratislava',
    'Limassol': 'AEL Limassol',
    'RSD Alcala': 'RSD Alcalá',
    'VfL Bad Oldesloe': 'VfL Oldesloe',
    'SV Kaufbeuren': 'SpVgg Kaufbeuren',
    'Torino': 'Torino FC',
    'VFC Setubal': 'Vitória de Setúbal',
    'Vitoria Setubal': 'Vitória de Setúbal',
    'Hibernians': 'Hibernian F.C.',
    'Hibernian': 'Hibernian F.C.',
    'ASV Bergsdorf': 'ASV Bergedorf',
    'VfL Osnabruck': 'VfL Osnabrück',
    'SV Muenster': 'SV Munster',
    'Zaglebie Lubin': 'Zagłębie Lubin',
    'Girona': 'Girona FC',
    'Luton Town': 'Luton Town F.C.',
    'National Fast Club': 'National Fast Clube',
    'Coleraine (Northern Ireland)': 'Coleraine F.C.',
    'Coleraine': 'Coleraine F.C.',
    'Tennis Borussia (Germany)': 'Tennis Borussia Berlin',
    'Neuchatel Xamax': 'Neuchâtel Xamax',
    'Cantazaro': 'US Catazaro 1929',
    'Catazaro': 'US Catazaro 1929',
    'Southampton Saints': 'Southampton F.C.',
    'Anderlecht': 'RSC Anderlecht',
    'Bangor City': 'Bangor City F.C.',
    'Den Bosch': 'FC Den Bosch',
    'DS79': 'FC Dordrecht',
    'SC Wageningen': 'SV Wageningen',
    'Naestved': 'Næstved BK',
    'BK Hacken': 'BK Häcken',
    'Stabaek': 'Stabæk Fotball',
    'SV Itsehoe': 'Itzehoer SV',
    '1. FC Saarbrucken': '1. FC Saarbrücken',
    'Ado Den Haag': 'ADO Den Haag',


    'C.A. Peñarol': 'CA Peñarol',
    'CD San Jose': 'CD San José',
    # Santiago>, <Team: SANTIAGO>]
    'Upton Park FC': 'Upton Park F.C.',
    'Nautico': 'Náutico',
    
    'Atletico de Madrid': 'Atlético de Madrid',
    'Atlético de Madrid': 'Atlético Madrid',
    'Atletico Madrid': 'Atlético Madrid',
    
    #Dominican Rep>, <Team: Dominican Rep.>]
    'Galt FC': 'Galt F.C.',
    'L.D.U. Quito': 'LDU Quito',
    'Project-40': 'Project40',
    
    'Independencia': 'Independência',
    'Central Espanol': 'Central Español',
    
    'Nublense': 'Ñublense',
    'EC Vitoria': 'EC Vitória',
    #Santa Lucia>, <Team: Santa Lucía>]
    'América Cali': 'América (Cali)',

    'University of Massachusetts-Amherst': 'University of Massachusetts Amherst',

    'Houston University': 'University of Houston',
    'Rockhurst College': 'Rockhurst University',
    'Kutztown State College': 'Kutztown University',
    'Glassboro State College': 'Rowan University',
    'Florida Tech': 'Florida Institute of Technology',
    'South Florida University': 'University of South Florida',
    'Metro State College': 'Metropolitan State University of Denver',
    'South East Massachusetts University': 'University of Massachusetts Dartmouth',
    'San Francisco State': 'San Francisco State University',
    'North Adams State College': 'Massachusetts College of Liberal Arts',
    'Southern Maine University': 'University of Southern Maine',
    'Spring Arbor College': 'Spring Arbor University',
    'Brockport State College': 'SUNY Brockport',
    'Lock Haven State College': 'Lock Haven University',
    'Plymouth State': 'Plymouth State University',
    'DeAnza Junior College': 'DeAnza College',
    'Sithoc': 'RKV FC SITHOC',
    'USC Spartanburg': 'University of South Carolina Upstate',
    'Cortland State College': 'SUNY Cortland',

    'Foothill Junior College': 'Foothill College',
    'Auburn University-Montgomery': 'Auburn University at Montgomery',
    'Etoile Haitienne': 'Etoile Haïtienne',
    'MPS Portland Phoenix': 'GPS Portland Phoenix',
    'Portland Phoenix': 'GPS Portland Phoenix',
    'Incarnate Word': 'University of the Incarnate Word',
    'Mount Union College': 'University of Mount Union',
    'Nova Southeastern': 'Nova Southeastern University',
    'Nike Project 40': 'Project 40',
    'US Project 40': 'Project 40',
    'San Antonio Scorpions FC': 'San Antonio Scorpions',

    # add name-maps.
    'Willamette Valley Firebirds': 'Palo Alto Firebirds',
    'Portland Firebirds': 'Palo Alto Firebirds',
    'Silicon Valley Firebirds': 'Palo Alto Firebirds',

    'Embry-Riddle Aeronautical University': 'Embry-Riddle',

    'Tulsa Ambush': 'St. Louis Ambush', # set name map.
    'Bahia': 'EC Bahia',
    'Xiamen Lanshi': 'Xiamen Blue Lions',
    'Shenzhen Jianlibao': 'Shenzhen Ruby',
    'Shenzhen Xiangxue': 'Shenzhen Ruby',
    'Shenzhen Shangqingyin': 'Shenzhen Ruby',
    'Shenzhen Kingway': 'Shenzhen Ruby',
    'Liaoning Yuandong': 'Liaoning Whowin',
    'Liaoning Hongyun': 'Liaoning Whowin',
    'Henan Siwu': 'Henan Jianye',
    'Henan Construction': 'Henan Jianye',
    'Hangzhou Lucheng': 'Hangzhou Greentown',
    'Wuhan Guanggu': 'Wuhan Optics Valley',
    'Wuhan Huanghelou': 'Wuhan Optics Valley',
    'Qingdao Zhongneng': 'Qingdao Jonoon',
    'Qingdao Beilaite': 'Qingdao Jonoon',
    'Beijing Hyundai': 'Beijing Guoan',
    'Shanghai Shenhua SVA': 'Shanghai Shenhua',
    'Chongqing Qiche': 'Chongqing Lifan',
    'Liaoning Zhongyu': 'Liaoning Whowin',
    'Trujillanos': 'Trujillanos FC',
    'Club Blooming': 'Blooming',
    'MTK': 'MTK Budapest',
    'Dynamo Bucharest': 'Dinamo Bucharest',
    'Dundee': 'Dundee FC', # Careful here.
    'Universidad Nacional': 'UNAM', # Bad name.
    'Werder Bremen': 'SV Werder Bremen',
    'Brooklyn Hispanos': 'Brooklyn Hispano',

    'Diriangen': 'Diriangén FC',
    'Haitien': 'R.C. Haïtien',
    'Cartagines': 'C.S. Cartaginés',
    
    'Baltimore Spirit': 'Baltimore Blast',

    #[<Team: Nacional (Uruguay
    #[<Team: Olimpia (Paraguay>, <

    'St Lawrence': 'St. Lawrence',
    'Litoral': 'Lítoral',
    'Lítoral': 'Club Litoral',
    'Prague Americans': 'Prague-Americans',
    'Pepsi Cola': 'Pepsi-Cola',
    'Critchleys': 'Critchley\'s',
    'Mexico FC': 'México FC',
    'IRT FC': 'IRT F.C.',
    'Caribbean All Stars': 'Caribbean All-Stars',
    'St Lawrence': 'St. Lawrence',
    'Dublin FC': 'Dublin F.C.',
    'Santa Lucía': 'Santa Lucia', # Is this saint lucia? (NO!)

    #[<Team: scaryice>, <Team: Scaryice>]
    #[<Team: headhunter>, <Team: HeadHunter>]
    #[<Team: Sean/Geneva>, <Team: Sean.../Geneva>]
    #[<Team: appooOnU>, <Team: AppooOnU>]
    #[<Team: gomichigan24>, <Team: GoMichigan24>]

    # Uncategorized.

    #Berlin (Kitchener) High School
    #Bigelow Sanford (NY)

    #Canadian Explosives (Beloeil)

    #Fairhill (New York)
    #Hermes SC (East NY)
    #Swiss SC (East NY)

    #German SC (Reading)

    #K.B. & B. (93)

    #Olympique (Morne-a-l'Eau)

    #St. Raphael (D5)

    #Vancouver (CSL)
    #Montreal (CSL)
    'Vancouver Canadians': 'Vancouver Royals',
    'Vancouver Royal Canadians': 'Vancouver Royals',

    'Italian Army Team': 'Italian Army',
    'All Skane': 'All-Skane',

    # Asia

    # Japan
    'Gamba Osaka - Japan': 'Gamba Osaka',
    'Grampus Eight - Japan': 'Grampus Eight',
    'Grampus Eight': 'Nagoya Grampus',
    'Instant Dict - Japan': 'Double Flower FA',
    'Shimizu S-Pulse - Japan': 'Shimizu S-Pulse',
    'Vissel Kobe - Japan': 'Vissel Kobe',

    # China

    #East (Hong Kong)
    'Beijing Guo\'an': 'Beijing Guoan',
    'Beijing Guoan - China': 'Beijing Guoan',
    'Guoan (China)': 'Beijing Guoan F.C.',
    'Quan Xing (China)': 'Sichuan Guancheng',
    'Sichuan Quanxing - China': 'Sichuan Quanxing',
    'Sichuan Quanxing': 'Sichuan Guancheng',
    'Team Seiko (Hong Kong)': 'Team Seiko',
    'Team Seiko': 'Seiko SA',

    # Egypt
    'Al-Ahly': 'Al Ahly SC',
    'Al-Ahly S.C.': 'Al Ahly SC',
    'Al Ahly': 'Al Ahly SC',
    'Al Ahly Sporting Club': 'Al Ahly SC',
    'Zamalek': 'Zamalek SC',

    # Australia

    #Victoria State (Australia)
    'Victoria State (Australia)': 'Victoria XI',

    'Adelaide City (Australia)': 'Adelaide City',
    'Sydney FC - Australia': 'Sydney FC',
    'Queensland Roar': 'Brisbane Roar',


    # Europe

    # Israel
    'hapoel': 'Hapoel',
    'Hapoel Tel Aviv': 'Hapoel Tel Aviv F.C.',
    'Hapoel Petah Tikvah': 'Hapoel Petah Tikva F.C.',
    'Hapoel Petah Tikva': 'Hapoel Petah Tikva F.C.',
    'Hapoel Haifa': 'Hapoel Haifa F.C.',
    'Maccabi Tel Aviv': 'Maccabi Tel Aviv F.C.',

    # Portugal
    #Oporto (Portugal)
    #Caldas (Portugal)

    'Belenenses': 'C.F. Os Belenenses',
    'Sporting Club Lisbon': 'Sporting Lisbon',
    'Sporting CP': 'Sporting Lisbon',

    'Academica de Coimbra': 'Académica de Coimbra',
    'Benfica - Portugal': 'S.L. Benfica',
    'Benfica (Portugal)': 'S.L. Benfica',
    'Benfica': 'S.L. Benfica',
    'S.L. Benfica': 'SL Benfica',
    'Marinhense': 'A.C. Marinhense',
    'Mariitimo': 'C.S. Maritimo',
    'Maritimo': 'C.S. Maritimo',
    'Santa Clara - Portugal': 'Santa Clara',
    'Santa Clara': 'C.D. Santa Clara',
    'Sporting Lisbon XI - Portugal': 'Sporting Lisbon XI',
    
    'Sporting Clube de Portugal': 'Sporting Lisbon',
    'varzim': 'Varzim',
    'Varzim': 'Varzim S.C.',
    'Varzim (Portugal)': 'Varzim S.C.',
    'Uniao de Santarem': 'União de Santarém',

    # Spain
    'Barcelona': 'FC Barcelona',
    'Barcelona (Spain)': 'FC Barcelona',
    'Barcelona B': 'FC Barcelona B',
    'Español': 'RCD Espanyol',
    'Espanyol': 'RCD Espanyol',
    'Sabadell': 'CE Sabadell FC',
    'Valladolid': 'Real Valladolid',

    # Belgium
    'Antwerp': 'Royal Antwerp F.C.',
    'Royal Antwerp': 'Royal Antwerp F.C.',

    # Luxembourg

    'Avenir Beggen': 'FC Avenir Beggen',

    # Croatia

    'Hadjuk Split': 'Hajduk Split',

    # Netherlands
    'ADO': 'Ado Den Haag',
    'A.D.O.': 'ADO Den Haag',

    'Ajax - Netherlands': 'Ajax',
    'Ajax': 'AFC Ajax',
    'Ajax Amsterdam': 'AFC Ajax',
    'Ajax Reserves': 'AFC Ajax Reserves',
    'PSV Eindhoven -- Netherlands': 'PSV Eindhoven',
    'Feyenoord - Netherlands': 'Feyenoord',
    'Feijenoord': 'Feyenoord',

    # France
    'Girondins de Bordeaux': 'FC Girondins de Bordeaux',
    'Istres (D2)': 'FC Istres',
    'Monaco': 'AS Monaco FC',
    'Nantes (France)': 'FC Nantes',
    'Nice reserves (D4)': 'OGC Nice Reserves',
    'Nice': 'OGC Nice',
    'Olympique Nice': 'OGC Nice',
    'Paris St.-Germain': 'Paris Saint-Germain F.C.',
    'PSG': 'Paris Saint-Germain F.C.',
    'Paris Saint-Germain': 'Paris Saint-Germain F.C.',
    'Paris St. Germain': 'Paris Saint-Germain F.C.',

    # Serbia

    'SD Crvena Zvezda': 'Red Star Belgrade',
    'Crvena zvezda': 'SD Crvena Zvezda',
    'Crvena Zvezda': 'SD Crvena Zvezda',
    # Partizan Belgrad, Beograd, ...FK Partizan
    'Partizan': 'Partizan Belgrade',

    # Greece
    'apollon': 'Apollon',
    'Apollon': 'Apollon Limassol',
    'A.O. Krete': 'AO Krete',
    'AEK': 'AEK Athens F.C.',
    'AEK Athens': 'AEK Athens F.C.',

    # Austria
    #Wacker (Austria)
    'Rapid Wien': 'Rapid Vienna',
    'FC Salzburg - Austria': 'FC Salzburg',
    'FC Salzburg': 'FC Red Bull Salzburg',
    
    # Switzerland
    'Zurich': 'FC Zurich',
    'FC Zurich': 'FC Zürich',
    'Grasshoppers': 'Grasshoppers Zurich',
    'Grasshoppers Zurich': 'Grasshopper Club Zürich',
    'Stade Laussane - Switzerland': 'Stade Laussane',
    'Young Boys\' Club': 'BSC Young Boys',
    'Young Boys Club': 'BSC Young Boys',
    'Young Boys': 'BSC Young Boys',

    # Italy
    'Torine (Italy)': 'Torino FC',

    'A.S. Roma': 'AS Roma',
    'Arezzo - Italy': 'Arezzo',
    'Bari': 'A.S. Bari',
    'Bologna': 'Bologna F.C. 1909',
    'Bologna FC': 'Bologna F.C. 1909',
    'Fiorentina - Italy': 'Fiorentina',
    'Fiorentina': 'AFC Fiorentina',
    'Genoa - Italy': 'Genoa',
    'Genoa': 'Genoa CFC',
    'Genoa 1893': 'Genoa CFC',
    'Internazionale': 'Inter Milan',
    'F.C. Internazionale Milano': 'Inter Milan',
    'Mantova': 'Mantova F.C.',
    'AC Milan - Italy': 'AC Milan',
    'A.C. Milan': 'AC Milan',
    'A. C. Milan': 'AC Milan',
    'Modena (Italy)': 'Modena F.C.',
    'Modena': 'Modena F.C.',
    'Modena - Italy': 'Modena',
    'Napoli': 'S.S.C. Napoli',
    'Reggina': 'Reggina Calcio',
    'Reggiana - Italy': 'Reggiana',
    'Reggiana': 'AC Reggiana 1919',
    'Roma': 'A.S. Roma',
    'Sampdoria - Italy': 'Sampdoria',
    'Sampdoria': 'U.C. Sampdoria',
    'Venezia - Italy': 'Venezia',
    'lanerossi': 'Lanerossi',
    'Lanerossi': 'Vicenza Calcio',
    'Lanerossi Vicenza': 'Vicenza Calcio',
    'AC Lanerossi-Vicenza': 'Vicenza Calcio',

    # Hungary
    'Ferencvaros': 'Ferencvárosi TC',
    'Ujpest Dosza': 'Újpest FC',
    'Ujpest': 'Újpest FC',

    # Czech
    'Slavia Prague': 'SK Slavia Prague',
    'SSK Vitkovice - Czech': 'SSK Vitkovice',
    'SSK Vitkovice': 'FC Vítkovice',

    # Poland
    'Amika Wronski (Poland)': 'Amica Wronki',
    'Gornik': 'Gornik Zabrze',
    'Gornik Zabrze': 'Górnik Zabrze',
    'K. S. Ruch': 'Ruch Chorzów',
    'K.S Ruch (Poland)': 'Ruch Chorzów',
    'K.S. Ruch': 'Ruch Chorzów',
    'KS Ruch': 'K.S. Ruch',
    'Legia Warsaw': 'Legia Warszawa',
    'Legia Warzaw': 'Legia Warszawa',
    'Legia-Daewoo Warsaw (Poland)': 'Legia Warsaw',
    'Legia-Daewoo Warsaw': 'Legia Warsaw',
    'Legia-Daewoo Warsaw - Poland': 'Legia-Daewoo Warsaw',
    'Wisla Krakow - Poland': 'Wisla Krakow',
    'Wisla Krakov': 'Wisła Kraków',
    'Wisla Krakow': 'Wisła Kraków',

    # Turkey
    'Besiktas': 'Beşiktaş J.K.',
    'Galatasaray - Turkey': 'Galatasaray',
    'Fenerbahce': 'Fenerbahçe S.K.',

    # Ukraine
    'Dynamo Kiev -- Ukraine': 'Dynamo Kiev',
    'Dinamo Kiev': 'FC Dynamo Kyiv',
    'Dynamo Kiev': 'FC Dynamo Kyiv',

    # Russia
    'Rubin Kazan -- Russia': 'Rubin Kazan',
    'Torpedo Moscow -- Russia': 'Torpedo Moscow',
    'Torpedo Moscow': 'FC Torpedo Moscow',
    'Moscow Torpedo': 'FC Torpedo Moscow',
    'Moscow Dynamo': 'FC Dynamo Moscow',

    # Scandinavia
    #Cevle (Bryn) # Very likely Gavle in Sweden.
    #Sweden
    #Norway
    #Denmark

    'Jonkopping (Sweden)': 'Jonkopping',

    'Malmo FF': 'Malmö FF',
    'Malmö': 'Malmö FF',

    'Gif Sundsvall': 'GIF Sundsvall',
    'Goteborg Orgryte': 'Örgryte IS',
    'Norrkoeping': 'IFK Norrköping',
    'Norrkoping': 'IFK Norrköping',
    'IFK Norrkoping': 'IFK Norrköping',
    'Hammarby': 'Hammarby IF',
    'Malmo': 'Malmö FF',
    'Malmö': 'Malmö FF',
    'Lille': 'Lille OSC',
    

    'Oporto (Portugal)': 'Oporto',
    

    'Helsingborg': 'Helsingborgs IF',
    'Helsingborgs': 'Helsingborgs IF',
    'Bodo/Glimt': 'FK Bodø/Glimt',
    'Orebro': 'Örebro SK',
    'Elfsborg': 'IF Elfsborg',
    'Gif Sundsvall -- Sweden': 'Gif Sundsvall',
    'Odd Grenland -- Norway': 'Odd Grenland',
    'Rosenborg Trondheim -- Norway': 'Rosenborg Trondheim',
    'Rosenborg Trondheim': 'Rosenborg BK',
    'Lyn Oslo -- Norway': 'Lyn Oslo',
    'Fylkir (Iceland)': 'Fylkir',
    'Fylkir - Iceland': 'Fylkir',
    'IBV - Iceland': 'IBV',
    'Lyngby - Denmark': 'Lyngby',
    'A.I.K.': 'AIK Fotboll',
    'AIK': 'AIK Fotboll',
    'G.A.I.S.': 'GAIS',    
    'Jonkopping': 'Jönköpings Södra IF',
    'Sundsvall': 'GIF Sundsvall',
    'Ikast (Denmark)': 'Ikast FS',
    'Ikast': 'Ikast FS',
    'Ikast - Denmark': 'Ikast',
    'IFK Gothenburg - Sweden': 'IFK Göteborg',
    'IFK Gothenburg': 'IFK Göteborg',
    'JFK Gothenburg (Sweden)': 'IFK Göteborg',

    'FinnPa - Finland': 'FinnPa',
    'Djurgardens IF': 'Djurgårdens IF',
    'Viborg - Denmark': 'Viborg',
    'Viborg': 'Viborg FF',
    'Valur': 'Valur FC',
    'Norresundby Boldklub - Denmark': 'Norresundby Boldklub',
    'Viking Stavangar -- Norway': 'Viking FK',
    'Bodo/Glimt -- Norway': 'Bodo/Glimt',
    'Stabaek -- Norway': 'Stabaek',

    # Germany

    #Tennis Borussia (Germany)
    #Hansa (Germany)
    #03 Lunenburg (Germany)

    'TSV Munich 1860': '1860 Munchen',

    'Freiburger': 'SC Freiburg',
    '1860 Munchen -- Germany': '1860 Munchen',
    '1860 Munchen': 'TSV 1860 München',
    'TSC Muenchen 1860': 'TSV 1860 München',
    '1860 Munich': 'TSV 1860 München',
    'Bayer Leverkusen - Germany': 'Bayer Leverkusen',
    'Bayern Munich - Germany': 'Bayern Munich',
    'Bayern Munchen': 'FC Bayern Munich',
    'Bayern Munich': 'FC Bayern Munich',
    'Bayern München': 'FC Bayern Munich',
    'VFL Bochum': 'VfL Bochum',
    'Borussia Brandaachen': 'Borussia Brand-Aachen',
    'Fortune Sittard': 'Fortuna Sittard',
    'Hamburg SV': 'Hamburger SV',
    'Hamburg SV - Germany': 'Hamburg SV',
    'H.S.V. Hannover': 'Hannover 96',
    'Hannover \'96': 'Hannover 96',
    'hertha': 'Hertha BSC',
    'Hertha': 'Hertha BSC',
    'Karlsruhe': 'Karlsruher SC',
    'Karlsruher SC': 'Karlsruher FV',
    'Karlsruhe FV': 'Karlsruher FV',
    'FC Cologne': '1. FC Köln',
    'F. C. Koln': '1. FC Köln',
    '1.FC Koln': '1. FC Köln',
    'FC Nurnberg - Germany': 'FC Nurnberg',
    'FC Nurnberg': '1. FC Nuremberg',
    'Nuernberg': '1. FC Nuremberg',
    'Reutlingen': 'SSV Reutlingen 05',
    'Saarbrucken': '1. FC Saarbrücken',
    'Saarbruecken': '1. FC Saarbrücken',
    'Schalke 04': 'FC Schalke 04',
    'Splitdorf FC': 'Splitdorf F.C',
    'V.F.B. Stuttgart': 'VfB Stuttgart',
    'Tusberg Landshut - Germany': 'Tusberg Landshut',

    # Ireland
    'Dundalk (Ireland)': 'Dundalk F.C.',
    'Dundalk': 'Dundalk F.C.',


    'Galway (Ireland)': 'Galway United FC',
    'Galway': 'Galway United FC',

    
    # Northern Ireland

    'Linfield (Northern Ireland)': 'Linfield F.C.',
    'Linfield': 'Linfield F.C.',
    'Glenavon (Northern Ireland)': 'Glenavon F.C.',
    'Glenavon': 'Glenavon F.C.',
    'Glenavon FC': 'Glenavon F.C.',
    'Ards (Northern Ireland)': 'Ards F.C.',
    'Ards': 'Ards F.C.',
    #Coleraine (Northern Ireland)


    # Scotland
    'Dumfermline': 'Dunfermline',
    'Dunfermline': 'Dunfermline Athletic F.C.',
    'Aberdeen': 'Aberdeen F.C.',
    'Aberdeen Dons': 'Aberdeen F.C.',
    'Celtic Glasgow - Scotland': 'Glasgow Celtic',
    'Celtic F.C.': 'Glasgow Celtic F.C.',
    'Celtic FC': 'Glasgow Celtic F.C.',
    'Celtic': 'Glasgow Celtic',
    'Glasgow Celtic F.C.': 'Glasgow Celtic',
    'Glasgow Rangers F.C.': 'Glasgow Rangers',
    'Glasgow Rangers - Scotland': 'Glasgow Rangers',
    'Rangers': 'Rangers F.C.',
    'Rangers FC': 'Rangers F.C.',
    'Rangers F.C.': 'Glasgow Rangers F.C.',
    'Heart of Midlothian': 'Heart of Midlothian F.C.',
    'Hearts of Midlothian F.C.': 'Heart of Midlothian F.C.',
    'Hearts': 'Hearts of Midlothian F.C.',
    'Hearts of Midlothian': 'Hearts of Midlothian F.C.',
    'Kilmarnock': 'Kilmarnock F.C.',
    'Kilmarnock FC': 'Kilmarnock F.C.',

    # England
    'Walsall': 'Walsall F.C.',

    'Notts Forest': 'Nottingham Forest', # Presumably there is not really a Notts Forest. (except in San Diego)
    'Millwall': 'Millwall F.C.',
    'Millwall FC': 'Millwall F.C.',
    'Royal Arsenal': 'Arsenal',
    'Newton Heath': 'Manchester United',
    'Macclesfield Town': 'Macclesfield Town F.C.',


    'Aston Villa': 'Aston Villa F.C.',
    'Aston Villa - England': 'Aston Villa',
    'Birmingham City': 'Birmingham City F.C.',
    'Blackpool': 'Blackpool F.C.',
    'Bristol (England)': 'Bristol City F.C.',
    'Bristol City': 'Bristol City F.C.',
    'Burnley': 'Burnley F.C.',
    'Burnley FC': 'Burnley F.C.',
    'Charlton Athletic': 'Charlton Athletic F.C.',
    'Chelsea': 'Chelsea FC',
    'Chelsea F.C.': 'Chelsea FC',
    'Coventry City': 'Coventry City FC',
    'Derby County - England': 'Derby County',
    'Everton': 'Everton F.C.',
    'Everton - England': 'Everton',
    'Fulham - England': 'Fulham',
    'Huddersfield Town': 'Huddersfield Town F.C.',
    'Ipswich Town': 'Ipswich Town F.C.',
    
'Leeds United A.F.C.': 'Leeds United',
    'Leeds United - England': 'Leeds United',
    'Leicester City - England': 'Leicester City',
    'Liverpool': 'Liverpool F.C.',
    'Liverpool FC': 'Liverpool F.C.',
    'Manchester City': 'Manchester City F.C.',
    'Manchester United - England': 'Manchester United',
    'Manchester United FC': 'Manchester United',
    'Middleborough FC': 'Middlesbrough F.C.',
    'Middlesbrough': 'Middlesbrough F.C.',
    'Newcastle': 'Newcastle United F.C.',
    'Newcastle United': 'Newcastle United F.C.',
    'Newcastle United - England': 'Newcastle United',
    'Norwich City': 'Norwich City F.C.',
    'Nottingham Forest': 'Nottingham Forest F.C.',
    'Plymouth Argyle': 'Plymouth Argyle F.C.',
    'Port Vale': 'Port Vale F.C.',
    'Portsmouth (England)': 'Portsmouth F.C.',
    'Portsmouth FC': 'Portsmouth F.C.',
    'Portsmouth': 'Portsmouth FC',
    'Preston North End': 'Preston North End F.C.',
    'Sheffield Wednesday - England': 'Sheffield Wednesday',
    'Sheffield United - England': 'Sheffield United',
    'Stockport County': 'Stockport County F.C.',
    'Stoke (England)': 'Stoke City F.C.',
    'Stoke City': 'Stoke City F.C.',
    'Sunderland - England': 'Sunderland',
    'Sunderland': 'Sunderland A.F.C.',
    'Tottenham Hotspur - England': 'Tottenham Hotspur',
    'Tottenham Hotspurs': 'Tottenham Hotspur',
    'West Brom Albion': 'West Bromwich Albion',
    'West Ham': 'West Ham United',
    'Wigan Athletic': 'Wigan Athletic F.C.',
    'Wolverhampton': 'Wolverhampton Wanderers F.C.',
    'Workington AFC': 'Workington A.F.C.',


    


    # South America

    # Venezuela

    'Minerven': 'Minervén',



    'Deportivo Tachira': 'Deportivo Táchira',
    'Tachira': 'Deportivo Táchira FC',
    'Táchira': 'Deportivo Táchira FC',
    'Deportivo Táchira': 'Deportivo Táchira FC',
    'Maritimo (Venezuela)': 'Marítimo (Venezuela)',
    'Caracas F.C.': 'Caracas FC',

    'Italchacao -- Venezuela': 'Italchacao',
    'Italchacao': 'Deportivo Petare',
    'Deportivo Italchacao': 'Deportivo ItalChacao',
    'Deportivo ItalChacao': 'Deportivo Petare',
    'Estudiantes (Venezuela)': 'Estudiantes de Mérida',
    'Maritimo (Venezuela': 'C.S. Marítimo de Venezuela',


    # Colombia
    'Medellin': 'Medellín',
    'Cucuta Deportivo': 'Cúcuta Deportivo',
    'Boyaca Chico': 'Boyacá Chicó',
    'Independiente Medellin': 'Independiente Medellín',
    'América (Cali)': 'América Cali',
    'Atletico Nacional': 'Atlético Nacional',
    'Junior (Colombia)': 'Junior de Barranquilla',
    'Atletico Junior': 'Junior de Barranquilla',
    'Atlético Junior': 'Junior de Barranquilla',
    'America de Cali': 'América de Cali',
    'America (Cali)': 'América de Cali',
    'América Cali': 'América de Cali',
    'America Cali': 'América de Cali',
    'America de Cali - Colombia': 'America de Cali',
    'America-Cali': 'América de Cali',
    'Buenaventura - Colombia': 'Buenaventura',
    'Bueneventura (Colombia)': 'Buenaventura',
    'Deportivo Cali - Colombia': 'Deportivo Cali',
    'Millonarios - Colombia': 'Millonarios',
    'Millionarios -- Colombia': 'Millonarios',
    'Millionarios': 'Millonarios FC',
    'Millonarios': 'Millonarios FC',
    'Soacha FC - Colombia': 'Soacha FC',
    'Indep. Medellín': 'Independiente Medellín',
    'DIM': 'Independiente Medellín',

    # Ecuador
    'Valdez S.C.': 'Valdez SC',
    'LDU (Quito)': 'LDU Quito',
    'LDU': 'LDU Quito',
    'America de Quito': 'América de Quito',
    'Aucas': 'SD Aucas',
    'Barcelona -- Ecuador': 'Barcelona Sporting Club',
    'Barcelona (Ecuador)': 'Barcelona Sporting Club',
    'El Nacional': 'CD El Nacional',
    'El Nacional (Quito)': 'CD El Nacional',
    'LDU (Quito)': 'LDU Quito',
    'Olmedo (Riobamba)': 'CD Olmedo',
    'Everest': 'CD Everest',

    # Peru
    'Universidad San Martin': 'Universidad San Martín',

    'Union Huaral': 'Unión Huaral',

    'Leon de Huanuco': 'León de Huánuco',
    'León de Huanuco': 'León de Huánuco',


    'Sport Ancash': 'Sport Áncash',
    'Alianza Lima - Peru': 'Alianza Lima',
    'Sporting Cristal -- Peru': 'Sporting Cristal',
    'Universitario (Peru)': 'Universitario',
    'Universitario (Lima)': 'Universitario',

    # Bolivia

    '31 de Octubre': 'Club 31 de Octubre',
    'Aurora (Bolivia)': 'Club Aurora',
    'Bolivar': 'Bolívar',
    'Bolívar': 'Club Bolívar',
    'Real Potosi': 'Real Potosí',
    'San Jose (Oruro)': 'CD San José',
    'San Jose (Bolivia)': 'San José (Bolivia)',
    'San Jose (Bolivia': 'CD San José',
    'San José (Bolivia)': 'CD San José',
    'Universitario (Sucre)': 'CD Universitario San Francisco Xavier',

    # Paraguay
    'Atl. Colegiales': 'Atlético Colegiales',

    'Atletico Colegiales': 'Atlético Colegiales',
    #'Guarani': 
    'Guarani': 'Club Guaraní',
    'Guaraní': 'Club Guaraní',
    'Guarani (Paraguay)': 'Club Guaraní',
    'Olimpia (Paraguay)': 'Club Olimpia',
    'Olimpia Paraguay': 'Club Olimpia',
    'Cerro Porteno': 'Cerro Porteño',
    'Nacional (Paraguay)': 'Club Nacional',
    'Nacional (Asunción)': 'Club Nacional',
    'Nacional (Asuncion)': 'Club Nacional',
    'Nueve de Octubre': '12 de Octubre',
    'Sol de America': 'Club Sol de América',
    'Sol de América': 'Club Sol de América',


    # Chile
    'Universidad de Concepcion': 'Universidad de Concepción',
    'Union Espanola': 'Unión Española',
    'Concepcion': 'Concepción',
    'Deportes Concepcion': 'Deportes Concepción',


    'Colo Colo - Chile': 'Colo Colo',
    'Colo Colo': 'Colo-Colo',
    'Everton (Chile)': 'Everton de Viña del Mar',
    'Magallanes - Chile': 'Magallanes',
    'Magallanes': 'Deportes Magallanes',
    'O\'Higgins': 'O\'Higgins F.C.',
    'Palestino - Chile': 'Palestino',
    'Palestino': 'CD Palestino',
    'San Felipe - Chile': 'Unión San Felipe',
    'Union San Felipe': 'Unión San Felipe',
    'Universidad de Chile - Chile': 'Club Universidad de Chile',
    'Universidad Catolica - Chile': 'CD Universidad Católica',
    'Universidad Catolica': 'CD Universidad Católica',
    'Universidad Católica': 'CD Universidad Católica',
    'Uni. Católica': 'CD Universidad Católica',
    'Univ. Católica': 'CD Universidad Católica',
    'Univ. Católica': 'CD Universidad Católica',

    # Uruguay

    'Danubio': 'Danubio FC',
    'Defensor': 'Defensor SC',
    'Defensor Sporting': 'Defensor SC',
    'Liverpool (Montevideo)': 'Liverpool FC (Montevideo)',
    'Liverpool (Uruguay)': 'Liverpool FC (Montevideo)',
    'Nacional de Montevideo': 'Nacional',
    'Club Nacional de Football': 'Nacional',
    'Nacional -- Uruguay': 'Nacional',
    'Nacional (Montevideo)': 'Nacional',
    'Nacional (Uruguay)': 'Nacional',
    'Penarol': 'C.A. Peñarol',
    'CA Penarol': 'C.A. Peñarol',
    'Peñarol': 'C.A. Peñarol',
    'Racing (Montevideo)': 'Racing Club de Montevideo',
    'River Plate (Uruguay)': 'River Plate (Montevideo)',

    # Argentina

    'Independiente (Argentina)': 'CA Independiente',
    'Velez Sarsfield': 'Vélez Sarsfield',
    'Arsenal (Argentina)': 'Arsenal de Sarandí',
    'Arsenal de Sarandi': 'Arsenal de Sarandí',
    'Colon (Argentina)': 'CA Colon',
    'Colon (Santa Fe)': 'CA Colon',
    'Colon': 'CA Colon',
    'Colón': 'CA Colon',
    'CA Colon': 'CA Colón',
'Belgrano': 'Club Atlético Belgrano',
    'Boca Juniors - Argentina': 'Boca Juniors',
'CA Boca Juniors': 'Boca Juniors',
    'Deportivo Moron': 'Deportivo Morón',
    'Estudiantes': 'Estudiantes de La Plata',
    'Estudiantes LP': 'Estudiantes de La Plata',
    'Estudiantes (Argentina)': 'Estudiantes de La Plata',
    'Huracan': 'Huracán',
    'Independiente': 'CA Independiente',
    'Independiente': 'CA Independiente',
    'Lanus': 'Lanús',
    'Newells Old Boys': 'Newell\'s Old Boys', 
    'Racing (Argentina)': 'Racing Club de Avellaneda',
    'Racing Club (Argentina)': 'Racing Club de Avellaneda',
    'Sacachisapas': 'Sacachispas Fútbol Club', 
    'Sacachispas': 'Sacachispas Fútbol Club',
    'San Lorenzo - Argentina': 'San Lorenzo',
    'San Lorenzo': 'San Lorenzo de Almagro',
    'San Lorenzo Alm.': 'San Lorenzo de Almagro',

    # Brazil
#America (RJ)>, <Team: América (RJ)>]
    'Criciuma': 'Criciúma',

    'America de Rio de Janeiro': 'America Rio',
    'America RJ': 'America Rio',
    'Atletico Mineiro': 'Atlético Mineiro',
    'Atletico Paranaense': 'Atlético Paranaense',
    'Avai': 'Avaí FC',
    'Avaí': 'Avaí FC',
    'Bangu AC': 'Bangu Atlético Clube',
    'Bangu': 'Bangu Atlético Clube',
    'Bonsucesso (Brazil)': 'Bonsucesso FC',
    'Botafogo FR': 'Botafogo',
    'Cruzeiro (Brazil)': 'Cruzeiro',
    'Flamengo (Brazil)': 'Flamengo',
    'CR Flamengo': 'Flamengo',
    'Goias': 'Goiás EC',
    'Goiás': 'Goiás EC',
    'Goias EC': 'Goiás EC',
    'Gremio': 'Grêmio',
    'Gremio (Porto Alegre)': 'Grêmio',
    'Macaupa (Brazil)': 'Macapá',
    'Macaupo': 'Macapá',
    'National Fast Club (Brazil)': 'National Fast Club',
    'Oscar\'s FC - Brazil': 'Oscar\'s FC',
    'Parana': 'Paraná',
    'Paraná': 'Paraná Clube',
    'Parana Clube': 'Paraná Clube',
    'Palmeiras - Brazil': 'Palmeiras',
    'Santos (Brazil)': 'Santos FC',
    'Santos': 'Santos FC',
    'Sao Caetano': 'São Caetano',
    'Sao Paulo FC': 'São Paulo FC',
    'Sao Paulo': 'São Paulo FC',
    'São Paulo': 'São Paulo FC',
    'Sport (Recife)': 'Sport Club do Recife',
    'Sport Club do Recife': 'SC Recife',
    'Recife': 'SC Recife',
    'Uberlandia (Brazil)': 'Uberlândia Esporte Clube',
    'Uberlandia': 'Uberlândia Esporte Clube',
    'Vasco da Gama -- Brazil': 'Vasco da Gama',
    'Vasco Da Gama': 'Vasco da Gama',
    'Vasco da Gama': 'CR Vasco da Gama',
    'Vitoria (Salvador)': 'EC Vitória',

    
    # CONCACAF

    # Suriname
    'Inter Monegotapoe': 'Inter Moengotapoe',
    'Inter Moengotapoe - Surinam': 'Inter Moengotapoe',
    'SV Leo Victor - Surinam': 'SV Leo Victor',
    'Robin Hood': 'S.V. Robinhood',
    'SV Robin Hood': 'S.V. Robinhood',
    'SV Robinhood': 'S.V. Robinhood',
    'Transvaal': 'SV Transvaal',
    'SV Transvaal -- Suriname': 'SV Transvaal',
    'Voorwaarts': 'SV Voorwaarts',

    # French Guiana
    'Sport Guyanais': 'ASL Sport Guyanais',

    # Bermuda
    #Vasco da Gama (Bermuda)
    'Vasco Da Gama (Bermuda)': 'Vasco da Gama (Bermuda)',
    'Pembroke-Hamilton': 'Pembroke Hamilton Club',
    'Pembroke-Hamilton Club': 'Pembroke Hamilton Club',

    # Aruba
    'RCA': 'Racing Club Aruba',
    'Racing Club Aruba': 'SV Racing Club Aruba',

    # Martinique
    'Olympique (Ft-de-France)': 'Olympique du Marin',
    'RC Riviere-Pilote': 'RC Rivière-Pilote',

    # Curacao
    'Undeba': 'UNDEBA',
    'Union Dep. Banda\'bou': 'UNDEBA',
    'Victory Boys': 'SV Victory Boys',


    # Guadeloupe
    #Red Star (Pointe-a-Pitre)
    #Arsenal (Petit-Bourg)
    #Gauloise (Basse-Terre)
    'Etoile de Monre-a-l\'Eau': 'Etoile de Morne-à-l\'Eau',
    'Etoile de Morne-a-l\'Eau': 'Etoile de Morne-à-l\'Eau',
    'Etoile de Morne-à-l\'Eau': 'L\'Etoile de Morne-à-l\'Eau',
    'Juventus (Saint-Martin)':  'Juventus de Saint-Martin',
    'Juventus de Saint-Anne': 'ASG Juventus de Sainte-Anne',
    'Solidarite Scolair': 'Solidarite Scolaire',

    # Antigua
    'Hoppers FC - Antigua': 'Hoppers FC',
    'HitachiCentre SAP FC - Antigua': 'Hitachi Centre SAP FC',

    'Antigua Barricudas FC': 'Antigua Barracuda',
    'Antigua Barracuda': 'Antigua Barracuda FC',

    # Jamaica
    #Cavalier (Jamiaca)
    #St. James (Jamaica)
    #Santos (Jamaica)
    'Regiment (JAM)': 'Regiment (Jamaica)',
    #Kingston (Jamaica)
    #Regiment (Jamaica)

    'Arnett Gardens-- Jamaica': 'Arnett Gardens',
    'Arnett Gardens': 'Arnett Gardens F.C.',
    'Harbour View FC -- Jamaica': 'Harbour View FC',
    'Harbour View': 'Harbour View FC',

    # Haiti
    #Victory Club (Haiti)
    #Victory Sportif (Haiti)

    'Victory Sportif (Haiti)': 'Victory Sportif Club',
    'Victory Club (Haiti)': 'Victory Sportif Club',
    'Racing Club (Haiti)': 'Racing Club Haitien',
    'Racing (Haiti)': 'Racing Club Haitien',
    'Racing Club Haitien': 'R.C. Haïtien',
    'Tempête': 'Tempête Football Club',
    'Tempete': 'Tempête Football Club',
    'Violette': 'Violette AC',
    
    # Trinidad

    'Regiment (TRI)': 'Regiment (Trinidad)',
    #ASL (Trinidad)
    #Regiment (Trinidad)

    'Joe Public -- T & T': 'Joe Public',
    'Joe Public': 'Joe Public F.C.',
    'Joe Public FC': 'Joe Public F.C.',
    'San Juan Jabloteh -- T & T': 'San Juan Jabloteh',
    'United Petrotrin -- T & T': 'United Petrotrin',
    'Trintoc': 'United Petrotrin',
    'Trintoc FC': 'United Petrotrin',
    'W Connection FC': 'W Connection',
    'W. Connection -- Jamaica': 'W Connection',
    'W. Connection FC - Trinidad': 'W Connection',


    # El Salvador
    #Independiente (El Salvador)
    'Aguila': 'C.D. Águila',
    'Aguila - El Salvador': 'CD Aguila',
    'Alianza FC': 'Alianza',
    'Alianza - El Salvador': 'Alianza',
    'CD Aguila - El Salvador': 'CD Aguila',
    'C.D. Aguila': 'C.D. Águila',
    'CD Aguila': 'C.D. Águila',
    'CD Aguila (El Salvador)': 'C.D. Águila',
    'FAS - El Salvador': 'FAS',
    'C.D. FAS': 'CD FAS',
    'C.D. Fas': 'CD FAS',
    'CD Fas': 'CD FAS',
    'FAS': 'C.D. FAS',
    'Deportivo FAS': 'C.D. FAS',
    'Isidro-Metapan': 'Isidro Metapán',
    'Isidro Metapan': 'Isidro Metapán',
    'Juventud Olimpica': 'Juventud Olímpica',
    'Luis Angel Firpo-- El Salvador': 'Luis Angel Firpo',
    'Luis Angel Firpo - El Salvador': 'Luis Angel Firpo',
    'LA Firpo': 'Luis Angel Firpo',
    'FC Firpo': 'Luis Angel Firpo',
    'Club Deportivo Marte': 'Marte',
    'Marte FC': 'Marte',
    'Marte': 'C.D. Atlético Marte',
    'Atletico Marte': 'C.D. Atlético Marte',
    'C.D. Atletico Marte': 'C.D. Atlético Marte',

    # Nicaragua 
    #Juventus (Nicaragua)
    'America (Nicaragua)': 'América Managua',
    'Real Estelí': 'Real Estelí F.C.',
    'Real Estelí': 'Real Estelí F.C.',
    'Esteli': 'Real Estelí F.C.',
    'Real Esteli': 'Real Estelí F.C.',
    'Real Estelí': 'Real Estelí F.C.',

    # Panama
    #Projusa (Veraguas)
    'Deportivo Arabe Unido --Panama': 'Arabe Unido',
    'Chorrillo': 'Chorrillo F.C.',
    'San Francisco': 'San Francisco FC',
    'Tauro': 'Tauro FC',

    # Belize
    #Boca Juniors (S. Ignacio)
    'Juventus (Orange Walk)': 'Juventus (Belize)',
    
    'Acros': 'Acros Crystal',
    'Hankok Verdes': 'Club Verdes',
    'Leslie Verdes': 'Club Verdes',
    'Real Verdes': 'Club Verdes',

    # Guatemala
    'Petapa': 'Deportivo Petapa',

    'Suchitepéquez': 'C.D. Suchitepéquez',

    'Teculutan': 'Teculután',
    'Amatitlan': 'Amatitlán',
    'Dep. Carcha': 'Deportivo Carchá',
    'Dep. Carchá': 'Deportivo Carchá',
    'Juv. Retalteca': 'Juventud Retalteca',
    'Juventud R.': 'Juventud Retalteca',

    'Aurora': 'Aurora F.C.',
    'Coban - Guatemala': 'Coban',
    'Coban': 'Cobán Imperial',
    'Cobán': 'Cobán Imperial',
    'Coban Imperial': 'Cobán Imperial',
    'Comunicaciones': 'C.S.D. Comunicaciones',
    'Comunciaciones': 'C.S.D. Comunicaciones',
    'Communicaciones': 'C.S.D. Comunicaciones',
    'C.S.D. Comunicaciones': 'CSD Comunicaciones',
    'Comunicaciones - Guatemala': 'CSD Comunicaciones',
    'CSD Comunicaciones-- Guatemala': 'CSD Comunicaciones',
    'Carcha': 'Deportivo Carchá',
    'Dep. Carchá': 'Deportivo Carchá',
    'Escuintla': 'Deportivo Escuintla',
    'Jalapa': 'CD Jalapa',
    'Galcasa': 'CSD Galcasa',
    'Municipal': 'CSD Municipal',
    'CSD Municipal -- Guatemala': 'CSD Municipal',
    'Suchitepequez - Guatemala': 'Suchitepequez',
    'Suchitepequez': 'C.D. Suchitepéquez',
    'USAC': 'Universidad de San Carlos',
    'Xelaju': 'Xelajú MC',
    'Xelajú': 'Xelajú MC',
    'Xelaju MC': 'Xelajú MC',
    'Zacapa': 'Deportivo Zacapa',

    # Honduras

    #Atletico Indio (Honduras)
    'Marathon': 'Marathón',
    'Motagua': 'CD Motagua',
    'Motagua -- Honduras': 'Motagua',
    'Olimpia': 'CD Olimpia',
    'Olimpia (Honduras)': 'CD Olimpia',

    'Olympia - Honduras': 'CD Olimpia',
    'CD Olympia-- Honduras': 'CD Olimpia',
    'Olimpia -- Honduras': 'Olimpia',
    'Olímpia (H)': 'CD Olimpia',
    'Universidad (Honduras)': 'Pumas UNAH',
    'Platense (Honduras)': 'Platense F.C.',
    'Platense': 'Platense F.C.',
    'Real Espana': 'Real España',
    'Real Espana-- Honduras': 'Real Espana',

    # Costa Rica

    'Perez Zeledon': 'Pérez Zeledón',

    #Uruguay (Coronado)
    'Alajuelense': 'L.D. Alajuelense',
    'LD Alajuelense-- Costa Rica': 'LD Alajuelense',
    'Alajuela -- Costa Rica': 'Alajuelense',
    'L.D. Alajuelense': 'LD Alajuelense',
    'Deportivo Belen - Costa Rica': 'Belen',
    'Brujas': 'Brujas FC',
    'Herediano': 'C.S. Herediano',
    'Herediano - Costa Rica': 'Herediano',
    'AD Limonense - Costa Rica': 'AD Limonense',
    'Limon - Costa Rica': 'Limon',
    'Limon': 'AD Limonense',
    'AD Limonense': 'Limón FC',
    'Puntarenas FC - Costa Rica': 'Puntarenas FC',
    'Puntarenas - Costa Rica': 'Puntarenas',
    'Puntarenas': 'Puntarenas FC',
    'San Lorenzo - Costa Rica': 'San Lorenzo Costa Rica',
    'Santa Teresita FC -Costa Rica': 'Santa Teresita FC',
    'Deportivo Saprissa -Costa Rica': 'Deportivo Saprissa',
    'CD Saprissa-- Costa Rica': 'Saprissa',
    'Saprissa': 'Deportivo Saprissa',
    'Deportivo Saprissa S.A.D.': 'Deportivo Saprissa',

    # Mexico

    #Universidad (Mexico)
    #Mirador (Mexico)
    #Gray Bears (Mexico)

    'CF América': 'Club América',
    'América': 'Club América',
    'Club America': 'Club América',
    'CF América': 'Club América',
    'Club America -- Mexico': 'Club America',
    'Asturias': 'CF Asturias',
    'Club de Fútbol Asturias': 'CF Asturias',
    'Real Club Espana': 'Real Club España',
    'Atlante - Mexico': 'Atlante',
    'Atlante FC': 'Atlante F.C.',
    'Atlante': 'Atlante F.C.',
    'Atlas - Mexico': 'Atlas',
    'Deportivo Atlas': 'Atlas',
    'Club Atlas': 'Atlas',
    'CA Atlas': 'Atlas',
    'F.C. Atlas': 'Atlas',
    'Atlas Academicos - Mexico': 'Atlas Academicos',
    'Atletico Espanol': 'Atlético Español',
    'Atletico Potosino': 'Atlético Potosino',
    'Bachilleres - Mexico': 'Bachilleres',
    'Bachilleres (Mexico)': 'Bachilleres',
    'Bachillieres (Mexico)': 'Bachilleres',
    'Club Celaya': 'Celaya FC',
    'Celaya': 'Celaya FC',
    'Colima Jaguares (Mexico)': 'Colima Jaguares',
    'Colima Jaguares - Mexico': 'Colima Jaguares',
    'CD Cruz Azul': 'Cruz Azul',
    'Cruz Azul (Mexico)': 'Cruz Azul',
    'Cruz Azul - Mexico': 'Cruz Azul',
    'Cruz Azul -- Mexico': 'Cruz Azul',
    'Indios': 'Indios de Ciudad Juárez',
    'C.D. Irapuato': 'CD Irapuato',
    'Irapuato': 'CD Irapuato',
    'Deportivo Irapuato': 'CD Irapuato',
    'CD Guadalajara -- Mexico': 'CD Guadalajara',
    'CD Guadalajara Chivas - Mexico': 'CD Guadalajara',
    'Chivas -- Mexico': 'Chivas',
    'C.D. Guadalajara Chivas': 'CD Guadalajara',
    'Guadalajara': 'CD Guadalajara',
    'Chivas Guadalajara': 'CD Guadalajara',
    'C.D. Guadalajara': 'CD Guadalajara',
    'Chivas': 'CD Guadalajara',
    'Guadalajara (Mexico)': 'CD Guadalajara',
    'Jaguares - Mexico': 'Jaguares',
    'Gallos de Jalisco - Mexico': 'Gallos de Jalisco',
    'Gallos de Jalisco': 'Club Jalisco',
    'Jalisco - Mexico': 'Jalisco',
    'Jalisco': 'Club Jalisco',
    'León': 'Club León',
    'Leon': 'Club León',
    'Club Leon': 'Club León',
    'Leon -- Mexico': 'Leon',
    'México Country Club': 'México Cricket Club',
    'Mexico Cricket Club': 'México Cricket Club',
    'Morelia - Mexico': 'Morelia',
    'Morelia -- Mexico': 'Morelia',
    'Athletico Morelia': 'Monarcas Morelia',
    'Athlético Morelia': 'Monarcas Morelia',
    'Atlético Morelia': 'Monarcas Morelia',
    'Morelia': 'Monarcas Morelia',
    'Athlético Morelia': 'Monarcas Morelia',
    'Atlético Morelia': 'Monarcas Morelia',
    
    'CA Monarcas Morelia': 'Monarcas Morelia',
    'Monterrey - Mexico': 'Monterrey',
    'Monterrey': 'CF Monterrey',
    'Monterrey (Mexico)': 'CF Monterrey',
    'C.F. Monterrey': 'CF Monterrey',
    'Club Monterrey': 'CF Monterrey',
    'Necaxa -- Mexico': 'Necaxa',
    'Necaxa - Mexico': 'Necaxa',
    'Necaxa (Mexico)': 'Necaxa',
    'Club Necaxa': 'Necaxa',
    'Deportivo Oro': 'C.D. Oro',
    'Oro - Mexico': 'CD Oro',
    'Oro': 'C.D. Oro',
    'C.D. Oro': 'CD Oro',
    
    'Queretaro': 'Querétaro FC',
    'Querétaro': 'Querétaro FC',

    # Actually separate teams?
    'Atletas Campesinos': 'Querétaro FC',
    'Gallos Blancos': 'Querétaro FC',
    #'Cobras de Queretaro': 'Querétaro FC',

    'Pachuca-- Mexico': 'Pachuca',
    'Pachuca': 'C.F. Pachuca',
    'Pachuca CF': 'C.F. Pachuca',
    'Pachuca AC': 'C.F. Pachuca',
    'Puebla - Mexico': 'Puebla',
    'Puebla F.C.': 'Puebla',
    'Puebla FC': 'Puebla',
    'Puebla AC': 'Puebla',
    'Rovers FC (Mexico)': 'Rovers FC Mexico',
    'San Luis': 'San Luis FC',
    'San Luis F.C.': 'San Luis FC',
    'Laguna F.C.': 'Santos Laguna',
    'Laguna FC': 'Santos Laguna',
    'Santos - Mexico': 'Santos Laguna',
    'Santos Laguna - Mexico': 'Santos Laguna',
    'Santos -- Mexico': 'Santos Laguna',
    'Club Sol - Mexico': 'Club Sol',
    'Tampico-Madero': 'Tampico Madero',
    'Tampico Madero': 'Tampico Madero FC',
    'Tapatio': 'CD Tapatio',
    'Tapatios': 'CD Tapatio',
    'Tapatio - Mexico': 'CD Tapatio',
    'Tapatillo': 'CD Tapatio',
    'CD Tapatio': 'CD Tapatío',
    'UAG - Mexico': 'Tecos',
    'Tecos - Mexico': 'Tecos',
    'U.A. de G.': 'Tecos',
    'Estudiantes Tecos': 'Tecos',
    'Estudiantes UAG': 'Estudiantes Tecos',
    'UAG': 'Tecos',
    'U.A.G.': 'Tecos',
    'UAG Tecos': 'Tecos',
    'Tecos U.A.G.': 'Tecos',
    'Tecos UAG': 'Tecos',
    'Tijuana': 'Club Tijuana',
    'Tijuana Chivas - Mexico': 'Tijuana Chivas',
    'Nacional de Tijuana - Mexico': 'Nacional de Tijuana',
    'CD Toluca': 'Toluca',
    'Toluca -- Mexico': 'Toluca',
    'Toluca - Mexico': 'Toluca',
    'Deportivo Toluca': 'Toluca',
    'Torreón F.C.': 'Torreón FC',
    'Univ. de Guadalajara - Mexico': 'Universidad de Guadalajara',
    'Univ. de Guadalajara': 'Universidad de Guadalajara',
    'Univ Guadalajara': 'Universidad de Guadalajara',
    'Universidad Guadalajara': 'Universidad de Guadalajara',
    'U de G': 'Universidad de Guadalajara',
    'U Guadalajara': 'Universidad de Guadalajara',
    'Club Tigres - Mexico': 'Tigres',
    'Tigres': 'UANL',
    'U.A.N.L': 'UANL',
    'U.A.N.L.': 'UANL',
    'Tigres UANL': 'UANL',
    'UANL Tigres': 'UANL',
    'Tigres de la UANL': 'UANL',
    'UNAM - Mexico': 'UNAM',
    'UNAM -- Mexico': 'UNAM',
    'Unam Pumas': 'UNAM',
    'Pumas': 'UNAM',
    'Pumas UNAM': 'UNAM',
    'UNAM Pumas': 'UNAM',
    'U.N.A.M.': 'UNAM',
    'Pumas U.N.A.M.': 'UNAM',
    'Club Deportivo Veracruz': 'Veracruz',
    'Veracruz - Mexico': 'Veracruz',
    'Veracruz (Mexico)': 'Tiburones Rojos de Veracruz',
    'Verarcuz': 'Tiburones Rojos de Veracruz',
    'Veracruz': 'Tiburones Rojos de Veracruz',
    'UAT': 'Correcaminos UAT',
    'U.A.T.': 'Correcaminos UAT',
    'Zacatepec': 'CD Zacatepec',
}
teams.update(world)


usa = {

    # Accurate?
    'Philadelphia 1928-1929': 'Philadelphia Field Club',
    'Philadelphia FC': 'Philadelphia Field Club',

    'Bridgeport': 'Bridgeport Bears',
    'Brooklyn Hakoah': 'Hakoah All-Stars',
    # Colliding with Jersey City slug.
    'Jersey City ?': 'Jersey City (?x)',


    # Division 1

    # ASL
    'Todd Shipyards F.C.': 'Todd Shipyards',
    'New York National Giants': 'New York Giants',
    'Hakoah All Stars': 'Hakoah All-Stars',
    'J&P Coats': 'J & P Coats',
    'J & P Coats': 'Pawtucket Rangers',
    'Pawtucket Rngers': 'Pawtucket Rangers',
    'NY Giants': 'New York Giants',
    'New york Field Club': 'New York Field Club',
    'Fall River County Street Rovers': 'Fall River Rovers',
    'Fall River United': 'Fall River Rovers',

    'Bethlehewm Steel': 'Bethlehem Steel',

    'New York Yankees': 'Fall River Marksmen',
    'New York Soccer Club': 'Fall River Marksmen',

    'Philadelphia Celtic': 'Philadelphia Field Club',
    'Providence Gold Bugs': 'Providence Clamdiggers', 

    # NASL
    'Washington Dips': 'Washington Diplomats',
    'Connecticut Bi-Centennials': 'Connecticut Bicentennials',
    'Hartford Bi-Centennials': 'Connecticut Bicentennials',
    'Hartford Bicentennials': 'Connecticut Bicentennials',
    'Atlanta Apollos': 'Atlanta Chiefs',
    'Cosmos': 'New York Cosmos',
    'Golden Bay Earthquakes': 'San Jose Earthquakes',
    'Toronto Metros': 'Toronto Blizzard',
    'Toronto Metros-Croatia': 'Toronto Blizzard',
    'Jacksonville Tea Men': 'New England Tea Men',

    # MLS
    'Chicago Fire S.C.': 'Chicago Fire',
    'CD Chivas USA': 'Chivas USA',
    'C.D. Chivas USA': 'Chivas USA',
    'D. C. United': 'D.C. United',
    'DC United': 'D.C. United',
    'F.C. Dallas': 'FC Dallas',
    'Dallas Burn': 'FC Dallas',
    'Dallas Burn/FC Dallas 96': 'FC Dallas',
    'FC Dallas 96': 'FC Dallas',
    'Houston 1836': 'Houston Dynamo',
    'Kansas City Wiz': 'Kansas City Wizards',
    'Kansas City Wizards': 'Sporting Kansas City',
    'Sporting KC': 'Sporting Kansas City',
    'LA Galaxy': 'Los Angeles Galaxy',
    'NE Revolution': 'New England Revolution',
    'NY/NJ Metrostars': 'New York Red Bulls',
    'Metrostars': 'New York Red Bulls',
    'MetroStars': 'New York Red Bulls',
    'New York/New Jersey MetroStars': 'New York Red Bulls',
    'NY/NJ MetroStars': 'New York Red Bulls',
    'NY Red Bulls': 'New York Red Bulls',
    'Red Bull New York': 'New York Red Bulls',
    'Philadephia Union': 'Philadelphia Union',
    'FC Portland': 'Portland Timbers',
    'Portland F.C.': 'Portland Timbers',
    'SJ Earthquakes': 'San Jose Earthquakes',
    'San Jose Clash': 'San Jose Earthquakes',
    'San Joe Earthquakes': 'San Jose Earthquakes',
    'Seattle Sounders FC': 'Seattle Sounders',
    'Sounders FC': 'Seattle Sounders',
    'Toronto F.C.': 'Toronto FC',
    'Vancouver 86ers': 'Vancouver Whitecaps',
    'Vancouver Whitecaps FC': 'Vancouver Whitecaps',

    # Division 1 Reserves
    'DC United Reserves': 'D.C. United Reserves',
    'Kansas City Wizards Reserves': 'Sporting Kansas City Reserves',
    'MetroStars Reserves': 'New York Red Bulls Reserves',
    'Chicago Fire Premier': 'Chicago Fire Reserves',


    # Division 2

    # ASL2
    'Boston Metros': 'Boston Tigers',
    'Cleveland Stars': 'Cleveland Cobras',
    'Georgia Generals': 'Cleveland Cobras',
    'Connecticut Wildcats': 'Connecticut Yankees',
    'Northeast United': 'Connecticut Yankees',
    'Hartford SC': 'Hartford Kings', # name map
    'Hartford FC': 'Hartford Kings',
    'Indianapolis Daredevils': 'Rhode Island Oceaneers',
    # 'Las Vegas Quicksilvers': 'Las Vegas Quicksilver', these are different teams.
    'Miami Americans': 'New Jersey Americans',
    'Syracus Suns': 'Syracuse Suns',
    'Syracuse Scorpions': 'Syracuse Suns',

    # USL-1/2

    'Atlanta Ruckus': 'Atlanta Silverbacks',
    'Atlanta Datagraphic Magic': 'Atlanta Magic',
    'Atlanta Datagraphic': 'Atlanta Magic',
    'Carolina Railhawks': 'Carolina RailHawks',
    'Dayton Dutch Lions FC': 'Dayton Dutch Lions',
    'Ft. Lauderdale Strikers': 'Fort Lauderdale Strikers',
    'Miami FC Blues': 'Fort Lauderdale Strikers',
    'Miami FC': 'Fort Lauderdale Strikers',
    'Minnesota Stars': 'Minnesota Stars FC',
    'New Orleans Gamblers': 'New Orleans Riverboat Gamblers',
    'New Orleans Storm': 'New Orleans Riverboat Gamblers',
    'NSC Minnesota Stars': 'Minnesota Stars FC',
    'Orlando City': 'Orlando City SC',
    'Puerto Rico Islanders - USL': 'Puerto Rico Islanders',
    'Rochester Raging Rhinos': 'Rochester Rhinos',
    'Team Sacramento': 'Sacramento Geckos',

    'FC Tampa Bay': 'Tampa Bay Rowdies',
    'Hampton Roads Mariners': 'Virginia Beach Mariners',
    'Hampton Rds Mariners': 'Virginia Beach Mariners',

    # PDL

    'Colorado Rapids U23\'s': 'Colorado Rapids U-23',
    'IMG Bradenton Academics': 'Bradenton Academics',
    'Louisiana Outlaws': 'Lafayette Swamp Cats',
    'Lafayette SwampCats': 'Lafayette Swamp Cats',
    'Mid-Michigan Bucks': 'Michigan Bucks',
    'Albany Blackwatch Highlanders': 'Albany Admirals',
    'Albany Black Watch Highlanders': 'Albany Blackwatch Highlanders',
    'South Jersey Barons': 'Ocean City Barons',
    'Williamsburg Legacy': 'Virginia Legacy',
    'Tacoma FC': 'Tacoma Tide',

    'Chivas El Paso Patriots': 'El Paso Patriots',
    'El Paso Sixshooters': 'El Paso Patriots',
    'El Paso Spurs': 'El Paso Patriots',

    'Austin Soccadillos': 'Austin Lone Stars',
    'Austin Sockadillos': 'Austin Lone Stars',

    'Rio Grande Valley Grandes FC': 'Rio Grande Valley Grandes',
    'Raleigh Elite': 'Raleigh CASL Elite',
    'CASL Elite': 'Raleigh CASL Elite',
    'Raleigh Express': 'Raleigh Capital Express',
    'Raleigh Capital Express': 'Raleigh Flyers',

    'Virginia Beach Submariners': 'Hampton Roads Piranhas',
    'Hampton Roads Piranhas': 'Virginia Beach Piranhas',
    'Boulder Rapids Reserves': 'Colorado Rapids U-23',
    'Boulder Rapids Reserve': 'Colorado Rapids U-23',
    'Abbotsford Rangers': 'Abbotsford Mariners',
    'Abbotsford Mariners': 'Fraser Valley Mariners',
    'Fraser Valley Mariners FC': 'Fraser Valley Mariners',
    'Los Angeles Storm': 'Los Angeles Legends',
    'Austin Stampede': 'Austin Aztex U23s',
    'Cary Railhawks U-23\'s': 'Cary Clarets',
    'Cary Railhawks U23\'s': 'Cary Clarets',
    'Cary RailHawks U23\'s': 'Cary Clarets',
    'New Orleans Shell Shockers': 'New Orleans Jesters',
    
    'Ocean City Barons': 'Ocean City Nor\'easters',
    'Los Angeles Legends': 'Los Angeles Azul Legends',
    'Los Angeles Azul Legends': 'Los Angeles Misioneros',
    'LA Misioneros FC': 'Los Angeles Misioneros',
    'Reading Rage': 'Reading United',
    'Reading United': 'Reading United AC',
    'Newark Ironbound Express': 'Jersey Express',

    'Los Angeles Blues 23': 'Pali Blues',
    'MPS Portlnad Phoenix': 'GPS Portland Phoenix',
    'New Hampshire Phantoms': 'Seacoast United Phantoms',
    'Tacoma Tide': 'Sounders FC U23',
    'Sounders FC U23': 'Seattle Sounders FC U-23',
    'West Texas Sockers': 'West Texas United Sockers',
    'Panama City Pirates': 'Panama City Beach Pirates',
    'Dwayne Demmin': 'Dwyane Demmin',
    
    




    # Uncategorized

    'St Lawrence': 'St. Lawrence',



    
    # Need to make sure America is not a regional US team.
    'America': 'América',


    # Northern New England
    'West End Polish FC': 'West End Polish Club',
    'Esmond Cortez': 'Esmond Cortex',

    'Club Espana': 'Club España',

    'German Americans': 'German-Americans',

    'Clan Macdonald': 'Clan MacDonald',

    'St. Michaels': 'St. Michael\'s',
    'St. Michael’s': 'St. Michael\'s',

    'American AA': 'American A.A.',

    'Buda AA': 'Buda A.A.', # Is this a different club - Budd A.A.?
    'Scots-Americans': 'Scots Americans',

    'Norwegian American SC': 'Norwegian American S.C.',
    'Madison SC': 'Madison S.C.',

    'Irish-Americans': 'Irish Americans',

    'MacDuffs': 'MacDuff FC',
    'MacDuffs FC': 'MacDuff FC',

    'Clan MacDonald': 'Clan MacDonald FC',
    'Clan MacDuff': 'Clan MacDuff FC',

    'North Grafton Association': 'North Grafton Association Foot Ball',

    'Manville AC': 'Manville Athletics',
    'Lonsdale Athletics': 'Lonsdale Athletes',
    'Lonsdales Association': 'Lonsdale Association',

    'Ansonias Association': 'Ansonia Association',
    'Braidwood Association': 'Braidwoods Association',

    'J & J Dobson AA': 'J & J Dobson FC',

    'US Pro 40': 'US Project 40',

    'St. Patricks': 'St. Patrick\'s',
    'St. George FC': 'St. George F.C.',

    'Espana': 'España', # This is a Mexican team.

    'Splitdorf F.C': 'Splitdorf F.C.', #find
    'San Sebastian': 'San Sebastián',

    'Angeles': 'Ángeles',



    # Kansas
    'Wichita Blue': 'Wichita Blue Angels', # Correct...?


    # Connecticut
    #Waterbury (CT)
    'Presbyterian FC (Bridgeport)': 'Bridgeport Presbyterian SC',
    'Bridgeport City AF.C': 'Bridgeport City AFC',
    'Danersk FC (Stamford)': 'Stamford Danersk FC',
    'Danersk Athletic FC': 'Stamford Danersk FC',
    'Vasco da Gama SC': 'Vasco Da Gama SC',
    'Vasco Da Gama SC': 'Bridgeport Vasco Da Gama',
    


    # Rhode Island
    #Stonington Sharks (RI)
    #Waypoyset FC (RI)
    #'Providence Wanderers': 'Providence Free Wanderers', # Check this - probably wrong...
    'Pawtucket FC': 'Pawtucket F.C.',

    'Thornton British Hosiers': 'Thornton Rovers',
    'Thornton British Hosieries': 'Thornton Rovers',

    # Florida
    #HRC Kickers (FL)
    'Ajax Orlando': 'Ajax Orlando Prospects',
    'HRC Kickers': 'St. Petersburg Kickers',
    'McCormick Kickers': 'St. Petersburg Kickers',
    'Central Florida Kraze': 'Orlando City U23',
    'Miami Strike Force': 'Miami Breakers',
    'Miami Tango': 'Miami Breakers',
    
    'Tampa Bay Cyclones': 'Jacksonville Cyclones', # Set team-name mapping.

    # Wisconsin

    #Serbian SC (WI)

    'Wacker SC (Milwaukee)': 'Milwaukee Wacker SC',
    'Schwaben (Milwaukee)': 'Milwaukee Schwaben',
    'Hungarian Sports Club (Milwaukee)': 'Milwaukee Hungarian SC',


    'Deutscher Sport Club (Milwaukee)': 'Milwaukee Deutscher Sport Club',
    'Falk Field Club (Milwaukee)': 'Milwaukee Falk Field Club',
    'Milwaukee Bavarian': 'Milwaukee Bavarian SC',
    'Milwaukee Bavarian Blue Ribbon': 'Milwaukee Bavarian SC',
    'Bavarian SC (WI)': 'Milwaukee Bavarians SC',
    'Milwaukee Bavarians': 'Milwaukee Bavarian SC',
    'Bavarian SC': 'Milwaukee Bavarian SC',

    'Falk Field Club (Mil.)': 'Milwaukee Falk FC',
    'Falk Field Club': 'Milwaukee Falk FC',

    # Georgia
    #Soccer City (GA)
    #Genesis (GA)
    'Atlanta Silverbacks U-23\'s': 'Atlanta Silverbacks U23\'s',
    'Augusta Fireball United': 'Augusta Fireball',

    # Indiana
    #North Shore FC (Evansville)
    'Ft. Wayne Fever': 'Fort Wayne Fever',
    'Gary Tigers': 'Indiana Tigers',

    # Utah
    #Flamengo SC (UT)

    # North Carolina
    #Village Tavern (NC)

    # California

    'Orange County Waves': 'Orange County Blue Star',
    'Orange County Zodiac': 'Orange County Blue Star',


    'Monterey Bay Jaguars': 'California Jaguars',

    #King Taco (South CA)
    #CD Mexico (North CA)
    #Los Angeles SC (South CA)
    'Maccabee AC (Los Angeles, CA)': 'Los Angeles Maccabee AC',
    #Magyar SC (South CA)
    #Mexico AC (North CA)
    #Pan-American SC (South CA)
    #Scots SC (South CA)
    #Strikers (South CA)
    #Teutonia SC (North CA)
    #United Scots (South CA)


    #Viking AC (North CA)
    #Viking SC (South CA)


    'Mexico AC (North California)': 'Mexico AC (North CA)',
    #Danish American SC (South CA)
    #El Salvador (North CA)
    #Exiles SC (South CA)
    #Fresno Oro (North CA)
    #Green American AC (North CA)
    #Alianza DF (South CA)
    #Armenian SC (South CA)
    #IAC (North CA)
    'Los Angeles Kickers-Victoria (South California)': 'Los Angeles Kickers',
    'Sacramento Spirits': 'Sacramento Gold',
    'Maccabee AC': 'Maccabi Los Angeles',
    'LA Blues': 'Los Angeles Blues',
    'Armenian SC (South CA)': 'Los Angeles Armenians',

    # Virginia
    
    #Iberia (DC/VA)
    #Uprising SC (DC/VA)


    'Aegean Hawks': 'Aegean Hawks FC',

    'Club Espana (DC/VA)': 'Club Espana',
    'Richhmond Kickers': 'Richmond Kickers',
    'North Virginia Royals': 'Northern Virginia Royals',
    'Roanoke River Dawgs': 'Roanoke RiverDawgs',
    'Roanoke Riverdawgs': 'Roanoke RiverDawgs',
    'Virginia Capitol Cavaliers': 'Washington Cavaliers',

    # Washington
    #FTI (WA)
    #Hungarian SC (WA)
    #Fatigue Technology (WA)
    #Mitre Eagles (WA)
    #Murphy's Pub (WA)
    'Everett BigFoot': 'Seattle BigFoot',
    'Everett Bigfoot': 'Seattle BigFoot',
    'Mitre Eagles (WA)': 'Seattle Mitre Eagles',

    'Viking S.C. (Seattle)': 'Seattle Viking SC',

    # Michigan
    #Magyar FC (Michigan)
    #Ukrainian SC (MI)
    #St. Andrews (MI)
    #Unionsport (CT)

    'Detroit Neon': 'Detroit Safari',


    'Celtic FC (Detroit)': 'Detroit Celtic FC',
    'All Scots FC (Detroit)': 'Detroit All Scots FC',
    'Bricklayers FC (Michigan)': 'Michigan Bricklayers FC',
    'Holley C.': 'Holley Carburetor F.C.',

    'Packard FC': 'Detroit Packard FC',

    'Wood Hydraulic (Detroit)': 'Detroit Wood Hydraulic',
    'Workers SC (Detroit)': 'Detroit Workers SC',
    'United German American AA (Detroit)': 'Detroit United German American AA',
    'Thistles SC (Detroit)': 'Detroit Thistles SC',
    'Swedish American FC (Detroit)': 'Detroit Swedish American FC',
    'Swedish American SC (Detroit)': 'Detroit Swedish American FC',

    'Pilgrims FC (Detroit)': 'Detroit Pilgrims FC',
    'Liberty SC (Detroit)': 'Detroit Liberty SC',
    'Highland Park (Detroit)': 'Detroit Highland Park',
    'Flandria SC (Detroit)': 'Detroit Flandria SC',



    # Louisiana

    # Oregon
    #Gresham United (OR)
    #Kell's Celtic (OR)
    'Portland Timbers U23': 'Portland Timbers U23\'s',

    # Idaho
    'Sioux Falls SpitFire': 'Sioux Falls Spitfire',

    # Texas

    #Border Bandits (South TX)
    #Rangers (South TX)


    'FC Dallas (Inter)': 'Dallas Mean Green',
    'FC Dallas (North TX)': 'Dallas Mean Green',


    'Austin Aztex U23s': 'Austin Aztex U23',
    'Austin Lighting': 'Autin Lightning',
    'Autin Lightning': 'Austin Lightning',

    'Dallas Express': 'Dallas Mean Green',
    'Dallas Inter': 'Dallas Mean Green',
    'Houston International': 'Dallas Mean Green',
    'San Antonio Alamo': 'San Antonio International',

    'Dallas Mulhausers': 'Dallas Mulhauser',



    'Arlington Arrows': 'DFW Tornados',
    'DFW Tornadoes': 'DFW Tornados',
    'Garland Genesis': 'DFW Tornados',
    'Addison Arrows': 'DFW Tornados',
    'North Texas United': 'DFW Tornados',
    'Fort Worth Kickers': 'DFW Tornados',
    'Dallas Kickers': 'DFW Tornados',
    'Dallas Americans': 'DFW Tornados',
    'Texas Rattlers': 'DFW Tornados',
    'Texas Spurs': 'DFW Tornados',
    'Texas Toros': 'DFW Tornados',
    'Dallas-Fort Worth Toros': 'DFW Tornados',
    'Dallas Toros': 'Dallas-Fort Worth Toros',
    'Dallas/Ft. Worth Toros': 'Dallas-Fort Worth Toros',
    'DFW Toros': 'Dallas-Fort Worth Toros',



    
    # California
    'McIlvane Canvasbacks': 'McIlvaine Canvasbacks',
    'McKeesport National Tube': 'McKeesport FC',

    'San Fern. Valley Golden Eagles': 'San Fernando Valley Golden Eagles',
    'Valley Golden Eagles': 'San Fernando Valley Golden Eagles',
    'SFV Golden Eagles': 'San Fernando Valley Golden Eagles',

    'CD Mexico (North California)': 'El Farolito Soccer Club',
    'San Fernando Quakes': 'San Fernando Valley Quakes',

    'Central Valley Hydra': 'CCV Hydra',
    'CCV Hydra': 'Central California Valley Hydra',

    'Greek American AC (North CA)': 'San Francisco Greek American AC',
    'San Francisco Greek Americans': 'San Francisco Greek American AC',

    'Bay Area Seals': 'San Francisco Bay Seals',
    'San Francisco Seals': 'San Francisco Bay Seals',
    'SFB Seals': 'San Francisco Bay Seals',

    'San Francisco AC': 'San Francisco A.C.',
    'San Jose Hawks': 'San Francisco Bay Blackhawks',
    'San Francisco C.D. Mexico' : 'El Farolito Soccer Club',



    # Arizona
    #Croatia (AZ)
    'Phoenix Hearts': 'Arizona Sahuaros',
    'Arizona Cotton': 'Arizona Sahuaros',
    'Arizona Phoenix': 'Arizona Sahuaros',


    # New York City
    
    #'New York Centaurs': 


    #German American SC (NYC)
    #German S.C. (Brooklyn)
    #'Hakoah SC (NYC)
    'Danish FC (NYC)': 'New York Danish FC',
    #Deutschungarn (New York)
    'Lexington FC (Brooklyn)': 'Brooklyn Lexington FC',
    'Norwegian American SC (NYC)': 'New York Norwegian American SC',
    'St. Mary\'s Celtic (Brooklyn)': 'Brooklyn St. Mary\'s Celtic',
    'Prague SC (NYC)': 'New York Prague SC',
    'Swedish FC (NYC)': 'New York Swedish FC',
    'Viking A.C. (NYC)': 'New York Viking AC',
    #Tappen Post (NYC)



    #'New York Association': 'New York FBC',

    'St George FC': 'St. George F.C',
    'Critchley AA': 'Critchley\'s',
    'Crithleys': 'Critchley\'s',
    'Crescent AC': 'Crescent A.C.',
    'Critchley': 'Critchley\'s',
    'Wissinoming': 'Wissinoming FC',

    'Hakoah FC': 'Hakoah F.C.',
    'Hatikvoh': 'Hatikvoh FC',

    'New York Irish-Americans': 'New York Irish Americans',
    'Ukrainian SC (East NY)': 'NY Ukrainian SC',

    'Hungaria': 'New York Hungaria',     
    'NY Hungaria': 'New York Hungaria',
    'New York Hungarian': 'New York Hungaria',
    'New York Hungarians': 'New York Hungaria',
    'Hungaria SC (East NY)': 'New York Hungaria',
    'Hungaria SC': 'New York Hungaria',

    'New York Hota': 'NY Hota SC',
    'Hota SC': 'NY Hota SC',
    'NY Hota-Bavarian SC': 'NY Hota SC',
    'NY Hota SC': 'New York Hota SC',
    
    'Galicia F.C.': 'New York Galicia',
    'Galicia FC': 'New York Galicia',
    'NY Galicia': 'New York Galicia',

    'Galicia SC': 'Brookhattan',
    'Galicia-Honduras': 'Brookhattan',
    'New York Brookhattan': 'Brookhattan',
    'Brookhattan-Galicia': 'Brookhattan',
    'Brookhattan Galicia': 'Brookhattan',

    'D.S.C. Brooklyn': 'DSC Brooklyn',

    'German Hungarian S.C. (NYC)': 'German Hungarian SC',

    'German American SC': 'German American S.C.',
    'German-American AC': 'German American AC',

    # This may not be right. Brooklyn Italians itself seems to have 
    # Gone to lower leagues, played as Palermo and Brokolyn Dodgers.
    'Inter-Brooklyn Italians': 'Brooklyn Italians',
    'New York Inter': 'Brooklyn Italians',
    'Inter SC': 'Brooklyn Italians',
    'Brooklyn-Italians': 'Brooklyn Italians',
    'Brooklyn Dodgers S.C.': 'Brooklyn Italians',
    'Brooklyn Dodgers SC': 'Brooklyn Italians',

    'St. Mary\'s Celtic': 'Brooklyn Celtic',
    'St. Mary’s Celtic': 'St. Mary\'s Celtic',
    'Brooklyn Celtic': 'Brooklyn Celtics',
    'St. Mary\'s Celtic': 'Brooklyn St. Mary\'s Celtic',
    'Brooklyn Celtics': 'Brooklyn St. Mary\'s Celtic',

    'New York Greeks': 'New York Apollo',
    'New York United': 'New York Apollo',

    'Hispano': 'Brooklyn Hispano',
    'Brooklyn Hispanos': 'Brooklyn Hispano',
    'New York Hispano': 'Brooklyn Hispano',
    'Centro-Hispano': 'Centro Hispano',
    'Brooklyn Giants': 'Brooklyn Hispano',

    'Brooklyn Robins Dry Dock': 'Robins Dry Dock',
    'Robbins Dry Dock': 'Robins Dry Dock',

    'Greek American SC (East NY)': 'NY Greek American Atlas',
    'Greek American Atlas': 'NY Greek American Atlas',
    'NY Greek-American Atlas': 'NY Greek American Atlas',
    'NY Greek-Americans Hellenic SC': 'NY Greek American Atlas',
    'Greek American AA': 'NY Greek American Atlas',
    'Greek-American A.C.': 'NY Greek American Atlas',
    'Greek American AC': 'NY Greek American Atlas',
    'New York Greek-Americans': 'NY Greek American Atlas',
    'Greek-Americans': 'NY Greek American Atlas',
    'NY Greek American SC': 'NY Greek American Atlas',
    'New York Greek-American': 'NY Greek American Atlas',
    'NY Greek-Americans': 'NY Greek American Atlas',
    'NY Greek American Atlas': 'New York Greek American Atlas',

    'NY Pancyprian-Freedoms': 'New York Pancyprian-Freedoms',
    'NY Pancyprian Freedoms': 'New York Pancyprian-Freedoms',

    'Gjoa SC': 'SC Gjoa',
    'Gjoa': 'SC Gjoa',
    'Gjoa FC': 'SC Gjoa',

    'Brooklyn FC': 'Brooklyn F.C.',
    'Brooklyn F.C.': 'Brooklyn Field Club',

    'German Hungarian SC (NYC)': 'German Hungarian S.C. (NYC)',
    'German Hungarian S.C. (NYC)': 'New York German Hungarian S.C.',

    'Eintracht SC': 'S.C. Eintracht',
    'Eintracht S.C.': 'S.C. Eintracht',
    'SC Eintracht':'S.C. Eintracht',

    'Brooklyn Cricket Association': 'Brooklyn Cricket Athletic Club',
    'Brooklyn Logs': 'Brooklyn Longfellows',

    'New York FC': 'New York Field Club',

    'Giuliana': 'Giuliana SC',
    'Guiliana SC (East NY)': 'Giuliana SC',

    'German-Hungarian SC': 'German Hungarian SC',
    'German-Hungarians': 'German Hungarian SC',
    'German Hungarians': 'German Hungarian SC',

    'Minerva-Pfuelzer': 'Minerva-Pfaelzer SC',

    'New York Freedom': 'New York Freedoms',

    'IRT Rangers': 'I.R.T. Rangers',
    'IRT Strollers': 'I.R.T. Strollers',

    'Alley Boys': 'Alley Boys FC',

    # New York State

    #Celtic AFC (NW NY)
    #Simon Pure SC (West NY)
    #Portuguese American SC (NW NY)

    'German AC (Rochester)': 'Rochester German AC',

    'Thistle SC (Rochester)': 'Rochester Thistles SC',
    'Kelly Celtic (Rochester)': 'Rochester Kelly Celtic',
    'Thistles SC (Rochester)': 'Rochester Thistles SC',


    'Rangers FC (Niagara Falls)': 'Niagara Falls Rangers',
    'MacKenzie FC (Niagara Falls)': 'Niagara Falls MacKenzie FC',



    'Kodak Park': 'Kodak Park FC',

    'Rochester Moose FC': 'Rochester City Moose',
    'Rochester Moose': 'Rochester City Moose',

    'Rochester Celtics': 'Rochester Celtic',
    'Rochester Celtic': 'Rochester Kelly Celtic',
    'Kelly Celtic': 'Rochester Kelly Celtic',
    'Kelly Celtic (Rochester': 'Rochester Kelly Celtic',

    'New Rochelle Association': 'New Rochelle Foot Ball Association',

    'Hungarian FC (Buffalo)': 'Buffalo Hungarian FC',
    'German American SC (Buffalo)': 'Buffalo Becks German American SC',
    'Becks German American SC (Buffalo)': 'Buffalo Becks',
    'Becks German American S.C. (Buffalo)': 'Becks German American SC (Buffalo)',
    'Becks German American SC (Buf.)': 'Becks German American S.C. (Buf.)',
    'Buffalo Becks': 'Buffalo Becks German American SC',
    'Becks German American S.C. (Buf.)': 'Buffalo Becks German American SC',

    'Hollywood Inn': 'Yonkers Hollywood Inn',
    'Yonkers Th.': 'Yonkers Thistle',
    'MacKenzie SC (Niagra Falls)': 'MacKenzie FC (Niagara Falls)',

    # New Jersey


    #Jersey City (?x)
    #Maritimo XI (Newark)
    #Celtics FC (New Jersey)
    'Trenton Americans': 'Trenton-Americans',
    #FC Porto (NJ)
    #Valenciano (NJ)
    #Polish Falcons (NJ)


    'Americus AA': 'Americus A.A.',

    'Bunker Hill F.C.': 'Bunker Hill FC',

    'Kearny Rovers': 'Kearney Rovers',
    'Kearny Rangers': 'Kearney Rangers',

    'Newark Scottish Americans': 'Newark Scottish-Americans',

    'East Newark Scottish American FC': 'East Newark Scottish-American FC',
    'Ukrainian Sitch (NJ)': 'Newark Ukrainian Sitch',


    'Paterson Caledonian Thistles': 'Paterson Thistles',
    'Swanton Field Club (Kearny, NJ)': 'Swanton Field Club',
    'Hoboken F.C.': 'Hoboken FC',
    'Holyoke Falco': 'Holyoke Falcos',
    'Holyoke Falcons': 'Holyoke Falcos',
    'Newark Ukrainian': 'Newark Ukrainian Sitch',

    'Paterson Silk Sox': 'Paterson F.C.',
    'Trenton Highlanders': 'Paterson F.C.',
    'Paterson Caledonian': 'Paterson F.C.',
    'Newark Germans': 'Paterson F.C.',

    'West Hudson AA': 'West Hudson A.A.',
    'West Hudson A.A': 'West Hudson A.A.',
    'West Hudson FC': 'West Hudson A.A.',
    'West Hudson AC': 'West Hudson A.A.',
    
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
    'Scots Americans': 'Kearny Scots',

    'Kearny Celtics': 'Kearny Celtic',
    'Kearny Irish': 'Kearny Celtic',

    'Montclair Standard Falcons': 'Montclair Falcons',
    'Fontana Falcons': 'Montclair Falcons',
    'Montclair': 'Fontana Falcons', # Uh...

    'Newark Falcons': 'Elizabeth Falcons',
    'Falcons SC': 'Elizabeth Falcons',
    'Falcons-Warsaw': 'Elizabeth Falcons',

    'New Brunswick Hungarian Americans': 'New Brunswick Hungarians',
    'New Jersey Shaefer Brewers': 'New Jersey Brewers',

    'Jershey Shore Boca': 'Jersey Shore Boca',

    'NY/NJ Stallions': 'New Jersey Stallions',

    'Celtics of New Jersey': 'Celtics FC (New Jersey)',
    'Newark SC': 'Newark S.C.',

    'Clark A.A': 'Clark A.A.',
    'Clark A.A.': 'Kearney Clarks ONT',
    'East Newark Clark AA': 'East Newark Clark A.A.',
    'East Newark Clark AA': 'Kearney Clarks ONT',
    'Clark O.N.T.': 'Kearney Clarks ONT',
    'Clark ONT': 'Kearney Clarks ONT',
    'Clark ONT': 'Clark O.N.T.',
    'Kearny Clarks ONT': 'Kearney Clarks ONT',

    'Central Jersey Rpitide': 'Central Jersey Riptide',

    'Jersey A.C': 'Jersey A.C.',
    'Jersey AC': 'Jersey A.C.',
    'Newark FC': 'Newark F.C.',
    'Newark F.C': 'Newark F.C.',

    'Bayonne Centerville': 'Centreville AC',    
    
    'Babcock & Wilcaox': 'Babcock & Wilcox',
    'Babcock & Wilson': 'Babcock & Wilcox',
    'Babcock and Wilcox': 'Babcock & Wilcox',
    'Bayonne Babcock & Wilcox': 'Babcock & Wilcox',

    'Beadling': 'Beadling SC',
    'Beadling FC': 'Beadling SC',
    'Beadlign FC': 'Beadling SC',
    'Beadling SC (West PA)': 'Beadling SC',

    'True Blues FC': 'Paterson True Blues',

    'Domestic': 'Newark Domestics',
    'Newark Domestics Baseball AC': 'Newark Domestics',

    'Trenton Association': 'Trentons Association',
    'Tiffany Rovers': 'Newark Tiffany Rovers',

    'Alma': 'Newark Almas',
    'Paterson FC': 'Paterson F.C.',

    'Newark Portugeuse': 'Newark Portuguese',
    'Newark Portuguese (NJ)': 'Newark Portuguese',

    # Need to figure out what name you want to use.
    'Harrison SC': 'Harrison S.C.',
    'Harrison Soccer Club': 'Harrison S.C.',
    'Harrison Field Club': 'Harrison S.C.',
    'Harrison FC': 'Harrison S.C.',
    'Harrison S.C.': 'Erie A.A.',
    'Harrison Erie S.C.': 'Erie AA',
    'Erie AA': 'Erie A.A.',
    'Erie A.A': 'Harrison Erie F.C.',

    # Illinois

    #Magyar FC (Illinois)
    #Necaxa (Chicago)
    #Polish American SC (Illinois)


    #Schwaben SC (IL)


    #American Hungarian FC (Illinois)


    #Lions SC (IL)
    #Italian American Maroons (IL)
    #Gillespie SC (Illinois)
    #Hansa (IL)
    #Scottish American FC (IL)


    'Swedish American SC (Chicago)': 'Chicago Swedish American SC',
    'Maccabee SC (Chicago)': 'Chicago Maccabee SC',
    'MacDuff FC (Chicago)': 'Chicago MacDuff FC',
    'Lawndale Rangers (Chicago)': 'Chicago Lawndale Rangers',
    'Hungarian American SC (Chicago)': 'Chicago Hungarian American SC',
    'Hakoah Center (Chicago)': 'Chicago Hakoah Center',
    'Thistles FC (Chicago)': 'Chicago Thistles FC',
    'Norwegian American SC (Chicago)': 'Chicago Norwegian American SC',
    'Vienna FC (Chicago)': 'Chicago Vienna FC',
    'Yugoslav American SC (Chicago)': 'Chicago Yugoslav American SC',



    'Croatian SC (Chicago)': 'Chicago Croatian SC',
    'Carpenters FC (Chicago)': 'Chicago Carpenters FC',

    'Simmons SC': 'Simmons FC',
    'Pullman Professional FC': 'Pullman FC',
    'Pullman Association FC': 'Pullman FC',


    'Yugoslav Americnan SC': 'Yugoslav American SC',
    'Slavia F.C.': 'Slavia FC',
    'Chicago Maccabi': 'Maccabee SC (Chicago)', #verify 11/22/1936 game vs. Tel Aviv Maccabi was Maccabee SC
    'Thistle FC (Chicago)': 'Thistles FC (Chicago)',
    'Buda A.A. (Harvey, Illinois)': 'Harvey Buda A.A.',
    'Manhattan Beer': 'Chicago Manhattan Beer',

    'Olympic SC (IL)': 'Olympia FC (Chicago)',
    'Olympia SC (Chicago)': 'Olympia FC (Chicago)',
    'Olympia FC (Chicago)': 'Chicago Olympia FC',

    'Viking AC': 'Chicago Viking AC',
    'Chicago Vikings': 'Chicago Viking AC',
    'Chicago Viking AC': 'Chicago Viking A.A.',
    'Chicago Viking': 'Chicago Viking A.A.',
    'Viking AA': 'Chicago Viking A.A.',
    'Viking A.A.': 'Chicago Viking A.A.',

    'Chicago Sparta Falstaff': 'Chicago Sparta ABA',
    'Chicago Sparta Fallstaff': 'Chicago Sparta ABA',
    'Chicago Sparta': 'Chicago Sparta ABA',
    'Sparta (Chicago)': 'Chicago Sparta ABA',
    #'Sparta': 'Chicago Sparta ABA',
    'Sparta FC': 'Chicago Sparta ABA',
    'Sparta F.C.': 'Chicago Sparta ABA',
    'Sparta ABA': 'Chicago Sparta ABA',
    'Sparta Leader': 'Chicago Sparta ABA',
    'Sparta Garden City': 'Chicago Sparta ABA',
    'Sparta Union': 'Chicago Sparta ABA',
    'Sparta Ogden Dairy': 'Chicago Sparta ABA',

    'Schwaben (Chicago)': 'Chicago Schwaben',

    'Johnston City AFC (Illinois)': 'Johnston City AFC',
    'Johnston City': 'Johnston City AFC',

    'Chicago Horizons': 'Chicago Horizon',

    'AAC Eagles': 'A.A.C. Eagles',
    'Chicago Eagles': 'A.A.C. Eagles',

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

    'RWB Adria (IL)': 'RWB Adria',

    'Slovak AA': 'Chicago Slovak SC',
    'Slovak SC': 'Chicago Slovak SC',

    'Chicago Croatian': 'Chicago Croatian SC',

    'Hansa (IL)': 'Chicago Hansa',

    # Pennsylvania

    'Beadling (West PA)': 'Beadling SC',

    'Heidelberg SC': 'Heidelberg S.C.',
    'Heidelberg Losegos': 'Heidelberg S.C.',

    'Centennial FC': 'Centennial F.C.',
    'Centennial': 'Centennial F.C.',

    'Puritan Y.M.L': 'Puritan Y.M.L.',
    'Puritan YML': 'Puritan Y.M.L',

    'Wanderers FC (Philadelphia)': 'Philadelphia Wanderers FC',
    'West Philadelphia': 'West Philadelphia FC',

    'Philadephia Shamrocks': 'Philadelphia Shamrocks',
    #Phoenix SC (Philadelphia)
    'German American SC (Philadelphia)': 'Philadelphia German Americans',
    #Donauschwaben (Philadelphia)
    #German SC (Philadelphia)


    # Cuddy is not Curry.
    'Cuddy': 'Cuddy AC',

    'Germantown BC': 'Germantown Boys Club',
    'Germantown Boys': 'Germantown Boys Club',

    'Vereinigung Erzgebirge (East PA)': 'Vereinigung Erzgebirge',
    'Ukrainian Nationals': 'Philadelphia Ukrainians',

    'Harmarville': 'Harmarville Hurricanes',

    'Merchant Ship B': 'Philadelphia Merchant Ship B',
    'Merchant Ship A': 'Philadelphia Merchant Ship',
    'Merchants Ship': 'Philadelphia Merchant Ship',
    'Merchant Ship': 'Philadelphia Merchant Ship',

    'Fleischer': 'Fleisher Yarn',
    'Fleischer Yarn': 'Fleisher Yarn',

    'Avella Polar Stars (W. Pa.)': 'Avella Polar Star',
    'Avella (W. Pa.)': 'Avella Polar Star',
    'Avella Polar Star (W. Pa.)': 'Avella Polar Star',

    # Uh...might not be a good name to use Uhrik Truckers.
    'Philadelphia Truckers': 'Uhrik Truckers',
    'Philadelphia Uhriks': 'Uhrik Truckers',
    'Uhrik Truckers': 'Philadelphia German Americans',
    'Philadelphia Uhrik Truckers': 'Uhrik Truckers',
    'Philadelphia German-Americans': 'Philadelphia German Americans',
    'Philadelphia German-American': 'Philadelphia German Americans',
    'Philadelphia German American': 'Philadelphia German Americans',
    'Philadelphia Americans': 'Philadelphia German Americans',

    'Fairhill FC (Philadelphia)': 'Philadelphia Fairhill FC',
    'Fairhill FC': 'Philadelphia Fairhill FC',

    'Passon SC': 'Philadelphia Passon',
    'Passon FC': 'Philadelphia Passon',
    'Philadelphia Passon F.C.': 'Philadelphia Passon',
    'Philadelphia Passon': 'Philadelphia Nationals',

    'Philadelphia Germans': 'Philadelphia German Americans',
    'General Electric': 'General Electric FC',

    'Allentown': 'Bethlehem Hungarian',

    'Philadelphia Hibernians': 'Philadelphia Hibernian',

    'Tacony Disston A.A.': 'Disston A.A.',
    'Philadelphia Disston': 'Disston A.A.',
    'Tacony FC': 'Disston A.A.',
    'Disston AA': 'Disston A.A.',
    'Disston FC': 'Disston A.A.',
    'Disston A.A.': 'Philadelphia Disston A.A.',



    'Morgan FC': 'Morgan Strasser',
    'Morgan SC': 'Morgan Strasser',
    'Morgan Haulers': 'Morgan Strasser',
    'Morgan Sport Club': 'Morgan Strasser',
    'Morgan': 'Morgan Strasser',

    #Pierpoints FC (Pittsburgh)
    #Vestaburg SC (Pittsburgh)
    #Muse (W. Pa.)
    #Harmarville FC (Pittsburgh)
    #Glendale (W. Pa.)
    #Bradling Terriers (West PA)
    #Cecil French (West PA)
    #Cecil Legion (W. Pa.)



    'Gallatin F.C.': 'Pittsburgh Gallatin SC',
    'Gallatin Sport Club': 'Pittsburgh Gallatin SC',
    'Gallatin': 'Pittsburgh Gallatin SC',
    'Gallatin-Dunlevy': 'Pittsburgh Gallatin SC',
    'Gallatin FC': 'Pittsburgh Gallatin SC',
    'Gallatin SC': 'Pittsburgh Gallatin SC',
    'Gallatin Sport Clun': 'Pittsburgh Gallatin SC',

    'Jeanette FC (Pittsburgh)': 'Jeanette FC',

    'Curry': 'Curry FC',
    'Curry FC': 'Curry Silver Tops',
    'Curry Vets': 'Curry FC',
    'Curry SC': 'Curry FC',
    'Curry S.C.': 'Curry FC',

    'Castle Shannon FC': 'Castle Shannon',

    # Missouri
    
    'Atlanta Attack': 'Kansas City Comets',
    'Kansas City Attack': 'Kansas City Comets',

    'Raftery Painters (St. Louis)': 'St. Louis Raftery Painters',
    'Norwegian American SC (St. Louis)': 'St. Louis Norwegian American SC',
    #St. Louis (CYC) Stars




    #St. Ambrose (MO)
    #Grapettes SC (MO)


    #Royalton Stars (St. Louis)
    #Michelob SC (MO)
    #Mike Duffy (MO)
    #Morgan Haulers (St. Louis)

    #Paddock Club (St. Louis)
    #National Slug (St. Louis)
    #Pants Store FC (St. Louis)
    #Udinese (MO)

    'Busch SC (MO)': 'St. Louis Busch',
    'Saint Louis Busch': 'St. Louis Busch',
    'St. Louis Busch Seniors': 'St. Louis Busch',


    'Anderson S.C.': 'Andersons',
    'Anderson SC': 'Anderson S.C.',

    'St. Louis Central Breweries F.C.': 'Central Breweries',
    'Hellrungs': 'Stix, Baer and Fuller F.C.',
    'Hellrung FC': 'Stix, Baer and Fuller F.C.',
    'Hellrungs SC': 'Hellrungs',
    'Hellrungs FC': 'Hellrungs',
    'Hellrung & Grimm': 'Hellrung FC',
    'Hellrung Grimm': 'Hellrung & Grimm',
    'Stix, Baer & Fuller': 'Stix, Baer and Fuller F.C.',
    'Stix, Baer and Fuller': 'Stix, Baer and Fuller F.C.',
    'Central Breweries': 'Stix, Baer and Fuller F.C.',
    'Stix Baer & Fuller': 'Stix, Baer and Fuller F.C.',

    'Minit Rubs (St. Louis)': 'Minit-Rubs',
    'Missouri Amateur AC': 'Missouri Amateur AA',
    'Pants Store FC (St. Louis)': 'St. Louis Pants Store FC',

    'Marres': 'Marre\'s',
    'Marre': 'Marre\'s',

    'St. Louis Irish Americans': 'St. Louis Irish Americans AC',

    'DeAndreis': 'DeAndreis Council',
    'De Andreis SC (St. Louis)': 'DeAndreis Council',

    'Busch SC': 'Busch SC (MO)',
    'St. Louis Carondolet': 'St. Louis Carondolets',

    'Wellston FC (St. Louis)': 'Wellston FC',
    'White Banner': 'White Banner Malt',
    'White Banner Malt (St. Louis)': 'White Banner Malt',

    'Correnti Cleaners (St. Louis)': 'Simpkins Ford',
    'St. Louis Simpkins-Ford': 'Simpkins Ford',
    'Simpkins F.C.': 'Simpkins Ford',
    'Simpkins S.C.': 'Simpkins Ford',

    'St. Louis Zenthoefer Furs': 'St. Louis Kutis',
    'Zenthoefer Furs': 'St. Louis Kutis',
    'St. Louis Raiders': 'St. Louis Kutis',
    'Kutis SC': 'St. Louis Kutis',
    'Kutis': 'St. Louis Kutis',
    'St. Louis Kutis SC': 'St. Louis Kutis',

    'Ben Miller FC': 'Ben Millers',
    'Ben Miller SC': 'Ben Millers',
    'Ben Miller A.C.': 'Ben Millers',

    # Pretty sure this is correct.
    'Coca Cola (St. L)': 'Kavanaugh',
    'Coca Cola': 'Kavanaugh',

    'Tablers': 'Tablers FC',

    'Innisfall FC': 'Innisfails FC',
    'Innisfalls FC': 'Innisfails FC',
    'Innisfails': 'Innisfails FC',

    'St. Louis Scullin Steel': 'Scullin Steel',
    'Scullin St.': 'Scullin Steel',
    'Scullin Steels': 'Scullin Steel',    

    'Vesper Buick': 'Vesper Buicks',
    'Wellston\'s': 'Wellston FC',

    'Raftery’s': 'Raftery Painters',

    # Maryland

    #Hasslinger SC (Baltimore)
    'St. Gerard (Baltimore)': 'Baltimore St. Gerard',
    #Ruggiero SC (Baltimore)
    #Hummer Sports Cafe (MD)
    #Hummers Sports Cafe (MD)

    'Davis SC (Baltimore)': 'Baltimore Davis SC',
    'Batchelors Café (Baltimore)': 'Baltimore Batchelors Café',
    'Baltimore Pompei': 'Baltimore Pompei SC',
    'Tower Ford Casa Bianca': 'Casa Bianca',
    'Tower Ford': 'Tower Ford Casa Bianca',

    'Real Maryland Monarchs FC': 'Real Maryland Monarchs',
    'Baltimore Pompeii': 'Baltimore Pompei SC',
    'Baltimore Canton': 'Baltimore Americans',
    'Baltimore German': 'Baltimore Americans',
    'Baltimore S.C.': 'Baltimore Americans',
    'Baltimore Rockets': 'Baltimore Pompei',
    'Baltimore St. Gerards': 'Baltimore Flyers',
    #'Baltimore Stars': 'Baltimore Bays',
    'Baltimore SC': 'Baltimore S.C.',
    
    # Massachusetts

    'Worcester Wildfire': 'Boston Bulldogs',

    #St. George AA (MA)
    #Hellenic (MA)

    'Cambridge Faialense (MA)': 'Cambridge Faialense',
    'St. Michael’s': 'St. Michael\'s', # Southern NE - not sure about MA

    'YMCTAS': 'YMCA Total Abstinence Society FC',
    'Merrimac Valley': 'Merrimac Valley FC',
    'Gray & Davis': 'Grey & Davis', # Not sure about this one.

    'Howard and Bullough': 'Howard & Bullough',

    'Crompton': 'Crompton FC',
    'Fore River SC': 'Fore River FC',
    'Fore River': 'Fore River FC',
    'Fore River FC': 'Fore River Rovers',

    'New Bedford FC': 'New Bedford F.C.',
    'New Bedford F.C.': 'New Bedford Whalers',
    'New Bedford Celtic': 'New Bedford Celtics',
    'Lucy Recs': 'Lusitania Recreation',

    'Abbott Worsted': 'Abbot Worsted',
    'Abbot W.': 'Abbot Worsted',

    'Lynn Gas & electric': 'Lynn Gas & Electric',

    'Fall River F.C.': 'Fall River FC',
    'Fall River Football Club': 'Fall River FC',
    'Fall River S.C.': 'Fall River SC',

    'Fall River Olympic': 'Fall River Olympics',
    
    'New England Oceaneers': 'Rhode Island Oceaneers',
    'Ludlow S.C.': 'Ludlow Lusitano',
    'Fall River Astros': 'Boston Astros',


    'Prospect H.': 'Prospect Hill FC',
    'Prospect Hill': 'Prospect Hill FC',
    'Prospect Hill FC (MA)': 'Prospect Hill FC',

    'Whittall': 'Whittall Carpet Mills F.C.',
    'Whitall Carpet Mill': 'Whittal F.C.',
    'Whittall Carpet Mill': 'Whittal F.C.',
    'Whittall Carpet Mills': 'Whittal F.C.',
    'Whittal Carpet Mill': 'Whittal F.C.',

    # Ohio
    #Banat German Sports (Cleveland)
    'Thistles FC (Cleveland)': 'Cleveland Thistles FC',
    'Shamrocks SC (Cleveland)': 'Cleveland Shamrocks SC',
    'Greenhut Jewelers (Cleveland)': 'Cleveland Greenhut Jewelers',

    'Columbus Invaders': 'Canton Invaders', # Name change; set team-name mapping.


    'Dalarda SC (Cleveland)': 'Cleveland Dalarda SC',
    'Favorite Knits FC (Cleveland)': 'Cleveland Favorite Knits FC',
    'Clan MacKenzie FC (Akron)': 'Akron Clan MacKenzie FC',
    'Akron Clan Mackenzie FC': 'Akron Clan MacKenzie FC',
    'Celtics FC (Cleveland)': 'Cleveland Celtics FC',
    'Alexis Florist (Toledo)': 'Toledo Alexis Florist',
    'British War Veterans (Cleveland)': 'Cleveland British War Veterans',
    'Bricklayers FC (Cleveland)': 'Cleveland Bricklayers FC',

    'Mahoning Valley FC': 'Mahoning Valley',

    'Goodyear FC': 'Akron Goodyear FC',
    'Goodyear FC (Akron)': 'Akron Goodyear FC',
    'Akron FC': 'Akron Goodyear FC',

    'Cleveland Hungarians': 'Cleveland American Hungarian FC',

    'Clan Mackenzie FC (Akron)': 'Clan MacKenzie FC (Akron)',
    'MacKenzie FC (Akron)': 'Clan Mackenzie FC (Akron)',
    'Clan MacKenzie': 'Clan Mackenzie FC (Akron)',
    'Clan Mackenzie FC (Akron)': 'Akron Clan Mackenzie FC',

    'Bruell Hungarian': 'Bruell Hungarians',
    'Bruell Hungarians': 'Bruell Insurance',
    'Bruell F.C.': 'Cleveland Bruell Insurance',
    'Bruell Insurance': 'Cleveland Bruell Insurance',
    'Cleveland Bruells': 'Cleveland Bruell Insurance',
    'Cleveland B.': 'Cleveland Bruell Insurance',

    'Bartunek Slavias': 'Bartunek Slavia',
    'Slavia Bartunek': 'Bartunek Slavia',
    'Rosenblum Slavia': 'Bartunek Slavia',
    'Cleveland Slavia': 'Bartunek Slavia',
    'Bartunek Clothes (Cleveland)': 'Bartunek Slavia',
    'Bartunek Slavia': 'Cleveland Bartunek Slavia',
    
    'White Auto FC': 'White Motor FC',
    'White Motors': 'White Motor FC',
    'White Auto': 'White Motor FC',
    'White Automobile': 'White Motor FC',
    'White Motor': 'White Motor FC',
    'White Motors FC': 'White Motor FC',
    'White Motor FC': 'Cleveland White Motor FC',

    # Tennessee
    #Nashville Blues (TN)
    #Survivors (TN)

    'Tennessee Rhythm': 'Nashville Metros',

    # Set team-mappings.
    'Memphis Jackals': 'Memphis Storm',
    'Memphis Survivors': 'Memphis Storm',
    'Memphis United Express': 'Memphis Storm',
    #'Memphis Rogues': 'Memphis Storm',


    # Minnesota
    'Twin Cities Phoenix': 'Twin Cities Tornado',

    # Ontario
    'Hamilton FC Rage': 'Hamilton Rage',
    'Toronto Supra Portuguese': 'Toronto Supra',
    'Toronto Ulster': 'Toronto Ulster United',
    'Ulster United': 'Toronto Ulster United',

    # Alberta
    'Team Calgary': 'Calgary Storm',
    'Edmonton FC': 'Edmonton F.C.',
    'Edmonton F.C.': 'Edmonton Aviators',
    'Calgary Storm Prospects': 'Calgary Storm Select',
    'Calgary Mustangs': 'Calgary Storm',

    # Quebec
    'Supra de Montreal': 'Montreal Supra',

    # British Columbia
    'Victoria Riptide': 'Victoria Riptides',
    'Vancouver North Shore United': 'Vancouver North Shore',
}

teams.update(usa)

college = {
    'CSU Dominguez-Hills': 'Cal State Dominguez Hills',

    'Cal State University-Hayward': 'California State University, East Bay',

    'Cal State-Northridge': 'California State University, Northridge',
    'CS Northridge': 'California State University, Northridge',
    'California State University, Northridge': 'Cal State Northridge',
    

    'CSU Bakersfield': 'California State University, Bakersfield',
    'Cal State-Bakersfield': 'California State University, Bakersfield',
    'California State University, Bakersfield': 'Cal State Bakersfield',
    
    'California State-Los Angeles': 'Cal State Los Angeles',
    'UCSB': 'University of California, Santa Barbara',
    'UC Santa Barbara': 'University of California, Santa Barbara',
    'California-Santa Barbara': 'University of California, Santa Barbara',



    'UNC-Greensboro': 'University of North Carolina at Greensboro',
    'North Carolina-Greensboro': 'University of North Carolina at Greensboro',
    'University of North Carolina at Greensboro': 'UNC Greensboro',
    'Cincinnati University': 'University of Cincinnati',
    'Western Baptist College': 'Corban University', # set name-map?
    'Fresno State': 'Fresno State University',
    'Loyola Marymount': 'Loyola Marymount University',
    'Loyola College Maryland': 'Loyola University Maryland',
    'Loyola College (Maryland)': 'Loyola University Maryland',
    'William Carey College': 'William Carey University',
    'University of Western Kentucky': 'Western Kentucky University',
    'Life College':'Life University',
    'University of West Virginia': 'West Virginia University',
    'University of Wisconsin-Madison': 'University of Wisconsin',
    'Appalachian State College': 'Appalachian State University',

    'Sacramento State': 'California State University, Sacramento',
    'New Hampshire University': 'University of New Hampshire',
    'Mobile University': 'University of Mobile',
    'New Mexico State': 'New Mexico State University',
    'Fairleigh Dickinson': 'Fairleigh Dickinson University',
    'Rochester University': 'University of Rochester',
    'University of Wake Forest': 'Wake Forest University',
    'Rhode Island University': 'University of Rhode Island',
    'Sangamon State': 'University of Illinois at Springfield',
    'Erskine University': 'Erskine College',
    'El Camino Junior College': 'El Camino College',
    'Chico State University': 'California State University, Chico',
    'Texas Tech': 'Texas Tech University',
    'Avila College': 'Avila University',
    'North Texas State University': 'University of North Texas',
    'Evansville University': 'University of Evansville',
    'California State-Fullerton': 'California State University, Fullerton',
    'San Diego State': 'San Diego State University',
    'San Jose State University': 'San Jose State',
    'Southwest Missouri State': 'Missouri State University',
    'Southwest Missouri State University': 'Missouri State University',
    'SW Missouri State': 'Missouri State University',
    'Missouri State': 'Missouri State University',
    'UMKC': 'University of Missouri-Kansas City',
    'Dayton University': 'University of Dayton',
    'Bowling Green State': 'Bowling Green State University',
    'Bowling Green University': 'Bowling Green State University',
    'Plattsburgh College': 'SUNY Plattsburgh',
    'Fairfield College': 'Fairfield University',
    'Georgia Perimeter Junior College': 'Georgia Perimeter College',
    'Hartford University': 'University of Hartford',
    'Tulsa University': 'University of Tulsa',
    'Dartmouth University': 'Dartmouth College',
    'Akron University': 'University of Akron',
    'California-Los Angeles': 'UCLA',
    'Harvard': 'Harvard University',

    'Generation Adidas': 'Generation adidas',
    'North Carolina State': 'North Carolina State University',
    'NC State': 'North Carolina State University',
    'St Johns University': 'St. John\'s University',
    'Saint John\'s University': 'St. John\'s University',
    'University of Syracuse': 'Syracuse University',
    'Michigan State': 'Michigan State University',
    'Old Dominion':'Old Dominion University',

    'University of Seattle': 'Seattle University',
    'UC Davis': 'University of California, Davis',
    'UTEP': 'University of Texas at El Paso',


    'Appalachian State': 'Appalachian State University',
    'Birmingham Southern': 'Birmingham-Southern College',
    'Birmingham Southern College': 'Birmingham-Southern College',


    'Oregon State': 'Oregon State University',

    #'Cal State Fullerton': 'Cal State-Fullerton',
    'SIU-Edwardsville': 'SIU Edwardsville',
    #'UC Santa Barbara': 'UC-Santa Barbara',
    #'UNC Charlotte': 'UNC-Charlotte',

    #'SIU Edwardsville': 'SIU-Edwardsville',
    'UC-Santa Barbara': 'UC Santa Barbara',
    'Cal State-Fullerton': 'Cal State Fullerton',
    'Odea High School, WA': 'O\'Dea High School, WA',
    'William & Mary': 'College of William and Mary',
    'William & Mary College': 'College of William and Mary',
    'William and Mary': 'College of William and Mary',
    'William and Mary College': 'College of William and Mary',
    'College of William & Mary': 'College of William and Mary',
    'Franklin Pierce College': 'Franklin Pierce University',
    'University of Albany': 'University at Albany, SUNY',
    'Tampa University': 'University of Tampa',

    # Colleges
    'UC Berkeley': 'University of California, Berkeley',
    'Cleveland State': 'Cleveland State University',
    'Evansville College': 'University of Evansville',
    'Pittsburgh University': 'University of Pittsburgh',
    'Southern Connecticut State': 'Southern Connecticut State University',
    'UIC': 'University of Illinois at Chicago',
    'UNC': 'University of North Carolina',
    'University of North Carolina-Chapel Hill': 'University of North Carolina',

    'Notre Dame': 'University of Notre Dame',

    'UC-Santa Barbara': 'UC Santa Barbara',


    'St. Louis University': 'Saint Louis University',
    'SMU': 'Southern Methodist University',
    'University of Wisconsin Milwaukee': 'University of Wisconsin-Milwaukee',
    'University of Wisconsin Green Bay': 'University of Wisconsin-Green Bay',
    'UConn': 'University of Connecticut',

    'UAB': 'University of Alabama at Birmingham',
    'University of Alabama Birmingham': 'University of Alabama at Birmingham',
    'University of Alabama-Birmingham': 'University of Alabama at Birmingham',
    'Alabama-Birmingham': 'University of Alabama at Birmingham',
    'Alabama A&M': 'Alabama A&M University',
    'Colorado-Colorado Springs': 'University of Colorado Colorado Springs',
    'SFU': 'Simon Fraser University',
    'Chico State': 'Chico State University',
    'Duke': 'Duke University',
    'Wake Forest': 'Wake Forest University',
    'Ohio State': 'Ohio State University',

    'SIU-Edwardsville': 'SIU Edwardsville',
    'Southern Illinois University Edwardsville': 'SIU Edwardsville',

    'Columbia College': 'Columbia University',
    'Princeton College': 'Princeton University',
    'Louisville University': 'University of Louisville',
    'Princeton': 'Princeton University',
    'DePaul': 'DePaul University',
    'Wright State': 'Wright State University',
    'Seton Hall': 'Seton Hall University',
    'Rutgers College': 'Rutgers University',
    'Rutgers': 'Rutgers University',
    'Clemson': 'Clemson University',
    'Yale College': 'Yale University',
    'Yale': 'Yale University',
    'City College New York': 'City College of New York',
    'Tufts College': 'Tufts University',
    'Brooklyn Poly Institute': 'Brooklyn Poly',
    'Penn (Gettysburg) College': 'Gettysburg College',
    'Cornell College': 'Cornell University',
    'Richmond College': 'University of Richmond',
    'State University of Iowa': 'Iowa State University',
    'Washington & Lee': 'Washington & Lee University',
    'Minnesota College': 'University of Minnesota',

    'UNC-Charlotte': 'UNC Charlotte',
    'North Carolina-Charlotte': 'UNC Charlotte',
    
    # High schools
    'Odea High School, WA': 'O\'Dea High School, WA',

}

teams.update(college)

international = {

    'US Maccabi': 'United States Maccabi',
    'Canada College': 'Cañada College',

    'Haití': 'Haiti',
    'US Virgin Islands': 'U.S. Virgin Islands',
    #Dominican Rep>, <Team: Dominican Rep.>]
    'Saint Vincent and The Grenadines': 'Saint Vincent and the Grenadines',
    'Cote d\'Ivoire': 'Côte d\'Ivoire',
    'Rumania': 'Romania',

    'Saint Vincent and Grenadines': 'Saint Vincent and the Grenadines',
    'St. Vincent and Grenadines': 'Saint Vincent and the Grenadines',
    'Netherlands Antilles': 'Curacao',

    'Demerara': 'Guyana',
    'British Guyana': 'Guyana',
    'French Guyana': 'French Guiana',
    'Dutch Guiana': 'Suriname',

    'St Kitts': 'Saint Kitts and Nevis',

    'Turks and Caicos': 'Turks and Caicos Islands',
    'St. Kitts and Nevis': 'Saint Kitts and Nevis',
    'St. Vincent and the Grenadines': 'Saint Vincent and the Grenadines',
    'Surinam': 'Suriname',
    'St. Lucia': 'Saint Lucia',
    'St Lucia': 'Saint Lucia',
    'Faeroe Islands': 'Faroe Islands',
    'Fr. Saint Martin': 'Saint Martin',

    'Haití': 'Haiti',
    'Bermuda Under-23': 'Bermuda U-23',
    'Trinidad & Tobago': 'Trinidad and Tobago',
    'Trinidad/Tobago': 'Trinidad and Tobago',
    'España': 'Spain',
    'Irak': 'Iraq',
    'Southafrica': 'South Africa',
    'Nueva Zealandia': 'New Zealand',

    'Mexico': 'México',
    'Peru': 'Perú',


    'Côte d\'Ivoire (Ivory Coast)': 'Côte d\'Ivoire',
    'Ivory Coast': 'Côte d\'Ivoire',
    'German Democratic Republic': 'East Germany',
    'German DR': 'East Germany',
    'Germany FR': 'West Germany',
    'FR Germany': 'West Germany',
    'Korea DPR': 'North Korea',
    'Korea Republic': 'South Korea',
    'USA': 'United States',
    'Dutch Antilles': 'Netherlands Antilles',
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
    'Colombia NT': 'Colombia',
    'Indonesia National Team': 'Indonesia',
    'Iran National Team': 'Iran',
    'Malaysia National Team': 'Malaysia',
    'Puerto Rico National Team': 'Puerto Rico',
    'Singapore National Team': 'Singapore',
    'U. S. National Team': 'United States',
    'Guatemala NT': 'Guatemala',
    'Haiti NT': 'Haiti',
    'Puerto Rico NT': 'Puerto Rico',
    'El Salvador National team': 'El Salvador',
    'Bermuda NT': 'Bermuda',
    'Mexico U-21 National team': 'Mexico U-21',
    'USSR': 'U.S.S.R.',
    'U.S.S.R': 'U.S.S.R.',
    'Soviet Union': 'U.S.S.R',
    }
teams.update(international)




all_star = {

    'Serie  C U-21 - Italy': 'Serie C U-21',

    'Japanese League All-Stars': 'Japanese All-Stars',
    'U.S. All-stars': 'U.S. All-Stars', #find
    'World All-stars': 'World All-Stars', #find


    'All Stockholm': 'Stockholm All-Stars',
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


mls_teams = {

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
    'Orange County': 'Orange County Blue Star', # This one is bad.
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
