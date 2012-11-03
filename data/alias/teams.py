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

    


world = {

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
    'Sydney FC - Australia': 'Sydney FC',


    # Europe

    # Israel
    'hapoel': 'Hapoel',
    'Hapoel Tel Aviv': 'Hapoel Tel Aviv F.C.',
    'Hapoel Petah Tikvah': 'Hapoel Petah Tikva F.C.',
    'Hapoel Petah Tikva': 'Hapoel Petah Tikva F.C.',
    'Hapoel Haifa': 'Hapoel Haifa F.C.',
    'Maccabi Tel Aviv': 'Maccabi Tel Aviv F.C.',

    # Portugal
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
    'Sporting Lisbon': 'Sporting Clube de Portugal',
    'varzim': 'Varzim',
    'Varzim': 'Varzim S.C.',
    'Varzim (Portugal)': 'Varzim S.C.',
    'Uniao de Santarem': 'União de Santarém',

    # Spain
    'Barcelona': 'FC Barcelona',
    'Barcelona (Spain)': 'FC Barcelona',
    'Barcelona B': 'FC Barcelona B',
    'Espanyol': 'RCD Espanyol',
    'Sabadell': 'CE Sabadell FC',
    'Valladolid': 'Real Valladolid',

    # Belgium
    'Antwerp': 'Royal Antwerp F.C.',

    # Netherlands
    'Ajax - Netherlands': 'Ajax',
    'Ajax': 'AFC Ajax',
    'Ajax Amsterdam': 'AFC Ajax',
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
    'Paris St.-Germain': 'Paris Saint-Germain F.C.',
    'Paris Saint-Germain': 'Paris Saint-Germain F.C.',
    'Paris St. Germain': 'Paris Saint-Germain F.C.',

    # Greece
    'apollon': 'Apollon',
    'Apollon': 'Apollon Limassol',
    'A.O. Krete': 'AO Krete',
    'AEK': 'AEK Athens F.C.',

    # Austria
    'Rapid Wien': 'Rapid Vienna',
    'FC Salzburg - Austria': 'FC Salzburg',
    'FC Salzburg': 'FC Red Bull Salzburg',
    
    # Switzerland
    'Grasshoppers': 'Grasshoppers Zurich',
    'Grasshoppers Zurich': 'Grasshopper Club Zürich',
    'Stade Laussane - Switzerland': 'Stade Laussane',
    'Young Boys\' Club': 'BSC Young Boys',

    # Italy
    'Arezzo - Italy': 'Arezzo',
    'Bari': 'A.S. Bari',
    'Bologna': 'Bologna F.C. 1909',
    'Fiorentina - Italy': 'Fiorentina',
    'Fiorentina': 'AFC Fiorentina',
    'Genoa - Italy': 'Genoa',
    'Genoa': 'Genoa CFC',
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

    # Scandinavia
    'Goteborg Orgryte': 'Örgryte IS',
    'Norrkoeping': 'IFK Norrköping',
    'Norrkoping': 'IFK Norrköping',
    'Hammarby': 'Hammarby IF',
    'Malmo': 'Malmö FF',
    'Helsingborg': 'Helsingborgs IF',
    'Helsingborgs': 'Helsingborgs IF',
    'Bodo/Glimt': 'FK Bodø/Glimt',
    'Orebro': 'Örebro SK',
    'Elfsborg': 'IF Elfsborg',
    'Gif Sundsvall -- Sweden': 'Gif Sundsvall',
    'Odd Grenland -- Norway': 'Odd Grenland',
    'Rosenborg Trondheim -- Norway': 'Rosenborg Trondheim',
    'Lyn Oslo -- Norway': 'Lyn Oslo',
    'Fylkir (Iceland)': 'Fylkir',
    'Fylkir - Iceland': 'Fylkir',
    'IBV - Iceland': 'IBV',
    'Lyngby - Denmark': 'Lyngby',
    'A.I.K.': 'AIK Fotboll',
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
    'Valur': 'Valur FC',
    'Norresundby Boldklub - Denmark': 'Norresundby Boldklub',
    'Viking Stavangar -- Norway': 'Viking FK',
    'Bodo/Glimt -- Norway': 'Bodo/Glimt',
    'Stabaek -- Norway': 'Stabaek',

    # Germany
    '1860 Munchen -- Germany': '1860 Munchen',
    '1860 Munchen': 'TSV 1860 München',
    'TSC Muenchen 1860': 'TSV 1860 München',
    'Bayer Leverkusen - Germany': 'Bayer Leverkusen',
    'Bayern Munich - Germany': 'Bayern Munich',
    'Bayern Munchen': 'FC Bayern Munich',
    'Bayern Munich': 'FC Bayern Munich',
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
    'FC Cologne': '1. FC Köln',
    'F. C. Koln': '1. FC Köln',
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
    'Ards (Northern Ireland)': 'Ards F.C.',
    'Ards': 'Ards F.C.',
    'Dundalk (Ireland)': 'Dundalk F.C.',
    'Dundalk': 'Dundalk F.C.',
    'Glenavon (Northern Ireland)': 'Glenavon F.C.',
    'Glenavon': 'Glenavon F.C.',
    'Linfield (Northern Ireland)': 'Linfield F.C.',
    'Linfield': 'Linfield F.C.',

    # Scotland
    'Aberdeen': 'Aberdeen F.C.',
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

    # England
    'Aston Villa': 'Aston Villa F.C.',
    'Aston Villa - England': 'Aston Villa',
    'Birmingham City': 'Birmingham City F.C.',
    'Blackpool': 'Blackpool F.C.',
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
    'Leeds United': 'Leeds United A.F.C.',
    'Leeds United - England': 'Leeds United',
    'Leicester City - England': 'Leicester City',
    'Liverpool': 'Liverpool F.C.',
    'Liverpool FC': 'Liverpool F.C.',
    'Manchester City': 'Manchester City F.C.',
    'Manchester United - England': 'Manchester United',
    'Manchester United FC': 'Manchester United',
    'Middleborough FC': 'Middlesbrough F.C.',
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
    'Wolverhampton': 'Wolverhampton Wanderers F.C.',
    'Workington AFC': 'Workington A.F.C.',


    # South America

    # Venezuela
    'Italchacao -- Venezuela': 'Italchacao',
    'Italchacao': 'Deportivo Petare',

    # Colombia
    'America de Cali': 'América de Cali',
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

    # Ecuador
    'Barcelona -- Ecuador': 'Barcelona Sporting Club',
    'Barcelona (Ecuador)': 'Barcelona Sporting Club',

    # Peru
    'Alianza Lima - Peru': 'Alianza Lima',
    'Sporting Cristal -- Peru': 'Sporting Cristal',

    # Chile
    'Colo Colo - Chile': 'Colo Colo',
    'Colo Colo': 'Colo-Colo',
    'Magallanes - Chile': 'Magallanes',
    'Magallanes': 'Deportes Magallanes',
    'Palestino - Chile': 'Palestino',
    'San Felipe - Chile': 'Unión San Felipe',
    'Union San Felipe': 'Unión San Felipe',
    'Universidad de Chile - Chile': 'Club Universidad de Chile',
    'Universidad Catolica - Chile': 'CD Universidad Católica',
    'Universidad Catolica': 'CD Universidad Católica',

    # Uruguay
    'Nacional': 'Club Nacional de Football',
    'Nacional -- Uruguay': 'Nacional',
    'Penarol': 'C.A. Peñarol',

    # Argentina
    'Belgrano': 'Club Atlético Belgrano',
    'Boca Juniors - Argentina': 'Boca Juniors',
    'Deportivo Moron': 'Deportivo Morón',
    'Independiente': 'CA Independiente',
    'Independiente': 'CA Independiente',
    'Racing (Argentina)': 'Racing Club de Avellaneda',
    'Racing Club (Argentina)': 'Racing Club de Avellaneda',
    'Sacachisapas': 'Sacachispas Fútbol Club', 
    'Sacachispas': 'Sacachispas Fútbol Club',
    'San Lorenzo - Argentina': 'San Lorenzo',

    # Brazil
    'America de Rio de Janeiro': 'America Rio',
    'America RJ': 'America Rio',
    'Bangu AC': 'Bangu Atlético Clube',
    'Bangu': 'Bangu Atlético Clube',
    'Bonsucesso (Brazil)': 'Bonsucesso FC',
    'Cruzeiro (Brazil)': 'Cruzeiro',
    'Flamengo (Brazil)': 'Flamengo',
    'Macaupa (Brazil)': 'Macapá',
    'Macaupo': 'Macapá',
    'National Fast Club (Brazil)': 'National Fast Club',
    'Oscar\'s FC - Brazil': 'Oscar\'s FC',
    'Palmeiras - Brazil': 'Palmeiras',
    'Santos (Brazil)': 'Santos FC',
    'Santos': 'Santos FC',
    'Uberlandia (Brazil)': 'Uberlândia Esporte Clube',
    'Uberlandia': 'Uberlândia Esporte Clube',
    'Vasco da Gama -- Brazil': 'Vasco da Gama',
    'Vasco Da Gama': 'Vasco da Gama',
    'Vasco da Gama': 'CR Vasco da Gama',

    
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
    'Arnett Gardens-- Jamaica': 'Arnett Gardens',
    'Arnett Gardens': 'Arnett Gardens F.C.',
    'Harbour View FC -- Jamaica': 'Harbour View FC',
    'Harbour View': 'Harbour View FC',

    # Haiti
    'Racing Club (Haiti)': 'Racing Club Haitien',
    'Racing (Haiti)': 'Racing Club Haitien',
    'Racing Club Haitien': 'R.C. Haïtien',
    'Tempête': 'Tempête Football Club',
    'Tempete': 'Tempête Football Club',
    'Violette': 'Violette AC',
    
    # Trinidad
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
    'Club Deportivo Marte': 'Marte',
    'Marte FC': 'Marte',
    'Marte': 'C.D. Atlético Marte',
    'C.D. Atletico Marte': 'C.D. Atlético Marte',

    # Nicaragua 
    'America (Nicaragua)': 'América Managua',
    'Real Estelí': 'Real Estelí F.C.',
    'Real Estelí': 'Real Estelí F.C.',
    'Esteli': 'Real Estelí F.C.',
    'Real Esteli': 'Real Estelí F.C.',
    'Real Estelí': 'Real Estelí F.C.',

    # Panama
    'Deportivo Arabe Unido --Panama': 'Arabe Unido',
    'Chorrillo': 'Chorrillo F.C.',
    'San Francisco': 'San Francisco FC',
    'Tauro': 'Tauro FC',

    # Belize
    'Acros': 'Acros Crystal',
    'Hankok Verdes': 'Club Verdes',
    'Leslie Verdes': 'Club Verdes',

    # Guatemala
    'Aurora': 'Aurora F.C.',
    'Coban - Guatemala': 'Coban',
    'Comunicaciones': 'C.S.D. Comunicaciones',
    'Comunciaciones': 'C.S.D. Comunicaciones',
    'Communicaciones': 'C.S.D. Comunicaciones',
    'C.S.D. Comunicaciones': 'CSD Comunicaciones',
    'Comunicaciones - Guatemala': 'CSD Comunicaciones',
    'CSD Comunicaciones-- Guatemala': 'CSD Comunicaciones',
    'Galcasa': 'CSD Galcasa',
    'Municipal': 'CSD Municipal',
    'CSD Municipal -- Guatemala': 'CSD Municipal',
    'Suchitepequez - Guatemala': 'Suchitepequez',
    'Xelaju': 'Xelajú MC',
    'Xelaju MC': 'Xelajú MC',

    # Honduras
    'Marathon': 'Marathón',
    'Motagua': 'CD Motagua',
    'Motagua -- Honduras': 'Motagua',
    'Olimpia': 'CD Olimpia',
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
    'San Lorenzo - Costa Rica': 'San Lorenzo Costa Rica',
    'Santa Teresita FC -Costa Rica': 'Santa Teresita FC',
    'Deportivo Saprissa -Costa Rica': 'Deportivo Saprissa',
    'CD Saprissa-- Costa Rica': 'Saprissa',
    'Saprissa': 'Deportivo Saprissa',
    'Deportivo Saprissa S.A.D.': 'Deportivo Saprissa',

    # Mexico
    'CF América': 'Club América',
    'América': 'Club América',
    'Club America': 'Club América',
    'CF América': 'Club América',
    'Club America -- Mexico': 'Club America',
    'Asturias': 'Club de Fútbol Asturias',
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
    'Colima Jaguares (Mexico)': 'Colima Jaguares',
    'Colima Jaguares - Mexico': 'Colima Jaguares',
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
    'Leon -- Mexico': 'Leon',
    'México Country Club': 'México Cricket Club',
    'Mexico Cricket Club': 'México Cricket Club',
    'Morelia - Mexico': 'Morelia',
    'Morelia -- Mexico': 'Morelia',
    'Athletico Morelia': 'Monarcas Morelia',
    'Athlético Morelia': 'Monarcas Morelia',
    'Atlético Morelia': 'Monarcas Morelia',
    'Morelia': 'Monarcas Morelia',
    'CA Monarcas Morelia': 'Monarcas Morelia',
    'Monterrey - Mexico': 'Monterrey',
    'Monterrey': 'CF Monterrey',
    'Monterrey (Mexico)': 'CF Monterrey',
    'C.F. Monterrey': 'CF Monterrey',
    'Necaxa -- Mexico': 'Necaxa',
    'Necaxa - Mexico': 'Necaxa',
    'Club Necaxa': 'Necaxa',
    'Deportivo Oro': 'C.D. Oro',
    'Oro - Mexico': 'CD Oro',
    'Oro': 'C.D. Oro',
    'CD Oro': 'C.D. Oro',
    'Pachuca-- Mexico': 'Pachuca',
    'Pachuca': 'C.F. Pachuca',
    'Pachuca CF': 'C.F. Pachuca',
    'Pachuca AC': 'C.F. Pachuca',
    'Puebla - Mexico': 'Puebla',
    'Puebla F.C.': 'Puebla',
    'Puebla FC': 'Puebla',
    'Puebla AC': 'Puebla',
    'San Luis': 'San Luis FC',
    'San Luis F.C.': 'San Luis FC',
    'Laguna F.C.': 'Santos Laguna',
    'Laguna FC': 'Santos Laguna',
    'Santos - Mexico': 'Santos Laguna',
    'Santos Laguna - Mexico': 'Santos Laguna',
    'Santos -- Mexico': 'Santos Laguna',
    'Club Sol - Mexico': 'Club Sol',
    'Tampico-Madero': 'Tampico Madero',
    'Tapatio': 'CD Tapatio',
    'Tapatios': 'CD Tapatio',
    'Tapatio - Mexico': 'CD Tapatio',
    'Tapatillo': 'CD Tapatio',
    'CD Tapatio': 'CD Tapatío',
    'UAG - Mexico': 'Tecos',
    'Tecos - Mexico': 'Tecos',
    'U.A. de G.': 'Tecos',
    'Estudiantes Tecos': 'Tecos',
    'UAG': 'Tecos',
    'U.A.G.': 'Tecos',
    'UAG Tecos': 'Tecos',
    'Tijuana Chivas - Mexico': 'Tijuana Chivas',
    'Nacional de Tijuana - Mexico': 'Nacional de Tijuana',
    'CD Toluca': 'Toluca',
    'Toluca -- Mexico': 'Toluca',
    'Toluca - Mexico': 'Toluca',
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
    'Club Deportivo Veracruz': 'Veracruz',
    'Veracruz - Mexico': 'Veracruz',
    'Veracruz (Mexico)': 'Tiburones Rojos de Veracruz',
    'Verarcuz': 'Tiburones Rojos de Veracruz',
    'Veracruz': 'Tiburones Rojos de Veracruz',
    'UAT': 'Correcaminos UAT',
    'U.A.T.': 'Correcaminos UAT',
}
teams.update(world)


usa = {

    # Accurate?
    'Philadelphia 1928-1929': 'Philadelphia Field Club',

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
    'Connecticut Bi-Centennials': 'Connecticut Bicentennials',
    'Hartford Bi-Centennials': 'Connecticut Bicentennials',
    'Hartford Bicentennials': 'Connecticut Bicentennials',
    'Atlanta Apollos': 'Atlanta Chiefs',
    'Cosmos': 'New York Cosmos',
    'Golden Bay Earthquakes': 'San Jose Earthquakes',

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
    'Metrostars': 'New York Red Bulls',
    'MetroStars': 'New York Red Bulls',
    'New York/New Jersey MetroStars': 'New York Red Bulls',
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
    'Hartford SC': 'Hartford Kings',
    'Hartford FC': 'Hartford Kings',
    'Indianapolis Daredevils': 'Rhode Island Oceaneers',
    'Las Vegas Quicksilvers': 'Las Vegas Quicksilver',
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
    'Albuquerque Geckos': 'Sacramento Geckos',
    'FC Tampa Bay': 'Tampa Bay Rowdies',
    'Hampton Roads Mariners': 'Virginia Beach Mariners',
    'Hampton Rds Mariners': 'Virginia Beach Mariners',


    # Uncategorized
    
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
    'Wichita Blue': 'Wichita Blue Angels', # Check these names.


    # Connecticut
    'Bridgeport City AF.C': 'Bridgeport City AFC',

    # Rhode Island
    'Providence Wanderers': 'Providence Free Wanderers', # Check this - probably wrong...
    'Pawtucket FC': 'Pawtucket F.C.',

    'Thornton British Hosiers': 'Thornton Rovers',
    'Thornton British Hosieries': 'Thornton Rovers',

    # Florida
    'HRC Kickers': 'St. Petersburg Kickers',
    'McCormick Kickers': 'St. Petersburg Kickers',

    # Wisconsin
    'Milwaukee Bavarian': 'Milwaukee Bavarian SC',
    'Milwaukee Bavarian Blue Ribbon': 'Milwaukee Bavarian SC',
    'Bavarian SC (WI)': 'Milwaukee Bavarians SC',
    'Milwaukee Bavarians': 'Milwaukee Bavarian SC',
    'Bavarian SC': 'Milwaukee Bavarian SC',

    'Falk Field Club (Mil.)': 'Milwaukee Falk FC',
    'Falk Field Club': 'Milwaukee Falk FC',

    # Georgia
    'Atlanta Silverbacks U-23\'s': 'Atlanta Silverbacks U23\'s',
    'Augusta Fireball United': 'Augusta Fireball',

    # Indiana
    'Ft. Wayne Fever': 'Fort Wayne Fever',
    'Gary Tigers': 'Indiana Tigers',

    # California
    'Los Angeles Kickers-Victoria (South California)': 'Los Angeles Kickers',
    'Sacramento Spirits': 'Sacramento Gold',
    'Maccabee AC': 'Maccabi Los Angeles',
    'LA Blues': 'Los Angeles Blues',

    # Virginia
    'Aegean Hawks': 'Aegean Hawks FC',

    'Club Espana (DC/VA)': 'Club Espana',
    'Richhmond Kickers': 'Richmond Kickers',
    'North Virginia Royals': 'Northern Virginia Royals',
    'Roanoke River Dawgs': 'Roanoke RiverDawgs',
    'Roanoke Riverdawgs': 'Roanoke RiverDawgs',
    'Virginia Capitol Cavaliers': 'Washington Cavaliers',

    # Washington
    'Everett BigFoot': 'Seattle BigFoot',
    'Everett Bigfoot': 'Seattle BigFoot',

    # Michigan
    'Holley C.': 'Holley Carburetor F.C.',
    'Mid-Michigan Bucks': 'Michigan Bucks',
    'Packard FC': 'Detroit Packard FC',

    # Louisiana
    'Louisiana Outlaws': 'Lafayette Swamp Cats',
    'Lafayette SwampCats': 'Lafayette Swamp Cats',

    # Oregon
    'Portland Timbers U23': 'Portland Timbers U23\'s',

    # Idaho
    'Sioux Falls SpitFire': 'Sioux Falls Spitfire',

    # Texas
    'Austin Aztex U23s': 'Austin Aztex U23',
    'Austin Lighting': 'Autin Lightning',
    'Autin Lightning': 'Austin Lightning',

    'Dallas Inter': 'Dallas Mean Green',
    'Dallas Mulhausers': 'Dallas Mulhauser',

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

    'Chivas El Paso Patriots': 'El Paso Patriots',
    'Rio Grande Valley Grandes FC': 'Rio Grande Valley Grandes',
    
    # California
    'McIlvane Canvasbacks': 'McIlvaine Canvasbacks',
    'McKeesport National Tube': 'McKeesport FC',

    'San Fern. Valley Golden Eagles': 'San Fernando Valley Golden Eagles',
    'Valley Golden Eagles': 'San Fernando Valley Golden Eagles',
    'SFV Golden Eagles': 'San Fernando Valley Golden Eagles',

    'CD Mexico (North California)': 'El Farolito Soccer Club',
    'San Fernando Quakes': 'San Fernando Valley Quakes',

    'Central Valley Hydra': 'CCV Hydra',

    'Greek American AC (North CA)': 'San Francisco Greek American AC',
    'San Francisco Greek Americans': 'San Francisco Greek American AC',

    'Bay Area Seals': 'San Francisco Bay Seals',
    'San Francisco Seals': 'San Francisco Bay Seals',
    'SFB Seals': 'San Francisco Bay Seals',

    'San Francisco AC': 'San Francisco A.C.',
    'San Jose Hawks': 'San Francisco Bay Blackhawks',
    'San Francisco C.D. Mexico' : 'El Farolito Soccer Club',


    # North Carolina
    'Raleigh Elite': 'Raleigh CASL Elite',
    'CASL Elite': 'Raleigh CASL Elite',
    'Raleigh Express': 'Raleigh Capital Express',
    'Raleigh Capital Express': 'Raleigh Flyers',

    # Arizona
    'Phoenix Hearts': 'Arizona Sahuaros',
    'Arizona Cotton': 'Arizona Sahuaros',
    'Arizona Phoenix': 'Arizona Sahuaros',


    # New York City
    'St George FC': 'St. George F.C',
    'Critchley AA': 'Critchley\'s',
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
    'Brooklyn Morse Dry Dock': 'Morse Dry Dock',

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

    'Albany Black Watch Highlanders': 'Albany Blackwatch Highlanders',

    'Kodak Park': 'Kodak Park FC',

    'Rochester Celtics': 'Rochester Celtic',
    'Rochester Celtic': 'Rochester Kelly Celtic',
    'Kelly Celtic': 'Rochester Kelly Celtic',
    'Kelly Celtic (Rochester': 'Rochester Kelly Celtic',

    'New Rochelle Association': 'New Rochelle Foot Ball Association',

    'Becks German American SC (Buffalo)': 'Buffalo Becks',
    'Becks German American S.C. (Buffalo)': 'Becks German American SC (Buffalo)',
    'Becks German American SC (Buf.)': 'Becks German American S.C. (Buf.)',
    'Buffalo Becks': 'Buffalo Becks German American SC',
    'Becks German American S.C. (Buf.)': 'Buffalo Becks German American SC',

    'Hollywood Inn': 'Yonkers Hollywood Inn',
    'Yonkers Th.': 'Yonkers Thistle',
    'MacKenzie SC (Niagra Falls)': 'MacKenzie FC (Niagara Falls)',

    # New Jersey
    'Americus AA': 'Americus A.A.',

    'Bunker Hill F.C.': 'Bunker Hill FC',

    'Kearny Rovers': 'Kearney Rovers',
    'Kearny Rangers': 'Kearney Rangers',

    'Paterson Caledonian Thistles': 'Paterson Thistles',
    'Swanton Field Club (Kearny, NJ)': 'Swanton Field Club',
    'Hoboken F.C.': 'Hoboken FC',
    'Holyoke Falco': 'Holyoke Falcos',
    'Newark Ukrainian': 'Newark Ukrainian Sitch',

    'Paterson Silk Sox': 'Paterson F.C.',
    'Trenton Highlanders': 'Paterson F.C.',
    'Paterson Caledonian': 'Paterson F.C.',
    'Newark Germans': 'Paterson F.C.',

    'West Hudson AA': 'West Hudson A.A.',
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
    'Montclair': 'Fontana Falcons',
    'Newark Falcons': 'Elizabeth Falcons',
    'Falcons SC': 'Elizabeth Falcons',
    'Falcons-Warsaw': 'Elizabeth Falcons',

    'New Brunswick Hungarian Americans': 'New Brunswick Hungarians',
    'New Jersey Shaefer Brewers': 'New Jersey Brewers',

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

    'Jersey AC': 'Jersey A.C.',
    'Newark FC': 'Newark F.C.',

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
    'Harrison S.C.': 'Erie A.A.',
    'Harrison Erie S.C.': 'Erie AA',
    'Erie AA': 'Erie A.A.',
    'Erie A.A': 'Harrison Erie F.C.',

    # Illinois
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
    'Sparta': 'Chicago Sparta ABA',
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

    # Pennsylvania

    'Heidelberg SC': 'Heidelberg S.C.',
    'Heidelberg Losegos': 'Heidelberg S.C.',

    'Centennial FC': 'Centennial F.C.',
    'Centennial': 'Centennial F.C.',

    'Puritan Y.M.L': 'Puritan Y.M.L.',
    'Puritan YML': 'Puritan Y.M.L',

    'Wanderers FC (Philadelphia)': 'Philadelphia Wanderers FC',
    'West Philadelphia': 'West Philadelphia FC',

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
    'Baltimore Stars': 'Baltimore Bays',
    'Baltimore SC': 'Baltimore S.C.',
    
    # Massachusetts
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

    'Mahoning Valley FC': 'Mahoning Valley',

    'Goodyear FC': 'Akron Goodyear FC',
    'Goodyear FC (Akron)': 'Akron Goodyear FC',
    'Akron FC': 'Akron Goodyear FC',

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

    # Ontario
    'Hamilton FC Rage': 'Hamilton Rage',
    'Toronto Supra Portuguese': 'Toronto Supra',
    'Toronto Ulster': 'Toronto Ulster United',
    'Ulster United': 'Toronto Ulster United',

    # Alberta
    'Team Calgary': 'Calgary Storm',
    'Edmonton FC': 'Edmonton F.C.',
    'Calgary Storm Prospects': 'Calgary Storm Select',

    # Quebec
    'Supra de Montreal': 'Montreal Supra',

    # British Columbia
    'Victoria Riptide': 'Victoria Riptides',
    'Vancouver North Shore United': 'Vancouver North Shore',
}

teams.update(usa)

college = {

    # Colleges

    'SFU': 'Simon Fraser University',
    'Chico State': 'Chico State University',
    'Duke': 'Duke University',
    'SIU-Edwardsville': 'SIU Edwardsville',
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
}

international = {

    'Côte d\'Ivoire (Ivory Coast)': 'Côte d\'Ivoire',
    'Ivory Coast': 'Côte d\'Ivoire',
    'German DR': 'East Germany',
    'Germany FR': 'West Germany',
    'Korea DPR': 'North Korea',
    'Korea Republic': 'South Korea',
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
    }
teams.update(international)




all_star = {

    'Serie  C U-21 - Italy': 'Serie C U-21',

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
