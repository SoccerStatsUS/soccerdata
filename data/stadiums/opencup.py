#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime

oc_stadiums = [
    {
        'name': 'Zephyr Field',
        'address': '6000 Airline Drive',
        'location': 'Metairie, LA',
        'opened': datetime.datetime(1997, 4, 11),
        'capacity': 10000,
        'cost': 26000000,
        'architect': 'HOK Sport',
        },
    {
        'name': 'Finley Stadium',
        'address': '1826 Carter Street',
        'location': 'Chattanooga, TN',
        'opened': datetime.datetime(1997, 10, 18),
        'capacity': 20668,
        'cost': 28500000,
        },
    {
        'name': 'Old Panther Field',
        'location': 'Duncanville, TX',
        },
    {
        'name': 'Frontier Field',
        'address': 'One Morrie Silver Way',
        'location': 'Rochester, NY',
        'opened': datetime.datetime(1996, 7, 11),
        'capacity': 10840,
        'cost': 35300000,
        },
    {
        'name': 'White Pine Stadium',
        'location': 'Saginaw Township, MI',
        },

    {
        'name': 'Virginia Beach Sportsplex',
        'address': '2181 Landstown Road',
        'location': 'Virginia Beach, VA',
        'opened': 1999,
        'capacity': 6000,
        'cost': 6800000,
        },
    {
        'name': 'Forest View Park',
        'location': 'Arlington Heights, IL',
        },
    {
        'name': 'Mitchel Athletic Complex',
        'location': 'Uniondale, NY',
        'opened': 1984,
        'capacity': 10102,
        },
    {
        'name': 'Maryland SoccerPlex',
        'address': '18031 Central Park Circle',
        'location': 'Boyds, MD',
        'opened': 2000,
        'capacity': 5126
        },

    {
        'name': 'Socorro Stadium',
        'location': 'El Paso, TX',
        },

    {
        'name': 'Blue Valley Sports Complex',
        'location': 'Overland Park, KS',
        },

    {
        'name': 'Negoesco Stadium',
        'location': 'San Francisco, CA',
        'opened': datetime.datetime(1982, 9, 17),
        'capacity': 3000,
        },


    {
        'name': 'James Griffin Stadium',
        'location': 'Saint Paul, MN',
        'opened': 1930,
        'capacity': 4367
        },

    {
        'name': 'Home Depot Center Track & Field Stadium',
        'location': 'Carson, CA',
        },

    {
        'name': 'Waukee Stadium',
        'address': '555 SE University Avenue',
        'location': 'Waukee, IA',
        'opened': 1996,
        'capacity': 7501,
        },

    {
        'name': 'Sahlen\'s Stadium',
        'location': 'Rochester, NY',
        'opened': datetime.datetime(2006, 6, 3),
        'capacity': 13768,
        'cost': 35000000,
        'architect': 'HOK Sport',
        },
    {
        'name': 'Buck Hardee Field at Legion Stadium',
        'address': '2149 Carolina Beach Road, Wilmington, NC',
        'location': 'Wilmington, NC',
        'opened': datetime.datetime(2006, 6, 3),
        },
    {
        'name': 'Starfire Sports Complex',
        'address': '6840 Fort Dent Way',
        'location': 'Tukwila, WA',
        'opened': datetime.datetime(2005, 4, 23),
        'capacity': 4500,
        'architect': 'HOK Sport',
        },
    {
        'name': 'Skyline Sports Complex',
        'address': '201 Championship Way',
        'location': 'Harrisburg, PA',
        'opened': 1987,
        'capacity': 4000,
        },
    {
        'name': 'Belson Stadium',
        'location': 'Jamaica, Queens, NY',
        'opened': datetime.datetime(2002, 9, 21),
        'capacity': 2600,
        },
    {
        'name': 'Sahlen\'s Stadium',
        'location': 'Rochester, NY',
        'opened': datetime.datetime(2006, 6, 3),
        'capacity': 13768,
        'cost': 35000000,
        'architect': 'HOK Sport',
        },
    {
        'name': 'Breese Stevens Field',
        'location': 'Madison, WI',
        'opened': datetime.datetime(1926, 5, 5),
        },
    {
        'name': 'Macpherson Stadium',
        'location': 'Browns Summit, NC',
        'opened': datetime.datetime(2002, 5, 4),
        'capacity': 7000,
        },
    {
        'name': 'Patriot Stadium',
        'location': 'El Paso, TX',
        'opened': 2005,
        'capacity': 3000,
        'cost': 7200000,
        },
    {
        'name': 'Valley Stadium',
        'location': 'West Des Moines, IA',
        },
    {
        'name': 'House Park',
        'location': 'Austin, TX',
        'opened': 1939,
        'capacity': 6500,
        },
    {
        'name': 'Nelson Field',
        'location': 'Austin, TX',
        },
    {
        'name': 'Carey Stadium',
        'location': 'Ocean City, NJ',
        },
    {
        'name': 'Tropical Park Stadium',
        'address': '7900 SW 40th Street',
        'location': 'Miami, FL',
        'capacity': 10000,
        },
    {
        'name': 'Sports Backers Stadium',
        'location': 'Richmond, VA',
        'opened': 1999,
        'capacity': 3250,
        },
    {
        'name': 'Ultimate Soccer Arena',
        'location': 'Pontiac, MI',
        },
    {
        'name': 'Cougar Stadium',
        'location': 'Azusa, CA',
        },
    {
        'name': 'DeKalb Memorial Stadium',
        'location': 'Clarkston, GA',
        },
    {
        'name': 'Yurcak Field',
        'location': 'Piscataway, NJ',
        'opened': 1994,
        'capacity': 5000,
        'cost': 28000000,
        },
    {
        'name': 'Husky Soccer Stadium',
        'location': 'Seattle, WA',
        },
    {
        'name': 'Uihlein Soccer Park',
        'address': '7101 W Good Hope Rd',
        'location': 'Milwaukee, WI',
        'opened': 1994,
        'capacity': 7000,
        },
    {
        'name': 'Dudley Field',
        'location': 'El Paso, TX',
        'opened': 1924,
        'closed': datetime.datetime(2005, 11, 5),
        },
    {
        'name': 'Singer Park',
        'location': 'Manchester, NH',
        },

    {
        'name': 'Interbay Stadium',
        'location': 'Seattle, WA',
        'capacity': 1000,
        },

    {
        'name': 'Sirrine Stadium',
        'location': 'Greenville, SC',
        'capacity': 15000,
        },

    {
        'name': 'Bethel Park Stadium',
        'location': 'Bethel Park, PA',
        },

    {
        'name': 'Flamingo Park',
        'location': 'Miami Beach, FL',
        },

    {
        'name': 'Doug Hitchen Stadium',
        'location': 'Arroyo Grande, CA',
        },

    {
        'name': 'Santa Ana Stadium',
        'location': 'Santa Ana, CA',
        },

    {
        'name': 'Baker Field',
        'location': 'New York, NY',
        },
    {
        'name': 'Klockner Stadium',
        'location': 'Charlottesville, VA',
        'opened': 1992,
        'capacity': 8000,
        'cost': 1200000,
        },
    {
        'name': 'Academica Fields',
        'location': 'Turlock, CA',
        },

    {
        'name': 'CSM Soccer Stadium',
        'location': 'Golden, CO',
        },
    {
        'name': 'Bavarian Soccer Park',
        'location': 'Milwaukee, WI',
        },
    {
        'name': 'Seminole Soccer Complex',
        'location': 'Sanford, FL',
        },
    {
        'name': 'Texas A&M International University Soccer Complex',
        'location': 'Laredo, TX',
        },
    {
        'name': 'RYSA Soccerplex',
        'location': 'Conyers, GA',
        },
    {
        'name': 'Toyota Park Practice Field',
        'location': 'Chicago, IL',
        },
    {
        'name': 'Bremerton Memorial Stadium',
        'location': 'Bremerton, WA',
        },
    {
        'name': 'Bremerton Memorial Stadium',
        'location': 'Bremerton, WA',
        },
    {
        'name': 'Chartiers Valley Stadium',
        'location': 'Bridgeville, PA',
        },
    {
        'name': 'George Mason Stadium',
        'location': 'Fairfax, VA',
        },
    {
        'name': 'Fullerton State Sports Complex',
        'location': 'Fullerton, CA',
        },
    {
        'name': 'University of Richmond Stadium',
        'location': 'Richmond, VA',
        },
    {
        'name': 'Richland Stadium',
        'location': 'Dallas, TX',
        },
    {
        'name': 'Cy Donnelly Stadium',
        'location': 'South Huntington, NY',
        },
    {
        'name': 'Central Broward Regional Park',
        'location': 'Lauderhill, FL',
        },
    {
        'name': 'Douglas Stadium',
        'location': 'San Diego, CA',
        },
    {
        'name': 'High Point Athletic Complex',
        'location': 'High Point, NC',
        },
    {
        'name': 'Peoria Sports Complex',
        'location': 'Peoria, AZ',
        },
    {
        'name': 'Alan Carson Field',
        'location': 'South Yarmouth, MA',
        },
    {
        'name': 'Mile High Greyhound Park',
        'location': 'Denver, CO',
        },
    {
        'name': 'Memorial Stadium (Seattle)',
        'location': 'Seattle, WA',
        },
    {
        'name': 'Adams Stadium',
        'location': 'Atlanta, GA',
        },
    {
        'name': 'Englewood Stadium',
        'location': 'Englewood, CO',
        },
    {
        'name': 'Royal Palm Polo Club',
        'location': 'Boca Raton, FL',
        },
    {
        'name': 'University of Redlands',
        'location': 'Redlands, CA',
        },
    {
        'name': 'Adams Stadium',
        'location': 'Atlanta, GA',
        },
    {
        'name': 'Adams Stadium',
        'location': 'Atlanta, GA',
        },
    {
        'name': 'Adams Stadium',
        'location': 'Atlanta, GA',
        },
    {
        'name': 'Adams Stadium',
        'location': 'Atlanta, GA',
        },

    



]