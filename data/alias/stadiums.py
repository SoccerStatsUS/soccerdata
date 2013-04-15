#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

# This should only be used for
# 1. Stadiums with multiple names
# 2. Stadiums whose names are incorrect (externally)


def get_stadium(s):
    """
    Recursive. 
    """
    #print s

    s = s.strip()
    if type(s) == type(''):
        s = unicode(s, 'utf-8')

    if s in sd:
        return get_stadium(sd[s])
    else:
        return s

sd = {}

stadiums = {
    'Starfire Stadium': 'Starfire Sports Complex',
    'Maryland Soccerplex Stadium': 'Maryland SoccerPlex',
    'Yurcak Field Stadium': 'Yurcak Field',
    'Estadio Jardines del Hipodromo': 'Estadio Jardines Del Hipódromo',
    'Estadio Jardines Del Hipodromo': 'Estadio Jardines Del Hipódromo',
    'Casa Grande Soccer Complex': 'Grande Sports World',
    'Premier Sports Campus at Lakewood Ranch': 'Premier Sports Campus',
    'Bayamon Soccer Complex': 'Bayamón Soccer Complex',
    'Hal Sherbeck Field House': 'Sherbeck Field',
    'Hal Sherbeck Field': 'Sherbeck Field',
    'Ultimate Soccer Arena': 'Ultimate Soccer Arenas',
    'Collins Perley Sports Complex': 'Collins Perley Sports Center',
    'Estadio Presidente Juan Domingo Peron': 'Estadio Presidente Juan Domingo Perón',
    'Estadio Orlando Scarpelli': 'Estádio Orlando Scarpelli',
    'Estádio Major Antônio Couto Pereira': 'Estádio Couto Pereira',
    'Estadio do Governo do Estadio de Goias': 'Estádio Serra Dourada',
    'Estádio Metropolitano Roberto Santos': 'Estádio de Pituaçu',
    'Estadio Olimpico Monumental': 'Estádio Olímpico Monumental',
    'FFB Field': 'FFB Stadium',
    'Ernst Happel Stadium': 'Ernst-Happel-Stadion',
    'Durban Stadium': 'Moses Mabhida Stadium',
    'City Island Stadium': 'Skyline Sports Complex',
    'Chamartin Stadium': 'Estadio Chamartín',
    'Centenario Stadium': 'Estadio Centenario',
    'Cara McGrane Stadium': 'Cara McGrane Memorial Stadium',
    'Calder Stadium': 'Nathan Calder Stadium',
    'Cardinal Stadium': 'Benedetti–Wehrli Stadium',
    'Bruce Stadium': 'Canberra Stadium',
    'Aurora Stadium': 'York Park',
    'Al-Nuhayyan Stadium': 'Al Nahyan Stadium',
    'Albert/Daly Stadium': 'Albert-Daly Field',
    'Estadio Nacional Julio Martinez Pradanos': 'Estadio Nacional Julio Martínez Prádanos',
    'Ernst-Happel Stadion': 'Ernst-Happel-Stadion',
    'Estadio Rommel Fernandez': 'Estadio Rommel Fernández',
    'Kashima Stadium': 'Kashima Soccer Stadium',
    'Niigata Stadium Big Swan': 'Tohoku Electric Power Big Swan Stadium',
    'Stadium Espenmoos': 'Espenmoos',
    'Easter Road Stadium': 'Easter Road',
    'Libya National Stadium': 'June 11 Stadium',
    'Ratina Stadium': 'Tampere Stadium',
    'Na Stinadlech': 'Na Stínadlech',
    'ABSA Stadium': 'Kings Park Stadium',
    'A. Le Coq Stadium': 'A. Le Coq Arena',
    'Valeriy Lobanovskyi Stadium': 'Valeriy Lobanovskyi Dynamo Stadium',
    'Antalya Ataturk Stadyumu': 'Antalya Atatürk Stadium',
    'Sports Authority Field': 'Sports Authority Field at Mile High',
    'Khalifa Stadium': 'Khalifa International Stadium',
    'UBC Thunderbird Stadium': 'Thunderbird Stadium',
    'Estadio Olimpico (Caracas FC)': 'Estadio Olímpico de la UCV',
    'Bayamon FC Soccer Complex': 'Bayamon Soccer Complex',
    'Hubert H. Humphrey Metrodome': 'Metrodome',
    'Balboa Park Stadium': 'Boxer Stadium',
    'UBC Thunderbird Stadium': 'Thunderbird Stadium',
    'Montclair St. University': 'Montclair State University',

    'Foothills Park': 'Foothills Stadium',
    'Atlanta Stadium': 'Atlanta-Fulton County Stadium',
    'Hanson Park': 'Hanson Stadium',
    'Rancho La Cienega Stadium': 'Rancho La Cienga Stadium',
    'Estadio Leon': 'Estadio León',
    'Estadio Cicero Pompeu de Toledo': 'Estádio do Morumbi',
    'Engenhao': 'Estádio Olímpico João Havelange',
    'Estadio Libertadores de America': 'Estadio Libertadores de América',
    'Estadio Ciudad de Cumana': 'Estadio Ciudad de Cumaná',
    'Estadio Parque El Teniente': 'Estadio El Teniente',
    'Estadio Gran Parque Central': 'Gran Parque Central',
    'Estadio Olimpico Joao Havelange': 'Estádio Olímpico João Havelange',
    'Estadio Juan Domingo': 'Estadio Presidente Juan Domingo Perón',
    'Palacio Duco': 'Estadio Tomás Adolfo Ducó',
    'Pacaembu Stadium': 'Estádio do Pacaembu',
    'Estadio Urbano Caldeira': 'Estádio Urbano Caldeira',
    'Estadio Nacional Julio Martinez Pradanos': 'Estadio Nacional Julio Martínez Prádanos',
    'Estadio Municipal Paulo Machado de Carvalho': 'Estádio do Pacaembu',
    'La Bombonera': 'Estadio Alberto J. Armando',
    'Estadio Ciudad de Lanus': 'Estadio Ciudad de Lanús',
    'Estadio Victor Agustin Ugarte': 'Estadio Víctor Agustín Ugarte',
    'Estadio Jose Pinheiro Borda': 'Estádio Beira-Rio',
    'Estadio Dr. Nicolas Leoz': 'Estadio Dr. Nicolás Leoz',
    'Arena do Gremio': 'Arena do Grêmio',
    'Estadio Jose Antonio Anzoategui': 'Estadio José Antonio Anzoátegui',
    'Estadio do Morumbi': 'Estádio do Morumbi',
    'Estadio Jose Dellagiovanna': 'Estadio José Dellagiovanna',
    'Truman Bodden Stadium': 'Truman Bodden Sports Complex',
    'Ergilio Hato Stadium': 'Stadion Ergilio Hato',
    'Estadio Mane Garrincha': 'Estádio Nacional de Brasília',
    'Estádio Nacional de Brasília': 'Estadio Nacional de Brasilia',
    'Estadio Agustin Tovar': 'Estadio Agustín Tovar',
    'Estadio La Carolina': 'Estadio Agustín Tovar',
    'Estadio Brigido Irarte': 'Estadio Brígido Iriarte',
    'Estadio Nacional de Chile': 'Estadio Nacional Julio Martínez Prádanos',
    'Estadio Nacional Julio Martinez': 'Estadio Nacional Julio Martínez Prádanos',
    'Estadio Monumental Antonio Vespuci Liberti': 'Estadio Monumental Antonio Vespucio Liberti',
    'Estadio Polideportivo Cachamay': 'Polideportivo Cachamay',
    'Estadio Mane Garrincha': 'Estádio Nacional de Brasília',
    'River Plate Stadium': 'Estadio Monumental Antonio Vespucio Liberti',
    'Estadio Olimpico do Para': 'Mangueirão',
    'Estádio Olímpico do Pará': 'Mangueirão',
    'Mangueirao': 'Mangueirão',
    'Estadio Rei Pele': 'Estádio Rei Pelé',
    'Estadio Morumbi': 'Estádio do Morumbi',
    'Estadio Monumental U': 'Estadio Monumental "U"',
    'Estádio Vivaldo Lima': 'Vivaldão',
    'Vivaldao': 'Vivaldão',
    'Estadio Beira-Rio': 'Estádio Beira-Rio',
    'Estadio Governador Joao Castelo': 'Estádio Governador João Castelo',
    'Estadio Couto Pereira': 'Estádio Couto Pereira',
    'Estadio Casa Blanca': 'Estadio de Liga Deportiva Universitaria',
    'Estadio Luis Loreto Lira': 'Estadio José Alberto Pérez',
    'Estadio do Arruba': 'Estádio do Arruda',
    'Estadío Ramón Aguilera': 'Estadio Ramón Tahuichi Aguilera',
    'Estadio Ramon Tahuichi Aguilera': 'Estadio Ramón Tahuichi Aguilera',
    'Estadio Defensores Del Chaco': 'Estadio Defensores del Chaco',
    'Estadio de los Defensores del Chaco': 'Estadio Defensores del Chaco',
    'Estadio Parque Antartica': 'Estádio Parque Antarctica',
    'Estadío Independencia': 'Estádio Independência',
    'Estadio Independencia': 'Estádio Independência',
    'Estadio Olimpico (Caracas)': 'Estadio Olímpico de la UCV',
    'Estadio Olimpico de CU': 'Estadio Olímpico Universitario',
    'Estádio Monumental David Arellano': 'Estadio Monumental David Arellano',

    'Estadio Vila Belmiro': 'Estádio Urbano Caldeira',
    'Estadio Municipal de Concepcion': 'Estadio Municipal de Concepción',
    'Estadio Feliciano Caceres': 'Estadio Feliciano Cáceres',
    'Estadio Metropolitano Roberto Melendez': 'Estadio Metropolitano Roberto Meléndez',
    'Estadio Olimpico Luis Ramos': 'Estadio José Antonio Anzoátegui',
    'Andre Kamperveen Stadion': 'André Kamperveen Stadion',
    'Andre Kamperveen Stadium': 'André Kamperveen Stadion',
    'Waterford National Stadium': 'Barbados National Stadium',
    'Kingston National Stadium': 'Jamaica National Stadium',
    #'Kasarani Stadium': 'Moi International Sports Centre',
    'Estadio Olimpico Juan Pablo Duarte': 'Estadio Olímpico Félix Sánchez',
    'Supachalasai Stadium': 'Thailand National Stadium',
    'Sangam Stadium': 'Seoul World Cup Stadium',

    'AO Shirley Recreational Grounds': 'A.O. Shirley Recreation Ground',
    'Arnos Vale Ground': 'Arnos Vale Stadium',
    'Loftus Road Stadium': 'Loftus Road',
    'Arnold Schwarzenegger Stadion': 'UPC-Arena',
    'Centro Epsortivo Miecimo da Silva': 'Centro Esportivo Miécimo da Silva',
    'Estadio General Severiano': 'Estádio de General Severiano',
    'Estadio General Severiano': 'Estádio General Severiano',
    'Estadio Morumbi': 'Estádio do Morumbi',
    'Estadio Parque do Sabia': 'Estádio Parque do Sabiá',
    'General Artigas Stadium': 'Estadio Parque Artigas',
    'Estadio Olimpico Patria': 'Estadio Olímpico Patria',
    'Estadio Monumental Rio Parapiti': 'Monumental Río Parapití',
    'Estadio Pascual Guerrero': 'Estadio Olímpico Pascual Guerrero',
    'Estadio Hernan Ramirez Villegas': 'Estadio Hernán Ramírez Villegas',
    'Estadio Elias Aguirre': 'Estadio Elías Aguirre',
    'Estadio Olimpico de la UCV': 'Estadio Olímpico de la UCV',
    'Estadio Ciudad de la Plata': 'Estadio Ciudad de La Plata',
    'Estadio Brigido Iriarte': 'Estadio Brígido Iriarte',
    'Estadio Camilo Cichero': 'Estadio Alberto J. Armando',
    'Estadio Ramon Aguilera': 'Estadio Ramón Tahuichi Aguilera',
    'Estadio Olimpico Atahualpa': 'Estadio Olímpico Atahualpa',
    'Estadio Playa Ancha': 'Estadio Elías Figueroa Brander',
    'Estadio do Arruda': 'Estádio do Arruda',
    'Estadio Fonte Nova': 'Estádio Fonte Nova',
    'Estadio Serra Dourada': 'Estádio Serra Dourada',
    'Estadio Olimpico Chateau Carreras': 'Estadio Mario Alberto Kempes',
    'Estadio Pascual Guerrero': 'Estadio Olímpico Pascual Guerrero',
    'Estadio Arequipa': 'Estadio Monumental Virgen de Chapi',
    'Estadio La Bombonera': 'Estadio Alberto J. Armando',

    'Estadio Metropolitano de Futbol de Lara': 'Estadio Metropolitano de Fútbol de Lara',
    'Estadio Monumental de Maturin': 'Estadio Monumental de Maturín',
    'Estadio Jose Pachencho Romero': 'Estadio José Pachencho Romero',
    'Estadio Jose Panchencho Romero': 'Estadio José Pachencho Romero',
    'Estadio Jose Panchenco Romero': 'Estadio José Pachencho Romero',
    'Estadio Jose Pachenco Romero': 'Estadio José Pachencho Romero',
    'Estadio Metropolitano de Merida': 'Estadio Metropolitano de Mérida',
    'Estadio del Bicentenario, San Juan, Argentina': 'Estadio San Juan del Bicentenario',
    'Estadio Brigadier General Estanislao Lopez': 'Estadio Brigadier General Estanislao López',
    'Estadio Jesus Bermudez': 'Estadio Jesús Bermúdez',
    'Mineirao': 'Mineirão',
    'Estadio Mineirao': 'Mineirão',
    'Estadio Felix Capriles': 'Estadio Félix Capriles',
    'Estadio Modelo': 'Estadio Modelo Alberto Spencer Herrera',
    'Estadio Monumental de Nunez': 'Estadio Monumental Antonio Vespucio Liberti',
    'Estadio Sao Januario': 'Estádio São Januário',
    'Sportivo Barracas Stadium': 'Estadio Sportivo Barracas',
    'Estadio Gasometro': 'Estadio Gasómetro',
    'Estadio Sport de Nunoa': 'Estadio Campos de Sports de Ñuñoa',
    'Stadío das Laranjeiras': 'Estádio das Laranjeiras',
    'Estadio das Laranjeiras': 'Estádio das Laranjeiras',
    'Giuseppe Meazza': 'San Siro',
    'Renato Dall Ara': 'Stadio Renato Dall\'Ara',
    'Sant Elia': 'Stadio Sant\'Elia',
    'Friuli': 'Stadio Friuli',
    'Geoffrey Prichard Stadium': 'Stade Geoffroy-Guichard',
    'Felix Bollaert': 'Stade Félix-Bollaert',

    'Marc Antonio Bentegodi': 'Stadio Marc\'Antonio Bentegodi',
    'Stade Chapou': 'Stade Municipal de Toulouse',
    'Stade Olympique de Colombes': 'Stade Olympique Yves-du-Manoir',
    'Velodrome Municipal': 'Stade Vélodrome',
    'Stadio Comunale': 'Stadio Artemio Franchi',
    'Comunale': 'Stadio Artemio Franchi',
    'Giovanni Berta': 'Stadio Artemio Franchi',
    'Estadio do Pacaembu': 'Estádio do Pacaembu',
    'Maracana': 'Estádio do Maracanã',
    'Estadio do Maracana': 'Estádio do Maracanã',
    'Estadio Ilha do Retiro': 'Estádio Ilha do Retiro',
    'Estadio Durival Britto': 'Estádio Vila Capanema',
    'Estádio Durival Britto e Silva': 'Estádio Vila Capanema',
    'Estadio Jose Maria Minella': 'Estadio José María Minella',
    'Estadio Chateau Carreras': 'Estadio Mario Alberto Kempes',

    'Karaiskaki': 'Karaiskakis Stadium',
    'City of Coventry Stadium': 'Ricoh Arena',
    'Latrobe City Stadium': 'LaTrobe City Stadium',
    'WIN Jubilee Oval': 'Jubilee Oval',
    'Jose Zorrilla': 'Estadio Nuevo José Zorrilla',
    'Benito Villamarin': 'Estadio Benito Villamarín',
    'Patersons Stadium': 'Subiaco Oval',
    'Allianz Stadium': 'Sydney Football Stadium',
    'Hunter Stadium': 'Newcastle International Sports Centre',
    'Ausgrid Stadium': 'Newcastle International Sports Centre',
    'AAMI Park': 'Melbourne Rectangular Stadium',
    'Bluetongue Stadium': 'Central Coast Stadium',
    'Skilled Park': 'Robina Stadium',
    'Dairy Farmers Stadium': 'Willows Sports Complex',
    'Melbourne Etihad Stadium': 'Docklands Stadium',
    'Telstra Dome': 'Docklands Stadium',
    'nib Stadium': 'Perth Oval',
    'Members Equity Stadium': 'Perth Oval',
    'ME Bank Stadium': 'Perth Oval',
    'Aussie Stadium': 'Sydney Football Stadium',
    'EnergyAustralia Stadium': 'Newcastle International Sports Centre',
    'Lang Park': 'Suncorp Stadium',
    'Stadio Ardenza': 'Stadio Armando Picchi',
    'Stadio Fuorigrotta': 'Stadio San Paolo',
    'Mitsuzawa Stadium': 'Nippatsu Mitsuzawa Stadium',
    'Komazawa Stadium': 'Komazawa Olympic Park Stadium',
    'Chichibu Stadium': 'Chichibunomiya Rugby Stadium',
    'Nova Creu Alta Stadium': 'Estadi de la Nova Creu Alta',
    'La Romereda Stadium': 'La Romareda',
    'Luis Casanova': 'Estadio de Mestalla',
    'Sarria': 'Estadi de Sarrià',
    'Luis Casanova Stadium': 'Estadio de Mestalla',
    'Pershing Park': 'Stade Pershing',
    'Nou Camp Stadium': 'Camp Nou',
    'Velodrome de Vincennes': 'Vélodrome de Vincennes',
    'Olympisch': 'Amsterdam Olympic Stadium',
    'Olympia Stadion': 'Olympiastadion',
    'Highbury': 'Arsenal Stadium',
    'Pallokenttä': 'Töölön Pallokenttä',
    'Olympic Park': 'Olympic Park Stadium',
    'Jalisco Stadium': 'Estadío Jalisco',

    'easyCredit-Stadion': 'Frankenstadion',
    'Munsu Stadium': 'Ulsan Munsu Football Stadium',
    'Suwon Stadium': 'Suwon World Cup Stadium',
    'Daejeon Stadium': 'Daejeon World Cup Stadium',
    'Munsu Football Stadium': 'Ulsan Munsu Football Stadium',
    'Ellis Park': 'Ellis Park Stadium',
    'Loftus Versfeld': 'Loftus Versfeld Stadium',
    'Queens Park Oval': 'Queen\'s Park Oval',
    'Estadio Nacional (Lima)': 'Estadio Nacional de Peru',
    'Estadio Nacional (Peru)': 'Estadio Nacional de Peru',

    'Estadío Francisco Morazán': 'Estadio Francisco Morazán',
    'Estadio El Campin': 'Estadio El Campín',
    'Restelo Stadium': 'Estádio do Restelo',
    'B.C. Place': 'BC Place',
    'Estadio Nacional de Tegucigalpa': 'Estadio Tiburcio Carías Andino',
    'Tegucigalpa Estadío Nacional': 'Estadio Tiburcio Carías Andino',
    'Estadio Tiburcio Carias Andino': 'Estadio Tiburcio Carías Andino',
    'Estadio Nacional Tiburcio Carias': 'Estadio Tiburcio Carías Andino',
    'Maksimir Stadion': 'Stadion Maksimir',
    'Estadio Zorilla': 'Estadio Nuevo José Zorrilla',
    'Tokyo National Stadium': 'Tokyo National Olympic Stadium',
    'Tynecastle Park': 'Tynecastle Stadium',
    'Ibrox Park': 'Ibrox Stadium',
    'Trent Bridge Ground': 'Trent Bridge',
    'Kennington Oval': 'The Oval',

    'Bislet Stadium': 'Bislett Stadion',
    'Fulton County Stadium': 'Atlanta-Fulton County Stadium',
    'Seattle Memorial Stadium': 'Seattle High School Memorial Stadium',
    'Allmend Stadium': 'Stadion Allmend',
    'Soccer and Sports Center': 'Kuntz Stadium',
    

    'Stade Municipal en Camee': 'Stade Alfred Marie-Jeanne',
    'Stade Municipal Pierre-Aliker': 'Stade Pierre-Aliker',
    'Estadio Excelsior': 'Estadio Excélsior',
    'Estadío Cuscatlán': 'Estadio Cuscatlán',
    'Estadio Cuscatlan': 'Estadio Cuscatlán',

    'Nep Stadium': 'Nepstadion',
    'Willow Memorial Park Stadium': 'New Britain Veterans Stadium',
    'Willowbrook Memorial Park': 'New Britain Veterans Stadium',
    'Estadio Jalisco': 'Estadío Jalisco',
    'Tuo Dong Stadium': 'Kunming Tuodong Sports Center',
    'New York Indiana Oval': 'New York Oval',

    
    'Estadio Alejandro Morera Soto': 'Estadío Alejandro Morera Soto',
    'Tony Glavin Complex': 'Tony Glavin Soccer Complex',

    'Texas A&M Intl Univ Soccer Complex': 'TAMIU Soccer Complex',
    'WoodForest Stadium': 'Woodforest Bank Stadium',
    'Memorial Stadium (Seattle)': 'Seattle Memorial Stadium',
    'Crescent Grounds': 'Crescent Athletic Club Grounds',
    'Soldiers Field': 'Harvard Stadium',
    'Soldier\'s Field': 'Harvard Stadium',
    'Staten Island Cricket Club Grounds': 'Staten Island Cricket Grounds',
    'Macomb\'s Dam Park': 'Macombs Dam Park',
    'Montreal Stade Saputo': 'Stade Saputo',
    'Maryland Soccerplex': 'Maryland SoccerPlex',
    'Maryland Soccer Plex': 'Maryland SoccerPlex',
    'RSL Training Field': 'America First Field',
    #'Kino Veterans Memorial Stadium': 'Kino Veterans Memorial Stadium',
    'Kino Sports Complex': 'Kino Veterans Memorial Stadium',

    'Estadio Nacional Mateo Flores': 'Estadio Mateo Flores',
    'Estadio Mateo Flores': 'Estadío Mateo Flores',
    'A.J. Siemon Stadium': 'A.J. Simeon Stadium',

    'Estadio Andres Quintana Roo': 'Estadio Quintana Roo',
    'Estadio Agustin Muquita Sanchez': 'Estadio Agustín Sánchez',
    'Estadio Agustin Sanchez': 'Estadio Agustín Sánchez',
    'Estadio Armando Dely Valdes': 'Estadio Armando Dely Valdés',
    'Estadio Nemesio Diez': 'Estadio Nemesio Díez',

    'Estadio Olimpico Universitario': 'Estadio Olímpico Universitario',
    'Estadio Tecnologico': 'Estadio Tecnológico',
    'Estadio Francisco Morazan': 'Estadio Francisco Morazán',

    'Estadio Olimpico Metropolitano': 'Estadio Olímpico Metropolitano',
    'Estadio Jorge Calero Suarez': 'Estadio Jorge Calero Suárez',
    'DSG Park': 'Dick\'s Sporting Goods Park',
    'Lehigh Stadium': 'Taylor Field',
    'Livestrong Sporting Park': 'Sporting Kansas City Park',
    'Starfire Complex': 'Starfire Sports Complex',
    'Rochester Rhinos Stadium': 'Sahlen\'s Stadium',
    'RE/MAX Greater Atlanta Stadium': 'Atlanta Silverbacks Park',
    'Silverbacks Stadium': 'Atlanta Silverbacks Park',
    'Cal State Fullerton Titan Stadium': 'Titan Stadium',
    'Fullerton Stadium': 'Titan Stadium',


    'Legion Sports Complex': 'Legion Stadium',
    'Krenzler Stadium': 'Krenzler Field',
    'Belson Stadium (St. John\'s University)': 'Belson Stadium',
    'Citibank Park': 'Bethpage Ballpark',
    'Stony Brook University Stadium': 'Kenneth P. LaValle Stadium',
    'Peter Johansen Stadium': 'Peter Johansen High School Stadium',
    'Collins-Perley Sports Complex': 'Collins Perley Sports Center',
    'Consol Energy Park': 'Falconi Field',
    '110th & 8th Ave Park': '110th and 8th Ave Park',
    'Ridgewood Baseball Park': 'Ridgewood Baseball Grounds',
    'North Ends Field': 'North Ends Grounds',
    'ONT AA Grounds': 'Clark ONT Field',
    'Clark Field': 'Clark ONT Field',
    'Wanderers Park': 'Wanderers Grounds',
    'East End Grounds': 'East End Park',
    'Visitation Oval': 'Visitation Park',
    'Harlem Field': 'Harlem Oval',
    'Walsh Stadium': 'Walsh Memorial Stadium',

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
    'Estadio dos Eucaliptos': 'Estádio dos Eucaliptos',
    'Roker Park Ground': 'Roker Park',
    'White City': 'White City Stadium',
    'Parc Lescure': 'Stade Chaban-Delmas',
    'La Corregidora': 'Estadio Corregidora',
    'Neza': 'Estadio Neza 86',
    'Tecnologico': 'Estadio Tecnológico',
    'Azteca': 'Estadio Azteca',
    'Jalisco': 'Estadio Jalisco',
    'Cuauhtemoc': 'Estadio Cuauhtémoc',
    
    'Estadío Cuauhtémoc': 'Estadio Cuauhtémoc',
    'Cuauhtemoc Stadium': 'Estadío Cuauhtémoc',
    'Estadio Cuauhtemoc': 'Estadio Cuauhtémoc',
    'Gerland': 'Stade de Gerland',
    'St. George Cricket Grounds': 'St. George\'s Cricket Grounds',
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
    'Estadio Centenario': 'Estadío Centenario',
    'King Baudouin Stadium': 'Stade Roi Baudouin',
    'Estadío Parque Espana': 'Parque Espana',
    'Pontiac Silverdome': 'Silverdome',
    'Las Vegas Stadium': 'Sam Boyd Stadium',
    'Atlanta Fulton County Stadium': 'Atlanta-Fulton County Stadium',
    'Aquinas Stadium': 'Holleder Memorial Stadium',
    'Robert F. Kennedy Stadium': 'Robert F. Kennedy Memorial Stadium',
    'Edinboro University Stadium': 'Sox Harrison Stadium',
    'Middlefield Cheese Stadium (Bedford)': 'Middlefield Cheese Stadium',
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
    'Claude Robillard Sports Complex': 'Complexe Sportif Claude-Robillard',
    'Centennial Stadium': 'Centennial Park Stadium',
    'Seahawks Stadium': 'CenturyLink Field',
    'P & C Stadium': 'Alliance Bank Stadium',
    'Uihlein Park': 'Uihlein Soccer Park',
    'Kuntz Memorial Stadium': 'Kuntz Stadium',
    'Crew Stadium': 'Columbus Crew Stadium',
    'Stade Saputo': 'Saputo Stadium',
    'JELD-WEN Field': 'Jeld-Wen Field',
    'San Diego Stadium': 'Qualcomm Stadium',
    'Portland Civic Stadium': 'Jeld-Wen Field',
    'Civic Stadium': 'Jeld-Wen Field', # There's another Civic Stadium in Eugene, OR.
    'BC Place Stadium': 'BC Place',


    'Stade Gerland': 'Stade de Gerland',
    'Oakland-Alameda County Coliseum': 'Oakland Coliseum',

    u'Estadío Sylvio Cator': 'Stade Sylvio Cator',
    u'Estadío Silvio Cator': 'Stade Sylvio Cator',
    u'Estadio Sylvio Cator': 'Stade Sylvio Cator',
    u'Sylvio Cator Stadium': 'Stade Sylvio Cator',

    'Estadío Tropical': 'Estadio Pedro Marrero',
    
    'Sun Bowl (UTEP)': 'Sun Bowl Stadium',
    'Sullivan Stadium': 'Foxboro Stadium',
    'Al Lang Stadium': 'Progress Energy Park',
    'Al Lang Field': 'Progress Energy Park',




    'Estadio Ricardo Saprisa': 'Estadio Ricardo Saprissa', 
    'Estadio Ricardo Saprissa Aymá': 'Estadio Ricardo Saprissa',
    'Estadio Saprissa': 'Estadio Ricardo Saprissa',
    'Azteca Stadium': 'Estadio Azteca',
    'Orange Bowl': 'Miami Orange Bowl',
    'The Polo Grounds': 'Polo Grounds',
    'Capitoline Lake': 'Capitoline Grounds',
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
    'SAS Soccer Park': 'WakeMed Soccer Park',
    'adidas Field at Pizza Hut Park': 'adidas Field',
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
    'Los Angeles Coliseum': 'Memorial Coliseum (Los Angeles)',
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
    
