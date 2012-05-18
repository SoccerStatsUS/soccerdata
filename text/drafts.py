#!/usr/bin/env python


# Clean up the drafts so that we can basically remove this. This is really unnecessary.
# Export to yaml and destroy.


DRAFTS_DIR = "/home/chris/www/soccerdata/data/drafts"

import datetime
import os
import re


draft_dates = [
    ('1996 Inaugural Draft', (1996, 2, 6), (1996, 2,7)),

    ('2002 Allocation Draft', (2002, 1, 11)),
    ('2002 Dispersal Draft', (2002, 1, 11)),

    ('1996 College Draft', (1996, 3, 4)),
    ('1997 College Draft', (1997, 2, 1), (1997, 2, 2)),
    ('1998 College Draft', (1998, 1, 31), (1998, 2, 1)),
    ('1999 College Draft', (1999, 2, 6), (1999, 2, 7)),


    ('1996 Supplemental Draft', (1996, 3, 4)),
    ('1997 Supplemental Draft', (1997, 2, 2)),
    ('1998 Supplemental Draft', (1998, 2, 1)),
    ('1999 Supplemental Draft', (1999, 2, 7)),
    ('2005 Supplemental Draft', (2005, 2, 4)),
    ('2006 Supplemental Draft', (2006, 1, 26)),
    ('2007 Supplemental Draft', (2007, 1, 18)),
    ('2008 Supplemental Draft', (2008, 1, 24)),
    ('2011 Supplemental Draft', (2011, 1, 18)),

    ('2000 SuperDraft', (2000, 2, 6)),
    ('2001 SuperDraft', (2001, 2, 5)),
    ('2002 SuperDraft', (2002, 2, 10)),
    ('2003 SuperDraft', (2003, 1, 17)),
    ('2004 SuperDraft', (2004, 1, 16)),
    ('2005 SuperDraft', (2005, 1, 14)),
    ('2006 SuperDraft', (2006, 1, 20)),
    ('2007 SuperDraft', (2007, 1, 12)),
    ('2008 SuperDraft', (2008, 1, 18)),
    ('2009 SuperDraft', (2009, 1, 15)),
    ('2010 SuperDraft', (2010, 1, 14)),
    ('2011 SuperDraft', (2011, 1, 13)),

    ('1997 Expansion Draft', (1997, 11, 6)),
    ('2004 Expansion Draft', (2004, 11, 19)),
    ('2006 Expansion Draft', (2006, 11, 17)),
    ('2007 Expansion Draft', (2007, 11, 21)),
    ('2008 Expansion Draft', (2008, 11, 26)),
    ('2009 Expansion Draft', (2009, 11, 25)),
    ('2010 Expansion Draft', (2010, 11, 24)),
    ('2011 Expansion Draft', (2011, 11, 23)),
    
    ]


    

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
    # Change this name.
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

        # Skip these for now.
        if draft_type == 'expansion' and year in ('2010', '2011'):
            return {}


        try:
            number, name, team = line.split('\t')
        except:
            import pdb; pdb.set_trace()


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
            # This doesn't seem to be working.
            'text': name,
            'team': team,
            'draft': draft_name,
            'competition': 'Major League Soccer',
            #'source': 'Wikipedia',
            }

    l = [process_line(line) for line in lines]
    return [e for e in l if e]



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



def process_usmnt_draft(fn, draft_name, parser=parse_line):
    """
    """

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
            #'position': number,
            'team': team,
            'text': player,
            'draft': draft_name,
            'competition': 'Friendly',
            }


    f = open(fn)
    l = [process_line(line) for line in f.readlines()]
    for i, d in enumerate(l, start=1):
        if d:
            d['position'] = i
    return l

            


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
    

def process_usa_drafts():
    l = []
    for e in range(2004, 2012):
        p =  "/home/chris/www/soccerdata/data/drafts/%s" % e
        results = process_usmnt_draft(p, "%s USMNT Draft" % e, draft_parsers[e])
        l.extend(results)

    return [e for e in l if e]


    

if __name__ == "__main__":
    print process_usa_drafts()
