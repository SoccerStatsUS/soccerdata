# What items are shown on the dashboard
STAT_TABLES = [
    'games', 
    'goals', 
    'fouls', 
    'lineups', 
    'stats', 
    'standings', 
    'bios',
    'rosters',
    'awards',
    ]


# Sources are listed in terms of reliability; Order affects priority when merging games.
SOURCES = [
    'asl',
    'nasl',
    'mls',

    'afa_cup',
    'open_cup',

    'olympics',
    'fifa',

    'melvin',
    'tours',
    'state',

    'nafbl',

    'esl',
    'lewis_cup',
    'asl2',
    'isl',
    #'indoor',

    'apsl',
    'usl',
    'usl_leach',
    'pdl',
    'misl',

    'mls_playoffs',
    'mls_soccernet',
    'mls_reserve',
    'ussf2',
    'nasl2',
    'city',
    'ncaa',
    #'world_cup',
    'usa',

    'uncaf',
    'copa_america',
    'concacaf',
    'concacaf_i',
    'conmebol_i',
    'mexico',
    'canada',
    'guatemala',
    'australia',
    'china',
        ]

# Skipping these.
l =    [ 
        'uslsoccer',
        'wiki',
        'kicker',
        'mediotiempo',
        'cnnsi',
        'eufootball',
        ]


SINGLE_SOURCES = [
    'sources',
    'countries',
    'states',
    'state_populations',
    'cities',
    'stadiums', 
    'salaries',
    'competitions',
    'teams', 
    'bios', 
    'awards', 
    'drafts',
    'picks',
    'positions', 
    'name_maps', 
    'stadium_maps', 
    'competition_maps', 
    'news',
    'prerosters',
    ]
