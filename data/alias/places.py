#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


def get_place(s):
    """
    Recursive. 
    """

    s = s.strip()
    if s in places:
        return get_place(places[s])
    else:
        return s


places = {
    
    'FIFA World Cup Stadium, Gelsenkirchen': 'Veltins-Arena', 
    'Estadío Tropical, Havana, Cuba': 'Estadio Pedro Marrero',
    'Tropical Stadium, Havana, Cuba': 'Estadio Pedro Marrero',
    'Estadío Olimpico, Mexico City': 'Estadio Olímpico Universitario',
    'Estadío Olimpica, Ciudad de México': 'Estadio Olímpico Universitario',
    'Baseball Stadium, Baltimore': 'Memorial Stadium Baltimore',
    'Estadío Universitario, Monterrey': 'Estadío Universitario de Monterrey',
    'Estadío Nacional, Tegucigalpa': 'Estadio Tiburcio Carías Andino',
    'Veteran\'s Stadium, New Britain, CT': 'New Britain Veterans Stadium',
    'Memorial Stadium, Seattle': 'Seattle High School Memorial Stadium',
    'Edinburg Field': 'Edinburg Stadium',
    'Empire Field Stadium': 'Empire Field',
    'JC Handly Park': 'JC Handley Park',
    'Celtic Park, Long Island, NY': 'Celtic Park, Queens, NY',
    'Cricket Club Grounds, Livingston, Staten Island, NY': 'Staten Island Cricket Grounds',
    'National Stadium (Olympic Stadium), Tokyo': 'National Olympic Stadium, Tokyo',
    'Maracanã - Estádio Jornalista Mário Filho, Rio De Janeiro': 'Estádio do Maracanã',
    'Pacaembu - Estádio Municipal Paulo Machado de Carv, Sao Paulo': 'Estádio do Pacaembu',
    'Morumbi - Estádio Cícero Pompeu de Toledo, Sao Paulo': 'Estádio do Morumbi',
    'Independencia, Belo Horizonte': 'Estádio Independência, Belo Horizonte',
    'Velodrome, Marseilles': 'Stade Vélodrome, Marseilles',
    'Olimpico, Rome': 'Stadio Olimpico, Rome, Italy',
    'Delle Alpi, Turin': 'Stadio delle Alpi',
    'Hillsborough, Sheffield': 'Hillsborough Stadium, Sheffield',

    'Compton Ave Park': 'Compton Avenue Park',
    'Capitoline Lake': 'Capitoline Grounds',
    'Trinidad': 'Trinidad and Tobago',
    'Cal State Fullerton': 'Titan Stadium, Fullerton, CA',
    'Richmond City Stadium': 'City Stadium, Richmond, VA',
    'USA': 'United States',


    
    'Layou, StVincent&amp;Grenadines': 'Layou, St. Vincent and Grenadines',
    'Los Angeles Memorial Coliseum': 'Memorial Coliseum, Los Angeles, CA',
    'Memorial Stadium Los Angeles': 'Memorial Coliseum, Los Angeles, CA',
    'Memorial Stadium, Long Beach, CA': 'Veterans Memorial Stadium, Long Beach, CA',

    'St. George Cricket Grounds, Hoboken': 'St. George\'s Cricket Grounds, Hoboken',

    'Southwestern College, San Diego, California': 'Southwestern College, Chula Vista, California',
    'Molson Stadium, Montreal': 'Percival Molson Memorial Stadium',
    'Olympic Park, Paterson': 'Olympic Field, Paterson',
    'Olympic Park, Paterson, NJ': 'Olympic Field, Paterson',
    'Island Stadium, Toronto': 'Hanlan\'s Point Stadium',

    'SAS Stadium, Cary, NC': 'WakeMed Soccer Park',
    'SAS Soccer Park, Cary, NC': 'WakeMed Soccer Park',



    'Dudley Stadium, El Paso, TX': 'Dudley Field',
    'Douglas Stadium, San Diego, CA': 'Merrill Douglas Stadium',
    'Santa Ana Bowl, Santa Ana, CA': 'Santa Ana Stadium',

    'Memorial Stadium, Seattle, WA': 'Memorial Stadium (Seattle), Seattle, WA',

    'Clark\'s Field, East Newark, NJ': 'Clark Field, Newark, NJ',
    'Clark\'s Field, Newark, NJ': 'Clark Field, Newark, NJ',

    'National Sports Center, Blaine, MN': 'National Sports Center Stadium',
    
}


states = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'FL': 'Florida',
    'HI': 'Hawaii',
    'GA': 'Georgia',
    'IA': 'Iowa',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'ON': 'Ontario',
    'OR': 'Oregon',
    'OK': 'Oklahoma',
    'PA': 'Pennsylvania',
    'QC': 'Quebec',
    'OH': 'Ohio',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tenneessee',
    'TX': 'Texas',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming',
    }
