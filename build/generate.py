from standings import get_standing


def generate():
    # Generate
    generate_standings()
    generate_stats()
    generate_transfers()



def generate_standings():
    # Use generic_load here.
    standings = generate_fbleague_standings()

def generate_fbleague_standings():
    coll = mongo.soccer_db.fbleague_scores
    seasons = set()
    for doc in coll.find():
        # Don't use a dict. unahshable
        t = (doc['competition'], doc['season'])
        seasons.add(t)
    
    standings = []
    for t in seasons:
        d = {'competition': t[0], 'season': t[1]}
        games = coll.find(d)
        standings.append(get_standings(games))
        
    return standings


def generate_stats():
    pass

                
def generate_transfers():
    pass
