


DIR = '/home/chris/www/soccerdata/lists'


def process_awards(d):
    """
    Given a dictionary, process the awards described inside.
    """
    l = []
    competition = d.pop('competition')

    if 'champion' in d:
        champion_name = d.pop('champion')
    else:
        champion_name = None
    

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

        if award == champion_name or award == 'Champion':
            award_type = 'champion'
        else:
            award_type = ''

        for e in v:
            if len(e) != 2:
                import pdb; pdb.set_trace()
            season, item = e
            try:
                season = unicode(season)
            except:
                import pdb; pdb.set_trace()
            template = {
                'competition': competition,
                'season': season,
                'award': award,
                'model': model,
                'type': award_type,
                }
                
            if type(item) == list:
                for recipient in item:
                    d = {'recipient': recipient }
                    d.update(template)
                    l.append(d)
            else:
                d = {'recipient': item }
                d.update(template)
                l.append(d)
    return l

                

def process_nasl_awards():
    from soccerdata.data.lists.awards.nasl import d
    return process_awards(d)

def process_csl_awards():
    from soccerdata.data.lists.awards.canada import csl
    return process_awards(csl)

def process_canada_awards():
    from soccerdata.data.lists.awards.canada import championship
    return process_awards(championship)


def process_ny_awards():
    from soccerdata.data.awards.lists import ny
    return process_awards(ny.mafl) + process_awards(ny.nysal) + process_awards(ny.snysfbac)


def process_concacaf_awards():
    from soccerdata.data.lists.awards.concacaf import champions_cup, champions_league, superliga
    return process_awards(champions_cup) + process_awards(champions_league) + process_awards(superliga)


def process_australia_awards():
    from soccerdata.data.lists.awards.australia import d
    return process_awards(d)



def process_olympics_awards():
    from soccerdata.data.lists.olympics import d
    return process_awards(d)


def process_conmebol_awards():
    from soccerdata.data.lists.awards.conmebol import copa_america
    return process_awards(copa_america)


def process_usa_awards():
    from soccerdata.data.lists.awards.nasl import usa
    return process_awards(usa)

def process_npsl_awards():
    from soccerdata.data.lists.awards.nasl import npsl
    return process_awards(npsl)

def process_ussf2_awards():
    from soccerdata.data.lists.awards.usl import ussf2
    return process_awards(ussf2)

def process_nasl2_awards():
    from soccerdata.data.lists.awards.usl import nasl2
    return process_awards(nasl2)

def process_nasl2p_awards():
    from soccerdata.data.lists.awards.usl import nasl2p
    return process_awards(nasl2p)


def process_mls_awards():
    from soccerdata.data.lists.awards.mls import d
    return process_awards(d)

def process_mls_reserve_awards():
    from soccerdata.data.lists.awards.mls import mlsrl
    return process_awards(mlsrl)


def process_mls_cup_awards():
    from soccerdata.data.lists.awards.mls import d2
    return process_awards(d2)

def process_wsa_awards():
    from soccerdata.data.lists.awards.wsa import d
    return process_awards(d)

def process_usl0_awards():
    from soccerdata.data.lists.awards.usl0 import d
    return process_awards(d)


def process_apsl_awards():
    from soccerdata.data.lists.awards.apsl import d
    return process_awards(d)

def process_apslpc_awards():
    from soccerdata.data.lists.awards.apsl import apslpc
    return process_awards(apslpc)


def process_american_cup_awards():
    from soccerdata.data.lists.awards.americancup import d
    return process_awards(d)

def process_us_open_cup_awards():
    from soccerdata.data.lists.awards.usopencup import d
    return process_awards(d)


def process_lewis_cup_awards():
    from soccerdata.data.lists.awards.lewis import d
    return process_awards(d)

def process_asl2_awards():
    from soccerdata.data.lists.awards.asl import d
    return process_awards(d)

def process_asl_awards():
    from soccerdata.data.lists.awards.asl0 import d
    return process_awards(d)


def process_nafbl_awards():
    from soccerdata.data.lists.awards.nafbl import nafbl
    return process_awards(nafbl)

def process_snesl_awards():
    from soccerdata.data.lists.awards.nafbl import snesl
    return process_awards(snesl)


def process_esl_awards():
    from soccerdata.data.lists.awards.asl0 import esl
    return process_awards(esl)



def process_ncaa_awards():
    from soccerdata.data.lists.awards.ncaa import d
    return process_awards(d)

def process_isl_awards():
    from soccerdata.data.lists.awards.isl import d
    return process_awards(d)


def process_usl_awards():
    from soccerdata.data.lists.awards import usl, usisl
    l = []
    l.extend(process_awards(usisl.usisl))
    l.extend(process_awards(usisl.usisl_pro))
    l.extend(process_awards(usisl.usisl_premier))
    l.extend(process_awards(usisl.usisl_select))

    l.extend(process_awards(usl.usl_pro))

    l.extend(process_awards(usl.usl_2))
    l.extend(process_awards(usl.usl_1))
    return l


def process_pdl_awards():
    from soccerdata.data.lists.awards import usl
    return process_awards(usl.usl_pdl)

def process_world_cup_awards():
    from soccerdata.data.lists.awards.world_cup import d
    return process_awards(d)


    


if __name__ == "__main__":
    print process_world_cup_awards()
