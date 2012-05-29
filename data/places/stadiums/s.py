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
    from opencup import oc_stadiums

    l = []
    l.extend(old)
    l.extend(mls_stadiums)
    l.extend(nasl2_stadiums)
    l.extend(foreign_stadiums)
    l.extend(apsl_stadiums)
    l.extend(oc_stadiums)
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




]
