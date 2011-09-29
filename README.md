
# Projects.

0. Use stats to get names.
0. Batch processing using AWS.
0. Deploy entire thing to AWS.
0. Add my old MLS stats; scrape cnnsi stats.
1. Strengthen wiki scraper and canvass team, player data.
2. Generate all standings.
3. News as data. Collect all the soccer news feeds. Use them to pull out interesting data.
4. Twitter stream. Um, get tweets about soccer I suppose. Preferably valuable tweets. Is there a service for this?
5. Add data consistency checking.
6. Create javascript to scrape statto page when I visit it!! Create javascript to randomly load pages! Create ajax function to tell which page to fetch!
7. Figure out how to handle new scores and updates to the database.
8. Learn about unicode and figure out these unicode problems in utils.
9. Probabilites of winning!



# Competition priority.

World Cup
MLS
Mexico
England
Spain
Italy
Germany
Australia
Ligue 1
Champions League
CONCACAF Champions League
Copa Libertadores
US Minor leagues
Netherlands
Portugal
Russia

Turkey
Argentina
Brazil
J-League
K-League
C-League
Europa League
Denmark
Sweden
Norway
Belgium
Greece
FA Cup
Copa del Rey
US Open Cup
UEFA Cup
Copa Sudamericana
Asian Champions League
CAF Champions league

# Defunct, but seems pretty easy to get data for.
# I think I've already got scores.
British Home Championship



# Checking data

What's are ways to check conflicting data?

# First, you have to normalize names.

1. Make sure that a team does not play more than one game on the same day.
2. Assert that when a team plays multiple games on the same day, they are identical.
3. Compare standings and make sure they are identical.
4. Merge bios together.


# Normalization - what do we need to normalize and how?

# Team names.

Just create a list of canonical team names. How should this interact with the teams from soccer?

# Player names.

1. Create guesses based on name similarity with birthdate
2. Use lineup data to create theories about likely players.
2. Create name translation machinery (?)
3. 



Competition names for everything.

Team names only:
 - scores
 - standings
 
Player names only:
 - goals
 - fouls, tackles, etc.
 - biographical data

Both: 
 - substitutions
 - game stats
 - competition stats
 - lineups


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
 - 


# Standardizations

I want to standardize on a text data format.

It seems obviously better to use yaml for everything.
That way it's neatly structured and already ready to use.

# can probably just dump my python creations as yaml?

# Bio data, e.g., should definitely be in yaml.
