#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


aliases = {}

full_alias = {
    'UNCAF Cup': 'Copa Centroamericana',
    'UNCAF Nations Cup': 'Copa Centroamericana',

    #'Copa America': 'Copa América',

    'United Soccer League': 'United Soccer League (1984-1985)',

    'Western Soccer Alliance': 'Western Soccer League',
    'Western Soccer Alliance Playoffs': 'Western Soccer League Playoffs',

    'Southwest Indoor Soccer League': 'United States Interregional Soccer League (indoor)',
    'Southwest Independent Soccer League (indoor)': 'United States Interregional Soccer League (indoor)',
    'Southwest Independent Soccer League': 'United States Interregional Soccer League',

    'USISL Premier League': 'USL Premier Developmental League',

    'USISL Professional League': 'USL Second Division',
    'USL Pro': 'USL Second Division',

    'A-League': 'USL First Division',

    'American Indoor Soccer Association': 'National Professional Soccer League (indoor)',

    'International Friendly': 'Friendly International',

    'Recopa CONCACAF': 'CONCACAF Cup Winners Cup',
    'CONCACAF Champions Cup': 'CONCACAF Champions\' Cup',

    'Premier Soccer Alliance': 'World Indoor Soccer League',

    'World Cup': 'FIFA World Cup',
    'Confederations Cup': 'FIFA Confederations Cup',

}

aliases.update(full_alias)

# Don't want to completely delete these.
partial_alias = {
    'Domestic Tour': 'Friendly',
    'International Tour': 'Friendly',
    'Desert Diamond Cup': 'Friendly',
    'Chicago Sister Cities International Cup': 'Friendly',



    'Bicentennial Cup': 'Friendly',
    'Carlsberg Cup': 'Friendly',
    'Carolina Challenge Cup': 'Friendly',
    'Dynamo Charities Cup': 'Friendly',
    'Europac International': 'Friendly',
    'Spring Cup Matches': 'Friendly',
    'Sunshine International': 'Friendly',
    'Toronto International': 'Friendly',
    'Tournament of Champions': 'Friendly',
    'Trans-Atlantic Challenge Cup': 'Friendly',

    'Amistad Cup': 'Friendly International',

    'International Cup': 'Friendly International',
    'Joe Robbie Cup': 'Friendly International',
    'Kirin Cup': 'Friendly International',
    'Los Angeles Soccer Tournament': 'Friendly',
    'Mexico City Tournament': 'Friendly International',
    'Miami Cup': 'Friendly International',
    'North American Nations Cup': 'Friendly International',
    'Presidents Cup': 'Friendly International',
    'Trinidad Tournament': 'Friendly International',
    }
aliases.update(partial_alias)


def get_competition(s):
    if s is None:
        return None
    
    s = s.strip()
    return aliases.get(s, s)
