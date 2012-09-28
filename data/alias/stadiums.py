#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

# This should only be used for
# 1. Stadiums with multiple names
# 2. Stadiums whose names are incorrect (externally)


def get_stadium(s):
    """
    Recursive. 
    """
    print s

    s = s.strip()
    if s in sd:
        return get_stadium(sd[s])
    else:
        return s

sd = {}

soccernet_errors = {
    'Rio Tinto Satadium': 'Rio Tinto Stadium',
    'AT&T; Park': 'AT&T Park',
    'LIVESTRONG Sporting Park': 'Livestrong Sporting Park',
    'JELD-WEN Park': 'Jeld-Wen Field',
    'Olímpico Universitario': 'Estadio Olímpico Universitario',
    'Tecnológico': 'Estadio Tecnológico',
    'Jorge Calero Suárez': 'Estadio Jorge Calero Suárez',
    'Nacional Tiburcio Carías Andino': 'Estadio Tiburcio Carías Andino',
    'Juan Ramón Loubriel': 'Estadio Juan Ramon Loubriel',
    'Saputo': 'Saputo Stadium',
    'Marvin Lee': 'Marvin Lee Stadium',
    'Estadio Corona': 'Estadio TSM Corona',
    'Hasely Crawford': 'Hasely Crawford Stadium',
    'Andrés Quintana Roo': 'Estadio Quintana Roo',
    'Complexe sportif Claude-Robillard': 'Complexe Sportif Claude-Robillard',
    'Estadio de la Ciudad de los Deportes, México DF': 'Estadio Azul',
}
sd.update(soccernet_errors)
    

stadiums = {
    'Edinboro University Stadium': 'Sox Harrison Stadium',
    'Middlefield Cheese Stadium (Bedford)': 'Middleford Cheese Stadium',
    'Florida Citrus Bowl': 'Citrus Bowl',
    'Richard Montgomery HS': 'Richard Montgomery High School',

    'Seahawk Stadium': 'CenturyLink Field',
    'Sticky Wicket Stadium': 'Stanford Cricket Ground',

    'PAETEC Park': 'Sahlen\'s Stadium',

    'Legion Stadium': 'Buck Hardee Field at Legion Stadium',
    'Silverbacks Park': 'Atlanta Silverbacks Park',
    'Soccorro Stadium': 'Socorro Stadium',


    'Paul Angelo Russo Stadium Field': 'Paul Angelo Russo Stadium',

    'Estadio Juan Ramón Loubriel': 'Estadio Juan Ramon Loubriel',
    'Juan Ramon Loubriel Stadium': 'Estadio Juan Ramon Loubriel',
    'Juan Ramón Loubriel Stadium': 'Estadio Juan Ramon Loubriel',

    'Carl Lewis Field': 'Carl Lewis Track & Field Stadium',
    'Centre Claude-Robillard': 'Complexe Sportif Claude-Robillard',
    'Crew Stadium': 'Columbus Crew Stadium',
    'Stade Saputo': 'Saputo Stadium',
    'JELD-WEN Field': 'Jeld-Wen Field',
    'San Diego Stadium': 'Qualcomm Stadium',
    'Portland Civic Stadium': 'Jeld-Wen Field',
    'Civic Stadium': 'Jeld-Wen Field', # There's another Civic Stadium in Eugene, OR.
    'BC Place Stadium': 'BC Place',


    'Stade Gerland': 'Stade de Gerland',
    'Oakland-Alameda County Coliseum': 'Oakland Coliseum',
    'Estadio Sylvio Cator': 'Stade Sylvio Cator',
    'Estadío Sylvio Cator': 'Stade Sylvio Cator',
    'Estadío Silvio Cator': 'Stade Sylvio Cator',
    
    'Sullivan Stadium': 'Foxboro Stadium',
    'Al Lang Stadium': 'Progress Energy Park',
    'Al Lang Field': 'Progress Energy Park',



    
    'Estadío Mateo Flores': 'Estadio Mateo Flores',
    'Estadio Ricardo Saprisa': 'Estadío Ricardo Saprissa', 
    'Azteca Stadium': 'Estadio Azteca',
    'Orange Bowl': 'Miami Orange Bowl',
    'The Polo Grounds': 'Polo Grounds',
    'Sparta Stadium': 'Sparta Field',
    'Marks Stadium': 'Mark\'s Stadium',
    'Dal-Hi Stadium': 'P.C. Cobb Stadium',
    'Gardner Park': 'Burnett Field',
    'Fair Park Stadium': 'Cotton Bowl',
    'Blue Valley Athletic Complex': 'Blue Valley Sports Complex',
    'Old Panther Stadium, Duncanville': 'Old Panther Field, Duncanville',
    'Chartiers Valley High School': 'Chartiers Valley Stadium',
    'Tacony Baseball Park': 'Tacony Baseball Grounds',
    'Soccorro Stadium': 'Socorro Stadium',
    'SAS Stadium': 'WakeMed Soccer Park',
    'National Sports Center': 'National Sports Center Stadium',
    'Husky Soccer Field': 'Husky Soccer Stadium',
    'PGE Park': 'JELD-WEN Field',
    'Home Depot Center Track': 'Home Depot Center Track & Field Stadium',
    'PAETEC Park': 'Sahlen\'s Stadium',
    'Marina Auto Stadium': 'Sahlen\'s Stadium',
    'Marina Auto Stadium, Rochester, NY': 'Sahlen\'s Stadium',
    'Nashville Coliseum': 'LP Field',
    'Alltel Stadium': 'EverBank Field',
    'Estadio Bella Vista': 'Estadio Bellavista',


    'Estadío Ricardo Saprissa': 'Estadio Ricardo Saprissa Aymá',
    'Freulinghausen Ave Grounds': 'Frelinghuysen Grounds',
    'Invesco Field': 'Sports Authority Field at Mile High',
    'INVESCO Field': 'Sports Authority Field at Mile High',
    'Nuevo Estadio Corona': 'Estadio TSM Corona',
    'Big Arch Stadium': 'Busch Memorial Stadium',
    'Rutgers Stadium': 'High Point Solutions Stadium',

    'Bank One Ballpark': 'Chase Field',
    'Skelly Field': 'Skelly Field at H. A. Chapman Stadium',
    'Chapman Stadium': 'Skelly Field at H. A. Chapman Stadium',
    'NSC Stadium': 'National Sports Center Stadium',
    'Clark\'s Athletic Field': 'Clark\'s Field',
    'RFK Stadium': 'Robert F. Kennedy Memorial Stadium',
    'RFK Memorial Stadium': 'Robert F. Kennedy Memorial Stadium',
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
