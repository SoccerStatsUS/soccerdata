from soccerdata.alias import get_team, get_name


DIR = '/home/chris/www/soccerdata/lists'


def process_awards(d):
    """
    Given a dictionary, process the awards described inside.
    """
    l = []
    competition = d.pop('competition')
    team_data = d.pop('team_data')
    for award, v in d.items():
        if award in team_data:
            model = 'Team'
        else:
            model = 'Bio'
            
        for season, item in v:
            season = unicode(season)
            template = {
                'competition': competition,
                'season': season,
                'award': award,
                'model': model,
                }
                
            if type(item) == list:
                for e in item:
                    if model == 'Bio':
                        e = get_name(e)
                    else:
                        e = get_team(e)

                    d = {'recipient': e}
                    d.update(template)
                    l.append(d)
            else:
                d = {'recipient': item}
                d.update(template)
                l.append(d)
    return l

                
            
def process_nasl_awards():
    from soccerdata.data.lists.nasl import d
    return process_awards(d)


def process_mls_awards():
    from soccerdata.data.lists.mls import d
    return process_awards(d)

def process_ncaa_awards():
    from soccerdata.data.lists.ncaa import d
    return process_awards(d)
    


if __name__ == "__main__":
    print process_nasl()
