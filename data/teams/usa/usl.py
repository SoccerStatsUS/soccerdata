#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime

l = [

    {
        'name': 'Northern Virginia Royals',
        'city': 'Manassas, VA',
        'founded': 1998,
        },
    {
        'name': 'Real Maryland Monarchs',
        'city': 'Rockville, MD',
        'founded': 2007,
        },
    {
        'name': 'Virginia Beach Piranhas',
        'city': 'Virginia Beach, VA',
        'founded': 2006,
        },
    {
        'name': 'Fredericksburg Hotspur',
        'city': 'Fredericksburg, VA',
        'founded': 2010,
        },
    {
        'name': 'Laredo Heat',
        'city': 'Laredo, TX',
        'founded': 2004,
        },
    {
        'name': 'Baton Rouge Capitals',
        'city': 'Baton Rouge, LA',
        'founded': 2007,
        },
    {
        'name': 'West Texas United Sockers',
        'city': 'Midland, TX',
        'founded': 2008
        },

    {
        'name': 'Mississippi Brilla',
        'city': 'Jackson, MI',
        'founded': 2006,
        },

    {
        'name': 'Reno Rattlers',
        'city': 'Reno, NV',
        'founded': 1994,
        'dissolved': 1998,
        },

    {
        'name': 'Kitsap Pumas',
        'city': 'Bremerton, WA',
        'founded': 2008,
        },

    {
        'name': 'Ogden Outlaws',
        'city': 'Ogden, UT',
        'founded': 2006,
        },

    {
        'name': 'Colorado Foxes',
        'city': 'Commerce City, CO',
        },

    {
        'name': 'Hawaii Tsunami',
        'city': 'Honolulu, Hawaii',
        },

    {
        'name': 'California Jaguars',
        'city': 'Salinas, CA',
        },

    {
        'name': 'North Jersey Imperials',
        'city': 'Paramus, NJ',
        },

    {
        'name': 'Long Island Rough Riders',
        'city': 'South Huntington, NY',
        },

    {
        'name': 'Raleigh Flyers',
        'city': 'Raleigh, NC',
        },

    {
        'name': 'Richmond Kickers',
        'city': 'Richmond, VA',
        },

    {
        'name': 'Virginia Beach Mariners',
        'city': 'Virginia Beach, VA',
        },

    {
        'name': 'Los Angeles Salsa',
        'city': 'Fullerton, CA',
        },

    {
        'name': 'Cascade Surge',
        'city': 'Salem, OR',
        },


    {
        'name': 'Montclair Falcons',
        'city': 'Montclair, CA',
        },

    {
        'name': 'North Bay Breakers',
        'city': 'Santa Rosa, CA',
        },

    {
        'name': 'St. Louis Knights',
        'city': 'St. Louis, MO',
        },

    {
        'name': 'New Orleans Riverboat Gamblers',
        'city': 'New Orleans, MO',
        },

    {
        'name': 'Cocoa Expos',
        'city': 'Cocoa, FL',
        },


    {
        'name': 'Charleston Battery',
        'city': 'Charleston, SC',
        },

    {
        'name': 'Seattle BigFoot',
        'city': 'Seattle, WA',
        },

    {
        'name': 'Rockford Raptors',
        'city': 'Rockford, IL',
        },

    {
        'name': 'Jersey Dragons',
        'city': 'Hoboken, NJ',
        },

    {
        'name': 'San Diego Top Guns',
        'city': 'San Diego, CA',
        },


    {
        'name': 'New York Centaurs',
        'city': 'New York, NY',
        'founded': 1995,
        'dissolved': 1995,
        # Technically, the Centaurs absorbed the Fever.
        },


    {
        'name': 'New York Fever',
        'city': 'New York, NY',
        'founded': 1994,
        'dissolved': 1996,
        },

    {
        'name': 'Myrtle Beach Boyz',
        'city': 'Myrtle Beach, SC',
        'founded': 1995,
        'dissolved': 1995,
        },

    {
        'name': 'Pittsburgh Riverhounds',
        'city': 'Pittsburgh, PA',
        'founded': 1999,
        },

    {
        'name': 'Lehigh Valley Steam',
        'city': 'Lehigh Valley, PA',
        'founded': 1999,
        'dissolved': 1999,
        },

    {
        'name': 'Minnesota Thunder',
        'city': 'Blaine, MN',
        'founded': 1990,
        'dissolved': 2009,
        },

    {
        'name': 'Orange County Blue Star', 
        'city': 'Irvine, CA',
        'founded': 1997,
        },

    {
        'name': 'Twin Cities Tornado',
        'city': 'Blaine, MN',
        'founded': 1997,
        'dissolved': 2001,
        },


    {
        'name': 'Miami Breakers',
        'city': 'Miami, FL',
        'founded': 1996,
        'dissolved': 2001,
        },


    {
        'name': 'Indiana Blast',
        'city': 'Indianapolis, IN',
        'founded': 1997,
        'dissolved': 2004,
        },

    {
        'name': 'Staten Island Vipers',
        'city': 'Staten Island, NY',
        'founded': 1998,
        'dissolved': 1999,
        },

    {
        'name': 'San Francisco Seals',
        'city': 'San Francisco, CA',
        'founded': 1992,
        'dissolved': 2008,
        },

    {
        'name': 'Rochester Rhinos',
        'city': 'Rochester, NY',
        'founded': 1996,
        },
    {
        'name': 'Spokane Shadow',
        'city': 'Spokane, WA',
        'founded': 1996,
        'dissolved': 2005,
        },


    {
        'name': 'Hershey Wildcats',
        'city': 'Hershey, PA',
        'founded': 1997,
        'dissolved': 2001,
        },


    {
        'name': 'Michigan Bucks',
        'city': 'Pontiac, MI',
        'founded': 1995,
        },

    {
        'name': 'Westchester Flames',
        'city': 'New Rochelle, NY',
        'founded': 1999,
        },

    {
        'name': 'Central Coast Roadrunners',
        'city': 'San Luis Obispo, CA',
        'founded': 1996,
        'dissolved': 2002,
        },

    {
        'name': 'Boston Bulldogs',
        'city': 'Framingham, MA',
        'founded': 1996,
        'dissolved': 2001,
        },

    {
        'name': 'Brooklyn Knights',
        'city': 'Brooklyn, NY',
        'founded': 1999,
        },


    {
        'name': 'Austin Aztex',
        'city': 'Austin, TX',
        'founded': 1998,
        'dissolved': 2010,
        },

    {
        'name': 'Delaware Wizards',
        'city': 'Wilmington, DE',
        'founded': 1993,
        'dissolved': 2000,
        },

    {
        'name': 'Memphis Storm',
        'city': 'Memphis, TN',
        'founded': 1986,
        'dissolved': 1994,
        },

    {
        'name': 'Milwaukee Rampage',
        'city': 'Milwaukee, WI',
        'founded': 1994,
        'dissolved': 2002,
        },

    {
        'name': 'New Orleans Jesters',
        'city': 'New Orleans, LA',
        'founded': 2003,
        },

    {
        'name': 'Carolina Dynamo',
        'city': 'Greensboro, NC',
        'founded': 1993,
        },

    {
        'name': 'Sacramento Scorpions',
        'city': 'Sacramento, CA',
        'founded': 1996,
        'dissolved': 1997,
        },

    {
        'name': 'El Paso Patriots',
        'city': 'El Paso, TX',
        'founded': 1989,
        },

    {
        'name': 'South Carolina Shamrocks',
        'city': 'Spartansburg, SC',
        'founded': 1996,
        'dissolved': 1999,
        },

    {
        'name': 'Nashville Metros',
        'city': 'Nashville, TN',
        'founded': 1989,
        'dissolved': 2012,
        },

    {
        'name': 'New Jersey Stallions',
        'city': 'Wayne, NJ',
        'founded': 1996, 
        'dissolved': 2004,
        },

    {
        'name': 'Western Mass Pioneers',
        'city': 'Ludlow, MA',
        'founded': 1998,
        },


    {
        'name': 'Central Jersey Riptide',
        'city': 'Clark, NJ',
        'founded': 1996,
        'dissolved': 2000,
        },


    {
        'name': 'Austin Lone Stars',
        'city': 'Austin, TX',
        'founded': 1987,
        'dissolved': 2000,
        },


    {
        'name': 'Cincinnati Riverhawks',
        'city': 'Cincinnati, OH',
        'founded': 1997,
        'dissolved': 2003,
        },


    {
        'name': 'Sacramento Geckos',
        'city': 'Sacramento, CA',
        'founded': 1997,
        'dissolved': 1999,
        },



    {
        'name': 'Toronto Lynx',
        'city': 'Toronto, ON',
        'founded': 1997,
        },


    {
        'name': 'Maryland Mania',
        'city': 'Baltimore, MD',
        'founded': 1999,
        'dissolved': 1999,
        },

    {
        'name': 'Connecticut Wolves',
        'city': 'New Britain, CT',
        'founded': 1993,
        'dissolved': 2002,
        },


    {
        'name': 'Charlotte Eagles',
        'city': 'Charlotte, NC',
        'founded': 1991,
        },

    {
        'name': 'Calgary Storm',
        'city': 'Calgary, AB',
        'founded': 2001,
        'dissolved': 2004,
        },

    {
        'name': 'Syracuse Salty Dogs',
        'city': 'Syracuse, NY',
        'founded': 2003,
        'dissolved': 2004,
        },

    {
        'name': 'Milwaukee Wave United',
        'city': 'Milwaukee, WI',
        'founded': 2003,
        'dissolved': 2004,
        },


    {
        'name': 'Edmonton Aviators',
        'city': 'Edmonton, AB',
        'founded': 2003,
        'dissolved': 2004,
        },



    {
        'name': 'Carolina RailHawks',
        'city': 'Cary, NC',
        'founded': 2006,
        },



    {
        'name': 'Atlanta Silverbacks',
        'city': 'Atlanta, GA',
        'founded': 1998,
        },



    {
        'name': 'Fort Lauderdale Strikers',
        'city': 'Fort Lauderdale, FL',
        'founded': 2006,
        },



    {
        'name': 'San Francisco Bay Blackhawks',
        'city': 'San Francisco, CA',
        'founded': 1989,
        'dissolved': 1993,
        },


    {
        'name': 'Nevada Wonders',
        'city': 'Carson City, NV',
        'founded': 2003,
        },

    {
        'name': 'Fresno Fuego',
        'city': 'Fresno, CA',
        'founded': 2003,
        },

    {
        'name': 'BYU Cougars',
        'city': 'Provo, UT',
        'founded': 1980,
        },

    {
        'name': 'Southern California Seahorses',
        'city': 'La Mirada, CA',
        'founded': 2001,
        },

    {
        'name': 'Richmond Kickers Future',
        'city': 'Richmond, VA',
        'founded': 2002,
        },

    {
        'name': 'Raleigh CASL Elite',
        'city': 'Cary, NC',
        'founded': 2009,
        },

    {
        'name': 'West Virginia Chaos',
        'city': 'Charleston, WV',
        'founded': 2003,
        },

    {
        'name': 'Virginia Legacy',
        'city': 'Williamsburg, VA',
        'founded': 2001,
        'dissolved': 2009,
        },

    {
        'name': 'Chesapeake Dragons',
        'city': 'Germantown, MD',
        'founded': 2001,
        # 'dissolved': 1993, # when?
        },

    {
        'name': 'Jersey Falcons',
        'city': 'Jersey City, NJ',
        'founded': 2001,
        },

    {
        'name': 'Worcester Kings',
        'city': 'Worcester, MA',
        'founded': 2002,
        'dissolved': 2003,

        },

    {
        'name': 'Albany Admirals',
        'city': 'Albany, NY',
        'founded': 2003,
        'dissolved': 2010,
        },

    {
        'name': 'Colorado Springs Blizzard',
        'city': 'Colorado Springs, CO',
        'founded': 2004,
        'dissolved': 2006,
        },

    {
        'name': 'Cleveland Internationals',
        'city': 'Cleveland, OH',
        'founded': 2004,
        'dissolved': 2010,
        },

    {
        'name': 'San Antonio Scorpions',
        'city': 'San Antonio, TX',
        'founded': 2010,
        },

    {
        'name': 'AC St. Louis',
        'city': 'St. Louis, MO',
        'founded': 2009,
        'dissolved': 2011,
        },

    {
        'name': 'Albany Alleycats',
        'city': 'Albany, NY',
        'founded': 1995,
        'dissolved': 1999,
        },

    {
        'name': 'Birmingham Grasshoppers',
        'city': 'Birmingham, AL',
        'founded': 1992,
        'dissolved': 1996,
        },
    {
        'name': 'Central California Valley Hydra',
        'city': 'Stockton, CA',
        'founded': 1994,
        'dissolved': 1996,
        },

    {
        'name': 'Cape Cod Crusaders',
        'city': 'Buzzards Bay, MA',
        'founded': 1994,
        'dissolved': 2008,
        },


    {
        'name': 'Utah Blitzz',
        'city': 'Salt Lake City, UT',
        'founded': 2000,
        'dissolved': 2004,
        },


    {
        'name': 'Yakima Reds',
        'city': 'Yakima, WA',
        'founded': 1995,
        'dissolved': 2010,
        },



    {
        'name': 'San Diego Flash',
        'city': 'San Diego, CA',
        'founded': 1998,
        },

    {
        'name': 'Minnesota United FC',
        'city': 'Blaine, MN',
        'founded': 2010,
        },
    {
        'name': 'Jersey Shore Boca',
        'city': 'Ocean County, NJ',
        'founded': 2003,
        },
    {
        'name': 'Hollywood United',
        'city': 'Santa Monica, CA',
        'founded': 1988,
        },
    {
        'name': 'Palo Alto Firebirds',
        'city': 'Palo Alto, CA',
        'founded': 1994,
        'dissolved': 2000,
        },
    {
        'name': 'San Diego Nomads',
        'city': 'San Diego, CA',
        'founded': 1986,
        'dissolved': 1990,
        },
    {
        'name': 'Southern California Lazers',
        'city': 'Torrance, CA',
        'founded': 1978,
        'dissolved': 1978,
        },
    {
        'name': 'Salt Lake Sting',
        'city': 'Salt Lake City, UT',
        'founded': 1990,
        'dissolved': datetime.datetime(1991, 7, 6),
        },
    {
        'name': 'Wilmington Hammerheads',
        'city': 'Wilmington, NC',
        'founded': 1996,
        },
    {
        'name': 'Harrisburg City Islanders',
        'city': 'Harrisburg, PA',
        'founded': 2004,
        },
    {
        'name': 'Cleveland City Stars',
        'city': 'Cleveland, OH',
        'founded': 2006,
        'dissolved': 2009,
        },
    {
        'name': 'Albany Capitals',
        'city': 'Albany, NY',
        'founded': 1989,
        'dissolved': 1991,
        },
    {
        'name': 'Los Angeles Skyhawks',
        'city': 'Los Angeles, CA',
        'founded': 1976,
        'dissolved': 1979,
        },
    {
        'name': 'New Jersey Americans',
        'city': 'New Brunswick, NJ',
        'founded': 1976,
        'dissolved': 1979,
        },
    {
        'name': 'Arizona Sahuaros',
        'city': 'Phoenix, AZ',
        'founded': 1989,
        },
    {
        'name': 'East Los Angeles Cobras',
        'city': 'East Los Angeles, CA',
        'founded': 1993,
        'dissolved': 1995,
        },
    {
        'name': 'Rhode Island Oceaneers',
        'city': 'Pawtucket, RI',
        'founded': 1974,
        'dissolved': 1978,
        },
    {
        'name': 'Indiana Invaders',
        'city': 'South Bend, IN',
        'founded': 1998,
        },
    {
        'name': 'Akron Summit Assault',
        'city': 'Akron, OH',
        'founded': 2010,
        'dissolved': 1991,
        },
    {
        'name': 'Cincinnati Kings',
        'city': 'Cincinnati, OH',
        'founded': 2005,
        },
    {
        'name': 'River City Rovers',
        'city': 'Louisville, KY',
        'founded': 2010,
        },
    {
        'name': 'Thunder Bay Chill',
        'city': 'Thunder Bay, ON',
        'founded': 2000,
        },
    {
        'name': 'Des Moines Menace',
        'city': 'Des Moines, IA',
        'founded': 1994,
        },
    {
        'name': 'Kansas City Brass',
        'city': 'Overland Park, KS',
        'founded': 1997,
        },
    {
        'name': 'Springfield Demize',
        'city': 'Springfield, MO',
        'founded': 2006
        },
    {
        'name': 'Reading United',
        'city': 'Reading, PA',
        'founded': 1996,
        },
    {
        'name': 'Jersey Express',
        'city': 'Newark, NJ',
        'founded': 2007,
        },
    {
        'name': 'Central Jersey Spartans',
        'city': 'Lawrenceville, NJ',
        'founded': 2009,
        },

    {
        'name': 'Ocean City Nor\'easters',
        'city': 'Ocean City, NJ',
        'founded': 1996,
        },
    {
        'name': 'GPS Portland Phoenix',
        'city': 'Portland, ME',
        'founded': 2009,
        },
    {
        'name': 'Chico Rooks',
        'city': 'Chico, CA',
        'founded': 1993,
        },
    {
        'name': 'Bakersfield Brigade',
        'city': 'Bakersfield, CA',
        'founded': 2005,
        'dissolved': 2009,
        },

    {
        'name': 'Boston Astros',
        'city': 'Boston, MA',
        'founded': 1969,
        'dissolved': 1975,
        },
    {
        'name': 'Maryland Bays',
        'city': 'Catonsville, MD',
        'founded': 1988,
        'dissolved': 1991,
        },
    {
        'name': 'Orlando Lions',
        'city': 'Orlando, FL',
        'founded': 1985,
        'dissolved': 1996,
        },
    {
        'name': 'Edmonton Brickmen',
        'city': 'Edmonton, AB',
        'founded': 1985,
        'dissolved': 1992
        },
    {
        'name': 'Ajax Orlando Prospects',
        'city': 'Orlando, FL',
        'founded': 2002,
        'dissolved': 2007,
        },




]
