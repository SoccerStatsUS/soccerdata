from collections import defaultdict


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

def make_name_ungetter():
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
        
        if name not in d:
            return name
        else:
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
        
        


def denormalize():
    from soccerdata.mongo import soccer_db, insert_rows
    
    print "Denormalizing"
    name_ungetter = make_name_ungetter()
    stadium_getter = make_stadium_getter()


    print "Denormalizing games"    
    l = []
    for e in soccer_db.games.find():
        if e['date']:
            e['team1_original_name'] = name_ungetter(e['team1'], e['date'])
            e['team2_original_name'] = name_ungetter(e['team2'], e['date'])

            home_team = e.get('home_team')
            if home_team and not e.get('stadium'):
                stadium = stadium_getter(home_team, e['date'])
                if stadium:
                    e['stadium'] = stadium

        l.append(e)

    soccer_db.games.drop()
    insert_rows(soccer_db.games, l)

    print "Denormalizing goals"
    l = []
    for e in soccer_db.goals.find():
        if e['date']:
            e['team_original_name'] = name_ungetter(e['team'], e['date'])

        l.append(e)

    soccer_db.goals.drop()
    insert_rows(soccer_db.goals, l)
            

    print "Denormalizing lineups"            
    l = []
    for e in soccer_db.appearances.find():
        if e['date']:
            e['team_original_name'] = name_ungetter(e['team'], e['date'])

        l.append(e)

    soccer_db.appearances.drop()
    insert_rows(soccer_db.appearances, l)

    hall_of_famers = set([e['recipient'] for e in soccer_db.awards.find({'award': 'US Soccer Hall of Fame'})])

    l = []
    for e in soccer_db.bios.find():
        e['hall_of_fame'] = e['name'] in hall_of_famers
        l.append(e)
    
    soccer_db.bios.drop()
    insert_rows(soccer_db.bios, l)

            


            
