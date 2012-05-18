#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

# This should only be used for
# 1. Stadiums with multiple names
# 2. Stadiums whose names are incorrect (externally)

def get_stadium(s):
    s = s.strip()
    return sd.get(s, s)

sd = {}

soccernet_errors = {
    'Rio Tinto Satadium': 'Rio Tinto Stadium',
    'AT&T; Park': 'AT&T Park',
    'LIVESTRONG Sporting Park': 'Livestrong Sporting Park',
    'JELD-WEN Park': 'Jeld-Wen Park',
    'Olímpico Universitario': 'Estadio Olímpico Universitario',
    'Tecnológico': 'Estadio Tecnológico',
    'Jorge Calero Suárez': 'Estadio Jorge Calero Suárez',
    'Nacional Tiburcio Carías Andino': 'Estadio Tiburcio Carías Andino',
    'Juan Ramón Loubriel': 'Juan Ramón Loubriel Stadium',
    'Saputo': 'Saputo Stadium',
    'Marvin Lee': 'Marvin Lee Stadium',
    'Estadio Corona': 'Estadio TSM Corona',
    'Hasely Crawford': 'Hasely Crawford Stadium',
    'Andrés Quintana Roo': 'Estadio Quintana Roo',
    'Complexe sportif Claude-Robillard': 'Complexe Sportif Claude-Robillard',
}
sd.update(soccernet_errors)
    

stadiums = {
    'Invesco Field': 'Sports Authority Field at Mile High',
    'INVESCO Field': 'Sports Authority Field at Mile High',
    'Nuevo Estadio Corona': 'Estadio TSM Corona',
    'Al Lang Stadium': 'Progress Energy Park',
    'Al Lang Field': 'Progress Energy Park',
    'Big Arch Stadium': 'Busch Memorial Stadium',
    'Rutgers Stadium': 'High Point Solutions Stadium',
    'Civic Stadium': 'Jeld-Wen Field', # There's another Civic Stadium in Eugene, OR.
    'Bank One Ballpark': 'Chase Field',
    'Skelly Field': 'Skelly Field at H. A. Chapman Stadium',
    'Chapman Stadium': 'Skelly Field at H. A. Chapman Stadium',
    'Juan Ramon Loubriel Stadium': 'Juan Ramón Loubriel Stadium',
    'Estadio Juan Ramón Loubriel': 'Juan Ramón Loubriel Stadium',
    'NSC Stadium': 'National Sports Center Stadium',
    'Clark\'s Athletic Field': 'Clark\'s Field',
    'RFK Stadium': 'Robert F. Kennedy Memorial Stadium',
    'Robert F. Kennedy Stadium': 'Robert F. Kennedy Memorial Stadium',
    'R.F.K. Stadium': 'Robert F. Kennedy Memorial Stadium',
    'Robert F. Kennedy Memorial': 'Robert F. Kennedy Memorial Stadium',
    'Los Angeles Memorial Coliseum': 'Memorial Coliseum (Los Angeles)',
    'Yankee Stadium': 'Yankees Stadium',
    'JFK Stadium': 'John F. Kennedy Stadium',
    'Philadelphia Municipal Stadium':  'John F. Kennedy Stadium',
    'Pizza Hut Park': 'FC Dallas Stadium',
    'Hermann Stadium': 'Robert R. Hermann Stadium',
    'Community America Ballpark': 'CommunityAmerica Ballpark',
    'The Home Depot Center': 'Home Depot Center',
    'Jack Murphy Stadium': 'Qualcomm Stadium',
    'Schaefer Stadium': 'Foxboro Stadium',
    'Triborough Stadium': 'Downing Stadium',
    'Randall\'s Island Stadium': 'Downing Stadium',
    'Randall\s Island Stadium': 'Downing Stadium',
    'Randall\s Island': 'Downing Stadium',
    'Fedex Field': 'FedEx Field',
    'Qwest Field': 'CenturyLink Field',
    'Kezar Field': 'Kezar Stadium',
    'Tacony Ball Park': 'Tacony Baseball Grounds',
    'Bethlehem Steel Field': 'Steel Field',
    'ONT Grounds': 'Clark Field',
    'Clark\'s Athletic Field': 'Clark Field',
    'Eagle State Street Grounds': 'Eagle Street Grounds',

    'Frelinghuysen Avenue Grounds': 'Frelinghuysen Grounds',
    'Frelinghuysen Avenue Ground': 'Frelinghuysen Grounds',
    'East State St Grounds': 'East State Street Grounds',

    
}
sd.update(stadiums)
