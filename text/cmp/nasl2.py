# This is for the New NASL!!!
# This should be split off into a separate file!!!
def process_stats():
    """
    Process modern NASL stats taken from nasl.com
    """

    NASL_STATS_DIR = '/home/chris/www/soccerdata/data/stats/d2'

    lst = []
    for fn in ('2011', '2012'):
        p = os.path.join(NASL_STATS_DIR, fn)
        f = open(p)
        for line in f:

            fields = line.split("  ") # 2 spaces
            fields = [e.strip() for e in fields if e.strip()]

            if fn == '2011':
                name, team, goals, assists, shots, yc, rc, minutes = fields
                sog = None
            else:
                try:
                    name, team, goals, assists, shots, sog, yc, rc, minutes = fields
                except:
                    print(line)
                    continue

                sog = int(sog)

            name = name.split(")")[1].strip()
            lst.append({
                    'competition': "North American Soccer League (2011-)",
                    'season': fn,
                    'name': name,
                    'team': team,
                    'position': '',
                    'goals': int(goals),
                    'assists': int(assists),
                    'shots': int(shots),
                    'shots_on_goal': sog,
                    'yellow_cards': int(yc),
                    'red_cards': int(rc),
                    'minutes': int(minutes),
                    })
                
    return lst

