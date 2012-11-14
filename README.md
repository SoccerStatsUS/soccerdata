

* Outstanding data gaps.

* 2010 World Cup
* MLS 2012 season data.
* Gold Cup champions; non-us results/goals/lineups
* United States game location information; scattered unknown opponent lineups.
* Open Cup information is spotty; watch out for release of new Open Cup data.
* NASL lineup and goal info.
* ASL game locations/refs; lineups + goals
* CCL lineup/goal info is very weak.
* SuperLiga non-US goals/lineups
* CCC information is quite weak.
* Copa America everything - available at RSSSF
* USL-1, USL-2 2001-2003 lineups/goals; 2008-2009 lineups/goals
* ISL data incomplete.
* PDL everything.
* Everything APSL pre-1993; 1994-1995 is spotty.
* ASL2 entirely terrible.







* Fix Brooklyn Hakoah name mapping (other ASL name mappings.)
* Draw graph of seasons.

0. Fix giant ASL team name bug issue - easy but producing a lot of errors.
1. Convert bios to yaml.
2. Consider moving aliases into data.

# Error detection

# This is an attempt to minimize errors; there will inevitably still be stuff that this doesn't check.

1. Teams playing multiple games on the same day.
2. Lineups without stat.
3. Lineup with fewer than 11 starters.
4. Goals don't equal score.
5. Similar names, same birthdate?
6. Make schemas that data has to match.

mlssoccer missing players:
1. Toni Stahl
2. Jimmy Nielsen (presumably more GK's)
3. Mamadou Diallo
4. Jonathan Bornstein
5. Wade Barrett


0. Use AWS to build database.
1. Convert data files to yaml (once sure it's being parsed correctly?)
2. Strengthen wiki scraper and canvass team, player data.
3. News as data. Collect all the soccer news feeds. Use them to pull out interesting data.
5. Add data consistency checking.
6. Learn about unicode and figure out these unicode problems in utils.

# Data definitions

game 
 - teams
 - score
 - date
 - competition
 - season
 - referee

 optional
 - location
 - attendance
 - notes

goal
 - player
 - minute

# Need to choose, either date & team or game; (probably game)
 - date
 - team
 - game
 
 optional
 - penalty
 - own_goal


stat
 - player
 - team
 - competition
 - season

 optional
 - minutes
 - games_started
 - games_played
 - goals
 - assists
 - shots
 - shots_on_goal
 - fouls_committed
 - fouls_suffered
 - yellow_cards
 - red_cards
 - wins, losses, ties, gf, ga, +/, etc.

game stat
 - player
 - team
 - game
 optional
 - same as stat

lineup
 - name
 - on
 - off
 - game
 - team


standing
 - team
 - wins
 - ties
 - losses
 - competition
 optional
 - goals_for
 - goals_against


bio
 - name
 optional
 - birthdate
 - birthplace
 - height
 - weight
 - college
 - nationality?


## Data breakdown

# Event data
 - goals
 - substitutions
 - fouls
 - tackles
 - passes
 - etc. 

# Summary data
 - scores
 - standings
 - game stats
 - competition stats (is a game a miniature competition?)
 - teams (?)
 - lineup data

# Ancillary data
 - salaries
 - awards
 - biographical data

# Prospective
 - place data


# Normalization - what do we need to normalize and how?

# Team names.

Just create a list of canonical team names.

# Player names.
1. Create guesses based on name similarity with birthdate
2. Use lineup data to create theories about likely players.

# What are these?
http://www.sports-reference.com/stathead/section/soccer/
http://www.soccermetricsblog.com/2011/06/pythagorean-table-2011-mls-regular-season-20110612-version.html


Data notes:
I moved Dallas - Apollon game on 7/8/1971 forward a day for convenience. Please look up the actual date.; Likewise the Hapoel gameo on 6/30/1970, and Veracruz in 7/11/1973 (Dallas/Atlanta)b. and 6/28/1970 Hapoel /St. Louis / Washington