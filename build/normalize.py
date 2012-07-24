import datetime


def make_stadium_getter():
    """
    Split off a stadium from a place name, if possible.
    Apply stadium location information if a stadium is found.

    Examples:
    'Pizza Hut Park, Dallas, TX' -> ('Pizza Hut Park', 'Dallas, TX')
    'Pizza Hut Park, Dallas, Texas' -> ('Pizza Hut Park', 'Dallas, TX')
    'Richardson, Texas' -> (None, 'Richardson, Texas')
    """

    from soccerdata.data.alias import get_place, get_stadium
    from soccerdata.mongo import soccer_db
    
    stadiums = soccer_db.stadiums.find()

    stadium_names = set()
    stadium_map = {}
    
    for stadium in stadiums:
        
        name = stadium['name']
        stadium_names.add(name)
        stadium_map[name] = stadium
    
    def getter(s):
        if ',' in s:
            potential_stadium, location_string = s.split(',', 1)
        else:
            potential_stadium, location_string = s, ''

        potential_stadium = get_stadium(potential_stadium)
        if potential_stadium in stadium_names:
            sx = stadium_map[potential_stadium]
            name, place = sx['name'], sx['location']
        
        else:
            name, place = None, get_place(s)

        return name, place
        
    return getter
            
    
    


def normalize():
    """
    Normalize different data types for collections.
    The goal here is to ensure that team, player, competition, and place names are consistent.
    That is, DaMarcus Beasley, Damarcus Beasley, and DeMarcus Beasley should all point to the same person.
    To do this, we aggressively standardize all names.
    Sometimes, this will result in different items being merged into one (e.g. Eddie Johnson and Edward Johnson)
    These will then be split up with denormalize.py.
    """

    from soccerdata.data.alias import get_team, get_name, get_competition, get_place
    from settings import SOURCES
    from soccerdata.mongo import generic_load, soccer_db, insert_rows, insert_row

    stadium_getter = make_stadium_getter()

    coll = soccer_db["stadiums"]
    l = []
    for e in coll.find():

        e['year_opened'] = e['year_closed'] = None
  
        if type(e['opened']) == int:
            e['year_opened'] = e.pop('opened')
            e['opened'] = None

        elif type(e['opened']) == datetime.datetime:
            e['year_opened'] = e['opened'].year

        if type(e['closed']) == int:
            e['year_closed'] = e.pop('closed')
            e['closed'] = None

        elif type(e['closed']) == datetime.datetime:
            e['year_closed'] = e['closed'].year


        l.append(e)

    coll.drop()
    insert_rows(coll, l)


        

    # Team names in games.
    for s in SOURCES:
        coll = soccer_db["%s_games" %s]

        l = []
        for e in coll.find():
            e['competition'] = get_competition(e['competition'])
            e['team1'] = get_team(e['team1'])
            e['team2'] = get_team(e['team2'])

            if 'location' in e:
                # First normalize place names.
                e['location'] = get_place(e['location'])
                # Get stadium data if possible.
                e['stadium'], e['location'] = stadium_getter(e['location'])

            if e.get('home_team'):
                e['home_team'] = get_team(e['home_team'])

            if e.get('referee'):
                e['referee'] = get_name(e['referee'])
            else:
                e['referee'] = None
            
            if 'linesmen' in e:
                linesmen = e.pop('linesmen')

                if len(linesmen) == 0:
                    pass
                elif len(linesmen) == 1:
                    e['linesman1'] = linesmen[0]
                elif len(linesmen) == 2:
                    e['linesman1'] = linesmen[0]
                    e['linesman2'] = linesmen[1]

                # This happens in one game...ok?
                elif len(linesmen) == 3:
                    e['linesman1'] = linesmen[0]
                    e['linesman2'] = linesmen[1]
                    e['linesman3'] = linesmen[2]
                else:
                    import pdb; pdb.set_trace()
                    x = 5

            l.append(e)

        coll.drop()
        insert_rows(coll, l)

    # Normalize goals.
    for s in SOURCES:
        coll = soccer_db["%s_goals" %s]
        l = []
        for e in coll.find():


            
            e['competition'] = get_competition(e['competition'])
            e['team'] = get_team(e['team'])
            try:
                e['goal'] = get_name(e['goal'])
            except:
                import pdb; pdb.set_trace()
            e['assists'] = [get_name(n) for n in e['assists']]

            l.append(e)

        coll.drop()
        insert_rows(coll, l)

    # Normalize stats
    for s in SOURCES:
        coll = soccer_db["%s_stats" %s]

        l = []
        for e in coll.find():
            e['competition'] = get_competition(e['competition'])
            e['team'] = get_team(e['team'])
            e['name'] = get_name(e['name'])


            for k in (
                'games_started', 
                'games_played', 
                'minutes', 
                'shots', 
                'shots_on_goal',
                'fouls_committed', 
                'fouls_suffered', 
                'yellow_cards', 
                'red_cards'):
                if e.get(k) == '':
                    e[k] = None

            for k in 'goals', 'assists':
                if e.get(k) == '':
                    e[k] = 0


            l.append(e)

        coll.drop()
        insert_rows(coll, l)

    # Normalize lineups
    for s in SOURCES:
        coll = soccer_db["%s_lineups" %s]
        l = []
        for e in coll.find():
            e['competition'] = get_competition(e['competition'])
            e['team'] = get_team(e['team'])
            e['name'] = get_name(e['name'])

            if type(e['on']) in (str, unicode) and e['on'].endswith('\''):
                e['on'] = e['on'][:-1]

            if type(e['off']) in (str, unicode) and e['off'].endswith('\''):
                e['off'] = e['off'][:-1]

                
            l.append(e)

        coll.drop()
        insert_rows(coll, l)

    # Normalize standings
    for s in SOURCES:
        coll = soccer_db["%s_standings" %s]

        l = []
        for e in coll.find():
            e['competition'] = get_competition(e['competition'])
            e['team'] = get_team(e['team'])

            l.append(e)

        print "Inserting %s items into %s" % (len(l), coll)
        coll.drop()
        insert_rows(coll, l)

    # Normalize awards
    for s in SOURCES:
        coll = soccer_db["%s_awards" %s]
        l = []
        for e in coll.find():
            e['competition'] = get_competition(e['competition'])

            if e['model'] == 'Team':
                e['recipient'] = get_team(e['recipient'])
            else:
                e['recipient'] = get_name(e['recipient'])

            # Skipping recipient until a little later.
            l.append(e)

        coll.drop()
        insert_rows(coll, l)

    # Normalize drafts
    coll = soccer_db["picks"]
    l = []
    for e in coll.find():
            # NB - weird naming.
        e['team'] = get_team(e['team'])
        e['text'] = get_name(e['text'])

        l.append(e)

    coll.drop()
    insert_rows(coll, l)


    # Normalize bios
    coll = soccer_db["bios"]
    l = []
    for e in coll.find():
            # NB - weird naming.
        e['name'] = get_name(e['name'])

        l.append(e)

    coll.drop()
    insert_rows(coll, l)

