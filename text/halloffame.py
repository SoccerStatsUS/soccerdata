





def load_hall_of_fame():

    f = open('/home/chris/www/soccerdata/data/lists/halloffame')
    l = []

    for line in f:
        player, year = line.strip().split(';')
        year = int(year)
        l.append({
                'competition': None,
                'year': year,
                'recipient': player,
                'model': 'Bio',
                'award': 'US Soccer Hall of Fame',
                })

    return l
                
        
        

