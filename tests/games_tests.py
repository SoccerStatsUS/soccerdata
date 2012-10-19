from nose.tools import *
import datetime

from soccerdata.text.games import process_string
from soccerdata.build.normalize import normalize_goal



BASIC = """
Competition: Major League Soccer
Season: 2010
12/10/2010; Seattle Sounders; 3-1; Real Salt Lake; Real Salt Lake; John Referee, Ramon Linesman, Dirk Assistant; 25000
Fredy Montero (unassisted) 2, Fredy Montero (Osvaldo Alonso) 8, Kasey Keller (pk) 18; Own Goal (Fredy Montero) 
Seattle Sounders: Kasey Keller, Osvaldo Alonso, Lamar Neagle, Fredy Montero
Real Salt Lake: Nick Rimando, Chris Schuler (Kyle Beckerman 30, Jason Kreis 60)
Source: Imagination
"""


def test_game():
    games, goals, misconduct, appearances = process_string(BASIC)
    g = games[0]
    assert_equal(g['competition'], 'Major League Soccer')
    assert_equal(g['season'], '2010')
    assert_equal(g['date'], datetime.datetime(2010, 12, 10))
    assert_equal(g['team1'], 'Seattle Sounders')
    assert_equal(g['team2'], 'Real Salt Lake')
    assert_equal(g['home_team'], 'Real Salt Lake')
    assert_equal(g['team1_score'], 3)
    assert_equal(g['team2_score'], 1)
    assert_equal(g['attendance'], 25000)
    assert_equal(g['location'], '')
    assert_equal(g['referee'], 'John Referee')
    assert_equal(g['linesmen'], ['Ramon Linesman', 'Dirk Assistant'])
    assert_equal(g['sources'], ['Imagination'])


def test_goals():
    games, goals, misconduct, appearances = process_string(BASIC)
    assert_equal(goals[0]['goal'], 'Fredy Montero')
    assert_equal(goals[0]['assists'], ['unassisted'])
    #assert_equal(goals[0]['unassisted'], True)
    assert_equal(goals[0]['date'], datetime.datetime(2010, 12, 10))
    assert_equal(goals[0]['minute'], 2)
    assert_equal(goals[0]['team'], 'Seattle Sounders')

    assert_equal(goals[1]['goal'], 'Fredy Montero')
    assert_equal(goals[1]['assists'], ['Osvaldo Alonso'])
    assert_equal(goals[1]['minute'], 8)

    assert_equal(goals[2]['goal'], 'Kasey Keller')
    assert_equal(goals[2]['assists'], ['pk'])
    #assert_equal(goals[2]['penalty_kick'], True)

    g2 = normalize_goal(goals[2])
    assert_equal(g2['assists'], [])
    assert_equal(g2['penalty'], True)

    assert_equal(goals[3]['goal'], 'Own Goal')
    assert_equal(goals[3]['assists'], ['Fredy Montero'])
    assert_equal(goals[3]['team'], 'Real Salt Lake')

    g3 = normalize_goal(goals[3])
    assert_equal(g3['own_goal'], True)
    assert_equal(g3['assists'], [])
    assert_equal(g3['own_goal_player'], 'Fredy Montero')
                        

def test_lineups():
    games, goals, misconduct, appearances = process_string(BASIC)
    assert_equal(len(appearances), 8)
    assert_equal([e['name'] for e in appearances], ['Kasey Keller', 'Osvaldo Alonso', 'Lamar Neagle', 'Fredy Montero', 'Nick Rimando', 'Chris Schuler', 'Kyle Beckerman', 'Jason Kreis'])
    assert_equal(appearances[0]['on'], 0)
    assert_equal(appearances[0]['off'], 90)
    assert_equal(appearances[0]['team'], 'Seattle Sounders')


    assert_equal(appearances[5]['name'], 'Chris Schuler')
    assert_equal(appearances[6]['name'], 'Kyle Beckerman')
    assert_equal(appearances[7]['name'], 'Jason Kreis')

    assert_equal(appearances[5]['on'], 0)
    assert_equal(appearances[6]['on'], 30)
    assert_equal(appearances[7]['on'], 60)

    assert_equal(appearances[5]['off'], 30)
    assert_equal(appearances[6]['off'], 60)
    assert_equal(appearances[7]['off'], 90)
