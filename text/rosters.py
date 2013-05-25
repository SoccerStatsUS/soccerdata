#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


import os
import re


 
def fix_roster_name(name):

    char_dict = {
        'Á': 'á',
        'Ã': 'ã',
        'Ó': 'ó',
        'É': 'é',
        'Ñ': 'ñ',
        'Ú': 'ú',
        'Í': 'í',
        'Ô': 'ô',
        }
    

    # Title doesn't work with abnormal characters.
    # Maybe coerce to unicode first?
    #name = unicode(name, 'utf-8')
    name_parts = name.split(' ')

    l = []
    for part in name_parts:
        part = part.lower()
        s = ''
        
        first_letter = True
        for char in part:
            if first_letter and char != '"':
                char = char.capitalize()
                first_letter = False

            char = char_dict.get(char, char)
            s += char
        l.append(s)

    return ' '.join(l)

        


def process_rosters(fn):

    l = []

    p = os.path.join('/home/chris/www/soccerdata/data/rosters/', fn)
    f = open(p)

    competition = season = team = None
    rp = RosterProcessor()
    for line in f:
        rp.process_line(line)

    return rp.rosters
            


class RosterProcessor(object):
    
    def __init__(self):
        self.competition = None
        self.season = None
        self.team = None

        self.rosters = []

    def process_line(self, line):
        line = line.strip()
        if not line:
            return

        if line.startswith('*'):
            return

        if line.startswith('NOTE'):
            return

        if line.startswith("Coach"):
            return

        # Set the competition.
        if line.startswith("Competition:"):
            self.competition = line.split("Competition:")[1].strip()
            return

        if line.startswith("Season:"):
            self.season = line.split("Season:")[1].strip()
            return

        if line.startswith("Team:"):
            self.team = line.split("Team:")[1].strip()
            return


        else:
            m = re.match("\d+(.*)", line)
            if m:
                s = m.groups()[0]
            else:
                s = line

            fields = s.split('  ')
            player = fields[0].strip()


            player = player.title()

            if player in  ('-', ''):
                return

            if '-' in player:
                player = player.split('-')[0].strip()

            player = fix_roster_name(player)

            self.rosters.append({
                    'competition': self.competition,
                    'season': self.season,
                    'team': self.team,
                    'name': player,
                    })


