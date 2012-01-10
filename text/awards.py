from soccerdata.alias import get_team, get_name


DIR = '/home/chris/www/soccerdata/lists'


def process_awards(d):
    """
    Given a dictionary, process the awards described inside.
    """
    l = []
    competition = d.pop('competition')

    # Which awards are given to teams rather than people
    if 'team_data' in d:
        team_data = d.pop('team_data')
    else:
        team_data = []
        print d

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
                for recipient in item:
                    recipient = recipient.strip()
                    if model == 'Bio':
                        recipient = get_name(recipient)
                    else:
                        recipient = get_team(recipient)

                    d = {'recipient': recipient}
                    d.update(template)
                    l.append(d)
            else:
                if model == 'Bio':
                    recipient = get_name(item)
                else:
                    recipient = get_team(item)

                d = {'recipient': recipient}
                d.update(template)
                l.append(d)
    return l

                
            
def process_nasl_awards():
    from soccerdata.data.lists.nasl import d
    return process_awards(d)


def process_mls_awards():
    from soccerdata.data.lists.mls import d
    return process_awards(d)

def process_wsa_awards():
    from soccerdata.data.lists.wsa import d
    return process_awards(d)

def process_usl0_awards():
    from soccerdata.data.lists.usl0 import d
    return process_awards(d)


def process_apsl_awards():
    from soccerdata.data.lists.apsl import d
    return process_awards(d)


def process_american_cup_awards():
    from soccerdata.data.lists.americancup import d
    return process_awards(d)

def process_us_open_cup_awards():
    from soccerdata.data.lists.usopencup import d
    return process_awards(d)


def process_lewis_cup_awards():
    from soccerdata.data.lists.lewis import d
    return process_awards(d)

def process_asl2_awards():
    from soccerdata.data.lists.asl import d
    return process_awards(d)


def process_ncaa_awards():
    from soccerdata.data.lists.ncaa import d
    return process_awards(d)


def process_usl_awards():
    from soccerdata.data.lists import usl, usisl
    l = []
    l.extend(process_awards(usisl.usisl))
    l.extend(process_awards(usisl.usisl_pro))
    l.extend(process_awards(usisl.usisl_premier))
    l.extend(process_awards(usisl.usisl_select))

    l.extend(process_awards(usl.usl_pro))
    l.extend(process_awards(usl.usl_pdl))
    l.extend(process_awards(usl.usl_2))
    return l

def process_world_cup_awards():
    from soccerdata.data.lists.world_cup import d
    return process_awards(d)


    


if __name__ == "__main__":
    print process_world_cup_awards()
