# What items are shown on the dashboard
STAT_TABLES = [
    'games', 
    'goals', 
    'fouls', 
    'lineups', 
    'stats', 
    'standings', 

    'rosters',
    'gen_rosters',
    'awards',
    'bios',
    ]


# Sources are listed in terms of reliability; Order affects priority when merging games.
SOURCES = [

    'world_i',
    #'world_cup',
    'fifa',

    'concacaf_i',
    'conmebol_i',
    'oceania_i',
    'usa',

    'world',
    'concacaf',
    'conmebol',
    'oceania',
    'uncaf',
    'cfu',

    'asl',
    'nasl',
    'mls',

    'nafbl',
    'asl2',
    #'indoor',
    #'misl',

    'us_d2',
    'us_d3',
    'us_d4',
    'ltrack',

    'us_cups',
    'us_friendly',

    'ncaa',
    'state',
    'city',

    'women',

    'canada',
    'mexico',

    'colombia',
    'uruguay',
    'chile',
    'argentina',
    'brazil',

    'china',
    'japan',
    'korea',

    'australia',


    #'mediotiempo',
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
    'competitions',
    'bios', 
    'teams', 
    'stadiums', 
    'cities',
    'states',
    'countries',

    'news',
    'sources',

    'awards', 
    'drafts',
    'picks',

    'salaries', # player, date -> integer
    'positions', # player, date -> team
    'state_populations', # state -> integer
    'name_maps', # team, date -> string
    'stadium_maps', # team, date -> stadium
    'competition_maps', # competition, date -> string

    # 'prerosters', # huh?#
    ]
