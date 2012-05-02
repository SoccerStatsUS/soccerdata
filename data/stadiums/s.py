

def get_stadium(s):
    


defaults = {
    'denomination': 'dollars',
    'measure': 'meters',
    'closed': None,
    'opened': None,
    'architect': None,
    'capacity': None,
    'location': '',
    'address': '',
    'cost': None
}


mls = [ {
        'stadium': 'Home Depot Center',
        'address': '18400 Avalon Boulevard',
        'location': 'Carson, CA'
        'capacity': 27000,
        'architect': 'Rossetti Architects',
        'opened': datetime.date(6, 1, 2003),
        'length': 109.7,
        'width': 68.6,
        },

        {
        'stadium': 'Cotton Bowl'l,
        'address': '1300 Robert B. Cullum Boulevard',
        'location': 'Dallas, TX',
        'capacity': 92100,
        'opened': 1930,
        'cost': 328200,
        },


        {
        'stadium': 'Lockhart Stadium',
        'address': '5201 NW 12th Ave',
        'location': 'Fort Lauderdale, FL',
        'capacity': 20450
        'opened': 1959,
        'notes': 'First Soccer Specific Stadium in Major League Soccer',
        },



        {
        'stadium': 'Blackbaud Stadium',
        'address': '1990 Daniel Island Drive',
        'location': 'Charleston, South Carolina ',
        'capacity': 5100,
        'opened': 1999,
        'notes': 'first privately funded soccer specific stadium in the United States',
        },


        {
        'stadium': 'City Stadium',
        'address': '3201 Maplewood Avenue',
        'location': 'Richmond, VA',
        'capacity': 22000,
        'opened': 1929
        'cost': 80000,
        },


        {
        'stadium': 'Atlanta Silverbacks Park',
        'address': '3200 Atlanta Silverbacks Way',
        'location': 'Atlanta, GA',
        'capacity': 5000,
        'opened': 2006,
        'cost': 80000,
        },


        {
        'stadium': 'Columbus Crew Stadium',
        'address': '1 Black and Gold Boulevard',
        'location': 'Columbus, OH',
        'capacity': 20145,
        'opened': datetime.date(5,15,1999),
        'cost': 28500000,
        'architect': 'NBBJ',
        'notes': 'First stadium built for an MLS team.',
        'length': 115,
        'width': 75
        'measure': 'yards',
        
    
        },



        {
        'stadium': 'Arrowhead Stadium',
        'address': '1 Arrowhead Drive',
        'location': 'Kansas City, MO',
        'capacity': 76416,
        'opened': datetime.date(1972, 8, 12),
        'cost': 43000000,
        'architect': 'Kivett and Myers',
        },



        {
        'stadium': 'Cardinal Stadium',
        'address': '455 South Brainard Street',
        'location': 'Naperville, IL',
        'capacity': 5500,
        'opened': 1999,
        },


        {
        'stadium': 'CommunityAmerica Ballpark',
        'address': '1800 Village West Pkwy',
        'location': 'Kansas City, KS',
        'capacity': 10385,
        'opened': datetime.date(2003, 6, 6),
        'cost': 12000000,
        'architect': 'Heinlein Schrock Stearns',
        },

        {
        'stadium': 'Dragon Stadium',
        'address': '1085 S Kimball Ave',
        'location': 'Southlake, TX',
        'capacity': 11000,
        'opened': 2001,
        'cost': 15000000,
        },
    
    {
        'stadium': 'FC Dallas Stadium',
        'address': '9200 World Cup Way, Ste 202',
        'location': 'Frisco, TX',
        'capacity': 20500,
        'cost': 80000000,
        'opened': datetime.date(2005, 8, 6),
        'length': 107,
        'width': 68,
        },

        {
        'stadium': 'Rose Bowl',
        'address': '1001 Rose Bowl Drive',
        'location': 'Pasadena, CA',
        'capacity': 91136,
        'cost': 272198,
        'opened': 1921,
        'architect': 'Myron Hunt',
        'length': 107,
        'width': 68,
        },

    
        {
        'stadium': 'Soldier Field',
        'address': '1410 S Museum Campus Drive',
        'location': 'Chicago, IL',
        'capacity': 61500,
        'cost': 13000000,
        'opened': datetime.date(1924, 10, 9),
        'architect': 'Holabird & Roche',
        },

        {
        'stadium': 'Giants Stadium',
        'address': '50 Route 120',
        'location': 'East Rutherford, NJ',
        'capacity': 80242,
        'cost': 78000000,
        'opened': datetime.dat(1976, 10, 10),
        'closed': datetime.date(2010, 1, 3),
        'architect': 'Kivett and Myers',
        },        

        {
        'stadium': 'Ohio Stadium',
        'address': '411 Woody Hayes Drive',
        'location': 'Columbus, OH',
        'capacity': 102329,
        'cost': 1340000,
        'opened': datetime.date(1922, 10, 7),
        'architect': 'Howard Dwight Smith',
        },        

        {
        'stadium':'Toyota Park',
        'address': '7000 South Harlem Avenue',
        'location': 'Chicago, IL',
        'capacity': 20000,
        'cost': 98000000,
        'opened': datetime.date(2006, 6, 11),
        'architect': 'Rossetti Architects',    
        'length': 120,
        'width': 75,
        'measure': 'yards',
        },        


        {
        'stadium': 'Jeld-Wen Field',
        'address': '1844 SW Morrison',
        'location': 'Portland, OR',
        'capacity': 20438,
        'cost': 502000,
        'opened': datetime.date(1926, 10, 9),
        'architect': 'A. E. Doyle',
        'length': 110,
        'width': 70,
        'measure': 'yards',
        },        

        {
        'stadium': 'Rio Tinto Stadium',
        'address': '9256 South State Street',
        'location': 'Sandy, UT',
        'capacity': 20213,
        'cost': 115000000,
        'opened': datetime.dat(2006, 10, 9),
        'architect': 'Rossetti Architects',
        'length': 120,
        'width': 75,
        'measure': 'yards',
        },        


        {
        'stadium': 'Spartan Stadium',
        'address': '1257 S 10th St',
        'location': 'San José, CA',
        'capacity': 30456, 
        'cost': None, 
        'opened': 1933,
        },        

        {
        'stadium': 'Foxboro Stadium',
        'address': 'Washington St. (Route 1)',
        'location': 'Foxborough, MA',
        'capacity': 60292,
        'cost': 7100000,
        'opened': datetime.date(1971, 8, 15),
        'closed': datetime.date(2002, 1, 19),
        },        

        {
        'stadium': 'Citrus Bowl',
        'address': '1610 W. Church Street',
        'location': 'Orlando, FL',
        'capacity': 70000,
        'cost': 115000,
        'opened': 1936,
        },        

        {
        'stadium': 'Silverdome',
        'address': '1200 Featherstone Road',
        'location': 'Pontiac, MI',
        'capacity': 70000,
        'cost': 55700000,
        'opened': datetime.date(1975, 8, 23),
        'architect': 'O\'Dell/Hewlett & Luckenbach',
        },        

    
        {
        'stadium': 'Robert F. Kennedy Memorial Stadium',
        'short_name': 'RFK Stadium',
        'address': '2400 East Capitol St. SE',
        'location': 'Washington, D.C.',
        'capacity': 46000,
        'cost': 24000000,
        'opened': datetime.date(1961, 10, 1),
        },        

        {
        'stadium': 'Stanford Stadium',
        'address': '625 Nelson Rd',
        'location': 'Stanford, CA',
        'capacity': 50000,
        'cost': 200000,
        'opened': datetime.date(1921, 10, 1),
        'renovations': [(datetime.date(2006, 9, 16), 90000000), ],
        },        

    

        {
        'stadium': 'FedEx Field',
        'address': '1600 FedEx Way',
        'location': 'Landover, MD',
        'capacity': 91000,
        'cost': 250500000
        'opened': datetime.date(1997, 9, 14),
        },        

    

        {
        'stadium': 'WakeMed Soccer Park', 
        'address': '201 Soccer Park Drive',
        'location': 'Cary, NC',
        'capacity': 10000,
        'cost': 14500000,
        'opened': 2002,
        },        

        {
        'stadium': 'Polo Grounds', 
        'address': 'West 155th Street and Eighth Avenue',
        'location': 'Manhattan, NY',
        'capacity': 55000,
        'opened': datetime.date(1890, 8, 19),
        'closed': 1963,
        },        

        {
        'stadium': 'Veterans Memorial Stadium',
        'address': '5000 East Lew Davis Street',
        'location': 'Long Beach, CA',
        'capacity': 11600,
        'opened': 1948,
        },        


        {
        'stadium': 'Varsity Stadium',
        'address': '299 Bloor Street West',
        'location': 'Toronto',
        'opened': 1898,
        'cost': 617000000,
        },        


        {
        'stadium': 'Wrigley Field',
        'location': 'Los Angeles, CA',
        'opened': 1925,
        'closed': 1965,
        },        

        {
        'stadium': 'Memorial Coliseum',
        'address': '3911 South Figueroa Street',
        'location': 'Los Angeles, CA',
        'opened': datetime.date(1923, 5, 1),
        'cost': 954872.98
        'capacity': 11600,
        },        

    {
        'stadium': 'Estadio Azteca',
        'address': 'Calzada de Tlalpan 3665'
        'location': 'Mexico City, Mexico',
        'capacity': 104000,
        'opened': datetime.date(1966, 5, 29),
        'cost': 260000000
        'denomination': 'pesos',
        },        
    
    {
        'stadium': 'Candlestick Park',
        'address': '490 Jamestown Avenue',
        'location': 'San Francisco, CA',
        'opened': datetime.date(1960, 4, 12),
        'cost': 15000000,
        'architect': 'John Bolles',
        'capacity': 69732,
        },

    {
        'stadium': 'Yankees Stadium',
        'address': 'East 161st St and River Ave',
        'location': 'Bronx, NY',
        'opened': datetime.date(1921, 4, 18),
        'cost': 2400000,
        'architect': 'Osborn Engineering Corporation',
        },

    {
        'stadium': 'Seattle High School Memorial Stadium',
        'address': '401 5th Ave N',
        'location': 'Seattle, WA',
        'opened': 1947,
        'architect': 'George Stoddard',
        'capacity': 17000,
        },

    {
        'stadium': 'Empire Stadium',
        'address': 'East Hastings Street',
        'location': 'Vancouver',
        'opened': 1954,
        'closed': 1993,
        'capacity': 32729,
            
        },
    {
        'stadium': 'Hofstra Stadium',
        'address': '225 Hofstra University',
        'location': 'Hempstead, NY',
        'opened': 1962,
        'capacity': 15000,
        },
    {
        'stadium': 'Kingdome',
        'address': '201 S. King Street',
        'location': 'Seattle, WA',
        'opened': datetime.date(1976, 3, 27),
        'architect': 'Naramore, Skilling & Praeger',
        },
    {
        'stadium': 'Busch Memorial Stadium',
        'address': '250 Stadium Plaza',
        'location': 'St. Louis, MO',
        'opened': datetime.date(1966, 5, 12),
        'closed': datetime.date(2005, 10, 19),
        'cost': 55000000,
        'architect': 'Sverdrup & Parcel',
        'capacity': 60292,
        },
    {
        'stadium': 'Tampa Stadium',
        'address': '4201 North Dale Mabry Highway',
        'location': 'Tampa, FL',
        'opened': datetime.date(1967, 11, 4),
        'closed': datetime.date(1998, 9, 13),
        'cost': 4400000,
        'architect': 'Watson & Company Architects',
        'capacity': 74301,
        },

    {
        'stadium': 'Sports Authority Field at Mile High',
        'address': '1701 Mile High Stadium Circle',
        'location': 'Denver, CO',
        'opened': datetime.date(2001, 9, 10),
        'cost': 400700000,
        'architect': 'HNTB',
        'capacity': 76125,
        },

    {
        'stadium': 'Mile High Stadium',
        'address': '2755 West 17th Avenue',
        'location': 'Denver, CO',
        'opened': datetime.date(1948, 8, 14),
        'closed': datetime.date(2000, 12, 23),
        'cost': 500000,
        'architect': 'Stanley E. Morse',
        'capacity': 76273,
        },

    {
        'stadium': 'Oakland-Alameda County Coliseum'
        'address': '7000 Coliseum Way',
        'location': 'Oakland, CA',
        'opened': datetime.date(1966, 9, 18),
        'cost': 25500000,
        'architect': 'Skidmore, Owings and Merrill',
        'capacity': 63026,
        },

    {
        'stadium': 'Raymond James Stadium',
        'address': '4201 N. Dale Mabry Highway',
        'location': 'Tampa, FL',
        'opened': datetime.date(1998, 9, 20),
        'cost': 168500000,
        'architect': 'HOK Sport',
        'capacity': 65857,
        },

    {
        'stadium': 'Rice-Eccles Stadium',
        'address': '451 South 1400 East',
        'location': 'Salt Lake City, Utah',
        'opened': datetime.date(1998, 9, 12),
        'cost': 50000000,
        'architect': 'FFKR Architects',
        'capacity': 45017
        },

    {
        'stadium': 'Robertson Stadium',
        'address': '3874 Holman Street',
        'location': 'Houston, TX',
        'opened': datetime.date(1948, 8, 14),
        'cost': 650000,
        'architect': 'Harry D. Payne',
        'capacity': 32000,
        },

    {
        'stadium': 'BBVA Compass Stadium',
        'address': 'East End',
        'location': 'Houston, TX',
        'cost': 95000000,
        'architect': 'Populous',
        'capacity': 22000,
        },

    {
        'stadium': 'BC Place',
        'address': '777 Pacific Boulevard',
        'location': 'Vancouver',
        'opened': datetime.date(1983, 6, 19),
        'cost': 126100000
        'denomination': 'Canadian dollars',
        'architect': 'Studio Phillips Barratt, Ltd',
        'capacity': 54320,
        },

    {
        'stadium': 'Sanford Stadium',
        'address': 'Sanford Dr and Field St',
        'location': 'Athens, GA',
        'opened': datetime.date(1929, 10, 12),
        'cost': 360000,
        'architect': 'TC Atwood',
        'capacity': 92746,
        },

    {
        'stadium': 'Legion Field',
        'address': '400 Graymont Avenue West',
        'location': 'Birmingham, AL',
        'opened': datetime.date(1927, 11, 19),
        'cost': 439000,
        'architect': 'D.O. Whildin',
        'capacity': 71594,
        },

    {
        'stadium': 'Cowboys Stadium',
        'address': '1 Legends Way',
        'location': 'Arlington, TX',
        'opened': datetime.date(2009, 5, 27),
        'cost': 1300000000,
        'architect': 'HKS, Inc.',
        'capacity': 80000,
        },

    {
        'stadium': 'MetLife Stadium',
        'address': 'One MetLife Stadium Drive',
        'location': 'East Rutherford, NJ',
        'opened': datetime.date(2010, 4, 10),
        'cost': 1600000000,
        'architect': '360 Architecture',
        'capacity': 82566,
        },

    {
        'stadium': 'M&T Bank Stadium',
        'address': '1101 Russell Street',
        'location': 'Baltimore, MD',
        'opened': datetime.date(1998, 9, 6),
        'cost': 220000000,
        'architect': 'HOK Sport',
        'capacity': 71008,
        },

    {
        'stadium': 'Reliant Stadium',
        'address': 'One Reliant Park',
        'location': 'Houston, TX',
        'opened': datetime.date(2002, 8, 24),
        'cost': 352000000,
        'architect': 'HOK Sport',
        'capacity': 71054,
        },

    {
        'stadium': 'Sun Life Stadium',
        'address': '2267 NW 199th Street',
        'location': 'Miami Gardens, FL',
        'opened': datetime.date(1985, 12, 1),
        'cost': 115000000,
        'architect': 'HOK Sport',
        'capacity': 74918,
        },

    {
        'stadium': 'Qualcomm Stadium',
        'address': '9449 Friars Road',
        'location': 'San Diego, CA',
        'opened': datetime.date(1967, 8, 20),
        'cost': 27000000,
        'architect': 'Frank L. Hope and Associates',
        'capacity': 70561,
        },

    {
        'stadium': 'Lincoln Financial Field',
        'address': '1020 Pattison Avenue',
        'location': 'Philadelphia, PA',
        'opened': datetime.date(2003, 8, 3),
        'cost': 512000000,
        'architect': 'NBBJ',
        'capacity': 68532,
        },


    {
        'stadium': 'Gillette Stadium',
        'address': '1 Patriot Place',
        'location': 'Foxborough, MA',
        'opened': datetime.date(2002, 9, 9)
        'cost': 325000000,
        'architect': 'Populous',
        'capacity': 68756,
        },


    {
        'stadium': 'BMO Field',
        'address': '170 Princes Boulevard',
        'location': 'Toronto',
        'opened': datetime.date(2007, 4, 20),
        'cost': 62900000,
        'denomination': 'Canadian dollars',
        'architect': 'Brisbin Brooks Beynon Architects ',
        'capacity': 21859,
        },

    {
        'stadium': 'Buck Shaw Stadium',
        'address': '500 El Camino Real',
        'location': 'Santa Clara, CA',
        'opened': datetime.date(1962, 9, 22),
        'capacity': 10525,
        },


    {
        'stadium': 'CenturyLink Field',
        'address': '800 Occidental Ave S',
        'location': 'Seattle, WA',
        'opened': datetime.date(2008, 7, 28),
        'cost': 430000000,
        'architect': 'Ellerbe Becket',
        'capacity': 67000
        },

    {
        'stadium': 'Dick\'s Sporting Goods Park',
        'address': '6000 Victory Way',
        'location': 'Commerce City, CO',
        'opened': datetime.date(2005, 9, 28),
        'cost': 131000000,
        'architect': 'HOK Sport',
        'capacity': 18086,
        },

    {
        'stadium': 'Livestrong Sporting Park',
        'address': 'One Sporting Way',
        'location': 'Kansas City, KS',
        'opened': datetime.date(2011, 6, 9),
        'cost': 200000000,
        'architect': 'NBBJ',
        'capacity': 18467,
        },

    {
        'stadium': 'PPL Park',
        'address': '1 Stadium Drive',
        'location': 'Chester, PA',
        'opened': datetime.date(2010, 6, 27),
        'cost': 120000000,
        'architect': 'Rossetti Architects',
        'capacity': 18500,
        },

    {
        'stadium': 'Red Bull Arena',
        'address': '600 Cape May Street',
        'location': 'Harrison, NJ',
        'opened': datetime.date(3, 20, 2010)
        'cost': 200000000,
        'architect': 'Rossetti Architects',
        'capacity': 25000,
        },

    {
        'stadium': 'Bank of America Stadium'
        'address': '800 South Mint Street',
        'location': 'Charlotte, NC',
        'opened': datetime.date(1996, 9, 14),
        'cost': 248000000,
        'architect': 'HOK Sport',
        'capacity': 73778,
        },

    {
        'stadium': 'University of Phoenix Stadium',
        'address': '1  Cardinals Drive',
        'location': 'Glendale, AZ',
        'opened': datetime.date(2006, 8, 1),
        'cost': 455000000,
        'architect': 'Eisenman Architects',
        'capacity': 63400,
        },

    {
        'stadium': 'Invesco Field', 
        'address': 'Georgia Dome',
        'location': 'Atlanta, GA',
        'opened': datetime.date(1992, 9, 6),
        'cost': 214000000,
        'architect': 'Heery International',
        'capacity': 71228,
        },

    {
        'stadium': 'Anaheim Stadium',
        'address': '2000 Gene Autry Way',
        'location': 'Anaheim, CA',
        'opened': datetime.date(1966, 4, 19),
        'cost': 24000000,
        'architect': 'Noble W. Herzberg and Associates ',
        'capacity': 45957,
        },

    {
        'stadium': 'Metropolitan Stadium',
        'address': '8000 Cedar Ave. South',
        'location': 'Bloomington, MN',
        'opened': datetime.date(1956, 4, 24),
        'cost': 8500000,
        'architect': 'Tepper Engineering',
        'capacity': 48446,
        },

    {
        'stadium': 'Yale Bowl',
        'address': '81 Central Avenue',
        'location': 'New Haven, CT',
        'opened': datetime.date(1914, 11, 21),
        'cost': 750000,
        'architect': 'Charles A. Ferry',
        'capacity': 64246,
        },


    {
        'stadium': 'Veterans Stadium',
        'address': '3501 South Broad Street',
        'location': 'Philadelphia, PA',
        'opened': datetime.date(1971, 4, 10),
        'cost': 50000000,
        'architect': 'Hugh Stubbins and Associates',
        'capacity': 65386,
        },

    {
        'stadium': 'Franklin Field',
        'address': 'South 33rd and Spruce Streets',
        'location': 'Philadelphia, PA',
        'opened': datetime.date(1895, 4, 20)
        'cost': 100000,
        'architect': 'Frank Miles Day & Brother',
        'capacity': 52593,
        },

    {
        'stadium': 'Citi Field',
        'address': '126th St. & Roosevelt Ave',
        'location': 'Flushing, NY',
        'opened': datetime.date(2009, 3, 29),
        'cost': 900000000,
        'architect': 'Populous',
        'capacity': 41922,
        },

    {
        'stadium': 'Comiskey Stadium',
        'address': '324 West 35th St',
        'location': 'Chicago, IL',
        'opened': datetime.date(1910, 7, 1),
        'closed': datetime.date(1990, 9, 30),
        'cost': 750000,
        'architect': 'Zachary Taylor Davis',
        'capacity': 43951,
        },

    {
        'stadium': 'Texas Stadium',
        'address': '2401 East Airport Freeway',
        'location': 'Irving, TX',
        'opened': datetime.date(1971, 9, 17),
        'closed': datetime.date(2008, 12, 20),
        'cost': 35000000,
        'architect': 'A. Warren Morey',
        'capacity': 41922,
        },

    {
        'stadium': 'AT&T Park',
        'address': '24 Willie Mays Plaza',
        'location': 'San Francisco, CA',
        'opened': datetime.date(2000, 3, 31),
        'cost': 357000000,
        'architect': 'Populous',
        'capacity': 40930,
        },

    {
        'stadium': 'Safeco Field',
        'address': '1516 First Avenue South',
        'location': 'Seattle, WA',
        'opened': datetime.date(1999, 7, 15),
        'cost': 517600000,
        'architect': 'NBBJ',
        'capacity': 47878,
        },

    {
        'stadium': 'Alamodome',
        'address': '100 Montana Street',
        'location': 'San Antonio, TX',
        'opened': datetime.date(1990, 11, 5),
        'cost': 186000000,
        'architect': 'Populous',
        'capacity': 65000,
        },

    {
        'stadium': 'Rentschler Field'
        'address': '615 Silver Lane',
        'location': 'East Hartford, CT',
        'opened': datetime.date(2003, 8, 30),
        'cost': 91200000,
        'architect': 'Ellerbe Becket',
        'capacity': 40000,
        },

    {
        'stadium': 'High Point Solutions Stadium',
        'address': '1 Scarlet Knight Way',
        'location': 'Piscataway, NJ',
        'opened': datetime.date(1994, 9, 3),
        'cost': 28000000,
        'architect': 'GSGSBH',
        'capacity': 52454,
        },

    {
        'stadium': 'Wrigley Field',
        'address': '1060 West Addison Street',
        'location': 'Chicago, IL',
        'opened': datetime.date(1914, 4, 23)
        'cost': 250000,
        'architect': 'Zachary Taylor Davis',
        'capacity': 41159,
        },

    {
        'stadium': 'Cardinal Stadium',
        'address': '937 Phillips Lane',
        'location': 'Louisville, KY',
        'opened': 1957,
        'capacity': 47925,
        },

    {
        'stadium': 'Astrodome',
        'address': '8400 Kirby Drive',
        'location': 'Houston, TX',
        'opened': datetime.date(1965, 4, 9),
        'cost': 35000000,
        'architect': 'Hermon Lloyd & W.B. Morgan',
        'capacity': 62439,
        },

    {
        'stadium': 'Chase Field',
        'address': '401 East Jefferson Street',
        'location': 'Phoenix, AZ',
        'opened': datetime.date(1998, 3, 31),
        'cost': 354000000,
        'architect': 'Ellerbe Becket',
        'capacity': 48633,
        },

    {
        'stadium': 'Fenway Park',
        'address': '4 Yawkey Way',
        'location': 'Boston, MA',
        'opened': datetime.date(1912, 4, 20),
        'cost': 650000,
        'architect': 'James McLaughlin',
        'capacity': 37493,
        },

    {
        'stadium': 'Shea Stadium',
        'address': '123-01 Roosevelt Avenue',
        'location': 'Flushing, NY',
        'opened': datetime.date(1964, 4, 17),
        'cost': 28500000,
        'architect': 'Praeger-Kavanagh-Waterbury',
        'capacity': 60372,
        },

    {
        'stadium': 'Skelly Field at H. A. Chapman Stadium',
        'address': 'S Florence & E 8th',
        'location': 'Tulsa, OK',
        'opened': datetime.date(1930, 10, 4),
        'cost': 275000,
        'architect': 'Robert H. Hienbrenáer',
        'capacity': 30000,
        },

    {
        'stadium': 'Shibe Park',
        'address': 'N 21st St & W Lehigh Ave,',
        'location': 'Philadelphia, PA',
        'opened': datetime.date(1909, 4, 12),
        'closed': datetime.date(1970, 10, 1),
        'cost': 301000,
        'architect': 'William Steele and Sons',
        'capacity': 33608, 
        },

    {
        'stadium': 'Ebbets Field',
        'address': '55 Sullivan Place',
        'location': 'Brooklyn, NY',
        'opened': datetime.date(1913, 4, 9),
        'closed': datetime.date(1960, 2, 23),
        'cost': 750000,
        'architect': 'Clarence Randall Van Buskirk',
        'capacity': 31902,
        },

    {
        'stadium': 'Cleveland Browns Stadium',
        'address': '100 Alfred Lerner Way',
        'location': 'Cleveland, OH',
        'opened': datetime.date(1999, 9, 12),
        'cost': 349000000,
        'architect': 'HOK Sport',
        'capacity': 73200,
        },


    {
        'stadium': 'Navy-Marine Corps Stadium',
        'address': 'Rowe Blvd & Taylor Ave',
        'location': 'Annapolis, MD',
        'opened': 1959,
        'cost': 3000000,
        'capacity': 34000,
        },


    {
        'stadium': 'LP Field',
        'address': '1 Titans Way',
        'location': 'Nashville, TN',
        'opened': datetime.date(1999, 8, 27),
        'cost': 290000000,
        'architect': 'Populous',
        'capacity': 69143,
        },


    {
        'stadium': 'Ford Field',
        'address': '2000 Brush Street',
        'location': 'Detroit, MI',
        'opened': datetime.date(2002, 8, 24),
        'cost': 430000000,
        'architect': 'SHG, Inc.',
        'capacity': 65000,
        },


    {
        'stadium': 'Harvard Stadium',
        'address': '95 N Harvard St',
        'location': 'Boston, MA',
        'opened': datetime.date(1904, 11, 14),
        'cost': 310000,
        'architect': 'Louis J. Johnson',
        'capacity': 30323,
        },


    {
        'stadium': 'Atlanta-Fulton County Stadium',
        'address': '521 Capitol Avenue SE',
        'location': 'Atlanta, GA',
        'opened': datetime.date(1965, 4, 12),
        'cost': 18000000,
        'architect': 'Heery & Heery',
        'capacity': 60606,
        },


    {
        'stadium': 'Downing Stadium',
        'address': 'Randall\'s Island',
        'location': 'New York, NY',
        'opened': datetime.date(1936, 7, 11),
        'closed' :2002,
        'architect': 'Robert Moses',
        'capacity': 22000,
        },


    {
        'stadium': 'Heinz Field',
        'address': '100 Art Rooney Avenue',
        'location': 'Pittsburgh, PA',
        'opened': datetime.date(2001, 8, 18),
        'cost': 281000000,
        'architect': 'HOK Sport',
        'capacity': 65050,
        },


    {
        'stadium': 'Tara Stadium',
        'address': '1055 Battle Creek Rd',
        'location': 'Jonesboro, GA',
        },


    {
        'stadium': 'Taylor Field',
        'location': 'Bethlehem, PA',
        },


    {
        'stadium': 'ONT AA Grounds',
        'location': 'Kearny, NJ',
        },


    {
        'stadium': 'Domestic Baseball Grounds',
        'locations': 'Newark, NJ',
        },


    {
        'stadium': 'Emmet Street Grounds',
        'location': 'Newark, NJ',
        },
    {
        'stadium': 'Olympic Grounds',
        'location': 'Paterson, NJ',
        },
    {
        'stadium': 'Cricket Grounds',
        'location': 'Trenton, NJ',
        },
    {
        'stadium': 'Frelinghuysen Grounds',
        'location': 'Newark, NJ',
        },
    {
        'stadium': 'Elysian Fields',
        'location': 'Hoboken, NJ',
        },
    {
        'stadium': 'Federal League Baseball Grounds',
        'location': 'Harrison, NJ',
        },
    {
        'stadium': 'Athletic Field',
        'location': 'Fall River, MA',
        },
    {
        'stadium': 'Handlan\'s Park',
        'location': 'St. Louis, MO',
        },
    {
        'stadium': 'Federal League Park',
        'location': 'St. Louis, MO',
        },
    {
        'stadium': 'Fall River Athletic Field',
        'location': 'Fall River, MA',
        },
    {
        'stadium': 'High School Field',
        'location': 'St. Louis, MO',
        },
    {
        'stadium': 'Mark\'s Stadium',
        'location': 'Tiverton, RI',
        'opened': 1922,
        'capacity': 15000,
        },
    {
        'stadium': 'University of Detroit Stadium',
        'location': 'Detroit, MI',
        'capacity': 25000,
        
        },
    {
        'stadium': 'Lonsdale Avenue Grounds',
        'location': 'Pawtucket, RI',
        },
    {
        'stadium': 'Sportsman\'s Park',
        'address': '2911 N Grand Blvd',
        'location': 'St. Louis, MO',
        'opened': datetime.date(1902, 4, 23),
        'closed': datetime.date(1966, 5, 8),
        'cost': 300000,
        'capacity': 30500,
        },
    {
        'stadium': 'Dexter Park',
        'location': 'Queens, NY',

        },
    {
        'stadium': 'Luna Park',
        'location': 'Cleveland, OH',
        },
    {
        'stadium': 'Sparta Field',
        'location': 'Chicago, IL',
        },
    {
        'stadium': 'DePaul Field',
        'location': 'Chicago, IL',
        },
    {
        'stadium': 'Mills Stadium',
        'location': 'Chicago, IL',
        'opened': 1913,
        'closed': 1941,
        'capacity': 10000,
        'source': 'http://www.projectballpark.org/history/nnl1/alt/pyotts.html',
        },
    {
        'stadium': 'Starlight Pakr',
        'location': 'Bronx, NY',
        'opened': 1918,
        'closed': 1932,
        },
    {
        'stadium': 'Commercial Field',
        'address': 'Albany Avenue',
        'location': 'Brooklyn, NY',
        'opened': 1906,
        
        },
    {
        'stadium': 'Walsh Memorial Stadium',
        'address': '5200 Oakland Ave',
        'location': 'St. Louis, MO',
        'opened': 1930,
        
        },
    {
        'stadium': 'Newark Schools Stadium',
        'address': '450 Bloomfield Avenue',
        'location': 'Newark, NJ',
        'opened': 1925,
        'closed': 2009,
        'capacity': 15000,
        },

    {
        'stadium': 'Rifle Club Grounds',
        'location': 'Philadelphia, PA',
        },
    {
        'stadium': 'Bridgeville Park',
        'location': 'Bridgeville, PA',
        },
    {
        'stadium': 'Bugle Field',
        'location': 'Baltimore, MD',
        },
    {
        'stadium': 'Legion Field',
        'location': 'Donora, PA',
        },
    {
        'stadium': 'Shaw Field',
        'location': 'Cleveland, HO',
        },
    {
        'stadium': 'Holmes Stadium',
        'location': 'Philadelphia, PA',
        },
    {
        'stadium': 'Metropolitan Oval',
        'location': 'Queens, NY',
        'opened': 1925,
        },
    {
        'stadium': 'Sterling Oval',
        'location': 'Bronx, NY',
        },
    {
        'stadium': 'Freeport Road Field',
        'location': 'Pittsburgh, PA',
        },
    {
        'stadium': 'Rancho La Cienga Stadium',
        'location': 'Los Angeles, CA',
        },
    {
        'stadium': 'Edison Field',
        'location': 'Philadelphia, PA',
        },
    {
        'stadium': 'Freeport Road Field',
        'location': 'Pittsburgh, PA',
        },
    {
        'stadium': 'Eintracht Oval',
        'location': 'Queens, NY',
        },
    {
        'stadium': 'Cambria Field',
        'location': 'Philadelphia, PA',
        },
    {
        'stadium': 'Hanson Stadium',
        'location': 'Chicago, IL',
        },
    {
        'stadium': 'PAL Stadium',
        'location': 'San Jose, CA',
        },
    {
        'stadium': 'Daniels Field',
        'location': 'San Pedro, CA',
        },
    {
        'stadium': 'PAL Stadium',
        'location': 'San Jose, CA',
        },
    {
        'stadium': 'Jackie Robinson Field',
        'location': 'Los Angeles, CA',
        },
    {
        'stadium': 'St. Louis Soccer Park'
        'location': 'Fenton, MO',
        },
    {
        'stadium': 'Kuntz Stadium',
        'location': 'Indanapolis, IN',
        },
    {
        'stadium': 'Brooklyn College',
        'location': 'Brooklyn, NY',
        },
    {
        'stadium': 'Indianapolis Soccer Stadium',
        'location': 'Indianapolis, IN',
        },
    {
        'stadium': 'PAL Stadium',
        'location': 'San Jose, CA',
        },

    {
        'stadium': 'Cleveland Browns Stadium',
        'address': '100 Alfred Lerner Way',
        'location': 'Cleveland, Ohio ',
        'opened': datetime.date(1999, 9, 12),
        'cost': 349000000,
        'architect': 'HOK Sport',
        'capacity': 73200,
        },


    {
        'stadium': 'Coates Field',
        'location': 'Pawtucket, RI',
        },


    {
        'stadium': 'Memorial Stadium Baltimore',
        'address': '900 East 33rd Street',
        'location': 'Balitmore, MD',
        'opened': datetime.date(1922, 12, 2),
        'closed': datetime.date(1997, 12, 14),
        'cost': 6500000,
        'capacity': 53371,
        'architect': 'L.P. Kooken Company',
        },  
  {
        'stadium': 'McMahon Stadium',
        'address': '1817 Crowchild Trail NW',
        'location': 'Calgary, Alberta',
        'opened': 1960,
        'cost': 1050000,
        'denomination': 'Canadian dollars',
        'capacity': 35650,
        'architect': 'Rule Wynn and Rule',
        },  
  {
        'stadium': 'Memorial Stadium Baltimore',
        'address': '900 East 33rd Street',
        'location': 'Balitmore, MD',
        'opened': datetime.date(1922, 12, 2),
        'closed': datetime.date(1997, 12, 14),
        'cost': 6500000,
        'capacity': 53371,
        'architect': 'L.P. Kooken Company',
        }, 
   {
        'stadium': 'Memorial Stadium Baltimore',
        'address': '900 East 33rd Street',
        'location': 'Balitmore, MD',
        'opened': datetime.date(1922, 12, 2),
        'closed': datetime.date(1997, 12, 14),
        'cost': 6500000,
        'capacity': 53371,
        'architect': 'L.P. Kooken Company',
        },


    {
        'stadium': 'Cleveland Stadium',
        'address': '1085 West 3rd Street',
        'location': 'Cleveland, OH',
        'opened': datetime.date(1931, 7, 1),
        'closed': datetime.date(1995, 12, 17),
        'cost': 3000000,
        'architect': 'Walker & Weeks',
        'capacity': 81000,
        },
    {
        'address': '10000 Hillcrest',
        'stadium': 'Franklin Stadium',
        'location': 'Dallas, TX',
        'opened': 1954,
        'capacity': 8500,
        },
    {
        'stadium': 'Ownby Stadium',
        'address': '5800 Ownby Dr',
        'location': 'Dallas, TX',
        'opened': 1926,
        'closed': 1988,
        'capacity': 23783,
        
        },
    {
        'stadium': 'Tigers Stadium',
        'address': '2121 Trumbull Street',
        'location': 'Detroit, MI',
        'opened': datetime.date(1912, 4, 20),
        'closed': datetime.date(1999, 9, 27),
        'capacity': 52416,
        'architect': 'Osborn Engineering',
        'cost': 300000,
        },
    {
        'stadium': 'Gator Bowl',
        'address': '1 Gator Bowl Boulevard',
        'location': 'Jacksonville, FL',
        'opened': 1928,
        'closed': 1994,
        'capacity': 80126,
        },
    {
        'stadium': 'Kansas City Municipal Stadium',
        'address'; '22nd St. and Brooklyn Ave',
        'location': 'Kansas City, MO',
        'opened': datetime.date(1923, 7, 3),
        'closed': 1976,
        'cost': 400000,
        'architect': 'Osborn Engineering',
        'capacity': 35561,
        },
    {
        'stadium': 'Metrodome',
        'address'; '900 South 5th Street',2
        'location': 'Minneapolis, MN',
        'opened': datetime.date(1982, 4, 3),
        'cost': 68000000,
        'architect': 'Skidmore, Owings & Merrill',
        'capacity': 64111,
        },
    {
        'stadium': 'Miami Orange Bowl',
        'address'; '1501 NW 3rd Street',
        'location': 'Miami, FL',
        'opened': datetime.date(1937, 12, 10),
        'closed': datetime.date(2008, 1, 26),
        'cost': 340000,
        'capacity': 72319,
        },
    {
        'stadium': 'Tamiami Park',
        'address'; '11201 Southwest 24th Street',
        'location': 'Miami, FL',
        },
    {
        'stadium': 'Autostade',
        'address'; '475 av. Des Pins Ouest',
        'location': 'Montreal',
        'capacity': 33172,
        },
    {
        'stadium': 'Olympic Stadium',
        'address'; '4545 Pierre de Coubertin Avenue',
        'location': 'Montreal, Quebec',
        'opened': datetime.date(1973, 4, 28)
        'cost': 770000000,
        'denomination': 'Canadian Dollars',
        'architect': 'Roger Taillibert',
        'capacity': 66308,
        },
    {
        'stadium': 'Holleder Memorial Stadium',
        'location': 'Rochester, NY',
        'capacity': 20000,
        },
    {
        'stadium': 'Valley View Casino Center',
        'address'; '3500 Sports Arena Boulevard',
        'location': 'San Diego, CA',
        'opened': datetime.date(1965, 11, 18),
        'cost': 6400000,
        'architect': 'Mark L. Faddis',
        'capacity': 12000,
        },
    {
        'stadium': 'Aztec Bowl',
        'address'; '5300 Campanile Dr',
        'location': 'San Diego, CA',
        'opened': datetime.date(1936, 10, 3),
        },


    {
        'stadium': 'Sam Boyd Stadium',
        'address'; '7000 East Russell Road',
        'location': 'Las Vegas, NV',
        'opened': datetime.date(1971, 10, 23),
        'cost': 3500000,
        'capacity': 36800,
        },


    {
        'stadium': 'Liberty Bowl Memorial Stadium',
        'address'; '335 South Hollywood Street',
        'location': 'Memphis, TN',
        'opened': datetime.date(1965, 9, 16)
        'cost': 3700000,
        'architect': 'Yeates, Gaskill & Rhodes',
        'capacity': 61008,
        },


    {
        'stadium': 'Alamo Stadium',
        'address'; '110 Tuleta Dr',
        'location': 'San Antonio, TX',
        'opened': 1940,
        'cost': 500000,
        'architect': 'Phelps & Dewees & Simmons',
        'capacity': 23000,
        },


    {
        'stadium': 'Aloha Stadium',
        'address'; '99-500 Salt Lake Blvd',
        'location': 'Honolulu, HI',
        'opened': datetime.date(1975, 9, 12),
        'cost': 3700000,
        'architect': 'The Luckman Partnership',
        'capacity': 50000,
        },


    {
        'stadium': 'Kansas City Municipal Stadium',
        'address'; '22nd St. and Brooklyn Ave',
        'location': 'Kansas City, MO',
        'opened': datetime.date(1923, 7, 3),
        'closed': 1976,
        'cost': 400000,
        'architect': 'Osborn Engineering',
        'capacity': 35561,
        },






    

]        

    


    


