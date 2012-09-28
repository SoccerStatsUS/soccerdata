#!/usr/local/bin/env python
# -*- coding: utf-8 -*-




def get_city(s):

    s = s.strip()
    if s in cities:
        return get_city(cities[s])
    else:
        return s
    


cities = {
    'Kristiana, Norway': 'Oslo, Norway',
    'Rio de Janeiro': 'Rio de Janeiro, Brazil',
    'Rome': 'Rome, Italy',
    'Glasgow': 'Glasgow, Scotland',

    'Montreal, QUE': 'Montreal',
    'Montreal, Que': 'Montreal',
    'Toronto, Canada': 'Toronto',
    'Ottawa, Canada': 'Ottawa',
    'Quebec, Canada': 'Quebec',
    'Havana': 'Havana, Cuba',
    'La Habana': 'Havana, Cuba',
    'Tegucigalpa': 'Tegucigalpa, Honduras',
    'San Pedro Sula': 'San Pedro Sula, Honduras',
    'Paramaribo': 'Paramaribo, Suriname',
    'Antigua': 'Antigua, Antigua and Barbuda',
    'Las Vegas': 'Las Vegas, NV',
    
    
   

    'Port-of-Spain, Trinidad & Tobago': 'Port of Spain, Trinidad and Tobago',
    'Port of Spain, Trinidad & Tobago': 'Port of Spain, Trinidad and Tobago',
    'Port of Spain, Trinidad & Tobago': 'Port of Spain, Trinidad and Tobago',
    'Port of Spain, Trinidad': 'Port of Spain, Trinidad and Tobago',
    'Port of Spain': 'Port of Spain, Trinidad and Tobago',
    'Mexico City, MX': 'Mexico City, Mexico',
    'Mexico City': 'Mexico City, Mexico',
    'Ciudad de México': 'Mexico City, Mexico',
    'Ciudad de México': 'Mexico City, Mexico',



    'Port-au-Prince': 'Port-au-Prince, Haiti',
    'Quito': 'Quito, Ecuador',
    'Riyadh': 'Riyadh, Saudi Arabia',
    'Reykjavik': 'Reykjavik, Iceland',
    'Guadalajara': 'Guadalajara, Mexico',
    'Vienna': 'Vienna, Austria',
    'Marrakech': 'Marrakech, Morocco',
    
    
    'Curitiba': 'Curitiba, Brazil',
    'Belo Horizonte': 'Belo Horizonte, Brazil',
    'Recife': 'Recife, Brazil',
    'Florence': 'Florence, Italy',
    'Nantes': 'Nantes, France',
    'Ljubljana': 'Ljubljana, Slovenia',
    'Brussels': 'Brussels, Belgium',
    
    'Warsaw': 'Warsaw, Poland',
    'Anaheim': 'Anaheim, CA',
    'Paris': 'Paris, France',
    'Philadelphia, Pa.': 'Philadelphia, PA',
    'Germantown, Pa.': 'Germantown, PA',
    'Brooklyn': 'Brooklyn, NY',
    'Philadelphia': 'Phialdelphia, PA',
    'St. Louis': 'St. Louis, MO',
    'Seattle': 'Seattle, WA',
    'Chicago': 'Chicago, IL',
    'San Diego': 'San Diego, CA',
    'Tulsa': 'Tulsa, OK',
    'Rochester': 'Rochester, NY',
    'Cincinnati': 'Cincinnati, OH',
    'Trenton': 'Trenton, NJ',
    'Newark': 'Newark, NJ',
    'Baltimore': 'Baltimore, MD',
    'Toronto': 'Toronto, ON',
    'Jersey City': 'Jersey City, NJ',

    'Jersey City, N.J.': 'Jersey City, NJ',
    'Bethlehem': 'Bethlehem, PA',
    'Bayonne': 'Bayonne, NJ',
    'New York, New York': 'New York, NY',
    'New York': 'New York, NY',
    'New York City': 'New York, NY',
    'East Newark': 'East Newark, NJ',
    'Montevideo': 'Montevideo, Uruguay',
    'Foxboro, MA': 'Foxborough, MA',
    'Oakland': 'Oakland, CA',
    'Pasadena': 'Pasadena, CA',
    'Tokyo': 'Tokyo, Japan',
    

    

    'Boras': 'Borås, Sweden',
    'Malmo': 'Malmö, Sweden',
    'Stockholm': 'Stockholm, Sweden',
    'Copenhagen': 'Copenhagen, Denmark',
    'Gavle': 'Gävle, Sweden',
    'Helsinburg': 'Helsingborg, Sweden',
    'Helsinborg': 'Helsingborg, Sweden',
    'Gothenburg': 'Gothenburg, Sweden',
    'Gothenborg': 'Gothenburg, Sweden',
    'Norrkoping': 'Norrköping, Sweden',
    'Dusseldorf': 'Dusseldorf, Germany',
    'Frankfurt': 'Frankfurt, Germany',
    'Edinburgh': 'Edinburgh, Scotland',    

    
    'Dublin': 'Dublin, Ireland',
    'Amsterdam': 'Amsterdam, Netherlands',
    'Amsterdam, Holland': 'Amsterdam, Netherlands',
    'Bogota': 'Bogota, Colombia',
    'Breskens, Holland': 'Breskens, Netherlands',
    'Budapest': 'Budapest, Hungary',
    'Cairo': 'Cairo, Egypt',
    'Calcutta': 'Calcutta, India',
    'Calbary': 'Calgary, AB',
    'Calbary, Alb': 'Calgary, AB',
    'Caracas': 'Caracas, Venezuela',

    'Edmonton': 'Edmonton, AB',
    'Ciudad de Guatemala': 'Guatemala City, Guatemala',
    
    'Vancouver': 'Vancouver, BC',
    'Montreal': 'Montreal, QC',
    'New Bedford': 'New Bedford, MA',
    'Pawtucket': 'Pawtucket, RI',
    'Providence': 'Providence, RI',
    'London': 'London, England',
    'Cleveland': 'Cleveland, OH',
    'Toronto': 'Toronto, ON',
    'Worcester': 'Worcester, MA',
    'Winnipeg': 'Winnipeg, MB',
    'Detroit': 'Detroit, MI',
    'Bronx': 'Bronx, NY',
    'Kearny': 'Kearny, NJ',
    'Dallas': 'Dallas, TX',
    'Ft. Lauderdale': 'Fort Lauderdale, FL',
    'Guatemala City': 'Guatemala City, Guatemala',
    'Hamilton, Ont': 'Hamilton, ON',
    'Milwaukee': 'Milwaukee, WI',
    'San Francisco': 'San Francisco, CA',
    'Ottawa': 'Ottawa, ON',
    'Hong Kong': 'Hong Kong, China',
    'Houston': 'Houston, TX',
    'Jersey City, N.J.': 'Jersey City, NJ',
    'Jerusalem': 'Jerusalem, Israel',
    'Los Angeles': 'Los Angeles, CA',

    'Minneapolis': 'Minneapolis, MN',
    'Monteal, PQ': 'Montreal, QC',
    'New Haven': 'New Haven, CT',



    'Adelaide': 'Adelaide, Australia',

    'Newport Beach , California': 'Newport Beach, CA',
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
    'Tampa Bay': 'Tampa, FL',
    'Tampa Bay, FL': 'Tampa, FL',
    'San José, CA': 'San Jose, CA',
    'Fort Lauderdale': 'Fort Lauderdale, FL',
    'Fort Worth': 'Fort Worth, TX',
}
