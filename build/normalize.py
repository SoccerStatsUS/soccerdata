
def normalize():
    from soccerdata.alias import get_team, get_name, get_competition
    from settings import SOURCES
    from soccerdata.mongo import generic_load, soccer_db, insert_rows, insert_row

        

    # Team names in games.
    for s in SOURCES:
        coll = soccer_db["%s_games" %s]
        l = []
        for e in coll.find():
            e['competition'] = get_competition(e['competition'])
            e['team1'] = get_team(e['team1'])
            e['team2'] = get_team(e['team2'])
            if e['home_team']:
                e['home_team'] = get_team(e['home_team'])

            l.append(e)

        coll.drop()
        insert_rows(coll, l)


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



    for s in SOURCES:
        coll = soccer_db["%s_lineups" %s]
        l = []
        for e in coll.find():
            e['competition'] = get_competition(e['competition'])
            e['team'] = get_team(e['team'])
            e['name'] = get_name(e['name'])

            l.append(e)

        coll.drop()
        insert_rows(coll, l)



    for s in SOURCES:
        coll = soccer_db["%s_standings" %s]
        l = []
        for e in coll.find():
            e['competition'] = get_competition(e['competition'])
            # NB - weird naming.
            e['team'] = get_team(e['team'])

            l.append(e)

        coll.drop()
        insert_rows(coll, l)



    for s in SOURCES:
        coll = soccer_db["%s_awards" %s]
        l = []
        for e in coll.find():
            e['competition'] = get_competition(e['competition'])
            # Skipping recipient until a little later.
            l.append(e)

        coll.drop()
        insert_rows(coll, l)




    for s in SOURCES:
        coll = soccer_db["%s_drafts" %s]
        l = []
        for e in coll.find():
            # NB - weird naming.
            e['team'] = get_team(e['team'])
            e['text'] = get_name(e['text'])

            l.append(e)

        coll.drop()

