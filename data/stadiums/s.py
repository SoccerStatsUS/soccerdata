#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime

def load_stadiums():
    print "Loading stadiums."
    from allaway import old
    from mls import mls_stadiums
    from nasl2 import nasl2_stadiums
    from foreign import foreign_stadiums
    from apsl import apsl_stadiums

    l = []
    l.extend(old)
    l.extend(mls_stadiums)
    l.extend(nasl2_stadiums)
    l.extend(foreign_stadiums)
    l.extend(apsl_stadiums)
    l.extend(stadiums)

    final = []
    
    for e in l:
        d = defaults.copy()
        d.update(e)
        final.append(d)

    return final
        

defaults = {
    'denomination': 'dollars',
    'measure': 'meters',
    'closed': None,
    'year_closed': None,
    'opened': None,
    'year_opened': None,
    'architect': None,
    'capacity': None,
    'location': '',
    'address': '',
    'cost': None,
}


stadiums = [

        {
        'name': 'Lockhart Stadium',
        'address': '5201 NW 12th Ave',
        'location': 'Fort Lauderdale, FL',
        'capacity': 20450,
        'opened': 1959,
        'notes': 'First Soccer Specific Stadium in Major League Soccer',
        },



        {
        'name': 'Blackbaud Stadium',
        'address': '1990 Daniel Island Drive',
        'location': 'Charleston, South Carolina ',
        'capacity': 5100,
        'opened': 1999,
        'notes': 'first privately funded soccer specific stadium in the United States',
        },


        {
        'name': 'City Stadium',
        'address': '3201 Maplewood Avenue',
        'location': 'Richmond, VA',
        'capacity': 22000,
        'opened': 1929,
        'cost': 80000,
        },


        {
        'name': 'Atlanta Silverbacks Park',
        'address': '3200 Atlanta Silverbacks Way',
        'location': 'Atlanta, GA',
        'capacity': 5000,
        'opened': 2006,
        'cost': 80000,
        },



        {
        'name': 'Citrus Bowl',
        'address': '1610 W. Church Street',
        'location': 'Orlando, FL',
        'capacity': 70000,
        'cost': 115000,
        'opened': 1936,
        },        

        {
        'name': 'Silverdome',
        'address': '1200 Featherstone Road',
        'location': 'Pontiac, MI',
        'capacity': 70000,
        'cost': 55700000,
        'opened': datetime.datetime(1975, 8, 23),
        'architect': 'O\'Dell/Hewlett & Luckenbach',
        },        

    


        {
        'name': 'Stanford Stadium',
        'address': '625 Nelson Rd',
        'location': 'Stanford, CA',
        'capacity': 50000,
        'cost': 200000,
        'opened': datetime.datetime(1921, 10, 1),
        'renovations': [(datetime.datetime(2006, 9, 16), 90000000), ],
        },        

    

        {
        'name': 'FedEx Field',
        'address': '1600 FedEx Way',
        'location': 'Landover, MD',
        'capacity': 91000,
        'cost': 250500000,
        'opened': datetime.datetime(1997, 9, 14),
        },        

    

        {
        'name': 'WakeMed Soccer Park', 
        'address': '201 Soccer Park Drive',
        'location': 'Cary, NC',
        'capacity': 10000,
        'cost': 14500000,
        'opened': 2002,
        },        

        {
        'name': 'Polo Grounds', 
        'address': 'West 155th Street and Eighth Avenue',
        'location': 'Manhattan, NY',
        'capacity': 55000,
        'opened': datetime.datetime(1890, 8, 19),
        'closed': 1963,
        },        

        {
        'name': 'Veterans Memorial Stadium',
        'address': '5000 East Lew Davis Street',
        'location': 'Long Beach, CA',
        'capacity': 11600,
        'opened': 1948,
        },        


        {
        'name': 'Varsity Stadium',
        'address': '299 Bloor Street West',
        'location': 'Toronto',
        'opened': 1898,
        'cost': 617000000,
        },        


        {
        'name': 'Wrigley Field (Los Angeles)',
        'location': 'Los Angeles, CA',
        'opened': 1925,
        'closed': 1965,
        },        

        {
        'name': 'Memorial Coliseum (Los Angeles)',
        'address': '3911 South Figueroa Street',
        'location': 'Los Angeles, CA',
        'opened': datetime.datetime(1923, 5, 1),
        'cost': 954872.98,
        'capacity': 11600,
        },        

    {
        'name': 'Candlestick Park',
        'address': '490 Jamestown Avenue',
        'location': 'San Francisco, CA',
        'opened': datetime.datetime(1960, 4, 12),
        'cost': 15000000,
        'architect': 'John Bolles',
        'capacity': 69732,
        },

    {
        'name': 'Yankees Stadium',
        'address': 'East 161st St and River Ave',
        'location': 'Bronx, NY',
        'opened': datetime.datetime(1921, 4, 18),
        'cost': 2400000,
        'architect': 'Osborn Engineering Corporation',
        },

    {
        'name': 'Seattle High School Memorial Stadium',
        'address': '401 5th Ave N',
        'location': 'Seattle, WA',
        'opened': 1947,
        'architect': 'George Stoddard',
        'capacity': 17000,
        },

    {
        'name': 'Empire Stadium',
        'address': 'East Hastings Street',
        'location': 'Vancouver',
        'opened': 1954,
        'closed': 1993,
        'capacity': 32729,
            
        },
    {
        'name': 'Hofstra Stadium',
        'address': '225 Hofstra University',
        'location': 'Hempstead, NY',
        'opened': 1962,
        'capacity': 15000,
        },
    {
        'name': 'Kingdome',
        'address': '201 S. King Street',
        'location': 'Seattle, WA',
        'opened': datetime.datetime(1976, 3, 27),
        'architect': 'Naramore, Skilling & Praeger',
        },
    {
        'name': 'Busch Memorial Stadium',
        'address': '250 Stadium Plaza',
        'location': 'St. Louis, MO',
        'opened': datetime.datetime(1966, 5, 12),
        'closed': datetime.datetime(2005, 10, 19),
        'cost': 55000000,
        'architect': 'Sverdrup & Parcel',
        'capacity': 60292,
        },
    {
        'name': 'Tampa Stadium',
        'address': '4201 North Dale Mabry Highway',
        'location': 'Tampa, FL',
        'opened': datetime.datetime(1967, 11, 4),
        'closed': datetime.datetime(1998, 9, 13),
        'cost': 4400000,
        'architect': 'Watson & Company Architects',
        'capacity': 74301,
        },

    {
        'name': 'Sports Authority Field at Mile High',
        'address': '1701 Mile High Stadium Circle',
        'location': 'Denver, CO',
        'opened': datetime.datetime(2001, 9, 10),
        'cost': 400700000,
        'architect': 'HNTB',
        'capacity': 76125,
        },

    {
        'name': 'Mile High Stadium',
        'address': '2755 West 17th Avenue',
        'location': 'Denver, CO',
        'opened': datetime.datetime(1948, 8, 14),
        'closed': datetime.datetime(2000, 12, 23),
        'cost': 500000,
        'architect': 'Stanley E. Morse',
        'capacity': 76273,
        },

    {
        'name': 'Oakland-Alameda County Coliseum',
        'address': '7000 Coliseum Way',
        'location': 'Oakland, CA',
        'opened': datetime.datetime(1966, 9, 18),
        'cost': 25500000,
        'architect': 'Skidmore, Owings and Merrill',
        'capacity': 63026,
        },

    {
        'name': 'Raymond James Stadium',
        'address': '4201 N. Dale Mabry Highway',
        'location': 'Tampa, FL',
        'opened': datetime.datetime(1998, 9, 20),
        'cost': 168500000,
        'architect': 'HOK Sport',
        'capacity': 65857,
        },

    {
        'name': 'Rice-Eccles Stadium',
        'address': '451 South 1400 East',
        'location': 'Salt Lake City, Utah',
        'opened': datetime.datetime(1998, 9, 12),
        'cost': 50000000,
        'architect': 'FFKR Architects',
        'capacity': 45017
        },

    {
        'name': 'Robertson Stadium',
        'address': '3874 Holman Street',
        'location': 'Houston, TX',
        'opened': datetime.datetime(1948, 8, 14),
        'cost': 650000,
        'architect': 'Harry D. Payne',
        'capacity': 32000,
        },

    {
        'name': 'BBVA Compass Stadium',
        'address': 'East End',
        'location': 'Houston, TX',
        'cost': 95000000,
        'architect': 'Populous',
        'capacity': 22000,
        },

    {
        'name': 'BC Place',
        'address': '777 Pacific Boulevard',
        'location': 'Vancouver',
        'opened': datetime.datetime(1983, 6, 19),
        'cost': 126100000,
        'denomination': 'Canadian dollars',
        'architect': 'Studio Phillips Barratt, Ltd',
        'capacity': 54320,
        },

    {
        'name': 'Sanford Stadium',
        'address': 'Sanford Dr and Field St',
        'location': 'Athens, GA',
        'opened': datetime.datetime(1929, 10, 12),
        'cost': 360000,
        'architect': 'TC Atwood',
        'capacity': 92746,
        },

    {
        'name': 'Legion Field',
        'address': '400 Graymont Avenue West',
        'location': 'Birmingham, AL',
        'opened': datetime.datetime(1927, 11, 19),
        'cost': 439000,
        'architect': 'D.O. Whildin',
        'capacity': 71594,
        },

    {
        'name': 'Cowboys Stadium',
        'address': '1 Legends Way',
        'location': 'Arlington, TX',
        'opened': datetime.datetime(2009, 5, 27),
        'cost': 1300000000,
        'architect': 'HKS, Inc.',
        'capacity': 80000,
        },

    {
        'name': 'MetLife Stadium',
        'address': 'One MetLife Stadium Drive',
        'location': 'East Rutherford, NJ',
        'opened': datetime.datetime(2010, 4, 10),
        'cost': 1600000000,
        'architect': '360 Architecture',
        'capacity': 82566,
        },

    {
        'name': 'M&T Bank Stadium',
        'address': '1101 Russell Street',
        'location': 'Baltimore, MD',
        'opened': datetime.datetime(1998, 9, 6),
        'cost': 220000000,
        'architect': 'HOK Sport',
        'capacity': 71008,
        },

    {
        'name': 'Reliant Stadium',
        'address': 'One Reliant Park',
        'location': 'Houston, TX',
        'opened': datetime.datetime(2002, 8, 24),
        'cost': 352000000,
        'architect': 'HOK Sport',
        'capacity': 71054,
        },

    {
        'name': 'Sun Life Stadium',
        'address': '2267 NW 199th Street',
        'location': 'Miami Gardens, FL',
        'opened': datetime.datetime(1985, 12, 1),
        'cost': 115000000,
        'architect': 'HOK Sport',
        'capacity': 74918,
        },

    {
        'name': 'Qualcomm Stadium',
        'address': '9449 Friars Road',
        'location': 'San Diego, CA',
        'opened': datetime.datetime(1967, 8, 20),
        'cost': 27000000,
        'architect': 'Frank L. Hope and Associates',
        'capacity': 70561,
        },

    {
        'name': 'Lincoln Financial Field',
        'address': '1020 Pattison Avenue',
        'location': 'Philadelphia, PA',
        'opened': datetime.datetime(2003, 8, 3),
        'cost': 512000000,
        'architect': 'NBBJ',
        'capacity': 68532,
        },



    {
        'name': 'Buck Shaw Stadium',
        'address': '500 El Camino Real',
        'location': 'Santa Clara, CA',
        'opened': datetime.datetime(1962, 9, 22),
        'capacity': 10525,
        },




    {
        'name': 'Bank of America Stadium',
        'address': '800 South Mint Street',
        'location': 'Charlotte, NC',
        'opened': datetime.datetime(1996, 9, 14),
        'cost': 248000000,
        'architect': 'HOK Sport',
        'capacity': 73778,
        },

    {
        'name': 'University of Phoenix Stadium',
        'address': '1  Cardinals Drive',
        'location': 'Glendale, AZ',
        'opened': datetime.datetime(2006, 8, 1),
        'cost': 455000000,
        'architect': 'Eisenman Architects',
        'capacity': 63400,
        },

    {
        'name': 'Georgia Dome',
        'location': 'Atlanta, GA',
        'opened': datetime.datetime(1992, 9, 6),
        'cost': 214000000,
        'architect': 'Heery International',
        'capacity': 71228,
        },

    {
        'name': 'Anaheim Stadium',
        'address': '2000 Gene Autry Way',
        'location': 'Anaheim, CA',
        'opened': datetime.datetime(1966, 4, 19),
        'cost': 24000000,
        'architect': 'Noble W. Herzberg and Associates ',
        'capacity': 45957,
        },

    {
        'name': 'Metropolitan Stadium',
        'address': '8000 Cedar Ave. South',
        'location': 'Bloomington, MN',
        'opened': datetime.datetime(1956, 4, 24),
        'cost': 8500000,
        'architect': 'Tepper Engineering',
        'capacity': 48446,
        },

    {
        'name': 'Yale Bowl',
        'address': '81 Central Avenue',
        'location': 'New Haven, CT',
        'opened': datetime.datetime(1914, 11, 21),
        'cost': 750000,
        'architect': 'Charles A. Ferry',
        'capacity': 64246,
        },


    {
        'name': 'Veterans Stadium',
        'address': '3501 South Broad Street',
        'location': 'Philadelphia, PA',
        'opened': datetime.datetime(1971, 4, 10),
        'cost': 50000000,
        'architect': 'Hugh Stubbins and Associates',
        'capacity': 65386,
        },

    {
        'name': 'Franklin Field',
        'address': 'South 33rd and Spruce Streets',
        'location': 'Philadelphia, PA',
        'opened': datetime.datetime(1895, 4, 20),
        'cost': 100000,
        'architect': 'Frank Miles Day & Brother',
        'capacity': 52593,
        },

    {
        'name': 'Citi Field',
        'address': '126th St. & Roosevelt Ave',
        'location': 'Flushing, NY',
        'opened': datetime.datetime(2009, 3, 29),
        'cost': 900000000,
        'architect': 'Populous',
        'capacity': 41922,
        },

    {
        'name': 'Comiskey Stadium',
        'address': '324 West 35th St',
        'location': 'Chicago, IL',
        'opened': datetime.datetime(1910, 7, 1),
        'closed': datetime.datetime(1990, 9, 30),
        'cost': 750000,
        'architect': 'Zachary Taylor Davis',
        'capacity': 43951,
        },

    {
        'name': 'Texas Stadium',
        'address': '2401 East Airport Freeway',
        'location': 'Irving, TX',
        'opened': datetime.datetime(1971, 9, 17),
        'closed': datetime.datetime(2008, 12, 20),
        'cost': 35000000,
        'architect': 'A. Warren Morey',
        'capacity': 41922,
        },

    {
        'name': 'AT&T Park',
        'address': '24 Willie Mays Plaza',
        'location': 'San Francisco, CA',
        'opened': datetime.datetime(2000, 3, 31),
        'cost': 357000000,
        'architect': 'Populous',
        'capacity': 40930,
        },

    {
        'name': 'Safeco Field',
        'address': '1516 First Avenue South',
        'location': 'Seattle, WA',
        'opened': datetime.datetime(1999, 7, 15),
        'cost': 517600000,
        'architect': 'NBBJ',
        'capacity': 47878,
        },

    {
        'name': 'Alamodome',
        'address': '100 Montana Street',
        'location': 'San Antonio, TX',
        'opened': datetime.datetime(1990, 11, 5),
        'cost': 186000000,
        'architect': 'Populous',
        'capacity': 65000,
        },

    {
        'name': 'Rentschler Field',
        'address': '615 Silver Lane',
        'location': 'East Hartford, CT',
        'opened': datetime.datetime(2003, 8, 30),
        'cost': 91200000,
        'architect': 'Ellerbe Becket',
        'capacity': 40000,
        },

    {
        'name': 'High Point Solutions Stadium',
        'address': '1 Scarlet Knight Way',
        'location': 'Piscataway, NJ',
        'opened': datetime.datetime(1994, 9, 3),
        'cost': 28000000,
        'architect': 'GSGSBH',
        'capacity': 52454,
        },

    {
        'name': 'Wrigley Field',
        'address': '1060 West Addison Street',
        'location': 'Chicago, IL',
        'opened': datetime.datetime(1914, 4, 23),
        'cost': 250000,
        'architect': 'Zachary Taylor Davis',
        'capacity': 41159,
        },

    {
        'name': 'Cardinal Stadium (Louisville)',
        'address': '937 Phillips Lane',
        'location': 'Louisville, KY',
        'opened': 1957,
        'capacity': 47925,
        },

    {
        'name': 'Astrodome',
        'address': '8400 Kirby Drive',
        'location': 'Houston, TX',
        'opened': datetime.datetime(1965, 4, 9),
        'cost': 35000000,
        'architect': 'Hermon Lloyd & W.B. Morgan',
        'capacity': 62439,
        },

    {
        'name': 'Chase Field',
        'address': '401 East Jefferson Street',
        'location': 'Phoenix, AZ',
        'opened': datetime.datetime(1998, 3, 31),
        'cost': 354000000,
        'architect': 'Ellerbe Becket',
        'capacity': 48633,
        },

    {
        'name': 'Fenway Park',
        'address': '4 Yawkey Way',
        'location': 'Boston, MA',
        'opened': datetime.datetime(1912, 4, 20),
        'cost': 650000,
        'architect': 'James McLaughlin',
        'capacity': 37493,
        },

    {
        'name': 'Shea Stadium',
        'address': '123-01 Roosevelt Avenue',
        'location': 'Flushing, NY',
        'opened': datetime.datetime(1964, 4, 17),
        'cost': 28500000,
        'architect': 'Praeger-Kavanagh-Waterbury',
        'capacity': 60372,
        },

    {
        'name': 'Skelly Field at H. A. Chapman Stadium',
        'address': 'S Florence & E 8th',
        'location': 'Tulsa, OK',
        'opened': datetime.datetime(1930, 10, 4),
        'cost': 275000,
        'architect': 'Robert H. Hienbrenáer',
        'capacity': 30000,
        },

    {
        'name': 'Shibe Park',
        'address': 'N 21st St & W Lehigh Ave,',
        'location': 'Philadelphia, PA',
        'opened': datetime.datetime(1909, 4, 12),
        'closed': datetime.datetime(1970, 10, 1),
        'cost': 301000,
        'architect': 'William Steele and Sons',
        'capacity': 33608, 
        },

    {
        'name': 'Ebbets Field',
        'address': '55 Sullivan Place',
        'location': 'Brooklyn, NY',
        'opened': datetime.datetime(1913, 4, 9),
        'closed': datetime.datetime(1960, 2, 23),
        'cost': 750000,
        'architect': 'Clarence Randall Van Buskirk',
        'capacity': 31902,
        },

    {
        'name': 'Cleveland Browns Stadium',
        'address': '100 Alfred Lerner Way',
        'location': 'Cleveland, OH',
        'opened': datetime.datetime(1999, 9, 12),
        'cost': 349000000,
        'architect': 'HOK Sport',
        'capacity': 73200,
        },


    {
        'name': 'Navy-Marine Corps Stadium',
        'address': 'Rowe Blvd & Taylor Ave',
        'location': 'Annapolis, MD',
        'opened': 1959,
        'cost': 3000000,
        'capacity': 34000,
        },


    {
        'name': 'LP Field',
        'address': '1 Titans Way',
        'location': 'Nashville, TN',
        'opened': datetime.datetime(1999, 8, 27),
        'cost': 290000000,
        'architect': 'Populous',
        'capacity': 69143,
        },


    {
        'name': 'Ford Field',
        'address': '2000 Brush Street',
        'location': 'Detroit, MI',
        'opened': datetime.datetime(2002, 8, 24),
        'cost': 430000000,
        'architect': 'SHG, Inc.',
        'capacity': 65000,
        },


    {
        'name': 'Harvard Stadium',
        'address': '95 N Harvard St',
        'location': 'Boston, MA',
        'opened': datetime.datetime(1904, 11, 14),
        'cost': 310000,
        'architect': 'Louis J. Johnson',
        'capacity': 30323,
        },


    {
        'name': 'Atlanta-Fulton County Stadium',
        'address': '521 Capitol Avenue SE',
        'location': 'Atlanta, GA',
        'opened': datetime.datetime(1965, 4, 12),
        'cost': 18000000,
        'architect': 'Heery & Heery',
        'capacity': 60606,
        },


    {
        'name': 'Downing Stadium',
        'address': 'Randall\'s Island',
        'location': 'New York, NY',
        'opened': datetime.datetime(1936, 7, 11),
        'closed' :2002,
        'architect': 'Robert Moses',
        'capacity': 22000,
        },


    {
        'name': 'Heinz Field',
        'address': '100 Art Rooney Avenue',
        'location': 'Pittsburgh, PA',
        'opened': datetime.datetime(2001, 8, 18),
        'cost': 281000000,
        'architect': 'HOK Sport',
        'capacity': 65050,
        },


    {
        'name': 'Tara Stadium',
        'address': '1055 Battle Creek Rd',
        'location': 'Jonesboro, GA',
        },


    {
        'name': 'Taylor Field',
        'location': 'Bethlehem, PA',
        },


    {
        'name': 'ONT AA Grounds',
        'location': 'Kearny, NJ',
        },


    {
        'name': 'Domestic Baseball Grounds',
        'location': 'Newark, NJ',
        },


    {
        'name': 'Emmet Street Grounds',
        'location': 'Newark, NJ',
        },
    {
        'name': 'Olympic Grounds',
        'location': 'Paterson, NJ',
        },
    {
        'name': 'Cricket Grounds',
        'location': 'Trenton, NJ',
        },
    {
        'name': 'Frelinghuysen Grounds',
        'location': 'Newark, NJ',
        },
    {
        'name': 'Elysian Fields',
        'location': 'Hoboken, NJ',
        },
    {
        'name': 'Federal League Baseball Grounds',
        'location': 'Harrison, NJ',
        },
    {
        'name': 'Athletic Field',
        'location': 'Fall River, MA',
        },
    {
        'name': 'Handlan\'s Park',
        'location': 'St. Louis, MO',
        },
    {
        'name': 'Federal League Park',
        'location': 'St. Louis, MO',
        },
    {
        'name': 'Fall River Athletic Field',
        'location': 'Fall River, MA',
        },
    {
        'name': 'High School Field',
        'location': 'St. Louis, MO',
        },

    {
        'name': 'University of Detroit Stadium',
        'location': 'Detroit, MI',
        'capacity': 25000,
        
        },
    {
        'name': 'Lonsdale Avenue Grounds',
        'location': 'Pawtucket, RI',
        },
    {
        'name': 'Sportsman\'s Park',
        'address': '2911 N Grand Blvd',
        'location': 'St. Louis, MO',
        'opened': datetime.datetime(1902, 4, 23),
        'closed': datetime.datetime(1966, 5, 8),
        'cost': 300000,
        'capacity': 30500,
        },
    {
        'name': 'Dexter Park',
        'location': 'Queens, NY',

        },
    {
        'name': 'Luna Park',
        'location': 'Cleveland, OH',
        },
    {
        'name': 'Sparta Field',
        'location': 'Chicago, IL',
        },
    {
        'name': 'DePaul Field',
        'location': 'Chicago, IL',
        },
    {
        'name': 'Mills Stadium',
        'location': 'Chicago, IL',
        'opened': 1913,
        'closed': 1941,
        'capacity': 10000,
        'source': 'http://www.projectballpark.org/history/nnl1/alt/pyotts.html',
        },
    {
        'name': 'Starlight Pakr',
        'location': 'Bronx, NY',
        'opened': 1918,
        'closed': 1932,
        },
    {
        'name': 'Commercial Field',
        'address': 'Albany Avenue',
        'location': 'Brooklyn, NY',
        'opened': 1906,
        
        },
    {
        'name': 'Walsh Memorial Stadium',
        'address': '5200 Oakland Ave',
        'location': 'St. Louis, MO',
        'opened': 1930,
        
        },
    {
        'name': 'Newark Schools Stadium',
        'address': '450 Bloomfield Avenue',
        'location': 'Newark, NJ',
        'opened': 1925,
        'closed': 2009,
        'capacity': 15000,
        },

    {
        'name': 'Rifle Club Grounds',
        'location': 'Philadelphia, PA',
        },
    {
        'name': 'Bridgeville Park',
        'location': 'Bridgeville, PA',
        },
    {
        'name': 'Bugle Field',
        'location': 'Baltimore, MD',
        },
    {
        'name': 'Legion Field (Donora)',
        'location': 'Donora, PA',
        },
    {
        'name': 'Shaw Field',
        'location': 'Cleveland, HO',
        },
    {
        'name': 'Holmes Stadium',
        'location': 'Philadelphia, PA',
        },

    {
        'name': 'Sterling Oval',
        'location': 'Bronx, NY',
        },
    {
        'name': 'Freeport Road Field',
        'location': 'Pittsburgh, PA',
        },
    {
        'name': 'Rancho La Cienga Stadium',
        'location': 'Los Angeles, CA',
        },
    {
        'name': 'Edison Field',
        'location': 'Philadelphia, PA',
        },

    {
        'name': 'Eintracht Oval',
        'location': 'Queens, NY',
        },
    {
        'name': 'Cambria Field',
        'location': 'Philadelphia, PA',
        },
    {
        'name': 'Hanson Stadium',
        'location': 'Chicago, IL',
        },
    {
        'name': 'PAL Stadium',
        'location': 'San Jose, CA',
        },
    {
        'name': 'Daniels Field',
        'location': 'San Pedro, CA',
        },

    {
        'name': 'Jackie Robinson Field',
        'location': 'Los Angeles, CA',
        },
    {
        'name': 'St. Louis Soccer Park',
        'location': 'Fenton, MO',
        },
    {
        'name': 'Kuntz Stadium',
        'location': 'Indanapolis, IN',
        },
    {
        'name': 'Brooklyn College',
        'location': 'Brooklyn, NY',
        },
    {
        'name': 'Indianapolis Soccer Stadium',
        'location': 'Indianapolis, IN',
        },



    {
        'name': 'Coates Field',
        'location': 'Pawtucket, RI',
        },


    {
        'name': 'Memorial Stadium Baltimore',
        'address': '900 East 33rd Street',
        'location': 'Balitmore, MD',
        'opened': datetime.datetime(1922, 12, 2),
        'closed': datetime.datetime(1997, 12, 14),
        'cost': 6500000,
        'capacity': 53371,
        'architect': 'L.P. Kooken Company',
        },  
  {
        'name': 'McMahon Stadium',
        'address': '1817 Crowchild Trail NW',
        'location': 'Calgary, Alberta',
        'opened': 1960,
        'cost': 1050000,
        'denomination': 'Canadian dollars',
        'capacity': 35650,
        'architect': 'Rule Wynn and Rule',
        },  


    {
        'name': 'Cleveland Stadium',
        'address': '1085 West 3rd Street',
        'location': 'Cleveland, OH',
        'opened': datetime.datetime(1931, 7, 1),
        'closed': datetime.datetime(1995, 12, 17),
        'cost': 3000000,
        'architect': 'Walker & Weeks',
        'capacity': 81000,
        },
    {
        'address': '10000 Hillcrest',
        'name': 'Franklin Stadium',
        'location': 'Dallas, TX',
        'opened': 1954,
        'capacity': 8500,
        },
    {
        'name': 'Ownby Stadium',
        'address': '5800 Ownby Dr',
        'location': 'Dallas, TX',
        'opened': 1926,
        'closed': 1988,
        'capacity': 23783,
        
        },
    {
        'name': 'Tigers Stadium',
        'address': '2121 Trumbull Street',
        'location': 'Detroit, MI',
        'opened': datetime.datetime(1912, 4, 20),
        'closed': datetime.datetime(1999, 9, 27),
        'capacity': 52416,
        'architect': 'Osborn Engineering',
        'cost': 300000,
        },
    {
        'name': 'Gator Bowl',
        'address': '1 Gator Bowl Boulevard',
        'location': 'Jacksonville, FL',
        'opened': 1928,
        'closed': 1994,
        'capacity': 80126,
        },
    {
        'name': 'Kansas City Municipal Stadium',
        'address': '22nd St. and Brooklyn Ave',
        'location': 'Kansas City, MO',
        'opened': datetime.datetime(1923, 7, 3),
        'closed': 1976,
        'cost': 400000,
        'architect': 'Osborn Engineering',
        'capacity': 35561,
        },
    {
        'name': 'Metrodome',
        'address': '900 South 5th Street',
        'location': 'Minneapolis, MN',
        'opened': datetime.datetime(1982, 4, 3),
        'cost': 68000000,
        'architect': 'Skidmore, Owings & Merrill',
        'capacity': 64111,
        },
    {
        'name': 'Miami Orange Bowl',
        'address':'1501 NW 3rd Street',
        'location': 'Miami, FL',
        'opened': datetime.datetime(1937, 12, 10),
        'closed': datetime.datetime(2008, 1, 26),
        'cost': 340000,
        'capacity': 72319,
        },
    {
        'name': 'Tamiami Park',
        'address': '11201 Southwest 24th Street',
        'location': 'Miami, FL',
        },
    {
        'name': 'Autostade',
        'address': '475 av. Des Pins Ouest',
        'location': 'Montreal',
        'capacity': 33172,
        },
    {
        'name': 'Olympic Stadium',
        'address': '4545 Pierre de Coubertin Avenue',
        'location': 'Montreal, Quebec',
        'opened': datetime.datetime(1973, 4, 28),
        'cost': 770000000,
        'denomination': 'Canadian Dollars',
        'architect': 'Roger Taillibert',
        'capacity': 66308,
        },
    {
        'name': 'Holleder Memorial Stadium',
        'location': 'Rochester, NY',
        'capacity': 20000,
        },
    {
        'name': 'Valley View Casino Center',
        'address': '3500 Sports Arena Boulevard',
        'location': 'San Diego, CA',
        'opened': datetime.datetime(1965, 11, 18),
        'cost': 6400000,
        'architect': 'Mark L. Faddis',
        'capacity': 12000,
        },
    {
        'name': 'Aztec Bowl',
        'address': '5300 Campanile Dr',
        'location': 'San Diego, CA',
        'opened': datetime.datetime(1936, 10, 3),
        },


    {
        'name': 'Sam Boyd Stadium',
        'address': '7000 East Russell Road',
        'location': 'Las Vegas, NV',
        'opened': datetime.datetime(1971, 10, 23),
        'cost': 3500000,
        'capacity': 36800,
        },


    {
        'name': 'Liberty Bowl Memorial Stadium',
        'address': '335 South Hollywood Street',
        'location': 'Memphis, TN',
        'opened': datetime.datetime(1965, 9, 16),
        'cost': 3700000,
        'architect': 'Yeates, Gaskill & Rhodes',
        'capacity': 61008,
        },


    {
        'name': 'Alamo Stadium',
        'address': '110 Tuleta Dr',
        'location': 'San Antonio, TX',
        'opened': 1940,
        'cost': 500000,
        'architect': 'Phelps & Dewees & Simmons',
        'capacity': 23000,
        },


    {
        'name': 'Aloha Stadium',
        'address': '99-500 Salt Lake Blvd',
        'location': 'Honolulu, HI',
        'opened': datetime.datetime(1975, 9, 12),
        'cost': 3700000,
        'architect': 'The Luckman Partnership',
        'capacity': 50000,
        },


    {
        'name': 'John F. Kennedy Stadium',
        'address': 'S Broad Street',
        'location': 'Philadelphia, PA',
        'opened': datetime.datetime(1926, 4, 15),
        'closed': datetime.datetime(1989, 7, 13),
        'architect': 'Simon & Simon',
        'capacity': 102000,
        },

            {
        'name': 'Swangard Stadium',
        'address': '3883 Imperial Street',
        'location': 'Burnaby, BC',
        'opened': datetime.datetime(1969, 4, 26),
        'capacity': 5288,
        },

        {
            'name': 'Edmonton Commonwealth Stadium',
            'address': '11000 Stadium Road',
            'location': 'Edmonton',
            'opened': 1978,
            'cost': 20900000,
            'denomination': 'Canadian Dollars',
            'capacity': 60081,
            },

        
        {
            'name': 'Empire Field',
            'address': 'East Hasting Street',
            'location': 'Vancouver',
            'opened': datetime.datetime(2010, 6, 15),
            'capacity': 27528,
            },

        {
            'name': 'Titan Stadium',
            'address': '800 North State College Blvd',
            'location': 'Fullerton, CA',
            'opened': 1992,
            'capacity': 10000,
            'cost': 10200000,
            'length': 120,
            'width': 75,
            'measure': 'yards',
            },


        {
            'name': 'Robert R. Hermann Stadium',
            'location': 'St. Louis, MO',
            'opened': datetime.datetime(1999, 8, 21),
            'capacity': 6050,
            'cost': 5100000,
            },

                {
            'name': 'Kezar Stadium',
            'address': '755 Stanyan Street',
            'location': 'San Francisco, CA',
            'opened': datetime.datetime(1925, 5, 2),
            'capacity': 9044,
            'cost': 300000,
            'architect': 'Willis Polk',
            },


]
