#!/usr/local/bin/env python
# -*- coding: utf-8 -*-




def get_city(s):


    s = s.strip()
    if s in places:
        return get_city(cities[s])
    else:
        return s
    


cities = {
    'Port-of-Spain, Trinidad & Tobago': 'Port of Spain, Trinidad and Tobago',
    'Port of Spain, Trinidad & Tobago>': 'Port of Spain, Trinidad and Tobago',

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
    'Tampa Bay': 'Tampa Bay, FL',
    'Tampa, FL': 'Tampa Bay, FL',
    'Fort Lauderdale': 'Fort Lauderdale, FL',
    'Fort Worth': 'Fort Worth, TX',
}
