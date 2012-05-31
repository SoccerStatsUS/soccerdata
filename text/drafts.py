#!/usr/bin/env python


# Clean up the drafts so that we can basically remove this. This is really unnecessary.
# Export to yaml and destroy.


DRAFTS_DIR = "/home/chris/www/soccerdata/data/lists/drafts"

import datetime
import os
import re


    

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


def load_draft_data():

    draft_filenames = ['allocation', 'college', 'dispersal', 'expansion', 'inaugural', 'nasl', 'superdraft', 'supplemental', 'supplemental2']

    l = []

    dp = DraftProcessor()
    
    for fn in draft_filenames:
        p = os.path.join(DRAFTS_DIR, fn)
        for line in open(p):
            dp.process_line(line)

    return dp


def load_drafts():
    return load_draft_data().drafts


def load_picks():
    return load_draft_data().picks
        

def process_date(s):
    month, day, year = [int(e) for e in s.split('/')]
    return datetime.datetime(year, month, day)

class DraftProcessor():
    
    def __init__(self):
        self.name = None
        self.season = None
        self.round = None
        self.pick_number = 1

        self.drafts = []
        self.picks = []


    @property
    def current_draft(self):
        return self.drafts[-1]


    def process_line(self, line):
        if line.startswith("Draft:"):
            self.name = line.replace("Draft:", '').strip()
            

        elif line.startswith("Season"):
            self.season = line.replace("Season:", '').strip()
            self.pick_number = 1
            self.drafts.append({
                    'name': self.name,
                    'season': self.season,
                    })

        elif line.startswith("Round:"):
            pass


        elif line.startswith("Date:"):
            s = line.replace("Date:", '')
            fields = s.split(',')

            fields = [e.strip() for e in fields]

            if len(fields) == 2:
                start, end = [process_date(e) for e in fields]
                
            elif len(fields) == 1:
                start = process_date(fields[0])
                end = start

            self.current_draft['start'] = start
            self.current_draft['end'] = end

        elif line.strip():
            fields = [e.strip() for e in line.split(';')]

            # Remove leading #'s if possible (we do them ourselves)
            # e.g. 12; MetroStars; Eddie Gaven; M -> MetroStars; Eddie Gaven; M

            try:
                int(fields[0])
                fields = fields[1:]
            except:
                pass

            if len(fields) == 2:
                team, text = fields
                position = former_team = None

            elif len(fields) == 3:
                team, text, position = fields
                former_team = None

            elif len(fields) == 4:
                team, text, position, former_team = fields

            else:
                import pdb; pdb.set_trace()

            self.picks.append({
                    'team': team,
                    'text': text,
                    'position': position,
                    'former_team': former_team,
                    'number': self.pick_number,
                    'draft': self.current_draft['name'],
                    'season': self.current_draft['season'],
                    })

            self.pick_number += 1







"""
def process_draft(text):
    
    # Clean up some extraneous info..
    text = text.replace("*", "")
    text = remove_pairs(text, "(", ")")
    text = remove_pairs(text, "[", "]")
    lines = [e for e in text.split("\n") if e]


    def process_line(line):

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
"""

                


            
if __name__ == "__main__":
    print load_drafts()
    
