#!/usr/local/bin/env python
# -*- coding: utf-8 -*-




def get_city(s):

    s = s.strip()
    if s in cities:
        return get_city(cities[s])
    else:
        return s
    


cities = {
    #[<City: Rancho la Cienega Stadium>, <City: Rancho La Cienega Stadium>]
    #[<City: Randall's Island, NYC>, <City: Randalls Island, NYC>]

    'México City, Mexico': 'Mexico City, Mexico',
    'Bayamon, PR': 'Bayamón, Puerto Rico',
    'Bayamón, PR': 'Bayamón, Puerto Rico',
    'Victoria, B.C.': 'Victoria, BC',
    'Los Ángeles, CA': 'Los Angeles, CA',

    'San Martin, Argentina': 'San Martín, Argentina', # real city?
    'Medellin, Colombia': 'Medellín, Colombia',
    'Goteborg, Sweden': 'Göteborg, Sweden',
    #[<City: Arlington Heights, IL>, <City: Arlington, Heights, IL>]
    'Colon, Panama': 'Colón, Panama',
    #[<City: away>, <City: Away>]
    'Dublin Ireland': 'Dublin, Ireland',
    #[<City: Miami, FL>, <City: Miami, Fl>]

    'Newcastle-upon-Tyne, England': 'Newcastle upon Tyne, England',
    'Queretaro': 'Querétaro, Mexico',
    'Querétaro': 'Querétaro, Mexico',
    'Paysandu, Uruguay': 'Paysandú, Uruguay',
    'San Luis Potosi, Mexico': 'San Luis Potosí, Mexico',
    'Yaounde, Cameroon': 'Yaoundé, Cameroon',
    'Leon, Mexico': 'León, Mexico',
    'Brasilia, Brazil': 'Brasília, Brazil',
    #[<City: Maloney's Park, Detroit, MI>, <City: Maloney’s Park, Detroit, MI>]
    'Zurich, Switzerland': 'Zürich, Switzerland',
    'San Cristobal, Venezuela': 'San Cristóbal, Venezuela',
    #[<City: Estadio Nacional, Tegucigalpa>, <City: Estadío Nacional, Tegucigalpa>]
    #[<City: Dragon Stadium - Round Rock>, <City: Dragon Stadium Round Rock>]
    'Port au Prince, Haiti': 'Port-au-Prince, Haiti',
    'Vancouver, B.C.': 'Vancouver, BC',
    'Sao Paulo, Brazil': 'São Paulo, Brazil',
    #[<City: Point Fortin, Trinidad & Tobago>, <City: Point-Fortin, Trinidad & Tobago>]
    'Puerto Cortes, Honduras': 'Puerto Cortés, Honduras',
    #[<City: Estadio Olimpico (Caracas)>, <City: Estadio Olimpico, Caracas>]
    #[<City: Newport Beach, CA>, <City: Newport Beach , CA
    'San Jose, Costa Rica': 'San José, Costa Rica',
    #[<City: Randall's Island>, <City: Randalls Island>]
    #[<City: Winnipeg, Man>, <City: Winnipeg, Man.>]
    #[<City: Brampton, ON>, <City: Brampton , ON>]
    #[<City: San Jose>, <City: San José>]
    #[<City: West Side Park, Jersey City, NJ>, <City: West Side Park, Jersey City, N.J.>]
    'Ciudad de Panama, Panama': 'Ciudad de Panamá, Panama',
    'Panama City, Panama': 'Ciudad de Panamá, Panama',
    'Merida, Venezuela': 'Mérida, Venezuela',
    'Bogota, Colombia': 'Bogotá, Colombia',
    'Fort de France, Martinique': 'Fort-de-France, Martinique',
    #[<City: St. Vincent St. Mary HS>, <City: St. Vincent-St. Mary HS>]
    'Asuncion, Paraguay': 'Asunción, Paraguay',
    'Vasteras, Sweden': 'Västerås, Sweden',
    
    'Mar Del Plata, Argentina': 'Mar del Plata, Argentina',
    'Dusseldorf, Germany': 'Düsseldorf, Germany',
    'Washington DC': 'Washington, D.C.',
    'Washington, DC': 'Washington, D.C.',
    #[<City: UISD - Student Activity Center>, <City: UISD Student Activity Center>]
    #[<City: Asuncion>, <City: Asunción>]
    'Sao Luis, Brazil': 'São Luís, Brazil',
    #[<City: Colorado College - Washburn Field>, <City: Colorado College Washburn Field>]
    #Rio de Janeiro>, <City: Río de Janeiro>]
    #[<City: Port of Spain, Trinidad & Tobago>, <City: Port-of-Spain, Trinidad & Tobago>]
    'Backa Topola, Serbia': 'Bačka Topola, Serbia',
    #[<City: St Lucia>, <City: St. Lucia>]
    #[<City: Port of Spain, Trinidad>, <City: Port-of-Spain, Trinidad>]
    #[<City: Kearny High School Stadium, Kearny, NJ>, <City: Kearny High School Stadium, Kearny , NJ>]
    'Acandi, Colombia': 'Acandí, Colombia',
    'Goiania, Brazil': 'Goiânia, Brazil',
    'Cordoba, Argentina': 'Córdoba, Argentina',
    #[<City: Estadio Universitario Monterrey>, <City: Estadio Universitario, Monterrey>, <City: Estadío Universitario, Monterrey>]
    'Concepcion, Chile': 'Concepción, Chile',
    
    'Rio De Janeiro, Brazil': 'Rio de Janeiro, Brazil',
    'Rio de Janeiro': 'Rio de Janeiro, Brazil',
    'Chorzow, Poland': 'Chorzów, Poland',
    #[<City: home>, <City: Home>]
    #[<City: David's Stadium, Newark, NJ>, <City: Davids Stadium, Newark, NJ>]
    'Vina del Mar, Chile': 'Viña del Mar, Chile',
    #[<City: neutral>, <City: Neutral>]
    'Valparaiso, Chile': 'Valparaíso, Chile',


    'Newcastle-upon-Tyne, England': 'Newcastle upon Tyne, England',
    'Kristiana, Norway': 'Oslo, Norway',

    'Rome': 'Rome, Italy',
    'Lyons, France': 'Lyon, France',
    'Glasgow': 'Glasgow, Scotland',
    'Belfast': 'Belfast, Northern Ireland',

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
    'Philadelphia': 'Philadelphia, PA',
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
    'Malmo, Sweden': 'Malmö, Sweden',
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
    'San José, CA': 'San Jose, CA',
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
