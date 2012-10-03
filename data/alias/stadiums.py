#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

# This should only be used for
# 1. Stadiums with multiple names
# 2. Stadiums whose names are incorrect (externally)


def get_stadium(s):
    """
    Recursive. 
    """

    s = s.strip()
    if s in sd:
        return get_stadium(sd[s])
    else:
        return s

sd = {}

stadiums = {
    'Cal State Fullerton Titan Stadium': 'Titan Stadium',
    'Sherbeck Field': 'Hal Sherbeck Field',
    'Legion Sports Complex': 'Legion Stadium',
    'Krenzler Stadium': 'Krenzler Field',
    'Belson Stadium (St. John\'s University)': 'Belson Stadium',
    'Citibank Park': 'Bethpage Ballpark',
    'Stony Brook University Stadium': 'Kenneth P. LaValle Stadium',
    'Peter Johansen Stadium': 'Peter Johansen High School Stadium',
    'Collins-Perley Sports Complex': 'Collins Perley Sports Center',
    'Consol Energy Park': 'Falconi Field',

    'Wembley': 'Wembley Stadium',
    'Niedersachsenstadion': 'AWD-Arena',
    'Neckerstadion': 'Mercedes-Benz Arena',
    'Santiago Bernabeu': 'Estadio Santiago Bernabéu',
    'Vicente Calderon': 'Estadio Vicente Calderón',
    'Jose Rico Perez': 'Estadio José Rico Pérez',
    'Riazor': 'Estadio Riazor',
    'La Rosaleda': 'Estadio La Rosaleda',
    'La Mosson': 'Stade de la Mosson',
    'The Willem II Stadium': 'Koning Willem II Stadion',

    'Vijverberg Stadium': 'De Vijverberg',
    'The Parkstad Limburg Stadium': 'Parkstad Limburg Stadion',
    'The Galgenwaard Stadium': 'Stadion Galgenwaard',
    'Rashid Al-Maktoum Stadium': 'Maktoum Bin Rashid Al Maktoum Stadium',
    'Zayed Sports City': 'Sheikh Zayed Stadium',
    'Mohammad Bin Zayed Stadium': 'Mohammed Bin Zayed Stadium',
    'Durival de Brito': 'Estádio Vila Capanema',
    'King Fahd International Stadium': 'King Fahd Stadium',
    'Eucaliptos': 'Estádio dos Eucaliptos',
    'Roker Park Ground': 'Roker Park',
    'White City': 'White City Stadium',
    'Parc Lescure': 'Stade Chaban-Delmas',
    'La Corregidora': 'Estadio Corregidora',
    'Neza': 'Estadio Neza 86',
    'Tecnologico': 'Estadio Tecnológico',
    'Azteca': 'Estadio Azteca',
    'Jalisco': 'Estadio Jalisco',
    'Cuauhtemoc': 'Estadio Cuauhtémoc',
    'Gerland': 'Stade de Gerland',
    'La Beaujoire': 'Stade de la Beaujoire',
    'Nazionale PNF': 'Stadio Nazionale del PNF',
    'Pocitos': 'Estadio Pocitos',
    'Benito Mussolini': 'Stadio Olimpico di Torino',
    'Giorgio Ascarelli': 'Stadio Giorgio Ascarelli',
    'Littorale': 'Stadio Renato Dall\'Ara',
    'Littorio': 'Stadio Littorio',
    'Luigi Ferraris': 'Stadio Luigi Ferraris',
    'Meinau': 'Stade de la Meinau',
    'Cavee Verte': 'Stade de la Cavée verte',
    'Victor Boucquey': 'Stade Victor Boucquey',
    'Fort Carree': 'Stade du Fort Carré',
    'Rasunda': 'Råsunda Stadium',
    'Jarnvallen': 'Jernvallen',
    'Nya Ullevi': 'Ullevi',


    'Wankdorf': 'Wankdorf Stadium',
    'La Pontaise': 'Stade Olympique de la Pontaise',
    'Charmilles': 'Charmilles Stadium',
    'Comunale di Cornaredo': 'Cornaredo Stadium',
    'St. Jacob Park': 'St. Jakob-Park',


    'New Meadowlands Stadium': 'Giants Stadium', # Huh?

    'Centenario': 'Estadio Centenario',
    'King Baudouin Stadium': 'Stade Roi Baudouin',
    'Estadío Parque Espana': 'Parque Espana',
    'Pontiac Silverdome': 'Silverdome',
    'Las Vegas Stadium': 'Sam Boyd Stadium',
    'Atlanta Fulton County Stadium': 'Atlanta-Fulton County Stadium',
    'Aquinas Stadium': 'Holleder Memorial Stadium',
    'Robert F. Kennedy Stadium': 'Robert F. Kennedy Memorial Stadium',
    'Edinboro University Stadium': 'Sox Harrison Stadium',
    'Middlefield Cheese Stadium (Bedford)': 'Middleford Cheese Stadium',
    'Florida Citrus Bowl': 'Citrus Bowl',
    'Richard Montgomery HS': 'Richard Montgomery High School',

    'Seahawk Stadium': 'CenturyLink Field',
    'Sticky Wicket Stadium': 'Stanford Cricket Ground',

    'PAETEC Park': 'Sahlen\'s Stadium',

    'Legion Stadium': 'Buck Hardee Field at Legion Stadium',
    'Silverbacks Park': 'Atlanta Silverbacks Park',
    'Soccorro Stadium': 'Socorro Stadium',

    'Invesco Field': 'Sports Authority Field at Mile High',
    'INVESCO Field': 'Sports Authority Field at Mile High',

    'Paul Angelo Russo Stadium Field': 'Paul Angelo Russo Stadium',

    'Estadio Juan Ramón Loubriel': 'Estadio Juan Ramon Loubriel',
    'Juan Ramon Loubriel Stadium': 'Estadio Juan Ramon Loubriel',
    'Juan Ramón Loubriel Stadium': 'Estadio Juan Ramon Loubriel',

    'Carl Lewis Field': 'Carl Lewis Track & Field Stadium',
    'Centre Claude-Robillard': 'Complexe Sportif Claude-Robillard',
    'Crew Stadium': 'Columbus Crew Stadium',
    'Stade Saputo': 'Saputo Stadium',
    'JELD-WEN Field': 'Jeld-Wen Field',
    'San Diego Stadium': 'Qualcomm Stadium',
    'Portland Civic Stadium': 'Jeld-Wen Field',
    'Civic Stadium': 'Jeld-Wen Field', # There's another Civic Stadium in Eugene, OR.
    'BC Place Stadium': 'BC Place',


    'Stade Gerland': 'Stade de Gerland',
    'Oakland-Alameda County Coliseum': 'Oakland Coliseum',
    'Estadio Sylvio Cator': 'Stade Sylvio Cator',
    'Estadío Sylvio Cator': 'Stade Sylvio Cator',
    'Estadío Silvio Cator': 'Stade Sylvio Cator',
    'Estadío Tropical': 'Estadio Pedro Marrero',
    
    'Sullivan Stadium': 'Foxboro Stadium',
    'Al Lang Stadium': 'Progress Energy Park',
    'Al Lang Field': 'Progress Energy Park',



    
    'Estadío Mateo Flores': 'Estadio Mateo Flores',
    'Estadio Ricardo Saprisa': 'Estadío Ricardo Saprissa', 
    'Azteca Stadium': 'Estadio Azteca',
    'Orange Bowl': 'Miami Orange Bowl',
    'The Polo Grounds': 'Polo Grounds',
    'Sparta Stadium': 'Sparta Field',
    'Marks Stadium': 'Mark\'s Stadium',
    'Dal-Hi Stadium': 'P.C. Cobb Stadium',
    'Gardner Park': 'Burnett Field',
    'Fair Park Stadium': 'Cotton Bowl',
    'Blue Valley Athletic Complex': 'Blue Valley Sports Complex',
    'Old Panther Stadium, Duncanville': 'Old Panther Field, Duncanville',
    'Chartiers Valley High School': 'Chartiers Valley Stadium',
    'Tacony Baseball Park': 'Tacony Baseball Grounds',
    'Soccorro Stadium': 'Socorro Stadium',
    'SAS Stadium': 'WakeMed Soccer Park',
    'National Sports Center': 'National Sports Center Stadium',
    'Husky Soccer Field': 'Husky Soccer Stadium',
    'PGE Park': 'JELD-WEN Field',
    'Home Depot Center Track': 'Home Depot Center Track & Field Stadium',
    'PAETEC Park': 'Sahlen\'s Stadium',
    'Marina Auto Stadium': 'Sahlen\'s Stadium',
    'Marina Auto Stadium, Rochester, NY': 'Sahlen\'s Stadium',
    'Nashville Coliseum': 'LP Field',
    'Alltel Stadium': 'EverBank Field',
    'Estadio Bella Vista': 'Estadio Bellavista',


    'Estadío Ricardo Saprissa': 'Estadio Ricardo Saprissa Aymá',
    'Freulinghausen Ave Grounds': 'Frelinghuysen Grounds',
    'Nuevo Estadio Corona': 'Estadio TSM Corona',
    'Big Arch Stadium': 'Busch Memorial Stadium',
    'Rutgers Stadium': 'High Point Solutions Stadium',

    'San Diego Sports Arena': 'Valley View Casino Center',
    'Bank One Ballpark': 'Chase Field',
    'Skelly Field': 'Skelly Field at H. A. Chapman Stadium',
    'Skelly Stadium': 'Skelly Field at H. A. Chapman Stadium',
    'Chapman Stadium': 'Skelly Field at H. A. Chapman Stadium',
    'NSC Stadium': 'National Sports Center Stadium',
    'Clark\'s Athletic Field': 'Clark\'s Field',
    'RFK Stadium': 'Robert F. Kennedy Memorial Stadium',
    'RFK Memorial Stadium': 'Robert F. Kennedy Memorial Stadium',
    'Robert F. Kennedy Stadium': 'Robert F. Kennedy Memorial Stadium',
    'R.F.K. Stadium': 'Robert F. Kennedy Memorial Stadium',
    'Robert F. Kennedy Memorial': 'Robert F. Kennedy Memorial Stadium',
    'Los Angeles Memorial Coliseum': 'Memorial Coliseum (Los Angeles)',
    'Yankee Stadium': 'Yankees Stadium',
    'JFK Stadium': 'John F. Kennedy Stadium',
    'Philadelphia Municipal Stadium':  'John F. Kennedy Stadium',
    'Pizza Hut Park': 'FC Dallas Stadium',
    'Hermann Stadium': 'Robert R. Hermann Stadium',
    'Community America Ballpark': 'CommunityAmerica Ballpark',
    'The Home Depot Center': 'Home Depot Center',
    'Jack Murphy Stadium': 'Qualcomm Stadium',
    'Schaefer Stadium': 'Foxboro Stadium',
    'Triborough Stadium': 'Downing Stadium',
    'Randall\'s Island Stadium': 'Downing Stadium',
    'Randall\s Island Stadium': 'Downing Stadium',
    'Randall\s Island': 'Downing Stadium',
    'Fedex Field': 'FedEx Field',
    'Qwest Field': 'CenturyLink Field',
    'Kezar Field': 'Kezar Stadium',
    'Tacony Ball Park': 'Tacony Baseball Grounds',
    'Bethlehem Steel Field': 'Steel Field',
    'ONT Grounds': 'Clark Field',
    'Clark\'s Athletic Field': 'Clark Field',
    'Eagle State Street Grounds': 'Eagle Street Grounds',
    'Frelinghuysen Avenue Grounds': 'Frelinghuysen Grounds',
    'Frelinghuysen Avenue Ground': 'Frelinghuysen Grounds',
    'East State St Grounds': 'East State Street Grounds',

    
}
sd.update(stadiums)


soccernet_errors = {
    'Rio Tinto Satadium': 'Rio Tinto Stadium',
    'AT&T; Park': 'AT&T Park',
    'LIVESTRONG Sporting Park': 'Livestrong Sporting Park',
    'JELD-WEN Park': 'Jeld-Wen Field',
    'Olímpico Universitario': 'Estadio Olímpico Universitario',
    'Tecnológico': 'Estadio Tecnológico',
    'Jorge Calero Suárez': 'Estadio Jorge Calero Suárez',
    'Nacional Tiburcio Carías Andino': 'Estadio Tiburcio Carías Andino',
    'Juan Ramón Loubriel': 'Estadio Juan Ramon Loubriel',
    'Saputo': 'Saputo Stadium',
    'Marvin Lee': 'Marvin Lee Stadium',
    'Estadio Corona': 'Estadio TSM Corona',
    'Hasely Crawford': 'Hasely Crawford Stadium',
    'Andrés Quintana Roo': 'Estadio Quintana Roo',
    'Complexe sportif Claude-Robillard': 'Complexe Sportif Claude-Robillard',
    'Estadio de la Ciudad de los Deportes, México DF': 'Estadio Azul',
}
sd.update(soccernet_errors)
    
