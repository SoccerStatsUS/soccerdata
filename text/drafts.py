#!/usr/bin/env python


# Clean up the drafts so that we can basically remove this. This is really unnecessary.

DRAFTS_DIR = "/home/chris/www/soccerdata/data/drafts"

import os
import re

from soccerdata.alias.teams import get_team
from soccerdata.alias.people import get_name

# This should probably be in utils.
def remove_pairs(text, start, end):
    """
    Removes pairs like (hello) or [whatever]
    """
    s = ""
    include = True
    for char in text:
        if char == start:
            include = False

        if include:
            s += char
        
        if char == end:
            include = True

    return s


def load_drafts():
    # Load all drafts. Not including usmnt drafts, which are formatted differently
    # And are sort of annoying.
    draft_filenames = [e for e in os.listdir(DRAFTS_DIR) if e.endswith(".csv")]
    l = []
    for fn in draft_filenames:
        name = fn.split(".csv")[0]
        p = os.path.join(DRAFTS_DIR, fn)
        text = open(p).read()
        l.extend(process_draft(text, name))
    return l
        




def process_draft(text, draft_name):
    
    # Clean up some extraneous info..
    text = text.replace("*", "")
    text = remove_pairs(text, "(", ")")
    text = remove_pairs(text, "[", "]")
    lines = [e for e in text.split("\n") if e]

    try:
        draft_type, year = re.match("([a-z]+)(\d+)", draft_name).groups()
    except:
        import pdb; pdb.set_trace()

    def process_line(line):
        number, name, team = line.split('\t')

        # Whoops!
        if draft_type == 'superdraft' and year == '2010':
            name, team = team, name

        if 'superdraft' in draft_type:
            draft_name = 'SuperDraft'
        else:
            draft_name = '%s Draft' % draft_type.title()
        draft_name = "%s %s" % (year, draft_name)

        return {
            'position': int(number),
            'text': get_name(name.strip()),
            'team': get_team(team.strip()),
            'draft': draft_name,
            'competition': 'Major League Soccer',
            #'source': 'Wikipedia',
            }

    return [process_line(line) for line in lines]



# Ack! USMNT Drafts!        
# Saving for later.

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



def process_usmnt_draft(fn, draft_name, year, parser=parse_line):

    def process_line(line):
        try:
            l = parser(line)
        except: 
            import pdb; pdb.set_trace()

        if not l:
            return {}

        number, team, player = l
        if not player:
            return {}

        return {
            'number': number,
            'team': team,
            'player': player,
            'draft_name': draft_name,
            }


    f = open(fn)
    return [process_line(line) for line in f.readlines()]

            


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
    p =  "/home/chris/www/soccerdata/data/drafts/%s" % year
    parser = draft_parsers[year]
    process_usmnt_draft(p, "%s USMNT Draft" % year, year, parser)
    
    
def main():
    p =  "/home/chris/www/soccerdata/data/drafts/2011"
    process_usmnt_draft(p, "2011 USMNT Draft", 2011, parse_line)


if __name__ == "__main__":
    print load_drafts()
