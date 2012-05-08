from collections import defaultdict


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


    print "Denormalizing games"    
    l = []
    for e in soccer_db.games.find():
        e['team1_name'] = e['team1']
        e['team2_name'] = e['team2']
        if e['date']:
            e['team1_original_name'] = name_ungetter(e['team1'], e['date'])
            e['team2_original_name'] = name_ungetter(e['team2'], e['date'])

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
            


            
