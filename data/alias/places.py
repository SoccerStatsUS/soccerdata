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

cities = {


    'Newport Beach , California': 'Newport Beach, California',
    'Rio De Janeiro, Brazil': 'Rio de Janeiro, Brazil',
    'Sao Paulo, Brazil': 'São Paulo, Brazil',
    'Medellin, Colombia': 'Medellín, Colombia',
    'Washington DC': 'Washington, D.C.',
    'Washington, DC': 'Washington, D.C.',
    'Washington D.C.': 'Washington, D.C.',
    'Kearny NJ': 'Kearny, New Jersey',
    'Kearny, N.J.': 'Kearny, New Jersey',
    'holland': 'Holland',
    'New York, N.Y.': 'New York, New York',
    'San José, California': 'San Jose, California',
    'San Jose, Costa Rica': 'San José, Costa Rica',
    
    'Miami': 'Miami, FL',
    'Denver': 'Denver, CO',
    'Boston': 'Boston, MA',
    'Montreal': 'Montreal, Quebec',
    'Montreal, Canada': 'Montreal, Quebec',
    'San Francisco': 'San Francisco, CA',
    'Tampa Bay': 'Tampa Bay, FL',
    'Tampa, FL': 'Tampa Bay, FL',
    'Fort Lauderdale': 'Fort Lauderdale, FL',
    'Fort Worth': 'Fort Worth, TX',
}

places = {
    'Layou, StVincent&amp;Grenadines': 'Layou, St. Vincent and Grenadines',
    'Dal-Hi Stadium': 'P.C. Cobb Stadium',
    'Gardner Park, Dallas': 'Burnett Field, Dallas',
    'Fair Park Stadium': 'Cotton Bowl',

    
    'Blue Valley Athletic Complex': 'Blue Valley Sports Complex',
    'Old Panther Stadium, Duncanville': 'Old Panther Field, Duncanville',
    'Chartiers Valley High School': 'Chartiers Valley Stadium',
    'Tacony Baseball Park': 'Tacony Baseball Grounds',
    'St. George Cricket Grounds, Hoboken': 'St. George\'s Cricket Grounds, Hoboken',


    'Southwestern College, San Diego, California': 'Southwestern College, Chula Vista, California',
    'Molson Stadium, Montreal': 'Percival Molson Memorial Stadium',
    'Olympic Park, Paterson': 'Olympic Field, Paterson',
    'Olympic Park, Paterson, NJ': 'Olympic Field, Paterson',
    'Island Stadium, Toronto': 'Hanlan\'s Point Stadium',
    'Soccorro Stadium, El Paso, TX': 'Socorro Stadium, El Paso, TX',
    'Soccorro Stadium': 'Socorro Stadium',
    'SAS Stadium, Cary, NC': 'WakeMed Soccer Park',
    'SAS Soccer Park, Cary, NC': 'WakeMed Soccer Park',
    'SAS Stadium': 'WakeMed Soccer Park',
    'Seahawk Stadium, Seattle, WA': 'CenturyLink Field',
    'PAETEC Park': 'Sahlen\'s Stadium',
    'PAETEC Park, Rochester, NY': 'Sahlen\'s Stadium',
    'Marina Auto Stadium': 'Sahlen\'s Stadium',
    'Marina Auto Stadium, Rochester, NY': 'Sahlen\'s Stadium',
    'Home Depot Center Track': 'Home Depot Center Track & Field Stadium',
    'Legion Stadium, Wilmington, NC': 'Buck Hardee Field at Legion Stadium',
    'Silverbacks Park, Chamblee, GA': 'Atlanta Silverbacks Park',
    'PGE Park': 'Jeld-Wen Field',
    'Husky Soccer Field': 'Husky Soccer Stadium',
    'Dudley Stadium, El Paso, TX': 'Dudley Field',
    'Douglas Stadium, San Diego, CA': 'Merrill Douglas Stadium',
    'Santa Ana Bowl, Santa Ana, CA': 'Santa Ana Stadium',

    'Memorial Stadium, Seattle, WA': 'Memorial Stadium (Seattle), Seattle, WA',

    'Clark\'s Field, East Newark, NJ': 'Clark Field, Newark, NJ',
    'Clark\'s Field, Newark, NJ': 'Clark Field, Newark, NJ',
    

    'National Sports Center': 'National Sports Center Stadium',
    'National Sports Center, Blaine, MN': 'National Sports Center Stadium',
    'Montreal, QUE': 'Montreal',
    'Montreal, Que': 'Montreal',

}

places.update(cities)

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
