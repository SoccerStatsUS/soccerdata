#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime


mls_stadiums = [
    {
        'name': 'Home Depot Center',
        'address': '18400 Avalon Boulevard',
        'location': 'Carson, CA',
        'capacity': 27000,
        'architect': 'Rossetti Architects',
        'opened': datetime.datetime(2003, 6, 1),
        'length': 109.7,
        'width': 68.6,
        },

        {
        'name': 'Cotton Bowl',
        'address': '1300 Robert B. Cullum Boulevard',
        'location': 'Dallas, TX',
        'capacity': 92100,
        'opened': 1930,
        'cost': 328200,
        },

    {
        'name': 'Gillette Stadium',
        'address': '1 Patriot Place',
        'location': 'Foxborough, MA',
        'opened': datetime.datetime(2002, 9, 9),
        'cost': 325000000,
        'architect': 'Populous',
        'capacity': 68756,
        },


    {
        'name': 'BMO Field',
        'address': '170 Princes Boulevard',
        'location': 'Toronto',
        'opened': datetime.datetime(2007, 4, 20),
        'cost': 62900000,
        'denomination': 'Canadian dollars',
        'architect': 'Brisbin Brooks Beynon Architects ',
        'capacity': 21859,
        },
    

    {
        'name': 'Saputo Stadium',
        'address': '4750 Rue Sherbrooke Est',
        'location': 'Montreal',
        'capacity': 20341, 
        'opened': datetime.datetime(2008, 5, 18),
        'cost': 17000000,
        'denomination': 'Canadian Dollars',
        'architect': 'Zinno Zappitell Architectes',
        'length': 110,
        'width': 70,
        'measure': 'meters',
        },


        {
        'name': 'Foote Field',
        'address': '11601 68 Avenue, University of Alberta South Campus',
        'location': 'Edmonton',
        'capacity': 5000,
        'opened': datetime.datetime(2001, 9, 8),
        'cost': 10500000,
        'denomination': 'Canadian Dollars',
        },

            {
        'name': 'Columbus Crew Stadium',
        'address': '1 Black and Gold Boulevard',
        'location': 'Columbus, OH',
        'capacity': 20145,
        'opened': datetime.datetime(1999, 5, 15), 
        'cost': 28500000,
        'architect': 'NBBJ',
        'notes': 'First stadium built for an MLS team.',
        'length': 115,
        'width': 75,
        'measure': 'yards',
        
    
        },

        {
        'name': 'CenturyLink Field',
        'address': '800 Occidental Ave S',
        'location': 'Seattle, WA',
        'opened': datetime.datetime(2008, 7, 28),
        'cost': 430000000,
        'architect': 'Ellerbe Becket',
        'capacity': 67000
        },

    {
        'name': 'Dick\'s Sporting Goods Park',
        'address': '6000 Victory Way',
        'location': 'Commerce City, CO',
        'opened': datetime.datetime(2005, 9, 28),
        'cost': 131000000,
        'architect': 'HOK Sport',
        'capacity': 18086,
        },

    {
        'name': 'Livestrong Sporting Park',
        'address': 'One Sporting Way',
        'location': 'Kansas City, KS',
        'opened': datetime.datetime(2011, 6, 9),
        'cost': 200000000,
        'architect': 'NBBJ',
        'capacity': 18467,
        },

    {
        'name': 'PPL Park',
        'address': '1 Stadium Drive',
        'location': 'Chester, PA',
        'opened': datetime.datetime(2010, 6, 27),
        'cost': 120000000,
        'architect': 'Rossetti Architects',
        'capacity': 18500,
        },

    {
        'name': 'Red Bull Arena',
        'address': '600 Cape May Street',
        'location': 'Harrison, NJ',
        'opened': datetime.datetime(2010, 3, 20),
        'cost': 200000000,
        'architect': 'Rossetti Architects',
        'capacity': 25000,
        },



        {
        'name': 'Arrowhead Stadium',
        'address': '1 Arrowhead Drive',
        'location': 'Kansas City, MO',
        'capacity': 76416,
        'opened': datetime.datetime(1972, 8, 12),
        'cost': 43000000,
        'architect': 'Kivett and Myers',
        },



        {
        'name': 'Cardinal Stadium',
        'address': '455 South Brainard Street',
        'location': 'Naperville, IL',
        'capacity': 5500,
        'opened': 1999,
        },


        {
        'name': 'CommunityAmerica Ballpark',
        'address': '1800 Village West Pkwy',
        'location': 'Kansas City, KS',
        'capacity': 10385,
        'opened': datetime.datetime(2003, 6, 6),
        'cost': 12000000,
        'architect': 'Heinlein Schrock Stearns',
        },

        {
        'name': 'Dragon Stadium',
        'address': '1085 S Kimball Ave',
        'location': 'Southlake, TX',
        'capacity': 11000,
        'opened': 2001,
        'cost': 15000000,
        },
    
    {
        'name': 'FC Dallas Stadium',
        'address': '9200 World Cup Way, Ste 202',
        'location': 'Frisco, TX',
        'capacity': 20500,
        'cost': 80000000,
        'opened': datetime.datetime(2005, 8, 6),
        'length': 107,
        'width': 68,
        },

        {
        'name': 'Rose Bowl',
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
        'name': 'Soldier Field',
        'address': '1410 S Museum Campus Drive',
        'location': 'Chicago, IL',
        'capacity': 61500,
        'cost': 13000000,
        'opened': datetime.datetime(1924, 10, 9),
        'architect': 'Holabird & Roche',
        },

        {
        'name': 'Giants Stadium',
        'address': '50 Route 120',
        'location': 'East Rutherford, NJ',
        'capacity': 80242,
        'cost': 78000000,
        'opened': datetime.datetime(1976, 10, 10),
        'closed': datetime.datetime(2010, 1, 3),
        'architect': 'Kivett and Myers',
        },        

        {
        'name': 'Ohio Stadium',
        'address': '411 Woody Hayes Drive',
        'location': 'Columbus, OH',
        'capacity': 102329,
        'cost': 1340000,
        'opened': datetime.datetime(1922, 10, 7),
        'architect': 'Howard Dwight Smith',
        },        

        {
        'name':'Toyota Park',
        'address': '7000 South Harlem Avenue',
        'location': 'Chicago, IL',
        'capacity': 20000,
        'cost': 98000000,
        'opened': datetime.datetime(2006, 6, 11),
        'architect': 'Rossetti Architects',    
        'length': 120,
        'width': 75,
        'measure': 'yards',
        },        


        {
        'name': 'Jeld-Wen Field',
        'address': '1844 SW Morrison',
        'location': 'Portland, OR',
        'capacity': 20438,
        'cost': 502000,
        'opened': datetime.datetime(1926, 10, 9),
        'architect': 'A. E. Doyle',
        'length': 110,
        'width': 70,
        'measure': 'yards',
        },        

        {
        'name': 'Rio Tinto Stadium',
        'address': '9256 South State Street',
        'location': 'Sandy, UT',
        'capacity': 20213,
        'cost': 115000000,
        'opened': datetime.datetime(2006, 10, 9),
        'architect': 'Rossetti Architects',
        'length': 120,
        'width': 75,
        'measure': 'yards',
        },        


        {
        'name': 'Spartan Stadium',
        'address': '1257 S 10th St',
        'location': 'San José, CA',
        'capacity': 30456, 
        'cost': None, 
        'opened': 1933,
        },        

        {
        'name': 'Foxboro Stadium',
        'address': 'Washington St. (Route 1)',
        'location': 'Foxborough, MA',
        'capacity': 60292,
        'cost': 7100000,
        'opened': datetime.datetime(1971, 8, 15),
        'closed': datetime.datetime(2002, 1, 19),
        },

            {
        'name': 'Robert F. Kennedy Memorial Stadium',
        'short_name': 'RFK Stadium',
        'address': '2400 East Capitol St. SE',
        'location': 'Washington, D.C.',
        'capacity': 46000,
        'cost': 24000000,
        'opened': datetime.datetime(1961, 10, 1),
        },        


]
