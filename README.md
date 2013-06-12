* Need to define parser, data formats better.

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




* American Soccer League team timeline.


Ph. FC/Bethlehem Steel        1921/1922 1923 1924 1925 1926 1927 1928. 1929. 1929. 1930s
NYFC1/Ind Floor/NY Nats/NYG   1921 1922 1923/1924 1925 1926/1927 1928f 1929s 1929f 1930s/1930f 1931s 1931f 1932s
Todd Shipyards                1921
Harrison Soccer Club          1921 1922 
J&P Coats/Paw. Rangers        1921 1922 1923 1924 1925 1926 1927 1928w/1929s 1929f 1930s 1930f 1931s 1931f 1932s 1932f
Fall River United             1921
Holyoke Falcos                1921
Jersey City Celtics           1921
Fall River Marksmen/NYY            1922 1923 1924 1925 1926 1927 1928f 1929s 1929f 1930s 1930f/1931s
Paterson Sox/NY Giants/NY SC       1922/1923 1924 1925 1926 1927 1928. 1929. 1929. 1930s/1930f
Brooklyn Wanderers                 1922 1923 1924 1925 1926 1927 1928f 1929s 1929f 1930s 1930f 1931s
Ph. FC2/Ph. Celtic                 1922 1923 1924 1925 1926 1927
Newark Skeeters                         1923 1924 1925 1926 1927 1928. 1929. 1929.
Boston Wonder Workers                        1924 1925 1926 1927 1928f 1929s/1929f/1930s 
New Bedford Whalers                          1924 1925 1926 1927 1928f 1929s 1929f 1930s 1930f 1931s
Prov. Clams/GBs/FR FC/NBW2                   1924 1925 1926 1927/1928f 1929s 1929f 1930s 1930f/1931s 1931f 1932s
Fleisher Yarn                                1924
Shawsheen Indians                                 1925
Springfield Babes                                      1926
Hartford Americans                                          1927
Philadelphia FC3                                                 1928a 1929s 1929f
Jersey City                                                            1929s 
Brooklyn Hakoah/Hakoah All-Stars                                             1929f/1930s 1930f 1931s 1931f 1932s 1932f
New York Hakoah                                                        1929. 1929.
IRT Rangers                                                            1929. 1929.
Philadelphia Centennials                                               1929. 1929.
New York Hispano                                                       1929. 1929. 
New York Celtic                                                        1929. 1929.
New York Hungaria                                                            1929.
Bridgeport Hungaria/Newark                                                         1930s
Newark Americans                                                                         1930f 1931s 1931f 1932s 
Boston Bears                                                                                   1931s 1931f 1932s 1932f
New York Americans                                                                                   1931f 1932s 1932f 1933s 1933f 1934 1935 1936 1937 1938 1939
Fall River FC (=NBW2?)                                                                                           1932f
New York Field Club #3                                                                                           1932f
Brooklyn Wanderers #2                                                                                            1932f 1933s
Queens Bohemians                                                                                                 1932f 1933s
Brookhattan                                                                                                            1933s 1933f 1934 1935 1936 1937 1938 1939
Prague Americans                                                                                                       1933s
Kearny Irish                                                                                                                 1933f 1934 1935 1936 1937 1938 1939
Kearny Scots                                                                                                                 1933f 1934 1935 1936 1937 1938 1939
Brooklyn Celtic                                                                                                              1933f 1934 1935 1936 1937 1938 1939
Newark Germans/Paterson Caledonian/Trenton Highlanders/Paterson FC                                                           1933f 1934 1935/1936 1937 1938 1939
Brooklyn Hispano                                                                                                             1933f 1934 1935 1936 1937 1938 1939
Philadelphia German-Americans                                                                                                1933f 1934 1935 1936 1937 1938 1939
Baltimore Canton/SC                                                                                                                1934 1935/1936 1937 1938 1939
Philadelphia Passon                                                                                                                          1936 1937 1938 1939
Bethlehem Hungarian/Allentown                                                                                                                          1938/1939
Baltimore German/Baltimore Americans                                                                                                                   1938/1939



1922. Philadelphia FC renamed to Bethlehem Steel, moved to Bethlehem.
1923. Paterson Silk Sox bought by Maurice Vanderweghe and moved to New York as Giants.
1924. Indiana Flooring took over the New York FC franchise.
1927. Philadelphia FC was purchased by Fred McGuinness, who renamed them Philadelphia Celtic. They folded in mid-October (date?) Hartford Americans, also performing badly, were thrown out at the same time to even the numbers. 
1928f. Providence Clamdiggers renamed Providence Gold Bugs.
1928f. NY Giants, Newark Skeeters, and Bethelhem Steel withdraw and form the 8-team Eastern Soccer League.
1929s. J&P Coats renamed Pawtucket Rangers
1929f. Boston Wonder Workers renamed Bears.
1929.. Hakoah All-Stars renamed New York Hakoah (?get accurate names for all periods.)
1930s. Brooklyn Hakoah merge with New York Hakoah. (?!)
1930s. Boston Wonder Workers removed nickname; terminated franchise after 4 games.
1930f. New York Giants renamed New York Soccer Club; New York Nationals renamed New York Giants.
1931s. Fall River Marksmen merge with New York SC (ex-Giants), become New York Yankees.
1931s. Providence Gold Bugs move to Fall River, renamed Fall River FC.
1931f. Fall River FC absorb New York Yankees, become New Bedford Whalers #2.
1935. Brooklyn Celtic became Brooklyn St. Mary's Celtic

1933f. League dissolves, re-established as ASL2.
1936. Baltimore Canton renamed Baltimore FC; Newark Germans taken over by Paterson Caledonians and moved.
1937. Paterson Caledonian move to Trenton, become Trenton Highlanders
1939. Trenton move to Paterson FC; Bethlehem Hungarian move to Allentown, fold.


Colorado Rapids                    1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013
Columbus Crew                      1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013
DC United                          1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013
Dallas Burn/FC Dallas              1996 1997 1998 1999 2000 2001 2002 2003 2004x2005 2006 2007 2008 2009 2010 2011 2012 2013
Kansas City Wiz/Wizards/SKC        1996#1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010x2011 2012 2013
Los Angeles Galaxy                 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013
NY/NJ MetroStars/NYRB              1996 1997 1998 1999 2000 2001 2002 2003 2004 2005x2006 2007 2008 2009 2010 2011 2012 2013
New England Revolution             1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013
San Jose Clash/Equakes/H. Dynamo   1996 1997 1998 1999x2000 2001 2002 2003 2004 2005x2006 2007 2008 2009 2010 2011 2012 2013
Tampa Bay Mutiny                   1996 1997 1998 1999 2000 2001
Chicago Fire                                 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013
Miami Fusion                                 1998 1999 2000 2001
Chivas USA                                                                      2005 2006 2007 2008 2009 2010 2011 2012 2013
Real Salt Lake                                                                  2005 2006 2007 2008 2009 2010 2011 2012 2013
Toronto FC                                                                                2007 2008 2009 2010 2011 2012 2013
San Jose Earthquakes                                                                           2008 2009 2010 2011 2012 2013
Seattle Sounders                                                                                    2009 2010 2011 2012 2013
Philadelphia Union                                                                                       2010 2011 2012 2013
Portland Timbers                                                                                              2011 2012 2013
Vancouver Whitecaps                                                                                           2011 2012 2013
Montreal Impact                                                                                                    2012 2013


Atlanta Chiefs/Apollos              1968 1969 1970 1971 1972x1973
Baltimore Bays                      1968 1969
Boston Beacons                      1968
Chicago Mustangs                    1968
Cleveland Stokers                   1968
Dallas Tornado                      1968 1969 1970 1971 1972 1973 1974 1975 1976 1977 1978 1979 1980 1981
Detroit Cougars                     1968
Houston Stars                       1968
Kansas City Spurs                   1968 1969 1970
Los Angeles Wolves                  1968
New York Generals                   1968
Oakland Clippers                    1968
St. Louis Stars/Anaheim Surf        1968 1969 1970 1971 1972 1973 1974 1975 1976 1977x1978 1979 1980 1981
San Diego Toros                     1968
Toronto Falcons                     1968
Vancouver Royals                    1968
Washington Whips                    1968
Rochester Lancers                             1970 1971 1972 1973 1974 1975 1976 1977 1978 1979 1980
W. Darts/Miami Gatos/Toros/Ft.L/MN Strikers   1970 1971x1972x1973 1974 1975 1976x1977 1978 1979 1980 1981 1982 1983x1984
New York Cosmos                                    1971 1972 1973 1974 1975 1976 1977 1978 1979 1980 1981 1982 1983 1984
Montreal Olympique                                 1971 1972 1973
Toronto Metros/M-Croatia/Blizzard                  1971 1972 1973 1974x1975 1976 1977 1978x1979 1980 1981 1982 1983 1984
Philadelphia Atoms                                           1973 1974 1975 1976                  
B'more Comets/SD Jaws/LV Quicksilver/SD Sockers                   1974 1975x1976x1977x1978 1979 1980 1981 1982 1983 1984
Boston Minutemen                                                  1974 1975 1976                     
Denver Dynamos/Minnesota Kicks                                    1974 1975x1976 1977 1978 1979 1980 1981
Los Angeles Aztecs                                                1974 1975 1976 1977 1978 1979 1980 1981
San Jose Earthquakes                                              1974 1975 1976 1977 1978 1979 1980 1981 1982 1983 1984       
Seattle Sounders                                                  1974 1975 1976 1977 1978 1979 1980 1981 1982 1983
Vancouver Whitecaps                                               1974 1975 1976 1977 1978 1979 1980 1981 1982 1983 1984
Washington Diplomats                                              1974 1975 1976 1977 1978 1979 1980
Chicago Sting                                                          1975 1976 1977 1978 1979 1980 1981 1982 1983 1984
Hartford/Conn. Bicentennials/Oakland Stompers/Ed. Drillers             1975 1976x1977x1978x1979 1980 1981 1982
Portland Timbers                                                       1975 1976 1977 1978 1979 1980 1981 1982
San Antonio Thunder/Team Hawaii/Tulsa Roughnecks                       1975 1976x1977x1978 1979 1980 1981 1982 1983 1984
Tampa Bay Rowdies                                                      1975 1976 1977 1978 1979 1980 1981 1982 1983 1984
Colorado Caribous/Atlanta Chiefs                                                      1978x1979 1980 1981
Detroit Express/Washington Diplomats                                                  1978 1979 1980x1981 
Houston Hurricane                                                                     1978 1979 1980
Philadelphia Fury/Montreal Manic                                                      1978 1979 1980x1981 1982 1983
New England Tea Men/Jacksonville Tea Men                                              1978 1979 1980x1981 1982
Memphis Rogues/Calgary Boomers                                                        1978 1979 1980x1981
Team America                                                                                                   1983



* Old clubs....

Pioneer Kickers
http://www.sportclub1924.com/

Brooklyn Italians
http://www.brooklynitalians.org/
