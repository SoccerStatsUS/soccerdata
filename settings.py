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
    'cfu',

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
    'nwsl',

    'mexico',
    'canada',

    'colombia',
    'uruguay',
    'chile',
    'argentina',
    'brazil',
    'australia',
    'china',
    'japan',
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
