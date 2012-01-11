import datetime
import os
import re

from soccerdata.alias import get_team, get_name
from soccerdata.cache import data_cache

PATH = '/home/chris/www/soccerdata/data/general/usa.text'


def get_team(s):
    t = s.strip().title()
    return team_map.get(t, t)

competition_map = {
    'FRIENDLY INTERNATIONAL': 'Friendly',
    'WORLD CUP FINALS (SOUTH KOREA) QUARTER FINAL': 'FIFA World Cup',
    'WORLD CUP FINALS (SOUTH KOREA) ROUND 2': 'FIFA World Cup',
    'WORLD CUP FINALS (SOUTH KOREA) ROUND 1': 'FIFA World Cup',
    'WORLD CUP FINALS ROUND 2': 'FIFA World Cup',
    'AMISTAD CUP': 'Amistad Cup',
    'MIAMI CUP': 'Miami Cup',
    'OLYMPIC QUALIFIER': 'Olympic Qualifier',
    'FRIENDLY INTERNATIONAL (Not Official-Italy)': 'Friendly',
    'WORLD CUP QUALIFIER/NORTH AMERICAN CHAMPIONSHIP': 'World Cup Qualifier',
    'OLYMPIC GAMES FINALS (ENGLAND)': 'Olympic Games',
    'GOLD CUP SEMI FINAL': 'Gold Cup',
    'GOLD CUP QUARTER FINAL': 'Gold Cup',
    'GOLD CUP GROUP': 'Gold Cup',
    'GOLD CUP GROUP ': 'Gold Cup',
    'WORLD CUP QUALIFIER': 'World Cup Qualifier',
    'US CUP': 'US Cup',
    'INTERNATIONAL FRIENDLY': 'Friendly',
    'CONFEDERATIONS CUP 3/4 PLACE (MEXICO)': 'Confederations Cup',
    'CONFEDERATIONS CUP SEMI FINAL (MEXICO)': 'Confederations Cup',
    'CONFEDERATIONS CUP ROUND 1 (MEXICO)': 'Confederations Cup',
    'WORLD CUP FINALS ROUND 1 (FRANCE)': 'FIFA World Cup',
    'GOLD CUP FINAL': 'Gold Cup',
    'GOLD CUP GROUP': 'Gold Cup',
    'GOLD CUP ROUND 1': 'Gold Cup',
    'GOLD CUP FINALS 3/4 PLACE': 'Gold Cup',
    'GOLD CUP FINALS GROUP MATCH': 'Gold Cup',
    'COPA AMERICA (URUGUAY) 3/4 PLACE': 'Copa America',
    'COPA AMERICA (URUGUAY) SEMI FINAL': 'Copa America',
    'COPA AMERICA (URUGUAY) QUARTER FINAL': 'Copa America',
    'COPA AMERICA (URUGUAY) GROUP MATCH': 'Copa America',
    'WORLD CUP FINALS ROUND 1': 'FIFA World Cup',
    'COPA AMERICA GROUP (ECUADOR)': 'Copa America',
    'INTERCONTINENTAL CUP 3/4 PLACE': 'Intercontinental Cup',
    'INTERCONTINENTAL CUP SEMI FINAL':'Intercontinental Cup',
    'INTERNATIONAL FRIENDLY (Not Official)': 'Friendly',
    'WORLD CUP FINALS (ITALY) ROUND 1': 'FIFA World Cup',
    'JOE ROBBIE CUP': 'Joe Robbie Cup',
    'OLYMPIC GAMES (Not Official)': 'Olympic Games',
    'OLYMPIC QUALIFIER (Not Official)': 'Olympic Qualifier',
    'NORTH AMERICAN CHAMPIONSHIP': 'North American Championship',
    'FRIENDLY INTERNATIONAL (Not Official)': 'Friendly',
    'FRIENDLY INTERNATIONAL (Not Official - Nigerian Club Side)': 'Friendly',
    'FRIENDLY INTERNATIONAL (Not Official - Scotland)': 'Friendly',
    'FRIENDLY INTERNATIONAL (Not Official - Northern Ireland)': 'Friendly',
    'MEXICO CITY TOURNAMENT': 'Mexico City Tournament',
    'MIAMI TOURNAMENT': 'Miami Tournament',
    'OLYMPIC GAMES (FRANCE) ROUND 1': 'Olympic Games',
    'PRESIDENTS CUP': 'President\'s Cup',
    'OLYMPIC GAMES (FRANCE) QUARTER FINAL': 'Olympic Games',
    'KIRIN CUP': 'Kirin Cup',
    'KIRIN CUP (JAPAN)': 'Kirin Cup',
    'CARLSBERG CUP (HONG KONG)': 'Carlsberg Cup',
    'TRINIDAD TOURNAMENT': 'Trinidad Tournament',
    'WORLD CUP FINALS (URUGUAY) ROUND 1': 'FIFA World Cup',
    'WORLD CUP FINALS (BRAZIL) ROUND 1': 'FIFA World Cup',
    'FRIENDLY INTERNATIONAL (Not Official - USSR)': 'Friendly',
    'WORLD CUP FINALS (URUGUAY) SEMI FINAL': 'FIFA World Cup',
    'OLYMPIC GAMES (NETHERLANDS) ROUND 1': 'Olympic Games',
    'PAN AMERICAN GAMES (Not Official)': 'Pan American Games',
    }

team_map = {
    'ALG': 'Algeria',
    'ARG': 'Argentina',
    'ARM': 'Armenia',
    'AUS': 'Australia',
    'AUT': 'Austria',
    'BEL': 'Belgium',
    'BER': 'Bermuda',
    'BOL': 'Bolivia',
    'BRA': 'Brazil',
    'BRB': 'Barbados',
    'BRZ': 'Brazil',
    'CAN': 'Canada',
    'CAY': 'Cayman Islands',
    'CHI': 'Chile',
    'CHINA': 'China',
    'CHN': 'China',
    'C.I.S.': 'Commonwealth of Independent States',
    'COL': 'Colombia',
    'CMR': 'Cameroon',
    'CR': 'Costa Rica',
    'CRC': 'Costa Rica',
    'CRO': 'Croatia',
    'CUB': 'Cuba',
    'CUBA': 'Cuba',
    'CZ': 'Czechoslovakia',
    'CZE': 'Czech Republic',
    'DEN': 'Denmark',
    'DPK': 'North Korea',
    'ECU': 'Ecuador',
    'EL': 'El Salvador',
    'EG': 'East Germany',
    'EGY': 'Egypt',
    'ENG': 'England',
    'ES': 'El Salvador',
    'ESP': 'Spain',
    'EST': 'Estonia',
    'FIN': 'Finland',
    'FRA': 'France',
    'GER': 'Germany',
    'GHA': 'Ghana',
    'GPE': 'Guadaloupe',
    'GR': 'Greece',
    'GRN': 'Grenada',
    'GUA': 'Guatemala',
    'HAI': 'Haiti',
    'HON': 'Honduras',
    'HTI': 'Haiti',
    'HUN': 'Hungary',
    'ICE': 'Iceland',
    'IRE': 'Ireland',
    'IRN': 'Iran',
    'ISR': 'Israel',
    'IT': 'Italy',
    'ITA': 'Italy',
    'IVC': 'Ivory Coast',
    'JAM': 'Jamaica',
    'JAP': 'Japan',
    'JPN': 'Japan',
    'KOR': 'South Korea',
    'KSA': 'Saudi Arabia',
    'LIE': 'Liechtenstein',
    'LUX': 'Luxembourg',
    'LVA': 'Latvia',
    'MAL': 'Malta',
    'MAR': 'Morocco',
    'MEX': 'Mexico',
    'MOL': 'Moldova',
    'MOR': 'Morocco',
    'MQE': 'Mozambique',
    'NA': 'Netherlands Antilles',
    'NED': 'Netherlands',
    'NGA': 'Nigeria',
    'NOR': 'Norway',
    'NZL': 'New Zealand',
    'PAN': 'Panama',
    'PAR': 'Paraguay',
    'PER': 'Peru',
    'POL': 'Poland',
    'PORT': 'Portugal',
    'RSA': 'South Africa',
    'RUM': 'Romania',
    'RUS': 'Russia',
    'SCO': 'Scotland',
    'SCOT': 'Scotland',
    'SLV': 'Slovenia',
    'SK': 'South Korea',
    'SUI': 'Switzerland',
    'SVK': 'Slovakia',
    'SVN': 'Slovenia',
    'SWE': 'Sweden',
    'THAI': 'Thailand',
    'TRI': 'Trinidad & Tobago',
    'TT': 'Trinidad & Tobago',
    'Trinidad/Tobago': 'Trinidad & Tobago',
    'Turk': 'Turkey',
    'TUR': 'Turkey',
    'TURK': 'Turkey',
    'UKR': 'Ukraine',
    'URU': 'Uruguay',
    'USA': 'United States',
    'Usa': 'United States',
    'USSR': 'USSR',
    'WAL': 'Wales',
    'YUG': 'Yugoslavia',
    'VEN': 'Venezuela',
    }
    

def process_game_chunk(s):
    lines = s.split('\n')
    competition, where, score = lines[:3]

    competition = competition_map.get(competition, competition)

    fields = where.split(',')
    if len(fields) == 2:
        date_string, city = fields
        attendance = stadium = None
    elif len(fields) == 3:
        try:
            attendance = int(fields[2])
            date_string, city = fields[:2]
            stadium = None
        except:
            date_string, city, stadium = fields
            attendance = None
    else:
        date_string, city, stadium, attendance = fields
        stadium = stadium.strip()
        attendance = int(attendance)
    
    date = datetime.datetime.strptime (date_string, "%d/%m/%Y")

    try:
        home_side, away_side = score.split('-', 1)
    except:
        import pdb; pdb.set_trace()
    home_team, home_score = re.match("(.*)\s(\d+)", home_side).groups()
    
    away_side = away_side.split('[')[0]
    away_score, away_team = re.match("(\d+)\s(.*)", away_side).groups()

    if stadium:
        location = "%s, %s" % (stadium, city)
    else:
        location = city

    game_data = {
        'date': date,
        'home_team': get_team(home_team),
        'away_team': get_team(away_team),
        'home_score': int(home_score),
        'away_score': int(away_score),
        'location': location,
        'attendance': attendance,
        'competition': competition,
        'season': unicode(date.year),
        #'source': 'http://rsssf.com/tablesu/usa-intres.html',
        }



    

    def group_parts(l):
        d = {
            'goals': '',
            'referee': '',
            'cards': ''
            }

        key = None
        l = [e.strip() for e in l]
        for line in l:
            text = line # text is everything by default
            if line.startswith("Scorer"):
                key = 'goals'
                text = line.split(':', 1)[1]
            elif line.startswith('Referee'):
                key = 'referee'
                text = line.split(':', 1)[1]
            elif line.startswith('Cards'):
                key = 'cards'
                text = line.split(':', 1)[1]

            else:
                for k in team_map:
                    if line.startswith(k):
                        key = team_map[k]
                        text = line.split(':', 1)[1]

            
            if key in d:
                d[key] = d[key] + " " + text
            else:
                d[key] = text

        return d


    def process_lineup(s, team):
        l = []
        for e in s.split(','):
            if '(' not in e:
                l.append({
                        'name': e.strip(),
                        'on': 0,
                        'off': 90,
                        })
            else:
                m = re.match("(.*)\((.*?)(\d+)\+?'?\)", e)
                if m:
                    starter, sub, minute = m.groups()
                    l.extend([{
                                'name': starter.strip(),
                                'on': 0,
                                'off': int(minute),
                                },{
                                'name': sub.strip(),
                                'on': int(minute),
                                'off': 90,
                                }])

                else:
                    m = re.match("(.*)\((.*?)\)", e)
                    if m:
                        starter, sub = m.groups()
                        l.extend([{
                                    'name': starter.strip(),
                                    'on': 0,
                                    'off': '',
                                    },{
                                    'name': sub.strip(),
                                    'on': '',
                                    'off': 90,
                                    }])
                    else:
                        import pdb; pdb.set_trace()

                    


        for d in l:
            d['name'] = get_name(d['name'])
            d.update({
              'team': team,
              'competition': competition,
              'date': date,
              'season': unicode(date.year),
              #'source': 'http://rsssf.com/tablesu/usa-intres.html',
              })


        return l
            
            

    remainder = lines[3:]
    parts = group_parts(remainder)


    def process_goals(s, lineups):

        l = []
        s = s.strip()

        if s.startswith("n/a"):
            s = s.replace("n/a", "").strip()
        s = s.replace("- ", ", ") # Watch out for Joe-Max Moore!
        if s.startswith(","):
            s = s[1:]

        if not s:
            return l


        for e in s.split(","):
            goal_type = 'normal'
            m = re.match("(.*?)(\d+)\+?'?\+?\s*\(.*?\)", e)
            if m:
                player = m.groups()[0].strip()
                minute = int(m.groups()[1])
            elif re.match("(.*?)(\d+)'?OG\s*\(.*?\)", e):
                m = re.match("(.*?)(\d+)'?OG\s*\(.*?\)", e)
                player = m.groups()[0].strip()
                minute = int(m.groups()[1])
                goal_type = 'own goal'
            elif re.match("(.*?)(\d+)'?pen\s*\(.*?\)", e):
                m = re.match("(.*?)(\d+)'?pen\s*\(.*?\)", e)
                player = m.groups()[0].strip()
                minute = int(m.groups()[1])
                goal_type = 'penalty'

            elif re.match("(.*?)(\d+)'?", e):
                m = re.match("(.*?)(\d+)'?", e)
                player = m.groups()[0].strip()
                minute = int(m.groups()[1])

            elif re.match("(.*?)\s*\(.*?\)", e):
                m = re.match("(.*?)\s*\(.*?\)", e)
                player = m.groups()[0].strip()
                minute = None
            else:
                player = e.strip()
                minute = None

            # Try to match a goal scorer to a team.
            team = None
            for d in lineups:
                if player == d['name']:
                    team = d['team']

            if team is None:
                print "No team."
                print player
                print goal_type
                print [e['name'] for e in lineups]
            else:
                l.append({
                        'goal': player,
                        'team': team,
                        'minute': minute,
                        'competition': competition,
                        'date': date,
                        'season': unicode(date.year),
                        #'source': 'http://rsssf.com/tablesu/usa-intres.html',
                        'type': goal_type,
                        'assists': [],
                        })
                
        return l
            
        

    if "referee" in parts:
        game_data['referee'] = parts.pop('referee')
        
    if 'cards' in parts:
        parts.pop('cards')
        


    lineups = []
    for k, v in parts.items():
        if k != 'goals':
            lineups.extend(process_lineup(v, k))

    if 'goals' in parts:
        goals = process_goals(parts.pop('goals'), lineups)
    else:
        goals = []

    cards = []
    
    return (game_data, goals, lineups, cards)
            
    


def process_usa_games():
    return process_data()[0]


def process_usa_goals():
    return process_data()[1]

def process_usa_lineups():
    return process_data()[2]

def process_data():
    games = []
    goals = []
    lineups = []
    text = open(PATH).read()
    chunks = [e.strip() for e in text.split("\n\n")]
    for chunk in chunks:
        game_data, goal_list, lineup_list, card_list = process_game_chunk(chunk)
        games.append(game_data)
        goals.extend(goal_list)
        lineups.extend(lineup_list)
    return (games, goals, lineups)
        

def process_usa_lineups_2002():
    f = open("/home/chris/www/soccerdata/data/lineups/usa.txt")
    lp = LineupProcessor()
    l = []
    for line in f:
        r = lp.process_row(line)
        if r:
            l.append(r)
    return r
        
        
        



class LineupProcessor(object):
    def __init__(self):
        self.date = None
        
        
    def process_row(self, row):
        if '/' in row:
            try:
                month, day, year = [int(e) for e in row.split('/')]
                self.date = datetime.datetime(year, month, day)
                return
            except:
                print row


        if row.startswith('Substitutes Not Used'):
            return 

        if row.startswith('Unavailable'):
            return 

        if row.startswith('Not Eligible'):
            return 

        if not row.strip():
            return


        if ':' in row:
            team, lineup = row.split(':', 1)
            team = team_map[team.strip()]

            if self.date is None:
                import pdb; pdb.set_trace()
            
            return {
                'date': self.date,
                'team': team,
                'season': unicode(self.date.year),
                }
            
        else:
            print row

        
            

        
    
if __name__ == "__main__":
    process_usa_lineups_2002()
