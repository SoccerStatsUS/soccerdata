#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime

l = [

    {
        'name': 'Doxa Italia',
        'city': 'Manhattan Beach, CA',
        'founded': 1997,
        },

    {
        'name': 'Oakland Buccaneers',
        'city': 'Oakland, CA',
        'founded': 1976,
        'dissolved': 1976,
        },

    {
        'name': 'Cal FC',
        'city': 'Thousand Oaks, CA',
        'founded': 2007
        },

    {
        'name': 'DV8 Defenders',
        'city': 'Redwood City, CA',
        'founded': 1999,
        },

    {
        'name': 'Fullerton Rangers',
        'city': 'Santa Ana, CA',
        'founded': 2012,
        },

    {
        'name': 'PSA Elite',
        'city': 'Irvine, CA',
        },

    {
        'name': 'Mexico SC',
        'city': 'Fresno, CA',
        },

    {
        'name': 'Salinas Valley Samba',
        'city': 'Salinas, CA',
        'founded': 2004,
        },

    {
        'name': 'CD Mexico',
        'city': 'San Francisco, CA',
        'founded': 1985,
        },


    {
        'name': 'Exiles SC',
        'city': 'Los Angeles, CA',
        'founded': 1976,
        },

    {
        'name': 'Alianza DF',
        'city': 'Los Angeles, CA',
        # http://www.cesla.med.ucla.edu/v1/Documents/oped/7-4-94.htm
        },


    {
        'name': 'Sonoma County Sol',
        'city': 'Santa Rosa, CA',
        'founded': 2004,
        },

    {
        'name': 'San Jose Oaks',
        'city': 'San Jose, CA',
        'founded': 1974,
        },
    {
        'name': 'California Sunshine',
        'city': 'Fountain Valley, CA',
        'founded': 1977,
        'dissolved': 1980,
        },

    {
        'name': 'Golden Gate Gales',
        'city': 'Oakland, CA',
        'founded': 1980,
        'dissolved': 1980,
        },
    {
        'name': 'Santa Barbara Condors',
        'city': 'Santa Barbara, CA',
        'founded': 1977,
        'dissolved': 1977,
        },


    {
        'name': 'Los Angeles Blues',
        'city': 'Fullerton, CA',
        'founded': 2010,
        },
    {
        'name': 'San Francisco Bay Diablos',
        'city': 'San Francisco, CA',
        'founded': 1993,
        'dissolved': 1995,
        },
    {
        'name': 'Riverside County Elite',
        'city': 'Hemet, CA',
        'founded': 1998,
        'dissolved': 2000,
        },
    {
        'name': 'Santa Cruz Surf',
        'city': 'Santa Cruz, CA',
        'founded': 1993,
        'dissolved': 1994,
        },

    {
        'name': 'Shasta Scorchers',
        'city': 'Redding, CA',
        'founded': 1994,
        'dissolved': 1995,
        },

    {
        'name': 'Stanislaus United Cruisers',
        'city': 'Modesto, CA',
        'founded': 1997,
        'dissolved': 2001,
        },

    {
        'name': 'OC Blues Strikers FC',
        'city': 'Pacific Palisades, CA',
        'founded': 2011
        },

    {
        'name': 'FC Hasental',
        'founded': 2005,
        'city': 'Agoura Hills, CA',
        },

    {
        'name': 'Silicon Valley Ambassadors',
        'founded': 1998,
        'dissolved': 1999,
        'city': 'Los Altos Hills, CA',
        },

    {
        'name': 'Ventura County Fusion',
        'founded': 2006,
        'city': 'Ventura, CA',
        },



    {
        'name': 'California Kickers',
        'founded': 1986,
        'dissolved': 1990,
        'city': 'Hollywood, CA',
        },

    {
        'name': 'Real Santa Barbara',
        'founded': 1989,
        'dissolved': 1990,
        'city': 'Santa Barbara, CA',
        },


    {
        'name': 'Sacramento Senators',
        'founded': 1989,
        'dissolved': 1989,
        'city': 'Sacramento, CA',
        },

    {
        'name': 'Los Angeles Heat',
        'founded': 1986,
        'dissolved': 1990,
        'city': 'Los Angeles, CA',
        },

    {
        'name': 'Los Angeles Heroes',
        'city': 'Los Angeles, CA',
        'founded': 1993,
        'dissolved': 2002,
        },
    {
        'name': 'Los Angeles Misioneros',
        'city': 'Los Angeles, CA',
        'founded': 2006,
        },

    {
        'name': 'San Fernando Valley Quakes',
        'city': 'Calabasas, CA',
        'founded': 2006,
        'dissolved': 2008,
        },

    {
        'name': 'San Jose Frogs',
        'city': 'San Jose, CA',
        'founded': 2005,
        'dissolved': 2008,
        },

    {
        'name': 'California Victory',
        'city': 'San Francisco, CA',
        'founded': 2006,
        'dissolved': 2007,
        },
    {
        'name': 'East Bay Red Riders',
        'city': 'Oakland, CA',
        'founded': 1992,
        'dissolved': 1993,
        },


    {
        'name': 'San Gabriel Valley Highlanders',
        'city': 'Glendale, CA',
        'founded': 1997,
        'dissolved': 2001,
        },


    {
        'name': 'Springfield Storm',
        'city': 'Glendora, CA',
        'founded': 2005,
        'dissolved': 2005,
        },

    {
        'name': 'California Gold',
        'city': 'Modesto, CA',
        'founded': 2002,
        'dissolved': 2006,
        },

    {
        'name': 'FC Santa Clarita',
        'city': 'Santa Clarita, CA',
        'founded': 2006,
        },

    {
        'name': 'Pali Blues',
        'city': 'Los Angeles, CA',
        'founded': 2008,
        },

    {
        'name': 'San Diego Gauchos',
        'city': 'San Diego, CA',
        'founded': 2002,
        'dissolved': 2006,
        },


    {
        'name': 'Santa Barbara Sharks',
        'city': 'Santa Barbara, CA',
        'founded': 2002,
        'dissolved': 2002,
        },

    {
        'name': 'Oakland Stompers',
        'city': 'Oakland, CA',
        'founded': 1978,
        'dissolved': 1978,
        },


    {
        'name': 'San Diego Jaws',
        'city': 'San Diego, CA',
        'founded': 1976,
        'dissolved': 1976,
        'next': 'Las Vegas Quicksilvers',
        },

    {
        'name': 'California Cougars',
        'city': 'Stockton, CA',
        'founded': 2004,
        'dissolved': 2011,
        },

    {
        'name': 'Los Angeles Maccabee AC',
        'city': 'Los Angeles, CA',
        'founded': 1971,
        'dissolved': 1982,
        },


    {
        'name': 'Sacramento Gold',
        'city': 'Sacramento, CA',
        'founded': 1976,
        'dissolved': 1980,
        },


    {
        'name': 'Bay Area Ambassadors',
        'city': 'Hayward, CA',
        'founded': 2009,
        },

]
 
