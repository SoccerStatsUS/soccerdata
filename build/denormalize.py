from collections import defaultdict
import datetime
import os

from soccerdata.data.alias import get_team
from soccerdata.mongo import soccer_db, insert_rows, generic_load

magic_names = {

    'Jorge Flores': [
        ('Jorge Villafaña', {'team': 'Chivas USA' }),
        ('Jorge Villafaña', {'team': 'Chivas USA Reserves' }),
        ],


    #'Chris Brown': [
    #    'Chris Brown 1971': {'team': 'FC Dallas' }
    }


# Use a partial?
def from_competition(competition):
    return lambda d: d['competition'] == competition

magic_teams = {
    'Olimpia': [
        (from_competition('Liga Nacional de Honduras'), 'CD Olimpia'),
        (from_competition('Copa Interclubes UNCAF'), 'CD Olimpia'),
        (from_competition('Copa Mercosur'), 'Club Olimpia'),
        (from_competition('Copa Libertadoers'), 'Club Olimpia'),

        ],

    'Necaxa': [
        (from_competition('Liga Nacional de Honduras'), 'CD Necaxa'),
        ],

    'Salzburg': [
        (from_competition('Liga Nacional de Honduras'), 'Honduras Salzburg'),
        ],

    'Valencia': [
        (from_competition('Liga Nacional de Honduras'), 'Municipal Valencia'),
        ],

    'Victoria': [
        (from_competition('Liga Nacional de Honduras'), 'CD Victoria'),
        ],

    'Juventud': [
        (from_competition('Liga Nacional de Honduras'), 'Real Juventud'),
        ],

    'Universidad': [
        (from_competition('Liga Nacional de Honduras'), 'Pumas UNAH'),
        ],

    'Antigua': [
        (from_competition('Liga Nacional de Guatemala'), 'Antigua GFC')
        ],

    'Atlético Nacional': [
        (from_competition('Liga Panameña de Fútbol'), 'Atlético Nacional (Panama)'),
        ],


    'Sacachispas': [
        (from_competition('Liga Nacional de Guatemala'), 'CSD Sacachispas')
        ],

    'Santa Lucia': [
        (from_competition('Liga Nacional de Guatemala'), 'Santa Lucía Cotzumalguapa'),
        ],

    'Heredia': [
        (from_competition('Liga Nacional de Guatemala'), 'Heredia Jaguares de Peten'),
        (from_competition('Primera División de Costa Rica'), 'CS Herediano'),
        ],

    'Santos': [
        (from_competition('Liga MX'), 'Santos Laguna'),
        (from_competition('Primera División de Costa Rica'), 'Santos de Guápiles'),
        ],

    'San Jose': [
        (from_competition('Liga de Fútbol Profesional Boliviano'), 'CD San José',),
        ],


    'Marte': [
        (from_competition('Salvadoran Primera División'), 'C.D. Atlético Marte'),
        ],


    'Sport': [
        (from_competition('Copa Libertadores'), 'SC Recife'),
        ],

    'Aguila': [
        (from_competition('Salvadoran Primera División'), 'CD Aguila'),
        (from_competition('Copa Interclubes UNCAF'), 'CD Aguila'),
        ],

    'Estudiantes': [
        (from_competition('Copa Libertadores'), 'Estudiantes de La Plata'),
        ],

    'Alianza': [
        (from_competition('Salvadoran Primera División'), 'Alianza F.C.'),
        (from_competition('Copa Interclubes UNCAF'), 'Alianza F.C.'),
        ],

    'America': [
        (from_competition('Liga MX'), 'Club America'),
        (from_competition('Liga MX Liguilla'), 'Club America'),
        ],

    'Estudiantes': [
        (from_competition('Liga MX'), 'Tecos'),
        ],

    'Real Espana': [
        (from_competition('Liga Nacional de Honduras'), 'Real C.D. España'),
        ],
    
    'Nacional': [
        (from_competition('Categoría Primera A'), 'Atlético Nacional'),
        (from_competition('Liga Panameña de Fútbol'), 'Atlético Nacional (Panama)'),
        ],

    'Sporting': [
        (from_competition('Liga Panameña de Fútbol'), 'Sporting San Miguelito'),
        ],

    'America': [
        (from_competition('Categoría Primera A'), 'America de Cali')
        ],

    'Junior': [
        (from_competition('Categoría Primera A'), 'Junior de Barranquilla'),
        ],

    'Cartagena': [
        (from_competition('Categoría Primera A'), 'Real Cartagena'),
        ],
    }



def get_magic_team(team, data):


    if team not in magic_teams:
        return team
    else:
        candidates = magic_teams[team]
        for pred, nteam in candidates:
            if pred(data):
                return nteam

    return get_team(team)


def get_magic_name(name, magic_d):
    # Confusing.
    # Just pass a predicate function?

    if name not in magic_names:
        return name
    else:
        names = magic_names[name]
        for n, nd in names:
            for k, v in nd.items():
                if magic_d.get(k) != v:
                    return name
            #import pdb; pdb.set_trace()
            #x = 5
            return n
    return name


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

    # To denormalize players, need to sort:
    # goals/assists, lineups, stats, ...
    denormalize_dream()

    
    team_name_ungetter = make_team_name_ungetter()
    stadium_getter = make_stadium_getter()
    team_city_map = dict([(get_team(e['name']), e.get('city')) for e in soccer_db.teams.find()])

    print("Generating cities.")
    generate_cities()

    print("Denormalizing standings")
    # Need to change standing team names.

    print("Denormalizing games"    )
    l = []
    for e in soccer_db.games.find():
        e['team1'] = get_magic_team(e['team1'], e)
        e['team2'] = get_magic_team(e['team2'], e)
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

            else:
                city = team_city_map.get(home_team)
                if city:
                    e['city'] = city
                

            

        l.append(e)

    soccer_db.games.drop()
    insert_rows(soccer_db.games, l)

    print("Denormalizing competitions")
    l = []

    print("Denormalizing goals")
    l = []
    for goal in soccer_db.goals.find():
        goal['team'] = get_magic_team(goal['team'], goal)
        goal['goal'] = get_magic_name(goal['goal'], goal)
        if goal['date']:
            goal['team_original_name'] = team_name_ungetter(goal['team'], goal['date'])

        l.append(goal)

    soccer_db.goals.drop()
    insert_rows(soccer_db.goals, l)


    print("Denormalizing stats")
    l = []
    for stat in soccer_db.stats.find():
        stat['team'] = get_magic_team(stat['team'], stat)
        stat['name'] = get_magic_name(stat['name'], stat)
        l.append(stat)

    soccer_db.stats.drop()
    insert_rows(soccer_db.stats, l)
            

    print("Denormalizing lineups")
    lineups = []
    for lineup in soccer_db.lineups.find():

        #if lineup['date'] == datetime.datetime(2012, 8, 7) and lineup['team'] == 'Chivas USA Reserves' and 'Jorge' in lineup['name']:
        #    import pdb; pdb.set_trace()

        lineup['team'] = get_magic_team(lineup['team'], lineup)
        lineup['name'] = get_magic_name(lineup['name'], lineup)
        lineup['team_original_name'] = team_name_ungetter(lineup['team'], lineup['date'])
        lineups.append(lineup)

    soccer_db.lineups.drop()
    insert_rows(soccer_db.lineups, lineups)

    hall_of_famers = set([e['recipient'] for e in soccer_db.awards.find({'award': 'US Soccer Hall of Fame'})])

    l = []
    for e in soccer_db.bios.find():
        e['hall_of_fame'] = e['name'] in hall_of_famers
        l.append(e)
    
    soccer_db.bios.drop()
    insert_rows(soccer_db.bios, l)

    print("Denormalizing standings")
    standings = []

    for s in soccer_db.standings.find():

        s['team'] = get_magic_team(s['team'], lineup)
        standings.append(s)

    soccer_db.standings.drop()
    insert_rows(soccer_db.standings, standings)



def denormalize_dream():
    return



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

