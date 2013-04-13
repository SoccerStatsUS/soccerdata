from collections import defaultdict
from soccerdata.mongo import soccer_db, insert_rows, generic_load

import os
import cPickle




def make_stadium_getter():
    """
    Given a team name, eg FC Dallas and a date, return the appropriate stadium.
    """
    
    from text import stadiummap

    d = defaultdict(list)
    for x in stadiummap.load():
        key = x['team']
        value = (x['stadium'], x['start'], x['end'])
        d[key].append(value)


    def getter(team, team_date):
        
        if team_date is None:
            return team
        
        if team not in d:
            return team
        else:
            times_list = d[team]

            for u in times_list:
                try:
                    t, start, end = u
                except:
                    import pdb; pdb.set_trace()
                if start <= team_date <= end:
                    return t

        # fallback.
        return team

    return getter



def make_team_name_ungetter():
    """
    Given a canonical name, eg FC Dallas, return the time-specific name, e.g. Dallas Burn.
    """
    from text import namemap

    d = defaultdict(list)
    for x in namemap.load():
        key = x['from_name']
        value = (x['to_name'], x['start'], x['end'])
        d[key].append(value)


    def getter(name, name_date):

        if name_date is None:
            return name
        
        if name not in d:
            return name



        # Load the mapping of dates to team names
        # and iterate through it
        # e.g. [('Dallas Burn', 1/1/1996, 12/31/2001), ...]
        times_list = d[name]
        for u in times_list:
            try:
                t, start, end = u
            except:
                import pdb; pdb.set_trace()
            if start <= name_date <= end:
                return t

        # fallback.
        return name


    return getter
        

def make_competition_name_ungetter():
    """
    Given a canonical name, eg US Open Cup, return the time-specific name, e.g. National Challenge Cup
    """
    from text import competitionnamemap

    d = defaultdict(list)
    for x in namemap.load():
        key = x['from_name']
        value = (x['to_name'], x['seasons'])
        d[key].append(value)


    def getter(name, name_season):

        if name_date is None:
            return name
        
        if name not in d:
            return name

        # Load the mapping of dates to team names
        # and iterate through it
        # e.g. [('Dallas Burn', 1/1/1996, 12/31/2001), ...]        

        to, seasons = d[name]
        if name_season in seasons:
            return to


        return name

    return getter
        
        


def denormalize():
    """
    Reverse the normalization process.
    This consists of a couple of different processes.
    First, we want to have correct, time-sensitive names for teams, competitions, and stadiums.
    So Sporting Kansas City should be Kansas City Wiz for 1996, Kansas City Wizards for 1997-2009, and 
    Sporting Kansas City for 2010-
    Furthermore, we will need to split some players and teams who share the same name.
    e.g. Eddie Johnson should be split into Eddie Johnson (1984) and Eddie Johnson (1988) (correct birthdates?)
    This is done by explicitly coding enough identity information to distinguish players.
    (Eddie Johnson (1984) played for FC Dallas, Sporting Kansas City, and Seattle Sounders)

    Additionally, this is where we apply stadium information to games. If we know the home team but not the location,
    we set the location to the team's stadium for that date if possible.
    """


    
    team_name_ungetter = make_team_name_ungetter()
    stadium_getter = make_stadium_getter()

    print "Generating cities."
    generate_cities()


    print "Denormalizing standings"
    # Need to change standing team names.

    print "Denormalizing games"    
    l = []
    for e in soccer_db.games.find():
        e['team1_original_name'] = team_name_ungetter(e['team1'], e['date'])
        e['team2_original_name'] = team_name_ungetter(e['team2'], e['date'])

        # I suspect that this is happening far too late in the process.
        # When do stadium / city pairs get generated?
        home_team = e.get('home_team')
        if home_team and not e.get('stadium'):
            stadium = stadium_getter(home_team, e['date'])

            # stadium_getter returns home_team as a fallback; don't set that.
            if stadium and stadium != home_team:
                e['stadium'] = stadium

        l.append(e)

    soccer_db.games.drop()
    insert_rows(soccer_db.games, l)

    print "Denormalizing competitions"
    l = []

    print "Denormalizing goals"
    l = []
    for e in soccer_db.goals.find():
        if e['date']:
            e['team_original_name'] = team_name_ungetter(e['team'], e['date'])

        l.append(e)

    soccer_db.goals.drop()
    insert_rows(soccer_db.goals, l)
            

    print "Denormalizing lineups\n\n"            
    l = []
    for e in soccer_db.lineups.find():

        e['team_original_name'] = team_name_ungetter(e['team'], e['date'])


        l.append(e)

    soccer_db.lineups.drop()
    insert_rows(soccer_db.lineups, l)

    hall_of_famers = set([e['recipient'] for e in soccer_db.awards.find({'award': 'US Soccer Hall of Fame'})])

    l = []
    for e in soccer_db.bios.find():
        e['hall_of_fame'] = e['name'] in hall_of_famers
        l.append(e)
    
    soccer_db.bios.drop()
    insert_rows(soccer_db.bios, l)

            


            

def generate_cities():

    cities = set()


    for e in soccer_db.teams.find():
        if 'city' in e:
            cities.add(e['city'])

    for e in soccer_db.bios.find():
        cities.add(e.get('birthplace'))
        cities.add(e.get('deathplace'))



    for e in soccer_db.games.find():
        if 'location' in e:
            cities.add(e['location'])



    for e in soccer_db.stadiums.find():
        cities.add(e['location'])

    if None in cities:
        cities.remove(None)


    city_dicts = [{'name': city} for city in sorted(cities)]
    
    generic_load(soccer_db.cities, lambda: city_dicts)
    return

"""
    return city_dicts

    from googlegeocoder import GoogleGeocoder
    geocoder = GoogleGeocoder()

    city_dicts = {}

    CITIES_FILE_PATH = "/home/chris/www/soccerdata/data/cities_data"

    if os.path.exists(CITIES_FILE_PATH):
        city_dicts = cPickle.load(open(CITIES_FILE_PATH))
    else:
        city_dicts = {}

    for city in sorted(cities)[:100]:
        if city not in city_dicts:
            try:
                locations = geocoder.get(city)
                location = locations[0]
            except ValueError:
                location = None

        city_dicts[city] = location
    
    cPickle.dump(city_dicts, open(CITIES_FILE_PATH, 'w'))

    #generic_load(soccer_db.cities, lambda: city_dicts)

"""
