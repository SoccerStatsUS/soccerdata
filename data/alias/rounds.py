#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


def get_round(s):
    """
    Recursive. 
    """

    s = s.strip()
    if s in rounds:
        return get_round(s)
    else:
        return s


rounds = {
    'Round  1': 'Round 1',
    'Round  2': 'Round 2',
    'Round  3': 'Round 3',
    'Round  4': 'Round 4',
    'Round  5': 'Round 5',
    'Round  6': 'Round 6',
    'Round  7': 'Round 7',
    'Round  8': 'Round 8',
    'Round  9': 'Round 9',
    'Semi Finals': 'semifinals',
    'Semi-Finals': 'semifinals',
    'Semifinal': 'semifinals',
    'Semifinal Round': 'semifinals',
    'Semifinal Stage': 'semifinals',
    'Semifinals': 'semifinals',

    'Bronze Medal': 'third place',
    'Bronze Medal Game': 'third place',
    'Bronze Medal Match': 'third place',

    'Third Place': 'third place',
    'Third Place Game': 'third place',
    'Third Place Match': 'third place',
    'Third Place Matches': 'third place',
    'Third Place Playoff': 'third place',
    'Third Round': 'third place',
    'Third place': 'third place',
    'third place': '3rd place',

    '3rd Place': '3rd place',
    '3rd Place Match': '3rd place',

    '5th Place Match': '5th place',

    '8th Place': '8th place',
    

    'Qualifying': 'qualifying',
    'Qualifying Matches': 'qualifying',
    'Qualifying Playoff':  'qualifying',
    'Qualifying Round':  'qualifying',
    'Qualifying Rounds':  'qualifying',
    'Qualifying round':  'qualifying',

    'Quarter Finals': 'quarterfinals',
    'Quarter-Finals':  'quarterfinals',
    'Quarter-finals': 'quarterfinals',
    'Quarterfinal': 'quarterfinals',
    'Quarterfinals': 'quarterfinals',



    'First Round': 'first',
    'First Rounds': 'first',

    'Final': 'finals',
    'Final Playoff': 'finals',
    'Final Round': 'finals',
    'Final Stage': 'finals',
    'Final Tournament': 'finals',
    'Finals': 'finals',
    'Grand Final': 'finals',

    'Intermediate Round': 'intermediate',

    'Fifth Place Match': '5th place',

    'Fourth Place Match': '4th place',

    'Play-Offs': 'playoffs',
    'Playoff': 'playoffs',

    'Play-in Round': 'play-in',

    'Repesca': 'repesca',
    'Triangular Final' : 'triangular final',

    '1/8 Final': 'round of 8',
    '1/8 final': 'round of 8',

    'Round of 16': 'round of 16',
    'Round of Sixteen': 'round of 16',
    '1/16 final': 'round of 16',

    'Round of 32': 'round of 32',
    'Round of 64': 'round of 64',




}
