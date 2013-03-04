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
    'gen_rosters',
    'awards',
    ]


# Sources are listed in terms of reliability; Order affects priority when merging games.
SOURCES = [

    'world_i',
    'fifa',
    'olympics',

    'concacaf_i',
    'conmebol_i',
    'oceania_i',
    'copa_america',

    'world',
    'concacaf',
    'conmebol',
    'oceania',
    'uncaf',

    'afa_cup',
    'open_cup',

    'asl',
    'nasl',

    'mls',
    'mls2',
    'mls_playoffs',
    'mls_soccernet',
    'mls_reserve',

    'melvin',
    'tours',
    'state',
    'lewis_cup',
    'nafbl',
    'esl',
    'asl2',
    'isl',
    #'indoor',

    'apsl',
    'usl',
    'usl_leach',
    'pdl',
    'misl',

    'ussf2',
    'nasl2',
    'city',
    'ncaa',
    #'world_cup',
    'usa',

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
