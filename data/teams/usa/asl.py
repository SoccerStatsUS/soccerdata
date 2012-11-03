#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import datetime

l = [

    # Need to separate later Philadelphia FC's.
    {
        'name': 'Philadelphia Field Club',
        'founded': 1921,
        'dissolved': 1922,
        'city': 'Philadelphia, PA',
        },
    {
        'name': 'New York Field Club',
        'founded': 1916,
        'dissolved': 1924,
        'city': 'New York, NY',
        },
    {
        'name': 'Todd Shipyards',
        'founded': 1921,
        'dissolved': 1922,
        'city': 'Brooklyn, NY',
        },
    {
        'name': 'Harrison Erie F.C.',
        'founded': 1919,
        'dissolved': 1923,
        'city': 'Harrison, NJ',
        },


    # This team may have lasted until 1942?
    {
        'name': 'Pawtucket Rangers',
        'founded': 1919,
        'dissolved': 1935,
        'city': 'Pawtucket, RI',
        },

    # Need to disambiguate Fall River United, which existed in 1933-1934
    {
        'name': 'Fall River Rovers',
        'founded': 1884,
        'dissolved': 1922,
        'city': 'Fall River, MA',
        },
    {
        'name': 'Holyoke Falcos',
        'founded': 1921,
        'dissolved': 1924,
        'city': 'Holyoke, NJ',
        },
    {
        'name': 'Jersey City Celtics',
        'founded': 1921,
        'dissolved': 1922,
        'city': 'Jersey City, NJ',
        },
    {
        'name': 'Bethlehem Steel',
        'founded': 1911,
        'dissolved': 1930,
        'city': 'Bethlehem, PA',
        },

    {
        'name': 'Fall River Marksmen',
        'founded': 1922,
        'dissolved': 1931,
        'city': 'Fall River, MA',
        },

    # Need to separate later Paterson FC teams (there are multiple.)
    {
        'name': 'Paterson F.C.',
        'founded': 1917,
        'dissolved': 1923,
        'city': 'Paterson, NJ',
        },

    # Need to separate later Brooklyn Wanderers teams (there are multiple.)
    {
        'name': 'Brooklyn Wanderers',
        'founded': 1895,
        'dissolved': 1931,
        'city': 'Brooklyn, NY',
        },
    {
        'name': 'Newark Skeeters',
        'founded': 1923,
        'dissolved': 1929,
        'city': 'Newark, NJ',
        },

    # Need to separate later New Bedford Whalers teams (there are multiple.)
    {
        'name': 'New Bedford Whalers',
        'founded': 1924,
        'dissolved': datetime.date(1931, 4, 19),
        'city': 'New Bedford, MA',
        },

    # Add Gold Bugs alias, de-alias.
    {
        'name': 'Providence Clamdiggers',
        'founded': 1924,
        'dissolved': 1930,
        'city': 'Providence, RI',
        },

    {
        'name': 'Boston Wonder Workers',
        'founded': 1924,
        'dissolved': 1929,
        'city': 'Boston, MA',
        },

    # Add Giants, Nationals alias,de-alias.
    {
        'name': 'Indiana Flooring',
        'founded': 1924
        'dissolved': 1927,
        'city': 'New York, NY',
        },

    # amateurs?
    {
        'name': 'Fleisher Yarn',
        'founded': 1921, # maybe earlier.
        'dissolved': 1925,
        'city': 'Philadelphia, PA',

        },

    {
        'name': 'Shawsheen Indians',
        'founded': 1923,
        'dissolved': 1926,
        'city': 'Andover, MA',
        },

    {
        'name': 'Springfield Babes',
        'founded': 1926,
        'dissolved': 1927,
        'city': 'Springfield, MA',
        },
    {
        'name': 'Hartford Americans',
        'founded': 1927,
        'dissolved': 1928,
        'city': 'Hartford, CT',
        },

    # Separate earlier New York, Brooklyn Hakoah teams.
    {
        'name': 'Hakoah All-Stars',
        'founded': datetime.date(1929, 11, 16),
        'dissolved': 1932,
        'city': 'New York, NY',
        },

    # Separate other Boston, Bridgeport teams from 1929, 1930.
    {
        'name': 'Boston Bears',
        'founded': 1931,
        'dissolved': 1932,
        'city': 'Boston, MA',
        },
    {
        'name': 'Newark Americans',
        'founded': 1930,
        'dissolved': 1932,
        'city': 'Newark, NJ',
        },

# Need to separate Fall River FC (1921), which is probs Fall River Rovers; two Fall River FC's that existed in 1931/1932 and became other clubs shortly.
#    {
#        'name': 'Fall River FC',
#        'founded': 1967, 
#        'dissolved': 1981,
#        'city': 'Atlanta, GA',
#        },

    # Separate from ISL New York Americans team.
    {
        'name': 'New York Americans',
        'founded': 1931,
        'dissolved': 1956,
        'city': 'New York, NY',
        },
    {
        'name': 'Queens Bohemians',
        'founded': 1932,
        'dissolved': 1933,
        'city': 'Queens, NY',
        },
]
