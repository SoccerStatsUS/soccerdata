#!/usr/bin/env python


from soccer.drafts.models import Draft, Pick
from soccer.players.models import Person
from soccer.leagues.models import League
from soccer.teams.models import Team

one_word_names = [e[0] for e in Person.objects.exclude(name__contains=" ").values_list('name')]


def parse_line_2004(l):
    n, r = l.split(".", 1)
    number = int(n.strip())
    name, position, t, team = [e.strip() for e in r.split(",")]
    if " " in name:
        return number, team, name
    else:
        return

def parse_line_2005(l):
    n, r = l.split(".", 1)
    number = int(n.strip())
    name, t, team = [e.strip() for e in r.split("---")]
    return number, team, name


def parse_line_2006(l):
    n, r = l.split(".", 1)
    number = int(n.strip())
    team, name = [e.strip() for e in r.split("--")]
    return number, team, name
    return number, team, name

def parse_line_2007(l):
    n, r = l.split(".", 1)
    number = int(n.strip())
    team, name = [e.strip() for e in r.split("-") if e.strip()]
    return number, team, name

parse_line_2008 = parse_line_2007
    

def parse_line_2011(l):
    assert l.count('-') == 1
    n, r = l.split(".", 1)
    number = int(n.strip())
    team, name = [e.strip() for e in r.split('-')]
    return number, team, name

def parse_line(l):
    l = l.strip()
    num, remainder =l.split('.', 1)
    number = int(num.strip())
    team, name = [e.strip() for e in remainder.split("-", 1)]
    return number, team, name




def create_or_get_team(name):
    try:
        return Team.objects.get(name=name)
    except:
        t = Team.objects.create(name=name, 
                                short_name=name,
                                league=League.objects.get(name="Big Soccer"))
        return t

def process_draft(fn, name, year, parser=parse_line):
    try: 
        d = Draft.objects.create(name=name, year=year)
    except:
        d = Draft.objects.get(name=name, year=year)
        for e in d.pick_set.all():
            e.delete()
    league = League.objects.get(name="Big Soccer")
    


    f = open(fn)
    i = 0
    for line in f.readlines():
        i += 1
        try:
            l = parser(line)
        except: 
            import pdb; pdb.set_trace()

        if not l:
            continue

        number, team, player = l
        if not player:
            continue

        t = create_or_get_team(team)
            
        try:
            p = Person.objects.get_person(player)
        except:
            p = Person.objects.create(name=player)
    
            
        
        Pick.objects.create(draft=d,
                            team=t,
                            player=p,
                            name=player,
                            number=i)


draft_parsers = {
    2004: parse_line_2004,
    2005: parse_line_2005,
    2006: parse_line_2006,
    2007: parse_line_2007,
    2008: parse_line_2008,
    2009: parse_line,
    2010: parse_line,
    2011: parse_line_2011,
    }
    




def run_draft(year):
    p =  "/home/chris/www/soccer/data/usmnt_drafts/%s" % year
    parser = draft_parsers[year]
    process_draft(p, "%s USMNT Draft" % year, year, parser)
    
    
def main():
    p =  "/home/chris/www/soccer/data/usmnt_drafts/2011"
    process_draft(p, "2011 USMNT Draft", 2011, parse_line)
